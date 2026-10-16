#!/usr/bin/env python3
"""Exact, independently replayable ideal-membership certificates over Q[x].

This is a *bounded* Buchberger implementation, not an oracle for real algebraic
geometry: ideal membership proves polynomial consequences only. Positivity,
non-zero side conditions and real radical membership require other tactics.
Every successful result carries a literal polynomial identity witness and can
be checked without executing the search algorithm.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from collections import deque
from fractions import Fraction
from typing import Sequence
import json
import time
from .geometry_exact import Polynomial, DomainError, BudgetExceeded, monomial_lcm


def _zero(n): return Polynomial.constant(n,0)
def _one(n): return Polynomial.constant(n,1)
def _divides(u,v): return all(a<=b for a,b in zip(u,v))
def _monomial_quotient(a,b):
    if not _divides(b,a):raise ValueError('non-divisible monomials')
    return tuple(x-y for x,y in zip(a,b))

@dataclass(frozen=True)
class IdealBudget:
    max_pairs:int=500
    max_basis:int=150
    max_terms:int=5000
    max_reductions:int=100000
    seconds:float=10.
    def __post_init__(self):
        if any(getattr(self,n)<=0 for n in ('max_pairs','max_basis','max_terms','max_reductions','seconds')):
            raise ValueError('ideal budgets must be positive')

@dataclass(frozen=True)
class WitnessRow:
    polynomial:Polynomial
    coefficients:tuple[Polynomial,...]

@dataclass(frozen=True)
class IdealCertificate:
    axioms:tuple[Polynomial,...]
    target:Polynomial
    multipliers:tuple[Polynomial,...]
    explored_pairs:int=0
    def verify(self):
        if len(self.axioms)!=len(self.multipliers):return False
        if any(x.nvars!=self.target.nvars for x in (*self.axioms,*self.multipliers)):
            return False
        return sum((a*m for a,m in zip(self.axioms,self.multipliers)),_zero(self.target.nvars))==self.target
    def stats(self):
        return {'axioms':len(self.axioms),'variables':self.target.nvars,
                'witness_terms':sum(len(p.terms) for p in self.multipliers),
                'pairs':self.explored_pairs,'replay_valid':self.verify()}

@dataclass(frozen=True)
class IdealAttempt:
    status:str
    certificate:IdealCertificate|None
    explored_pairs:int
    reductions:int
    basis_size:int
    reason:str
    def __post_init__(self):
        if self.status=='proved' and (self.certificate is None or not self.certificate.verify()):
            raise AssertionError('cannot expose an unverified proof')

class ExactIdealEngine:
    """Buchberger with provenance vectors and a global monotonic deadline."""
    def __init__(self,budget:IdealBudget=IdealBudget()): self.budget=budget
    def membership(self,axioms:Sequence[Polynomial],target:Polynomial):
        A=tuple(axioms);n=target.nvars
        if any(p.nvars!=n for p in A):raise DomainError('incompatible rings')
        if not target:
            return IdealAttempt('proved',IdealCertificate(A,target,tuple(_zero(n) for _ in A)),0,0,0,'zero identity')
        if not A or not any(A):return IdealAttempt('unknown',None,0,0,0,'empty ideal')
        budget=self.budget;deadline=time.monotonic()+budget.seconds
        rows=[]
        for i,p in enumerate(A):
            if p:
                _,lead=p.leading();f=p.scale(1/lead)
                cof=tuple(_one(n).scale(1/lead) if j==i else _zero(n) for j in range(len(A)))
                rows.append(WitnessRow(f,cof))
        pairs=deque((i,j) for i in range(len(rows)) for j in range(i+1,len(rows)))
        examined=0;reductions=0
        try:
            while pairs:
                if time.monotonic()>deadline:raise BudgetExceeded('wall clock limit')
                if examined>=budget.max_pairs:raise BudgetExceeded('S-pair limit')
                if len(rows)>=budget.max_basis:raise BudgetExceeded('basis limit')
                i,j=pairs.popleft();examined+=1
                f,g=rows[i],rows[j]
                fm,fc=f.polynomial.leading();gm,gc=g.polynomial.leading()
                # Buchberger's product criterion: the S-polynomial will reduce to zero.
                if all(min(a,b)==0 for a,b in zip(fm,gm)):continue
                lcm=monomial_lcm(fm,gm)
                mf=_monomial_quotient(lcm,fm);mg=_monomial_quotient(lcm,gm)
                factor_f=Polynomial.from_dict(n,{mf:Fraction(1,1)/fc})
                factor_g=Polynomial.from_dict(n,{mg:Fraction(1,1)/gc})
                poly=f.polynomial*factor_f-g.polynomial*factor_g
                coef=tuple(a*factor_f-b*factor_g for a,b in zip(f.coefficients,g.coefficients))
                if len(poly.terms)>budget.max_terms:raise BudgetExceeded('intermediate term limit')
                remainder,coefficients,consumed=self._reduce(poly,coef,rows,deadline,budget)
                reductions+=consumed
                if reductions>budget.max_reductions:raise BudgetExceeded('total reductions limit')
                if remainder:
                    pivot=remainder.leading()[1]
                    normalized=remainder.scale(1/pivot)
                    if len(normalized.terms)>budget.max_terms:raise BudgetExceeded('normal form term limit')
                    row=WitnessRow(normalized,tuple(x.scale(1/pivot) for x in coefficients))
                    if not any(q.polynomial==row.polynomial for q in rows):
                        k=len(rows);rows.append(row)
                        pairs.extend((p,k) for p in range(k))
            rem,cof,extra=self._reduce(target,tuple(_zero(n) for _ in A),rows,deadline,budget)
            reductions+=extra
            if rem:
                return IdealAttempt('unknown',None,examined,reductions,len(rows),'nonzero normal form')
            multipliers=tuple(-c for c in cof)
            cert=IdealCertificate(A,target,multipliers,examined)
            return IdealAttempt('proved',cert,examined,reductions,len(rows),'verified polynomial identity')
        except (BudgetExceeded,OverflowError) as exc:
            return IdealAttempt('resource_exhausted',None,examined,reductions,len(rows),str(exc))
    @staticmethod
    def _reduce(poly,coefficients,rows,deadline,budget):
        """Maintain polynomial = original combination + remainder via provenance.

        At entry poly = sum(coef_i * axiom_i). Reducing by q represented as
        sum(row.coef_i * axiom_i) updates the witness accordingly.
        """
        current=poly;coeff=list(coefficients)
        remainder=_zero(poly.nvars);steps=0
        while current:
            if steps>=budget.max_reductions or time.monotonic()>deadline:
                raise BudgetExceeded('reduction limit')
            if len(current.terms)>budget.max_terms:raise BudgetExceeded('intermediate growth')
            lm,lc=current.leading()
            selected=None
            for row in rows:
                rm,rc=row.polynomial.leading()
                if _divides(rm,lm):selected=(row,rm,rc);break
            if selected is None:
                mon=Polynomial.from_dict(poly.nvars,{lm:lc})
                remainder+=mon;current-=mon
            else:
                row,rm,rc=selected
                mon=Polynomial.from_dict(poly.nvars,{_monomial_quotient(lm,rm):lc/rc})
                current-=mon*row.polynomial
                coeff=[a-b*mon for a,b in zip(coeff,row.coefficients)]
            steps+=1
        return remainder,tuple(coeff),steps


def polynomial_to_object(p:Polynomial):
    return {'nvars':p.nvars,'terms':[[list(m),str(c)] for m,c in p.terms]}

def polynomial_from_object(obj):
    return Polynomial.from_dict(int(obj['nvars']),{
        tuple(int(x) for x in mono):Fraction(coef) for mono,coef in obj['terms']})

def certificate_to_json(cert:IdealCertificate):
    if not cert.verify():raise ValueError('invalid certificate')
    return json.dumps({'schema':'geoforge-ideal-v1','axioms':[polynomial_to_object(p) for p in cert.axioms],
        'target':polynomial_to_object(cert.target),
        'multipliers':[polynomial_to_object(p) for p in cert.multipliers],
        'explored_pairs':cert.explored_pairs},sort_keys=True)

def verify_certificate_json(text):
    try:
        data=json.loads(text)
        if data.get('schema')!='geoforge-ideal-v1':return False
        c=IdealCertificate(tuple(map(polynomial_from_object,data['axioms'])),
                           polynomial_from_object(data['target']),
                           tuple(map(polynomial_from_object,data['multipliers'])),
                           int(data.get('explored_pairs',0)))
        return c.verify()
    except (ValueError,TypeError,KeyError,OverflowError):return False
