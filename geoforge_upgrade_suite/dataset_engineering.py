#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Reproducible, auditable synthetic proof datasets with leakage controls.

This module never invents a theorem: supplied records must carry certificates
that a separately loaded GeometryProofChecker accepts.  Shards are atomic,
content-addressed and reproducible.  Family holdout is deterministic.
"""
from __future__ import annotations
from dataclasses import dataclass,field
from collections import Counter,defaultdict
from pathlib import Path
from typing import Any,Iterable,Mapping,Sequence
from fractions import Fraction
import csv
import gzip
import hashlib
import io
import itertools
import json
import math
import os
import random
import shutil
import statistics
import tempfile
import time


class DatasetIntegrityError(RuntimeError):pass


def json_bytes(value:Any)->bytes:
    return json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(',',':'),
                      allow_nan=False).encode('utf-8')


def stable_hash(value:Any)->str:
    return hashlib.sha256(json_bytes(value)).hexdigest()


def deterministic_seed(root:int,index:int,domain:str='problems')->int:
    if root<0 or index<0:raise ValueError('seed/index must be >=0')
    h=hashlib.sha256(f'geoforge-v5:{domain}:{root}:{index}'.encode()).digest()
    return int.from_bytes(h[:8],'big')


@dataclass(frozen=True)
class DatasetConfig:
    seed:int=2026
    shard_size:int=256
    validation_percent:int=10
    test_percent:int=10
    compression:int=6
    max_proof_steps:int=10000
    def __post_init__(self):
        if not 1<=self.shard_size<=100000:raise ValueError('invalid shard size')
        if min(self.validation_percent,self.test_percent)<0 or (
            self.validation_percent+self.test_percent>=100):
            raise ValueError('invalid split percentages')
        if not 0<=self.compression<=9:raise ValueError('invalid gzip compression')
        if self.max_proof_steps<1:raise ValueError('invalid proof step bound')


class ProofRecordValidator:
    """Checks structure and a proof checker callable; no numeric assumption trust."""
    def __init__(self,checker=None):self.checker=checker
    def validate(self,record:Mapping)->tuple[bool,str]:
        if record.get('schema')!='geoforge-synthetic-v2':
            return False,'unsupported schema'
        prob=record.get('problem')
        if not isinstance(prob,dict):return False,'missing problem'
        if not isinstance(prob.get('hypotheses'),list):return False,'bad hypotheses'
        if not isinstance(prob.get('goal'),str):return False,'missing goal'
        if not isinstance(record.get('family'),str):return False,'missing family'
        if not isinstance(record.get('proof'),dict):return False,'missing proof'
        proof=record['proof']
        if proof.get('schema')!='geoforge-proof-v1':return False,'wrong proof schema'
        # V5 requires the record to use the exact certified canonical form.
        # In particular, a valid proof of another goal MUST NOT validate it.
        if proof.get('goal')!=prob['goal']:
            return False,'proof does not prove the advertised goal'
        if set(proof.get('assumptions',[]))!=set(prob['hypotheses']):
            return False,'proof assumptions differ from problem hypotheses'
        if not isinstance(proof.get('steps'),list):return False,'missing steps'
        if self.checker is None:return False,'independent proof checker unavailable'
        try:
            result=self.checker(proof)
            if isinstance(result,tuple):ok,msg=result
            else:ok,msg=bool(result),'checker returned false'
            return bool(ok),str(msg)
        except Exception as e:
            return False,'checker error: '+type(e).__name__


class FamilySplit:
    def __init__(self,config:DatasetConfig):self.config=config
    def split(self,family:str):
        if not family:raise ValueError('empty family')
        slot=int(stable_hash({'family':family,'seed':self.config.seed})[:12],16)%100
        if slot<self.config.test_percent:return 'test'
        if slot<self.config.test_percent+self.config.validation_percent:return 'val'
        return 'train'


class DatasetCanonicalizer:
    @staticmethod
    def exact(record):
        p=record['problem']
        return stable_hash({'hypotheses':sorted(p['hypotheses']),
                            'goal':p['goal']})
    @staticmethod
    def structural(record):
        p=record['problem'];hyp=tuple(sorted(p['hypotheses']));goal=p['goal']
        # Color-refinement fingerprint, NOT full graph isomorphism.
        lines=[x.split() for x in (*hyp,goal)]
        points=sorted({x for row in lines for x in row[1:]})
        colors={p:'POINT' for p in points}
        for _ in range(5):
            nxt={}
            for p in points:
                adjacent=[]
                for row in lines:
                    if p in row[1:]:
                        adjacent.append((row[0],row==goal.split(),
                            tuple(i for i,v in enumerate(row[1:]) if v==p),
                            tuple(colors.get(x,'SCALAR') for x in row[1:])))
                nxt[p]=stable_hash(sorted(adjacent,key=repr))
            colors=nxt
        return stable_hash({'colors':sorted(colors.values()),
                    'kinds':sorted(Counter(x[0] for x in lines).items())})
    @staticmethod
    def renamed(record,seed:int=0):
        data=json.loads(json.dumps(record))
        p=data['problem']
        names=sorted({x for st in (*p['hypotheses'],p['goal']) for x in st.split()[1:]})
        target=['pt'+str(i) for i in range(len(names))]
        random.Random(seed).shuffle(target)
        remap=dict(zip(names,target))
        def translate(st):
            tok=st.split();return ' '.join([tok[0],*(remap.get(x,x) for x in tok[1:])])
        p['hypotheses']=[translate(x) for x in p['hypotheses']]
        p['goal']=translate(p['goal'])
        cert=data['proof'];cert['assumptions']=[translate(x) for x in cert['assumptions']]
        cert['goal']=translate(cert['goal'])
        for step in cert['steps']:
            step['premises']=[translate(x) for x in step['premises']]
            step['conclusion']=translate(step['conclusion'])
        return data


@dataclass(frozen=True)
class DatasetManifest:
    schema:str
    config:dict
    files:tuple[dict,...]
    totals:dict
    seen_records:int
    accepted_records:int
    dedupe_mode:str
    created_utc:str
    dataset_hash:str
    def to_dict(self):return dict(self.__dict__)


class AtomicDatasetWriter:
    """Writes deterministic gzip files and a checksummed manifest.

    No unvalidated record is ever committed.  Writer accepts a deterministic
    ordered stream and uses fixed gzip metadata to preserve reproducibility.
    """
    def __init__(self,path:str|Path,config:DatasetConfig,validator:ProofRecordValidator):
        self.path=Path(path);self.config=config;self.validator=validator
        self.path.mkdir(parents=True,exist_ok=True)
    def _shard_bytes(self,records:Sequence[dict])->bytes:
        buff=io.BytesIO()
        with gzip.GzipFile(fileobj=buff,mode='wb',filename='',mtime=0,
                           compresslevel=self.config.compression) as f:
            for record in records:
                f.write(json_bytes(record)+b'\n')
        return buff.getvalue()
    def _atomic(self,target:Path,content:bytes):
        with tempfile.NamedTemporaryFile(dir=target.parent,delete=False) as f:
            temp=Path(f.name);f.write(content);f.flush();os.fsync(f.fileno())
        os.replace(temp,target)
    def write(self,records:Iterable[dict],dedupe='exact',max_records=None):
        if dedupe not in ('none','exact','structural'):
            raise ValueError('unsupported dedupe mode')
        target=self.path/'manifest_v5.json'
        if target.exists():raise FileExistsError('dataset exists: choose another folder')
        chunks=defaultdict(list);seen=set();files=[];total=0;accepted=0
        split_by=FamilySplit(self.config)
        for item in records:
            total+=1
            valid,why=self.validator.validate(item)
            if not valid:
                raise DatasetIntegrityError('record '+str(total)+' invalid: '+why)
            key=(DatasetCanonicalizer.exact(item) if dedupe=='exact' else
                 DatasetCanonicalizer.structural(item) if dedupe=='structural' else None)
            if key is not None and key in seen:continue
            if key is not None:seen.add(key)
            split=split_by.split(item['family'])
            chunks[split].append(item);accepted+=1
            if len(chunks[split])>=self.config.shard_size:
                files.append(self._flush(split,chunks[split],len(files)))
                chunks[split].clear()
            if max_records is not None and accepted>=max_records:break
        for split,batch in sorted(chunks.items()):
            if batch:files.append(self._flush(split,batch,len(files)))
        dataset_hash=stable_hash([x['sha256'] for x in files])
        manifest=DatasetManifest('geoforge-manifest-v5',dict(self.config.__dict__),
             tuple(files),dict(Counter({split:sum(f['count'] for f in files if f['split']==split)
                          for split in ('train','val','test')})),total,accepted,dedupe,
             'deterministic-artifact-no-wallclock',dataset_hash)
        self._atomic(target,json_bytes(manifest.to_dict()))
        return manifest
    def _flush(self,split,records,index):
        data=self._shard_bytes(records)
        name=f'{split}_{index:07d}.jsonl.gz'
        self._atomic(self.path/name,data)
        return {'name':name,'sha256':hashlib.sha256(data).hexdigest(),
                'count':len(records),'split':split}


class DatasetAuditor:
    def __init__(self,validator:ProofRecordValidator):self.validator=validator
    def verify(self,path:str|Path,fail_fast=False):
        base=Path(path);manifest=json.loads((base/'manifest_v5.json').read_text())
        errors=[];seen=set();count=0;splits=Counter();families=defaultdict(set)
        for desc in manifest['files']:
            file=base/desc['name']
            if not file.is_file():
                errors.append('missing '+desc['name']);continue
            blob=file.read_bytes()
            if hashlib.sha256(blob).hexdigest()!=desc['sha256']:
                errors.append('bad checksum '+desc['name']);continue
            in_file=0
            try:
                with gzip.open(file,'rt',encoding='utf-8') as stream:
                    for line in stream:
                        record=json.loads(line);in_file+=1;count+=1
                        good,reason=self.validator.validate(record)
                        if not good:errors.append(f'{desc["name"]}:{in_file}: {reason}')
                        fam=record['family'];split=desc['split'];splits[split]+=1
                        families[fam].add(split)
                        key=DatasetCanonicalizer.exact(record)
                        if key in seen and manifest.get('dedupe_mode')!='none':
                            errors.append('duplicate exact item')
                        seen.add(key)
                        if fail_fast and errors:break
            except (OSError,ValueError,KeyError) as ex:
                errors.append('invalid shard '+desc['name']+': '+type(ex).__name__)
            if in_file!=desc['count']:errors.append('incorrect shard record count')
        for family,locations in families.items():
            if len(locations)!=1:errors.append('split leakage for '+family)
        if count!=manifest['accepted_records']:
            errors.append('manifest accepted count mismatch')
        actual_hash=stable_hash([x['sha256'] for x in manifest['files']])
        if actual_hash!=manifest['dataset_hash']:
            errors.append('manifest aggregate checksum mismatch')
        return {'passed':not errors,'records':count,'splits':dict(splits),
                'families':len(families),'errors':errors[:100]}


class DatasetStatistics:
    def summarize(self,records:Iterable[dict]):
        counts=Counter();lengths=[];predicates=Counter();aux=Counter()
        for item in records:
            counts[item['family']]+=1
            lengths.append(len(item['proof']['steps']))
            for s in item['problem']['hypotheses']:
                predicates[s.split()[0]]+=1
            aux[len(item.get('auxiliaries',()))]+=1
        return {'total':sum(counts.values()),'families':dict(counts),
                'predicates':dict(predicates),'auxiliary_count':dict(aux),
                'mean_steps':statistics.mean(lengths) if lengths else 0,
                'median_steps':statistics.median(lengths) if lengths else 0,
                'max_steps':max(lengths,default=0)}


class StreamingDatasetReader:
    def __init__(self,path:str|Path,split=None):
        self.path=Path(path);self.split=split
    def __iter__(self):
        manifest=json.loads((self.path/'manifest_v5.json').read_text())
        for entry in manifest['files']:
            if self.split and entry['split']!=self.split:continue
            with gzip.open(self.path/entry['name'],'rt',encoding='utf-8') as stream:
                for line in stream:yield json.loads(line)


class DatasetCurriculum:
    def __init__(self,seed=0):self.seed=seed
    @staticmethod
    def difficulty(record):
        steps=len(record['proof']['steps']);h=len(record['problem']['hypotheses'])
        aux=len(record.get('auxiliaries',()))
        return steps+2*aux+math.log1p(h)
    def sample(self,records:Sequence[dict],epoch:int,limit:int):
        if epoch<0 or limit<0:raise ValueError('invalid epoch or limit')
        if not records or not limit:return ()
        arr=sorted(records,key=lambda r:(self.difficulty(r),stable_hash(r['problem'])))
        fraction=min(1.,0.15+0.1*epoch)
        eligible=arr[:max(1,math.ceil(len(arr)*fraction))]
        rng=random.Random(deterministic_seed(self.seed,epoch,'curriculum'))
        return tuple(rng.choice(eligible) for _ in range(limit))


class LeakageAuditor:
    def __init__(self):self.names=set();self.structures=set()
    def add_training(self,record):
        self.names.add(DatasetCanonicalizer.exact(record))
        self.structures.add(DatasetCanonicalizer.structural(record))
    def test(self,record):
        exact=DatasetCanonicalizer.exact(record) in self.names
        structural=DatasetCanonicalizer.structural(record) in self.structures
        return {'exact':exact,'structural_fingerprint':structural,
            'warning':'WL fingerprint is not a complete graph-isomorphism test'}


__all__=[name for name in globals() if not name.startswith('_') and name not in {
    'Any','Iterable','Mapping','Sequence','Counter','defaultdict','Path','Fraction',
    'csv','gzip','hashlib','io','itertools','json','math','os','random','shutil',
    'statistics','tempfile','time','dataclass','field'}]
