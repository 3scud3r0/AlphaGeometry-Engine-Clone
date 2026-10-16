#!/usr/bin/env python3
"""Fast affine-algebra tactic with exact polynomial identity certificates.

Given linear constraints in coordinate variables (midpoints, coincidences,
linear coordinate construction), build a rational row-echelon basis; divide an
arbitrary polynomial goal by this basis and reconstruct literal multipliers of
the ORIGINAL source equations. This is a safe algebraic proof, not a numeric
check. Nonlinear premises are ignored by this tactic, never assumed as linear.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as Q
from typing import Sequence
from .geometry_exact import Polynomial,DomainError,BudgetExceeded
from .deterministic_ideal import IdealCertificate


def linear_coefficients(pol):
    if not pol:return (Q(0),)*(pol.nvars+1)
    vector=[Q(0)]*(pol.nvars+1)
    for mon,coeff in pol.terms:
        degree=sum(mon)
        if degree==0:vector[-1]+=coeff
        elif degree==1:
            index=mon.index(1)
            vector[index]+=coeff
        else:return None
    return tuple(vector)


def multiply_poly_by_rational(poly,c):return poly.scale(Q(c))

@dataclass(frozen=True)
class AffineRow:
    pivot:int
    expression:Polynomial
    provenance:tuple[Q,...]

@dataclass(frozen=True)
class AffineProofAttempt:
    status:str
    certificate:IdealCertificate|None
    rank:int
    used_premises:int
    reason:str

class AffineIdealTactic:
    """RREF over Q with provenance back to the provided polynomial list."""
    def __init__(self,max_rows=400,max_steps=6000):
        if max_rows<1 or max_steps<1:raise ValueError('positive budget required')
        self.max_rows=max_rows;self.max_steps=max_steps
    def prove(self,axioms:Sequence[Polynomial],goal:Polynomial):
        source=tuple(axioms);n=goal.nvars
        if any(a.nvars!=n for a in source):raise DomainError('incompatible rings')
        if len(source)>self.max_rows:
            return AffineProofAttempt('resource_exhausted',None,0,0,'too many equations')
        rows={};linear_used=0
        for i,pol in enumerate(source):
            coeff=linear_coefficients(pol)
            if coeff is None or not pol:continue
            linear_used+=1
            combination=[Q(0)]*len(source);combination[i]=Q(1)
            current=pol
            for pivot,old in sorted(rows.items()):
                v=linear_coefficients(current)[pivot]
                if v:
                    current=current-old.expression.scale(v)
                    combination=[a-v*b for a,b in zip(combination,old.provenance)]
            if not current:continue
            vec=linear_coefficients(current)
            pivot=next((i for i,c in enumerate(vec[:-1]) if c),None)
            if pivot is None:
                # A nonzero constant equation makes the algebraic ideal the
                # unit ideal. Reporting theorem from inconsistent premises is
                # logically vacuous but not geometrically useful; abstain.
                return AffineProofAttempt('inconsistent_linear_equations',None,
                                          len(rows),linear_used,'constant contradiction')
            value=vec[pivot]
            row=AffineRow(pivot,current.scale(1/value),tuple(c/value for c in combination))
            rows[pivot]=row
            for other,old in tuple(rows.items()):
                if other==pivot:continue
                val=linear_coefficients(old.expression)[pivot]
                if val:
                    rows[other]=AffineRow(other,old.expression-row.expression.scale(val),
                           tuple(a-val*b for a,b in zip(old.provenance,row.provenance)))
        basis=[rows[k] for k in sorted(rows)]
        if not basis:
            if goal:return AffineProofAttempt('unknown',None,0,linear_used,'no linear equations')
            return AffineProofAttempt('proved',IdealCertificate(source,goal,
                         tuple(Polynomial.constant(n,0) for _ in source)),0,linear_used,'zero identity')
        try:
            quotients,remainder=goal.divided_remainder([r.expression for r in basis],self.max_steps)
        except BudgetExceeded:
            return AffineProofAttempt('resource_exhausted',None,len(rows),linear_used,'reduction budget')
        if remainder:
            return AffineProofAttempt('unknown',None,len(rows),linear_used,'nonzero affine normal form')
        multipliers=[]
        for i in range(len(source)):
            m=Polynomial.constant(n,0)
            for q,row in zip(quotients,basis):
                if row.provenance[i]:m+=q.scale(row.provenance[i])
            multipliers.append(m)
        certificate=IdealCertificate(source,goal,tuple(multipliers))
        if not certificate.verify():raise AssertionError('affine linear combination failed to replay')
        return AffineProofAttempt('proved',certificate,len(rows),linear_used,
                                  'verified affine polynomial identity')
