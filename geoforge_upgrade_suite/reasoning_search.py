#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Auditable proof search and bounded shared-knowledge search trees.

This implementation intentionally distinguishes:
- unconditional proof: certificate from exactly the original hypotheses;
- conditional auxiliary derivation: certificate depends on constructed facts;
- numeric observation: never added as a theorem without a formal derivation.
It is an independently useful SKEST-inspired research baseline, not AG2 SKEST.
"""
from __future__ import annotations
from collections import Counter, defaultdict, deque
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable, Iterable, Mapping, Sequence
from functools import lru_cache
from fractions import Fraction
import copy
import hashlib
import heapq
import importlib.util
import itertools
import json
import math
import random
import sys
import threading
import time


@lru_cache(maxsize=4)
def load_engine(path:str):
    p=Path(path).resolve()
    if not p.is_file():raise FileNotFoundError(p)
    key='geoforge_embedded_'+hashlib.sha256(str(p).encode()).hexdigest()[:12]
    if key in sys.modules:return sys.modules[key]
    spec=importlib.util.spec_from_file_location(key,str(p))
    if spec is None or spec.loader is None:raise ImportError(str(p))
    module=importlib.util.module_from_spec(spec)
    sys.modules[key]=module
    spec.loader.exec_module(module)
    return module


@dataclass(frozen=True)
class Budget:
    seconds:float=5.0
    max_nodes:int=100
    max_facts:int=1500
    max_auxiliary_points:int=2
    beam_width:int=12
    parallelism:int=1
    def __post_init__(self):
        if self.seconds<=0 or min(self.max_nodes,self.max_facts,self.beam_width,self.parallelism)<1:
            raise ValueError('all resource budgets must be positive')
        if self.max_auxiliary_points<0:raise ValueError('negative auxiliary budget')


@dataclass(frozen=True)
class Auxiliary:
    point:str
    constraints:tuple[tuple[str,tuple[str,...]],...]
    branch:int=0
    def __post_init__(self):
        if not self.point or not self.constraints or self.branch<0:
            raise ValueError('invalid auxiliary candidate')
        if len(set(self.constraints))!=len(self.constraints):
            raise ValueError('duplicated construction constraints')
    def fingerprint(self):
        data=(self.point,tuple(sorted(self.constraints)),self.branch)
        return hashlib.sha256(repr(data).encode()).hexdigest()


@dataclass(frozen=True)
class SearchNode:
    constructions:tuple[Auxiliary,...]
    assumptions:tuple[str,...]
    parent_id:str
    depth:int
    priority:float
    state_id:str
    numerical_coords:tuple[tuple[str,float,float],...]=()
    def __post_init__(self):
        if self.depth!=len(self.constructions):
            raise ValueError('node depth must equal number of auxiliaries')
    def coordinates(self):
        return {n:(x,y) for n,x,y in self.numerical_coords}


@dataclass(frozen=True)
class ProvedFact:
    conclusion:str
    certificate_json:str
    hypotheses:tuple[str,...]
    source_tree:int
    def __post_init__(self):
        if not self.certificate_json:raise ValueError('proof certificate is empty')


class SharedKnowledgeWorkspace:
    """Shares only facts independently certified from BASE hypotheses.

    Facts with premises mentioning auxiliary points, or which have simply been
    observed in a sample diagram, are NEVER promoted to base knowledge.
    """
    def __init__(self,core,base_hypotheses:tuple[str,...]):
        self.core=core
        self.base_hypotheses=tuple(sorted(set(base_hypotheses)))
        self._items={}
        self._lock=threading.RLock()
        self._base_points={p for h in self.base_hypotheses for p in h.split()[1:]}
    def add(self,item:ProvedFact)->bool:
        parser=self.core.GeometryParser()
        try:
            cert=self.core.ProofCertificate.from_dict(json.loads(item.certificate_json))
            ok,_=self.core.ProofCheckerV2().verify(cert)
        except Exception:
            return False
        if not ok:return False
        if set(map(str,cert.assumptions))!=set(self.base_hypotheses):return False
        if str(cert.goal)!=item.conclusion:return False
        if not set(cert.goal.args)<=self._base_points:return False
        if set(item.hypotheses)!=set(self.base_hypotheses):return False
        with self._lock:
            if item.conclusion in self._items:return False
            self._items[item.conclusion]=item
        return True
    def snapshot(self)->tuple[ProvedFact,...]:
        with self._lock:
            return tuple(self._items[k] for k in sorted(self._items))
    def __len__(self):
        with self._lock:return len(self._items)


class AuxiliaryCandidateGenerator:
    """Deterministic, geometry-valid midpoint/foot/line-intersection proposals."""
    def __init__(self,core,seed=0,max_candidates=40):
        self.core=core
        self.seed=int(seed)
        self.max_candidates=max_candidates
    def propose(self,coords:Mapping[str,tuple[float,float]],used:Iterable[str]=())->tuple[Auxiliary,...]:
        names=sorted(coords)
        if len(names)<2:return ()
        occupied=set(names)|set(used)
        def free_name():
            for n in ('x','y','z','u','v','w','p','q','r','s','t'):
                if n not in occupied:return n
            for i in range(10000):
                s='aux'+str(i)
                if s not in occupied:return s
            raise RuntimeError('auxiliary namespace exhausted')
        p=free_name()
        results=[]
        for a,b in itertools.combinations(names,2):
            results.append(Auxiliary(p,(('midpoint',(a,b)),)))
            if len(results)>=self.max_candidates:break
        if len(results)<self.max_candidates:
            for a in names:
                for b,c in itertools.combinations((x for x in names if x!=a),2):
                    results.append(Auxiliary(p,(('foot',(a,b,c)),)))
                    if len(results)>=self.max_candidates:break
                if len(results)>=self.max_candidates:break
        # Ordered pair of lines with four distinct defining points.
        if len(results)<self.max_candidates:
            for quad in itertools.combinations(names,4):
                for a,b,c,d in ((quad[0],quad[1],quad[2],quad[3]),
                                (quad[0],quad[2],quad[1],quad[3]),
                                (quad[0],quad[3],quad[1],quad[2])):
                    results.append(Auxiliary(p,(('on_line',(a,b)),('on_line',(c,d)))))
                    if len(results)>=self.max_candidates:break
                if len(results)>=self.max_candidates:break
        rng=random.Random(self.seed)
        rng.shuffle(results)
        return tuple(results)


class AuxiliaryBuilder:
    def __init__(self,core):self.core=core
    def build(self,candidate:Auxiliary,coords:Mapping[str,tuple[float,float]]):
        cons=tuple(self.core.ConstructionConstraint(op,args) for op,args in candidate.constraints)
        out=self.core.ConstructionSolver2().construct(candidate.point,cons,dict(coords),
                        branch=candidate.branch,allow_overlap=False,require_unique=False)
        newcoords=dict(coords);newcoords[candidate.point]=out.point
        return newcoords,self._construction_hypotheses(candidate)
    def _construction_hypotheses(self,candidate):
        p=candidate.point;givens=[]
        for kind,points in candidate.constraints:
            if kind=='on_line':
                givens.append(f'coll {p} {points[0]} {points[1]}')
            elif kind=='parallel':
                givens.append(f'para {points[0]} {p} {points[1]} {points[2]}')
            elif kind=='perpendicular':
                givens.append(f'perp {points[0]} {p} {points[1]} {points[2]}')
            elif kind=='midpoint':
                givens.append(f'midp {p} {points[0]} {points[1]}')
            elif kind=='foot':
                givens.append(f'coll {p} {points[1]} {points[2]}')
                givens.append(f'perp {points[0]} {p} {points[1]} {points[2]}')
            elif kind=='on_circle':
                givens.append(f'cong {points[0]} {p} {points[0]} {points[1]}')
            else:
                raise ValueError('no certified construction constraints for '+kind)
        return tuple(givens)


@dataclass(frozen=True)
class SearchResult:
    status:str
    goal:str
    tree_count:int
    expanded_nodes:int
    derived_facts:int
    elapsed_s:float
    shared_facts:int
    certificate:dict|None
    auxiliary_constructions:tuple[Auxiliary,...]
    conditional_assumptions:tuple[str,...]
    failure_reasons:dict[str,int]
    def report(self):
        return {'status':self.status,'goal':self.goal,
                'tree_count':self.tree_count,'expanded_nodes':self.expanded_nodes,
                'derived_facts':self.derived_facts,'elapsed_s':round(self.elapsed_s,6),
                'shared_facts':self.shared_facts,'certificate':self.certificate,
                'auxiliary_constructions':[
                    {'point':x.point,'constraints':x.constraints,'branch':x.branch}
                    for x in self.auxiliary_constructions],
                'conditional_assumptions':list(self.conditional_assumptions),
                'failure_reasons':self.failure_reasons}


class CertifiedSearchEnsemble:
    """Finite multi-tree baseline with explicit safe result classification.

    The AG2 neural policy/SKEST are NOT included. Can accept candidate-provider
    strategies and share unconditional proofs, with deterministic scheduling.
    """
    def __init__(self,core,budget:Budget=Budget(),seed=0):
        self.core=core;self.budget=budget;self.seed=int(seed)
    def _fact(self,text):return self.core.GeometryParser().fact(text)
    def _canonical(self,fact):
        return str(self.core.GeometryCanonicalizer().fact(self._fact(fact)))
    def _solve(self,assumptions,goal,deadline):
        facts=tuple(self._fact(s) for s in assumptions)
        motor=self.core.CertifiedDDAR2Engine(facts,maxfacts=self.budget.max_facts,
                                            deadline=deadline).close(max_steps=20000)
        cert=motor.certificate(self._fact(goal))
        if cert is None:return motor,None
        ok,msg=self.core.ProofCheckerV2().verify(cert)
        if not ok:raise RuntimeError('solver returned invalid certificate: '+msg)
        return motor,cert
    def solve(self,hypotheses:Sequence[str],goal:str,
              coordinates:Mapping[str,tuple[float,float]]|None=None,
              proposals:Sequence[Auxiliary]|None=None,n_trees=3)->SearchResult:
        started=time.monotonic();deadline=started+self.budget.seconds
        if n_trees<1:raise ValueError('n_trees must be positive')
        base=tuple(dict.fromkeys(self._canonical(f) for f in hypotheses))
        objective=self._canonical(goal)
        reasons=Counter()
        try:
            motor,cert=self._solve(base,objective,deadline)
        except Exception as ex:
            return SearchResult('invalid_problem',objective,n_trees,0,0,
                                time.monotonic()-started,0,None,(),(),{type(ex).__name__:1})
        if cert is not None:
            return SearchResult('certified',objective,n_trees,1,len(motor.known),
                  time.monotonic()-started,0,cert.to_dict(),(),(),{})
        if not coordinates or self.budget.max_auxiliary_points==0:
            return SearchResult('not_proven',objective,n_trees,1,len(motor.known),
                    time.monotonic()-started,0,None,(),(),{'no_auxiliary_search':1})
        workspace=SharedKnowledgeWorkspace(self.core,base)
        builder=AuxiliaryBuilder(self.core)
        provider=AuxiliaryCandidateGenerator(self.core,self.seed,self.budget.beam_width*8)
        coords={k:tuple(map(float,v)) for k,v in coordinates.items()}
        candidates=tuple(proposals) if proposals is not None else provider.propose(coords)
        # This is finite distributed-style search; trees explore different slice
        # orders and share only facts proven from original assumptions.
        trees=[]
        for t in range(n_trees):
            rng=random.Random(self.seed+t*10007)
            order=list(candidates);rng.shuffle(order)
            trees.append(deque(((),coords,base,(p,)) for p in order[:self.budget.beam_width]))
        seen=set();expanded=1;facts_seen=len(motor.known)
        while any(trees) and expanded<self.budget.max_nodes and time.monotonic()<deadline:
            for ti in range(n_trees):
                if expanded>=self.budget.max_nodes or time.monotonic()>=deadline:break
                if not trees[ti]:continue
                prior,curcoords,curassumptions,requests=trees[ti].popleft()
                if not requests:continue
                aux=requests[0]
                state_key=(tuple(sorted(curassumptions)),aux.fingerprint())
                if state_key in seen:continue
                seen.add(state_key)
                try:
                    next_coords,introduced=builder.build(aux,curcoords)
                    assumptions=tuple(dict.fromkeys((*curassumptions,*introduced)))
                    if time.monotonic()>=deadline:break
                    eng,branch_cert=self._solve(assumptions,objective,deadline)
                    expanded+=1;facts_seen+=len(eng.known)
                except Exception as ex:
                    reasons[type(ex).__name__]+=1;continue
                if branch_cert is not None:
                    # Only a conditional proof: the auxiliary hypotheses have
                    # not been discharged by an existential construction proof.
                    return SearchResult('conditional_auxiliary_derivation',objective,n_trees,
                        expanded,facts_seen,time.monotonic()-started,len(workspace),
                        branch_cert.to_dict(),prior+(aux,),tuple(introduced),dict(reasons))
                if len(prior)+1<self.budget.max_auxiliary_points:
                    more=provider.propose(next_coords,used=(a.point for a in prior+(aux,)))
                    for proposal in more[:max(1,self.budget.beam_width//4)]:
                        trees[ti].append((prior+(aux,),next_coords,assumptions,(proposal,)))
        return SearchResult('not_proven',objective,n_trees,expanded,facts_seen,
                time.monotonic()-started,len(workspace),None,(),(),dict(reasons))


class ProofGapAnalyzer:
    """Compare implications of premises and provisional goal without leakage."""
    def __init__(self,core):self.core=core
    def compare(self,hypotheses:Sequence[str],goal:str,timeout=5.0,maxfacts=750):
        parse=self.core.GeometryParser().fact
        giv=tuple(parse(t) for t in hypotheses)
        deadline=time.monotonic()+timeout
        base=self.core.CertifiedDDAR2Engine(giv,maxfacts=maxfacts,deadline=deadline).close()
        direct=set(map(str,base.known))
        assumed=self.core.CertifiedDDAR2Engine((*giv,parse(goal)),maxfacts=maxfacts,
                                  deadline=deadline).close()
        provisional=set(map(str,assumed.known))
        return {'proven_from_premises':sorted(direct),
                'assuming_goal_additionally':sorted(provisional-direct),
                'assumption_is_proven':str(parse(goal)) in direct,
                'warnings':['Goal-assumption consequences are hypothetical, not proved facts.']}


class SearchTrace:
    def __init__(self):self.events=[]
    def log(self,name,**payload):
        self.events.append({'seq':len(self.events),'event':name,'payload':payload})
    def json(self):return json.dumps(self.events,sort_keys=True,ensure_ascii=False)
    def verify_sequence(self):
        return all(e['seq']==i for i,e in enumerate(self.events))


class SearchStateCanonicalizer:
    def __init__(self,core):self.core=core
    def key(self,assumptions:Sequence[str],constructions:Sequence[Auxiliary]):
        facts=sorted({str(self.core.GeometryCanonicalizer().fact(
            self.core.GeometryParser().fact(x))) for x in assumptions})
        aux=sorted((tuple(sorted(c.constraints)),c.branch) for c in constructions)
        return hashlib.sha256(json.dumps({'facts':facts,'aux':aux},sort_keys=True).encode()).hexdigest()


class BranchSelector:
    def __init__(self,seed=0):self.seed=seed
    def diverse(self,branches:Sequence[tuple[float,Any]],limit:int):
        if limit<0:raise ValueError('negative limit')
        ordered=sorted(branches,key=lambda pair:(-pair[0],repr(pair[1])))
        return tuple(value for _,value in ordered[:limit])
    def softmax(self,scores:Sequence[float],temperature=1.0):
        if temperature<=0 or not math.isfinite(temperature):raise ValueError('bad temperature')
        if not scores:return ()
        mx=max(scores)
        if not math.isfinite(mx):raise ValueError('nonfinite score')
        weights=[math.exp((v-mx)/temperature) for v in scores]
        den=sum(weights)
        return tuple(w/den for w in weights)
    def sample(self,items:Sequence[Any],scores:Sequence[float],k:int):
        if len(items)!=len(scores):raise ValueError('unaligned scores')
        if k<0:raise ValueError('negative k')
        rng=random.Random(self.seed);pool=list(zip(items,scores));chosen=[]
        while pool and len(chosen)<k:
            probabilities=self.softmax([s for _,s in pool]);u=rng.random();acc=0
            for i,w in enumerate(probabilities):
                acc+=w
                if u<=acc or i==len(probabilities)-1:
                    chosen.append(pool.pop(i)[0]);break
        return tuple(chosen)


class BoundedJobScheduler:
    """Workers do not execute user-provided source; functions are supplied in process."""
    def __init__(self,parallelism=1):
        if parallelism<1:raise ValueError('parallelism must be positive')
        self.parallelism=parallelism
    def map(self,function:Callable[[Any],Any],jobs:Sequence[Any],timeout=20.):
        if timeout<=0:raise ValueError('timeout must be positive')
        with ThreadPoolExecutor(max_workers=self.parallelism) as pool:
            futures=[pool.submit(function,j) for j in jobs]
            deadline=time.monotonic()+timeout;results=[]
            for f in futures:
                remaining=max(0.001,deadline-time.monotonic())
                results.append(f.result(timeout=remaining))
        return tuple(results)


__all__=[name for name in globals() if not name.startswith('_') and name not in {
    'Any','Callable','Iterable','Mapping','Sequence','Counter','defaultdict','deque',
    'ThreadPoolExecutor','as_completed','dataclass','field','Path','lru_cache','Fraction',
    'copy','hashlib','heapq','importlib','itertools','json','math','random','sys','threading','time'}]
