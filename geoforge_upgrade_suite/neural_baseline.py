#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Optional PyTorch transformer for formal auxiliary-construction prediction.

A working small, trainable baseline, not pretrained Gemini/AG2 weights.
The model may only *suggest* formal constructions: all mathematical facts are
still checked by the independent symbolic solver.
"""
from __future__ import annotations
from dataclasses import dataclass,asdict
from pathlib import Path
from typing import Any,Iterable,Sequence
from collections import Counter
import hashlib
import json
import math
import os
import random
import re
import tempfile
import time

try:
    import torch
    from torch import nn
    from torch.nn import functional as F
except ImportError:
    torch=None
    nn=None
    F=None


class TorchUnavailable(RuntimeError):pass


def require_torch():
    if torch is None:raise TorchUnavailable('install torch for optional neural backend')


TOKEN_PATTERN=re.compile(r'[a-zA-Z_][a-zA-Z_0-9]*|\d+/\d+|\d+|=>|\S')


class GeometryTokenizer:
    SPECIAL=('<pad>','<bos>','<eos>','<unk>','<sep>')
    def __init__(self,vocab=None):
        vocab=self.SPECIAL if vocab is None else tuple(vocab)
        if tuple(vocab[:5])!=self.SPECIAL or len(set(vocab))!=len(vocab):
            raise ValueError('invalid vocabulary special tokens')
        self.vocab=tuple(vocab);self.to_id={v:i for i,v in enumerate(vocab)}
    @classmethod
    def fit(cls,texts:Iterable[str],min_frequency:int=1,max_vocab:int=8192):
        if min_frequency<1 or max_vocab<len(cls.SPECIAL):raise ValueError('invalid vocab limit')
        counts=Counter(token for text in texts for token in TOKEN_PATTERN.findall(text))
        words=sorted((w for w,c in counts.items() if c>=min_frequency and w not in cls.SPECIAL),
                     key=lambda x:(-counts[x],x))
        return cls((*cls.SPECIAL,*words[:max_vocab-len(cls.SPECIAL)]))
    def tokens(self,text):return TOKEN_PATTERN.findall(text)
    def encode(self,text,add_bos=True,add_eos=True):
        out=[self.to_id['<bos>']] if add_bos else []
        out.extend(self.to_id.get(s,self.to_id['<unk>']) for s in self.tokens(text))
        if add_eos:out.append(self.to_id['<eos>'])
        return out
    def decode(self,ids,remove_special=True):
        names=[self.vocab[int(i)] for i in ids]
        if remove_special:names=[n for n in names if n not in self.SPECIAL]
        return ' '.join(names)
    def save(self,path):
        Path(path).write_text(json.dumps(self.vocab,ensure_ascii=False),encoding='utf8')
    @classmethod
    def load(cls,path):return cls(json.loads(Path(path).read_text(encoding='utf8')))


@dataclass(frozen=True)
class TransformerConfig:
    vocab_size:int
    context:int=128
    dim:int=128
    heads:int=4
    layers:int=3
    dropout:float=0.0
    ff_multiplier:int=4
    experts:int=0
    top_k:int=2
    def __post_init__(self):
        if self.vocab_size<5 or self.context<8 or self.dim<8 or self.layers<1:
            raise ValueError('invalid transformer size')
        if self.dim%self.heads:raise ValueError('model dimension must divide head count')
        if self.experts and not 1<=self.top_k<=self.experts:
            raise ValueError('invalid top-k experts')
        if not 0<=self.dropout<1:raise ValueError('dropout outside [0,1)')


if nn is not None:
    class SparseMoE(nn.Module):
        """Small MoE feedforward layer with top-k gating and differentiable routing."""
        def __init__(self,dim,experts=4,top_k=2,multiplier=4):
            super().__init__()
            self.router=nn.Linear(dim,experts,bias=False)
            self.experts=nn.ModuleList(nn.Sequential(nn.Linear(dim,dim*multiplier),
                         nn.GELU(),nn.Linear(dim*multiplier,dim)) for _ in range(experts))
            self.top_k=top_k
        def forward(self,x):
            logits=self.router(x)
            scores,indices=torch.topk(logits,self.top_k,dim=-1)
            weights=torch.softmax(scores,dim=-1)
            outputs=torch.stack([module(x) for module in self.experts],dim=-2)
            selected=torch.gather(outputs,-2,indices.unsqueeze(-1).expand(
                *indices.shape,x.shape[-1]))
            result=(selected*weights.unsqueeze(-1)).sum(dim=-2)
            probabilities=torch.softmax(logits,dim=-1)
            routing=F.one_hot(indices,num_classes=len(self.experts)).float().sum(-2)
            avg_proba=probabilities.mean(dim=(0,1))
            avg_routes=routing.mean(dim=(0,1))/self.top_k
            balance=len(self.experts)*(avg_proba*avg_routes).sum()
            return result,balance


    class DecoderBlock(nn.Module):
        def __init__(self,config:TransformerConfig):
            super().__init__()
            self.ln1=nn.LayerNorm(config.dim)
            self.attn=nn.MultiheadAttention(config.dim,config.heads,
                        dropout=config.dropout,batch_first=True)
            self.ln2=nn.LayerNorm(config.dim)
            self.moe=SparseMoE(config.dim,config.experts,config.top_k,
                      config.ff_multiplier) if config.experts else None
            self.ff=(None if self.moe else nn.Sequential(
                nn.Linear(config.dim,config.dim*config.ff_multiplier),nn.GELU(),
                nn.Linear(config.dim*config.ff_multiplier,config.dim)))
            self.dropout=nn.Dropout(config.dropout)
        def forward(self,x,mask):
            q=self.ln1(x)
            att,_=self.attn(q,q,q,attn_mask=mask,need_weights=False)
            x=x+self.dropout(att)
            y=self.ln2(x)
            if self.moe is not None:
                z,balance=self.moe(y)
            else:z,balance=self.ff(y),x.new_zeros(())
            return x+self.dropout(z),balance


    class GeometryTransformer(nn.Module):
        def __init__(self,config:TransformerConfig):
            super().__init__();self.config=config
            self.embed=nn.Embedding(config.vocab_size,config.dim)
            self.pos=nn.Embedding(config.context,config.dim)
            self.blocks=nn.ModuleList(DecoderBlock(config) for _ in range(config.layers))
            self.norm=nn.LayerNorm(config.dim)
            self.head=nn.Linear(config.dim,config.vocab_size,bias=False)
        def forward(self,tokens,targets=None):
            if tokens.ndim!=2:raise ValueError('input must be B x T')
            b,t=tokens.shape
            if t>self.config.context:raise ValueError('input context overflow')
            x=self.embed(tokens)+self.pos(torch.arange(t,device=tokens.device))
            mask=torch.ones((t,t),dtype=torch.bool,device=tokens.device).triu(1)
            balances=[]
            for block in self.blocks:
                x,balance=block(x,mask);balances.append(balance)
            logits=self.head(self.norm(x))
            if targets is None:return logits
            loss=F.cross_entropy(logits.reshape(-1,logits.size(-1)),targets.reshape(-1),
                                 ignore_index=0)
            if self.config.experts:
                loss=loss+0.01*torch.stack(balances).mean()
            return logits,loss
        @torch.no_grad()
        def sample(self,context,max_tokens=32,temperature=1.,top_k=32,seed=0):
            if temperature<=0:raise ValueError('temperature must be positive')
            gen=torch.Generator(device=context.device);gen.manual_seed(seed)
            was_training=self.training;self.eval()
            result=context.clone()
            for _ in range(max_tokens):
                scores=self(result[:,-self.config.context:])[:,-1,:]/temperature
                if top_k and top_k<scores.size(-1):
                    vals,_=torch.topk(scores,top_k)
                    scores=scores.masked_fill(scores<vals[:,-1,None],float('-inf'))
                probs=torch.softmax(scores,dim=-1)
                next_id=torch.multinomial(probs,1,generator=gen)
                result=torch.cat((result,next_id),dim=-1)
                if torch.all(next_id==2):break
            if was_training:self.train()
            return result
else:
    class GeometryTransformer:
        def __init__(self,*args,**kwargs):require_torch()


@dataclass(frozen=True)
class TrainingConfig:
    steps:int=100
    batch:int=16
    learning_rate:float=0.0005
    weight_decay:float=0.01
    clip_grad:float=1.0
    warmup:int=10
    seed:int=42
    def __post_init__(self):
        if min(self.steps,self.batch)<1 or self.learning_rate<=0:
            raise ValueError('training config requires positive steps/batch/lr')


class ProofTextDataset:
    def __init__(self,texts:Sequence[str],tokenizer:GeometryTokenizer,context:int):
        self.tokens=[tokenizer.encode(t) for t in texts if t.strip()]
        self.context=context
        self.starts=[i for i,t in enumerate(self.tokens) if len(t)>=3]
        if not self.starts:raise ValueError('dataset contains no valid sequences')
    def sample(self,batch:int,seed:int,device='cpu'):
        require_torch();rng=random.Random(seed);seq=[]
        for _ in range(batch):
            t=self.tokens[rng.choice(self.starts)]
            if len(t)>self.context+1:
                start=rng.randrange(len(t)-self.context)
                t=t[start:start+self.context+1]
            if len(t)<self.context+1:
                t=t+[0]*(self.context+1-len(t))
            seq.append(t)
        token_tensor=torch.tensor(seq,dtype=torch.long,device=device)
        return token_tensor[:,:-1],token_tensor[:,1:]


class NeuralTrainer:
    def __init__(self,model:GeometryTransformer,config:TrainingConfig):
        require_torch();self.model=model;self.config=config
    def train(self,examples:ProofTextDataset,device='cpu'):
        random.seed(self.config.seed);torch.manual_seed(self.config.seed)
        model=self.model.to(device).train()
        optimizer=torch.optim.AdamW(model.parameters(),lr=self.config.learning_rate,
                                    weight_decay=self.config.weight_decay)
        losses=[]
        for step in range(self.config.steps):
            x,y=examples.sample(self.config.batch,self.config.seed+step,device)
            optimizer.zero_grad(set_to_none=True)
            _,loss=model(x,y)
            if not torch.isfinite(loss):raise FloatingPointError('non-finite loss')
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(),self.config.clip_grad)
            factor=min(1.,(step+1)/max(1,self.config.warmup))
            for group in optimizer.param_groups:group['lr']=self.config.learning_rate*factor
            optimizer.step();losses.append(float(loss.detach().cpu()))
        return {'steps':len(losses),'first_loss':losses[0],
                'last_loss':losses[-1],'mean_last_10':sum(losses[-10:])/min(10,len(losses))}
    def save_checkpoint(self,path,tokenizer:GeometryTokenizer,metadata=None):
        require_torch()
        target=Path(path)
        target.parent.mkdir(parents=True,exist_ok=True)
        content={'model':self.model.state_dict(),'config':asdict(self.model.config),
                 'tokenizer':list(tokenizer.vocab),'training':asdict(self.config),
                 'metadata':metadata or {}}
        tmp=target.with_suffix('.part')
        torch.save(content,tmp);os.replace(tmp,target)
    @staticmethod
    def load_checkpoint(path,map_location='cpu'):
        require_torch()
        # PyTorch 2.6+ loads tensors and basic containers with weights_only.
        data=torch.load(path,map_location=map_location,weights_only=True)
        model=GeometryTransformer(TransformerConfig(**data['config']))
        model.load_state_dict(data['model']);model.eval()
        tokenizer=GeometryTokenizer(data['tokenizer'])
        return model,tokenizer,data.get('metadata',{})


class ConstructionGrammar:
    """Validates decoder outputs without trusting mathematical validity."""
    PRIMITIVES={
        'midpoint':2,'on_line':2,'on_circle':2,'foot':3,'parallel':3,
        'perpendicular':3,'circumcenter':3,'orthocenter':3,
    }
    def parse(self,text,existing_points:Sequence[str]):
        tokens=text.strip().replace('=',' = ').split()
        if len(tokens)<4 or tokens[1]!='=':raise ValueError('expected name = operator args')
        target=tokens[0];op=tokens[2];args=tokens[3:]
        if op not in self.PRIMITIVES:raise ValueError('unknown construction')
        if len(args)!=self.PRIMITIVES[op]:raise ValueError('wrong number of arguments')
        if target in existing_points or not re.fullmatch('[a-z][a-z0-9_]*',target):
            raise ValueError('invalid/new point name required')
        if any(a not in existing_points for a in args):
            raise ValueError('point used before definition')
        return target,op,tuple(args)


__all__=[name for name in globals() if not name.startswith('_') and name not in {
    'dataclass','asdict','Path','Any','Iterable','Sequence','Counter','hashlib',
    'json','math','os','random','re','tempfile','time'}]
