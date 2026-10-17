#!/usr/bin/env python3
"""Deterministic, training-free GeoForge theorem-proving portfolio.

Strict distinction:
 PROVED         replayable deductive or coordinate-ideal certificate + side guards;
 COUNTEREXAMPLE a rational realization satisfying every premise and not goal;
 CONDITIONAL    ideal identity holds but additional side conditions unproved;
 UNKNOWN        bounded proof procedures made no claim.
A bounded algorithm cannot decide every statement in all geometry languages.
"""
from __future__ import annotations
from dataclasses import dataclass,field
from collections import defaultdict
from fractions import Fraction as Q
from pathlib import Path
from typing import Mapping,Sequence
from .geometry_exact import Vec2,DomainError,Polynomial
from .symbolic_coordinates import CoordinatePredicateCompiler,UnsupportedPredicate
from .deterministic_ideal import (IdealBudget,ExactIdealEngine,
                                  certificate_to_json,verify_certificate_json,
                                  polynomial_from_object,polynomial_to_object)
import hashlib,importlib,json,itertools,math,random,time


def split_fact(text):
    tokens=str(text).strip().lower().split()
    if not tokens:raise ValueError('empty fact')
    if any(not x.replace('_','').isalnum() for x in tokens):
        raise ValueError('invalid geometry token')
    return tokens[0],tuple(tokens[1:])


def _pair(a,b):return tuple(sorted((a,b)))

class GuardLedger:
    """Soundly collects *implied* named nondegeneracy constraints.

    Conservative: unsupported guard is unresolved even when mathematically true.
    """
    def __init__(self,hypotheses:Sequence[str]):
        self.facts=set();self.distinct=set();self.ncoll=set();self.overlap=set()
        self.midpoints=[];self.contradictions=[]
        for text in hypotheses:
            kind,a=split_fact(text)
            self.facts.add((kind,a))
            if kind in ('distinct','noverlap') and len(a)==2:
                if a[0]==a[1]:
                    self.contradictions.append('self-distinctness is impossible: '+a[0])
                else:
                    self.distinct.add(_pair(*a))
            if kind=='ncoll' and len(a)==3:
                t=frozenset(a)
                if len(t)!=3:self.contradictions.append('ncoll has repeating points')
                else:
                    self.ncoll.add(t)
                    self.distinct.update(_pair(x,y) for x,y in itertools.combinations(a,2))
            if kind=='cyclic' and len(a)==4:
                if len(set(a))!=4:
                    self.contradictions.append('cyclic requires four distinct points')
                else:
                    self.ncoll.update(frozenset(t) for t in itertools.combinations(a,3))
                    self.distinct.update(_pair(x,y) for x,y in itertools.combinations(a,2))
            if kind=='overlap' and len(a)==2:self.overlap.add(_pair(*a))
            if kind in ('para','perp') and len(a)==4:
                if a[0]==a[1] or a[2]==a[3]:
                    self.contradictions.append(kind+' requires nonzero line directions')
                else:
                    self.distinct.update((_pair(a[0],a[1]),_pair(a[2],a[3])))
            # Collinearity is a symmetric determinant identity, including
            # repeated points. It cannot imply distinctness of any pair.
            if kind=='eqratio' and len(a)==8:
                if any(a[i]==a[i+1] for i in range(0,8,2)):
                    self.contradictions.append('eqratio requires nonzero segments')
                else:
                    self.distinct.update(_pair(a[i],a[i+1]) for i in range(0,8,2))
            if kind=='midp' and len(a)==3:self.midpoints.append(a)
        self._derive()
    def _derive(self):
        # Midpoints of distinct endpoints are distinct from each endpoint.
        for m,a,b in self.midpoints:
            if _pair(a,b) in self.distinct:
                self.distinct.add(_pair(m,a));self.distinct.add(_pair(m,b))
        # If A,B,C are non-collinear and D,E are midpoints AB and AC,
        # D!=E follows because B!=C (even if not explicitly stated).
        for (d,a,b),(e,x,c) in itertools.permutations(self.midpoints,2):
            for ta,tb in ((a,b),(b,a)):
                for tx,tc in ((x,c),(c,x)):
                    if ta==tx and frozenset((ta,tb,tc)) in self.ncoll:
                        self.distinct.add(_pair(d,e))
        for p in self.overlap & self.distinct:
            self.contradictions.append('overlap and distinct: '+' '.join(p))
        for k,args in self.facts:
            if k=='coll' and frozenset(args) in self.ncoll:
                self.contradictions.append('coll and ncoll contradiction')
    def entails(self,requirement):
        kind,a=split_fact(requirement)
        if (kind,a) in self.facts:return True
        if kind in ('distinct','noverlap') and len(a)==2:
            return _pair(*a) in self.distinct
        if kind=='ncoll' and len(a)==3:
            return frozenset(a) in self.ncoll
        return False
    def unresolved(self,requirements):
        return tuple(sorted(set(str(x) for x in requirements if not self.entails(x))))


