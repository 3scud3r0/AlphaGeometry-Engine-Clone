#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rational polynomial translation of Euclidean plane predicates.

Only equality consequences can be certified from polynomial ideals.  The
Groebner method here is exact but incomplete when an inequality/nondegeneracy
hypothesis matters; such inputs must be explicitly marked as unsupported.
Avoid accepting a polynomial ideal result from a degenerate component.
"""
from __future__ import annotations
from dataclasses import dataclass,field
from fractions import Fraction as Q
from itertools import combinations
from collections import Counter,defaultdict
from typing import Any, Mapping, Sequence
import hashlib
import json
import math
try:
    from .geometry_exact import Polynomial,prove_polynomial_membership,DomainError,BudgetExceeded
except ImportError:  # standalone execution compatibility
    from geometry_exact import Polynomial,prove_polynomial_membership,DomainError,BudgetExceeded


class UnsupportedPredicate(ValueError):pass


@dataclass(frozen=True)
class CoordinateEquation:
    source:str
    polynomials:tuple[Polynomial,...]
    nondegeneracy:tuple[str,...]=()


class CoordinateSymbolTable:
    """Maps symbolic points to x/y polynomial coordinate pairs."""
    def __init__(self,points:Sequence[str]):
        names=sorted(set(points))
        if not names:raise DomainError('empty point list')
        if any(not n or not n[0].isalpha() or not n.replace('_','').isalnum() for n in names):
            raise DomainError('invalid point identifier')
        self.names=tuple(names)
        self.index={n:i for i,n in enumerate(names)}
        self.nvars=2*len(names)
    def xy(self,name:str):
        if name not in self.index:raise KeyError(name)
        index=2*self.index[name]
        return Polynomial.variable(self.nvars,index),Polynomial.variable(self.nvars,index+1)
    def difference(self,a,b):
        x1,y1=self.xy(a);x2,y2=self.xy(b)
        return x1-x2,y1-y2
    def length_squared(self,a,b):
        u,v=self.difference(a,b)
        return u*u+v*v
    def dot(self,a,b,c,d):
        u,v=self.difference(b,a);w,z=self.difference(d,c)
        return u*w+v*z
    def det(self,a,b,c,d):
        u,v=self.difference(b,a);w,z=self.difference(d,c)
        return u*z-v*w
    def area2(self,a,b,c):
        return self.det(a,b,a,c)


class CoordinatePredicateCompiler:
    """Algebraic encodings valid under explicit nondegeneracy conditions."""
    SUPPORTED=frozenset({'coll','para','perp','cong','midp','overlap','cyclic','eqratio'})
    def __init__(self,points:Sequence[str]):
        self.symbols=CoordinateSymbolTable(points)
    def compile(self,kind:str,args:Sequence[str])->CoordinateEquation:
        k=kind.lower();a=tuple(args);s=self.symbols
        if any(n not in s.index for n in a):raise KeyError('unknown point')
        if k=='coll' and len(a)==3:
            return CoordinateEquation(k+' '+' '.join(a),(s.area2(*a),),
                (f'distinct {a[0]} {a[1]}',))
        if k=='para' and len(a)==4:
            return CoordinateEquation(k+' '+' '.join(a),(s.det(*a),),
                (f'distinct {a[0]} {a[1]}',f'distinct {a[2]} {a[3]}'))
        if k=='perp' and len(a)==4:
            return CoordinateEquation(k+' '+' '.join(a),(s.dot(*a),),
                (f'distinct {a[0]} {a[1]}',f'distinct {a[2]} {a[3]}'))
        if k=='cong' and len(a)==4:
            return CoordinateEquation(k+' '+' '.join(a),(
                s.length_squared(*a[:2])-s.length_squared(*a[2:]),),())
        if k=='midp' and len(a)==3:
            xm,ym=s.xy(a[0]);xa,ya=s.xy(a[1]);xb,yb=s.xy(a[2])
            return CoordinateEquation(k+' '+' '.join(a),
                                      (2*xm-xa-xb,2*ym-ya-yb),())
        if k=='overlap' and len(a)==2:
            xa,ya=s.xy(a[0]);xb,yb=s.xy(a[1])
            return CoordinateEquation(k+' '+' '.join(a),(xa-xb,ya-yb),())
        if k=='cyclic' and len(a)==4:
            # Incircle determinant; no division/denominators.
            mat=[]
            for name in a:
                x,y=s.xy(name)
                mat.append((x*x+y*y,x,y,Polynomial.constant(s.nvars,1)))
            determinant=self._determinant(mat)
            return CoordinateEquation(k+' '+' '.join(a),(determinant,),
                ('ncoll '+' '.join(a[:3]),))
        if k=='eqratio' and len(a)==8:
            # Squared ratio equations are only necessary, not sufficient for
            # directed ratios; if lengths positive they are equivalent.
            lengths=[s.length_squared(*a[i:i+2]) for i in range(0,8,2)]
            pol=lengths[0]*lengths[3]-lengths[1]*lengths[2]
            return CoordinateEquation(k+' '+' '.join(a),(pol,),tuple(
                f'distinct {a[i]} {a[i+1]}' for i in range(0,8,2)))
        raise UnsupportedPredicate(f'unsupported coordinate predicate: {kind}/{len(a)}')
    @staticmethod
    def _determinant(a):
        n=len(a)
        if n==1:return a[0][0]
        accum=Polynomial.constant(a[0][0].nvars,0)
        for i,v in enumerate(a[0]):
            smaller=[row[:i]+row[i+1:] for row in a[1:]]
            accum=accum+(-1)**i*v*CoordinatePredicateCompiler._determinant(smaller)
        return accum


@dataclass(frozen=True)
class AlgebraicProofResult:
    status:str
    theorem:str
    hypotheses:tuple[str,...]
    polynomial_count:int
    groebner_basis_size:int
    reductions:int
    assumptions_needed:tuple[str,...]
    warnings:tuple[str,...]
    def to_dict(self):return dict(self.__dict__)


class AlgebraicCoordinateProver:
    """Proves purely polynomial entailment; does not discharge side conditions."""
    def __init__(self,max_pairs=100,max_points=12):
        self.max_pairs=max_pairs;self.max_points=max_points
    def prove(self,hypotheses:Sequence[str],goal:str):
        parts=[x.split() for x in (*hypotheses,goal)]
        points={t for a in parts for t in a[1:]}
        if len(points)>self.max_points:raise BudgetExceeded('too many points')
        compiler=CoordinatePredicateCompiler(sorted(points))
        hyps=[compiler.compile(x[0],x[1:]) for x in parts[:-1]]
        target=compiler.compile(parts[-1][0],parts[-1][1:])
        assumptions=tuple(sorted({cond for x in (*hyps,target) for cond in x.nondegeneracy}))
        polynomials=[p for f in hyps for p in f.polynomials]
        if not polynomials:
            return AlgebraicProofResult('not_proven',goal,tuple(hypotheses),0,0,0,
                  assumptions,('No polynomial hypotheses supplied',))
        total=0;size=0
        for objective in target.polynomials:
            success,info,reason=prove_polynomial_membership(objective,polynomials,
                                                              max_pairs=self.max_pairs)
            size=max(size,len(info.basis));total+=info.reductions
            if not success:
                return AlgebraicProofResult('unknown',goal,tuple(hypotheses),
                    len(polynomials),size,total,assumptions,
                    ('Membership attempt: '+reason,))
        # Even if polynomial identity is proved, side conditions may not be
        # contained in the input. These must be checked by a separate kernel.
        have=set(hypotheses)
        needed=tuple(x for x in assumptions if x not in have)
        status='conditional_polynomial_identity' if needed else 'polynomial_identity_proven'
        return AlgebraicProofResult(status,goal,tuple(hypotheses),len(polynomials),
                                    size,total,needed,())


class PolynomialIdentityVerifier:
    """Checks explicit integer/rational polynomial identities exactly."""
    @staticmethod
    def equal(lhs:Polynomial,rhs:Polynomial)->bool:return lhs==rhs
    @staticmethod
    def linear_combination(target:Polynomial,
                           premises:Sequence[Polynomial],multipliers:Sequence[Polynomial]):
        if len(premises)!=len(multipliers):raise ValueError('bad witness length')
        if any(p.nvars!=target.nvars for p in (*premises,*multipliers)):
            raise DomainError('polynomial ring mismatch')
        return target==sum((a*b for a,b in zip(premises,multipliers)),
                           Polynomial.constant(target.nvars,0))
    @staticmethod
    def verify_division(target:Polynomial,divisors:Sequence[Polynomial],
                        quotients:Sequence[Polynomial],remainder:Polynomial):
        if len(divisors)!=len(quotients):return False
        return target==sum((d*q for d,q in zip(divisors,quotients)),
                           remainder)


class CoordinateNormalization:
    """Canonical affine normalizations that preserve polynomial theorem validity."""
    @staticmethod
    def translate(symbols:CoordinateSymbolTable,points:Mapping[str,tuple[Q,Q]],shift):
        sx,sy=map(Q,shift)
        return {k:(Q(x)+sx,Q(y)+sy) for k,(x,y) in points.items()}
    @staticmethod
    def uniformly_scale(points,scale):
        s=Q(scale)
        if s==0:raise DomainError('zero uniform scale')
        return {k:(Q(x)*s,Q(y)*s) for k,(x,y) in points.items()}
    @staticmethod
    def rotate90(points):
        return {k:(-Q(y),Q(x)) for k,(x,y) in points.items()}
    @staticmethod
    def reflect_x(points):
        return {k:(Q(x),-Q(y)) for k,(x,y) in points.items()}


class NumericalEquationValidator:
    """Computes exact residuals on rational coordinate realizations."""
    @staticmethod
    def check(kind,args,points):
        compiler=CoordinatePredicateCompiler(tuple(points))
        eq=compiler.compile(kind,args)
        values=[]
        for key in compiler.symbols.names:
            if key not in points:raise KeyError(key)
            values.extend(map(Q,points[key]))
        return all(p.eval(values)==0 for p in eq.polynomials)
    @staticmethod
    def residuals(kind,args,points):
        compiler=CoordinatePredicateCompiler(tuple(points))
        eq=compiler.compile(kind,args)
        values=[]
        for key in compiler.symbols.names:values.extend(map(Q,points[key]))
        return tuple(p.eval(values) for p in eq.polynomials)


class SystemSolvabilityGuard:
    """Degeneracy checks necessary before treating polynomial zeros as geometry."""
    def __init__(self,points:Mapping[str,tuple[Q,Q]]):
        self.points={k:(Q(x),Q(y)) for k,(x,y) in points.items()}
    def verify_condition(self,text):
        items=text.split();name=items[0];args=items[1:]
        if name in ('distinct','noverlap') and len(args)==2:
            return self.points[args[0]]!=self.points[args[1]]
        if name=='ncoll' and len(args)==3:
            (ax,ay),(bx,by),(cx,cy)=(self.points[x] for x in args)
            return (bx-ax)*(cy-ay)!=(by-ay)*(cx-ax)
        raise UnsupportedPredicate('unsupported condition '+text)
    def all(self,conditions:Sequence[str]):
        return all(self.verify_condition(t) for t in conditions)


__all__=[name for name in globals() if not name.startswith('_') and name not in {
    'dataclass','field','Q','combinations','Counter','defaultdict','Any','Mapping',
    'Sequence','hashlib','json','math'}]
