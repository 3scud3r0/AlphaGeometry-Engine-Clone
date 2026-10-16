#!/usr/bin/env python3
"""Rabinowitsch saturation certificates for Euclidean nonzero side conditions.

If exact polynomial equations f_i=0 and nonzero polynomials q_j !=0 hold,
add a fresh variable t and equation t*(product q_j)-1=0. A witness for the
original goal polynomial in this ideal proves the goal on the original
(non-degenerate) real domain. Every certificate includes the extra axiom and
can be replayed against the declarations of source guards.

This increases expressive power without a learned model; bounded ideal search
is sound but incomplete and can be very expensive.
"""
from __future__ import annotations
from dataclasses import dataclass
from collections import Counter
from typing import Sequence
from .geometry_exact import Polynomial,DomainError
from .symbolic_coordinates import CoordinatePredicateCompiler,UnsupportedPredicate
from .deterministic_ideal import (ExactIdealEngine,IdealBudget,
                                  certificate_to_json,verify_certificate_json,
                                  polynomial_from_object)
from .deterministic_solver import GuardLedger,split_fact
import json,time


def lift(polynomial):
    n=polynomial.nvars+1
    return Polynomial.from_dict(n,{(*m,0):c for m,c in polynomial.terms})


def nonzero_guard_expression(compiler,text):
    """Algebraic polynomial known nonzero from a mathematically stated guard."""
    k,a=split_fact(text);s=compiler.symbols
    if k in ('distinct','noverlap') and len(a)==2:
        return s.length_squared(*a)
    if k=='ncoll' and len(a)==3:
        return s.area2(*a)
    raise UnsupportedPredicate('not a recognized nonzero polynomial guard: '+text)


def gather_guards(hypotheses,compiler,limit=8):
    ledger=GuardLedger(hypotheses);candidates=set()
    # Use explicit guards and every known pair/triple implied by geometrical
    # givens. No numeric observations are considered.
    for a,b in ledger.distinct:
        candidates.add('distinct '+a+' '+b)
    for trio in ledger.ncoll:
        candidates.add('ncoll '+' '.join(sorted(trio)))
    result=[]
    for name in sorted(candidates,key=lambda x:(0 if x.startswith('ncoll') else 1,x)):
        pol=nonzero_guard_expression(compiler,name)
        if not pol:continue
        result.append((name,pol))
        if len(result)>=limit:break
    return tuple(result)

@dataclass(frozen=True)
class SaturationAttempt:
    status:str
    theorem:str
    certificate:dict|None
    guards:tuple[str,...]
    extra_side_conditions:tuple[str,...]
    reason:str
    explored_pairs:int


class SaturatedGeometryProver:
    def __init__(self,budget:IdealBudget=IdealBudget(seconds=5,max_pairs=100),
                 max_points=8,max_guard_factors=5):
        self.budget=budget;self.max_points=max_points
        self.max_guard_factors=max_guard_factors
    def prove(self,hypotheses:Sequence[str],goal:str):
        tokens=[split_fact(x) for x in (*hypotheses,goal)]
        points=sorted({p for _,names in tokens for p in names})
        if not points or len(points)>self.max_points:
            return SaturationAttempt('unknown',goal,None,(),(),'point budget',0)
        comp=CoordinatePredicateCompiler(points)
        try:
            source=[comp.compile(k,a) for k,a in tokens[:-1]
                    if k not in ('distinct','noverlap','ncoll','sameclock','lessthan')]
            target=comp.compile(*tokens[-1])
        except (UnsupportedPredicate,KeyError,ValueError) as exc:
            return SaturationAttempt('unsupported',goal,None,(),(),str(exc),0)
        guards=gather_guards(hypotheses,comp,self.max_guard_factors)
        if not guards:
            return SaturationAttempt('unknown',goal,None,(),(),'no nonzero guards',0)
        product=Polynomial.constant(comp.symbols.nvars,1)
        for name,p in guards:product=product*p
        n=comp.symbols.nvars+1;t=Polynomial.variable(n,n-1)
        u=t*lift(product)-Polynomial.constant(n,1)
        lifted_axioms=tuple(lift(pol) for item in source for pol in item.polynomials)+(u,)
        certificates=[];count=0
        for p in target.polynomials:
            out=ExactIdealEngine(self.budget).membership(lifted_axioms,lift(p))
            count+=out.explored_pairs
            if out.status!='proved':
                return SaturationAttempt('unknown',goal,None,
                     tuple(x for x,_ in guards),(),out.reason,count)
            certificates.append(json.loads(certificate_to_json(out.certificate)))
        unresolved=GuardLedger(hypotheses).unresolved(target.nondegeneracy)
        record={'schema':'geoforge-saturated-coordinate-v1',
                'guards':[x for x,_ in guards],
                'goal_side_conditions':list(target.nondegeneracy),
                'source_equation_count':len(lifted_axioms)-1,
                'witnesses':certificates}
        return SaturationAttempt('proved' if not unresolved else 'conditional',goal,
                 record,tuple(x for x,_ in guards),unresolved,
                 'saturated identity certified',count)


class SaturationCertificateChecker:
    """Recompile every premise, nonzero guard and goal from the input strings."""
    def verify(self,hypotheses,goal,record):
        try:
            if record.get('schema')!='geoforge-saturated-coordinate-v1':return False
            tokens=[split_fact(t) for t in (*hypotheses,goal)]
            pts=sorted({p for _,a in tokens for p in a})
            comp=CoordinatePredicateCompiler(pts)
            source=[comp.compile(k,a) for k,a in tokens[:-1]
                    if k not in ('distinct','noverlap','ncoll','sameclock','lessthan')]
            target=comp.compile(*tokens[-1]);ledger=GuardLedger(hypotheses)
            if record['goal_side_conditions']!=list(target.nondegeneracy):return False
            g_names=record['guards']
            if len(g_names)!=len(set(g_names)):return False
            if any(not ledger.entails(s) for s in g_names):return False
            product=Polynomial.constant(comp.symbols.nvars,1)
            for g in g_names:product=product*nonzero_guard_expression(comp,g)
            n=comp.symbols.nvars+1
            new_axiom=Polynomial.variable(n,n-1)*lift(product)-Polynomial.constant(n,1)
            axioms=tuple(lift(p) for f in source for p in f.polynomials)+(new_axiom,)
            if record['source_equation_count']!=len(axioms)-1:return False
            if len(target.polynomials)!=len(record['witnesses']):return False
            for objective,raw in zip(target.polynomials,record['witnesses']):
                if tuple(map(polynomial_from_object,raw['axioms']))!=axioms:return False
                if polynomial_from_object(raw['target'])!=lift(objective):return False
                if not verify_certificate_json(json.dumps(raw)):return False
            return True
        except (KeyError,ValueError,TypeError,UnsupportedPredicate,DomainError):return False