class ExactFactEvaluator:
    """Check concrete rational-coordinate statements; no sampling implication."""
    def __init__(self,coordinates:Mapping[str,Sequence[object]]):
        self.points={str(n).lower():Vec2(Q(str(x)),Q(str(y))) for n,(x,y) in coordinates.items()}
    def check(self,text):
        k,names=split_fact(text)
        p=[self.points[n] for n in names]
        if k in ('distinct','noverlap') and len(p)==2:return p[0]!=p[1]
        if k=='overlap' and len(p)==2:return p[0]==p[1]
        if k=='ncoll' and len(p)==3:
            return (p[1]-p[0]).cross(p[2]-p[0])!=0
        if k=='coll' and len(p)==3:
            # Symmetric predicate: sorting/repeating names must not change truth.
            # Nonzero line direction is a separate guard for line operations.
            return (p[1]-p[0]).cross(p[2]-p[0])==0
        if k=='para' and len(p)==4:
            return p[0]!=p[1] and p[2]!=p[3] and (p[1]-p[0]).cross(p[3]-p[2])==0
        if k=='perp' and len(p)==4:
            return p[0]!=p[1] and p[2]!=p[3] and (p[1]-p[0]).dot(p[3]-p[2])==0
        if k=='cong' and len(p)==4:
            return (p[1]-p[0]).norm2()==(p[3]-p[2]).norm2()
        if k=='midp' and len(p)==3:
            return p[0]*2==p[1]+p[2]
        if k=='cyclic' and len(p)==4:
            if any(p[i].eq(p[j]) if hasattr(p[i],'eq') else p[i]==p[j] for i in range(4) for j in range(i+1,4)):
                return False
            if any((p[1]-p[0]).cross(q-p[0])==0 for q in p[2:]):return False
            from sympy import Matrix
            arr=[[q.x*q.x+q.y*q.y,q.x,q.y,1] for q in p]
            return Matrix(arr).det()==0
        if k=='eqratio' and len(p)==8:
            ds=[(p[i+1]-p[i]).norm2() for i in range(0,8,2)]
            return all(ds) and ds[0]*ds[3]==ds[1]*ds[2]
        if k=='eqangle' and len(p)==8:
            u=[p[i+1]-p[i] for i in range(0,8,2)]
            if any(v.norm2()==0 for v in u):return False
            # Equal *directed* angles modulo pi iff tan difference equals zero;
            # cross(a,b)*dot(c,d)-dot(a,b)*cross(c,d) = 0.
            return u[0].cross(u[1])*u[2].dot(u[3])==u[0].dot(u[1])*u[2].cross(u[3])
        if k=='sameclock' and len(p)==6:
            x=(p[1]-p[0]).cross(p[2]-p[0]);y=(p[4]-p[3]).cross(p[5]-p[3])
            return x*y>0
        if k=='lessthan' and len(p)==4:
            return (p[1]-p[0]).norm2()<(p[3]-p[2]).norm2()
        raise UnsupportedPredicate(f'unrecognized evaluator predicate {k}/{len(p)}')
    def all_hold(self,hypotheses:Sequence[str]):
        return all(self.check(x) for x in hypotheses)

@dataclass(frozen=True)
class DeterministicBudget:
    seconds:float=8.
    max_points:int=9
    max_pairs:int=180
    max_basis:int=80
    max_terms:int=3000
    max_reductions:int=20000
    max_facts:int=2000
    sample_attempts:int=100
    def __post_init__(self):
        if any(getattr(self,n)<=0 for n in ('seconds','max_points','max_pairs','max_basis',
                    'max_terms','max_reductions','max_facts','sample_attempts')):
            raise ValueError('budgets must be positive')

@dataclass(frozen=True)
class DeterministicResult:
    status:str
    goal:str
    hypotheses:tuple[str,...]
    method:str
    certificate:dict|None
    unresolved_guards:tuple[str,...]
    counterexample:dict|None
    attempts:tuple[dict,...]
    elapsed_s:float
    def to_dict(self):
        return {'schema':'geoforge-deterministic-result-v1',
                'status':self.status,'goal':self.goal,'hypotheses':list(self.hypotheses),
                'method':self.method,'certificate':self.certificate,
                'unresolved_guards':list(self.unresolved_guards),
                'counterexample':self.counterexample,'attempts':list(self.attempts),
                'elapsed_s':round(self.elapsed_s,6)}


def polynomial_guard_strategy(hypotheses,goal,budget:DeterministicBudget,deadline):
    tokens=[split_fact(t) for t in (*hypotheses,goal)]
    points=sorted({p for _,names in tokens for p in names})
    if len(points)>budget.max_points:
        return 'unknown',None,(),{'reason':'point limit','points':len(points)}
    compiler=CoordinatePredicateCompiler(points)
    hs=[]
    for kind,args in tokens[:-1]:
        if kind in ('distinct','noverlap','ncoll','sameclock','lessthan'):
            continue  # nonzero/inequality conditions are guards, not equations.
        hs.append(compiler.compile(kind,args))
    target=compiler.compile(*tokens[-1])
    axioms=tuple(p for item in hs for p in item.polynomials)
    ledger=GuardLedger(hypotheses)
    guards=ledger.unresolved(target.nondegeneracy)
    i_budget=IdealBudget(max_pairs=budget.max_pairs,max_basis=budget.max_basis,
        max_terms=budget.max_terms,max_reductions=budget.max_reductions,
        seconds=max(.001,deadline-time.monotonic()))
    certificates=[];pairs=0;reductions=0
    backend_counts={'affine':0,'buchberger':0}
    for target_pol in target.polynomials:
        from .affine_certificate import AffineIdealTactic
        quick=AffineIdealTactic(max_steps=6000).prove(axioms,target_pol)
        if quick.status=='proved':
            cert=quick.certificate;backend_counts['affine']+=1
        else:
            out=ExactIdealEngine(i_budget).membership(axioms,target_pol)
            pairs+=out.explored_pairs;reductions+=out.reductions
            if out.status!='proved':
                return 'unknown',None,guards,{'reason':out.reason,'pairs':pairs,'reductions':reductions}
            cert=out.certificate;backend_counts['buchberger']+=1
        certificates.append(json.loads(certificate_to_json(cert)))
    proof={'schema':'geoforge-coordinate-theorem-v1',
           'compiled_axiom_labels':[x.source for x in hs],
           'compiled_goal_label':target.source,'witnesses':certificates,
           'side_guards':list(target.nondegeneracy)}
    return ('proved' if not guards else 'conditional'),proof,guards,{
        'reason':'exact polynomial identity','pairs':pairs,'reductions':reductions,
        'backends':backend_counts}


def _coordinate_assignments(hypotheses,seed,limit):
    """Generate *exact rational* candidate diagrams, not proof-by-sampling.

    Constraint propagation supports midpoints and coincidences; other equalities
    are tested exactly and may not be satisfied by random assignments.
    """
    tokens=[split_fact(x) for x in hypotheses]
    points=sorted({p for _,a in tokens for p in a})
    rng=random.Random(seed)
    constructed={args[0] for kind,args in tokens if kind in ('midp','overlap')}
    for _ in range(limit):
        coords={p:(Q(rng.randint(-9,9)),Q(rng.randint(-9,9))) for p in points if p not in constructed}
        # Repeated passes support midpoint chains.
        for _ in range(len(points)+1):
            changed=False
            for kind,a in tokens:
                if kind=='midp' and len(a)==3 and a[1] in coords and a[2] in coords:
                    v=tuple((x+y)/2 for x,y in zip(coords[a[1]],coords[a[2]]))
                    if a[0] not in coords:coords[a[0]]=v;changed=True
                if kind=='overlap' and len(a)==2:
                    if a[0] in coords and a[1] not in coords:coords[a[1]]=coords[a[0]];changed=True
                    if a[1] in coords and a[0] not in coords:coords[a[0]]=coords[a[1]];changed=True
            if not changed:break
        if len(coords)<len(points):continue
        yield coords


def exact_counterexample(hypotheses,goal,attempts=100,seed=1729,deadline=None):
    for i,coords in enumerate(_coordinate_assignments(hypotheses,seed,attempts)):
        if deadline is not None and time.monotonic()>deadline:break
        try:
            ev=ExactFactEvaluator(coords)
            if ev.all_hold(hypotheses) and not ev.check(goal):
                data={name:[str(v[0]),str(v[1])] for name,v in sorted(coords.items())}
                return {'coordinates':data,'attempt_index':i,
                        'reason':'all premises hold and goal is false in exact rationals'}
        except (ValueError,KeyError,DomainError,UnsupportedPredicate):continue
    return None


class DeterministicGeometrySolver:
    """Separate actual certificates from conditional algebra and heuristic search."""
    def __init__(self,budget:DeterministicBudget=DeterministicBudget(),
                 source_path=None,seed=1729):
        self.budget=budget;self.source_path=source_path
        self.seed=int(seed)
    def prove(self,hypotheses:Sequence[str],goal:str,provided_coordinates=None):
        start=time.monotonic();deadline=start+self.budget.seconds
        hs=tuple(dict.fromkeys(' '.join(x.strip().lower().split()) for x in hypotheses))
        goal=' '.join(goal.strip().lower().split())
        if not goal:raise ValueError('empty goal')
        ledger=GuardLedger(hs)
        attempts=[]
        if ledger.contradictions:
            return self._make('invalid_problem',hs,goal,'input_guards',None,(),None,
                    [{'reason':'; '.join(ledger.contradictions)}],start)
        if goal in hs:
            return self._make('proved',hs,goal,'assumption',
                    {'schema':'geoforge-assumption-proof-v1','goal':goal},(),None,
                    [{'method':'assumption','status':'proved'}],start)
        if self.source_path:
            try:
                from .reasoning_search import load_engine
                core=load_engine(str(self.source_path))
                facts=tuple(core.GeometryParser().fact(s) for s in hs)
                motor=core.CertifiedDDAR2Engine(facts,maxfacts=self.budget.max_facts,deadline=deadline).close()
                cert=motor.certificate(core.GeometryParser().fact(goal))
                attempts.append({'method':'dd/verified','status':'proved' if cert else 'not_proven',
                                 'derived_facts':len(motor.known)})
                if cert:
                    return self._make('proved',hs,goal,'ddar_certified',
                        {'schema':'geoforge-deduction-wrapper-v1','certificate':cert.to_dict()},(),None,attempts,start)
            except Exception as ex:
                attempts.append({'method':'dd/verified','status':'unavailable','reason':str(ex)[:250]})
        conditional=None;pending=()
        try:
            status,proof,guards,stats=polynomial_guard_strategy(hs,goal,self.budget,deadline)
            attempts.append({'method':'buchberger/witness','status':status,**stats})
            if status=='proved':
                return self._make('proved',hs,goal,'polynomial_certificate',proof,(),None,attempts,start)
            if status=='conditional': conditional=proof;pending=guards
        except (UnsupportedPredicate,ValueError,KeyError,DomainError) as ex:
            attempts.append({'method':'buchberger/witness','status':'unsupported',
                             'reason':str(ex)[:250]})
        # Saturation uses *only named, logically implied nonzero guards*.
        # The additional inverse variable cannot appear as an unverified axiom.
        if time.monotonic()+0.1<deadline and len(hs)<=12:
            try:
                from .saturation_solver import SaturatedGeometryProver
                from .deterministic_ideal import IdealBudget
                seconds=min(1.25,max(.05,deadline-time.monotonic()-0.05))
                saturated=SaturatedGeometryProver(IdealBudget(seconds=seconds,
                    max_pairs=min(60,self.budget.max_pairs),
                    max_basis=min(40,self.budget.max_basis),
                    max_terms=min(900,self.budget.max_terms),
                    max_reductions=min(3000,self.budget.max_reductions)),
                    max_points=min(7,self.budget.max_points),max_guard_factors=3).prove(hs,goal)
                attempts.append({'method':'saturation/certified','status':saturated.status,
                                 'reason':saturated.reason,'pairs':saturated.explored_pairs})
                if saturated.status=='proved':
                    return self._make('proved',hs,goal,'saturated_certificate',
                        saturated.certificate,(),None,attempts,start)
                if saturated.status=='conditional' and conditional is None:
                    conditional=saturated.certificate;pending=saturated.extra_side_conditions
            except (ValueError,KeyError,DomainError,UnsupportedPredicate) as ex:
                attempts.append({'method':'saturation/certified','status':'unsupported',
                                 'reason':str(ex)[:180]})
        # An exact countermodel *overrides* conditional polynomial membership:
        # an algebraic equality alone may not imply the predicate semantics.
        if provided_coordinates is not None:
            try:
                evaluator=ExactFactEvaluator(provided_coordinates)
                if evaluator.all_hold(hs) and not evaluator.check(goal):
                    coords={k:[str(x) for x in p] for k,p in provided_coordinates.items()}
                    return self._make('counterexample',hs,goal,'rational_model',None,(),
                        {'coordinates':coords,'provided':True},attempts,start)
            except (UnsupportedPredicate,ValueError,KeyError,DomainError):pass
        if time.monotonic()<deadline:
            counter=exact_counterexample(hs,goal,self.budget.sample_attempts,
                                self.seed,deadline)
            attempts.append({'method':'rational_model_search',
                             'status':'found' if counter else 'not_found'})
            if counter:return self._make('counterexample',hs,goal,'rational_model',
                                      None,(),counter,attempts,start)
        if conditional:
            method=('saturated_certificate' if conditional.get('schema')=='geoforge-saturated-coordinate-v1' else 'polynomial_certificate')
            return self._make('conditional',hs,goal,method,
                              conditional,pending,None,attempts,start)
        return self._make('unknown',hs,goal,'bounded_portfolio',None,(),None,attempts,start)
    @staticmethod
    def _make(status,hs,goal,method,certificate,guards,counter,attempts,start):
        return DeterministicResult(status,goal,hs,method,certificate,
                   tuple(guards),counter,tuple(attempts),time.monotonic()-start)


class IndependentResultChecker:
    """Replay proof against source declarations, not just stored polynomials."""
    def __init__(self,core_path=None):self.core_path=core_path
    def verify(self,data):
        if isinstance(data,DeterministicResult):data=data.to_dict()
        hs=tuple(data['hypotheses']);goal=data['goal'];method=data['method'];status=data['status']
        if status=='proved' and method=='assumption':return goal in hs
        if status=='counterexample':
            coords=data['counterexample']['coordinates'];ev=ExactFactEvaluator(coords)
            return ev.all_hold(hs) and not ev.check(goal)
        if method=='ddar_certified' and status=='proved':
            if self.core_path is None:return False
            from .reasoning_search import load_engine
            core=load_engine(str(self.core_path))
            raw=data['certificate']['certificate']
            cert=core.ProofCertificate.from_dict(raw)
            ok,_=core.ProofCheckerV2().verify(cert)
            return ok and set(map(str,cert.assumptions))==set(hs) and str(cert.goal)==str(core.GeometryCanonicalizer().fact(core.GeometryParser().fact(goal)))
        if method=='saturated_certificate' and status in ('proved','conditional'):
            from .saturation_solver import SaturationCertificateChecker
            cert=data['certificate']
            if not SaturationCertificateChecker().verify(hs,goal,cert):return False
            try:
                tokens=[split_fact(x) for x in (*hs,goal)]
                compiler=CoordinatePredicateCompiler(sorted({p for _,a in tokens for p in a}))
                g=compiler.compile(*tokens[-1])
                missing=GuardLedger(hs).unresolved(g.nondegeneracy)
                return ((status=='proved') == (not missing)) and tuple(data['unresolved_guards'])==missing
            except (UnsupportedPredicate,DomainError,ValueError):return False
        if method=='polynomial_certificate' and status in ('proved','conditional'):
            p=data['certificate']
            if p.get('schema')!='geoforge-coordinate-theorem-v1':return False
            try:
                all_tokens=[split_fact(x) for x in (*hs,goal)]
                names=sorted({z for _,a in all_tokens for z in a})
                compiler=CoordinatePredicateCompiler(names)
                hypotheses=[compiler.compile(k,a) for k,a in all_tokens[:-1]
                            if k not in ('distinct','noverlap','ncoll','sameclock','lessthan')]
                g=compiler.compile(*all_tokens[-1]);axioms=tuple(pol for h in hypotheses for pol in h.polynomials)
                if len(p['witnesses'])!=len(g.polynomials):return False
                if p['compiled_axiom_labels']!=[h.source for h in hypotheses]:return False
                if p['compiled_goal_label']!=g.source:return False
                if p['side_guards']!=list(g.nondegeneracy):return False
                for raw,target in zip(p['witnesses'],g.polynomials):
                    if raw['schema']!='geoforge-ideal-v1':return False
                    if tuple(map(polynomial_from_object,raw['axioms']))!=axioms:return False
                    if polynomial_from_object(raw['target'])!=target:return False
                    if not verify_certificate_json(json.dumps(raw)):return False
                unresolved=GuardLedger(hs).unresolved(g.nondegeneracy)
                if tuple(data['unresolved_guards'])!=unresolved:return False
                return (status=='proved') == (not unresolved)
            except (KeyError,ValueError,DomainError,UnsupportedPredicate,TypeError):return False
        return False
