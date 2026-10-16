#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Exact geometry, polynomials and certified transformations for GeoForge.

Everything in this file is exact over Q unless explicitly named ``approx``.
A construction coordinate certificate is NOT, by itself, an olympiad theorem.
Each function rejects degeneracy in its declared domain. No hidden numeric
comparison is used to justify any universal theorem.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as Q
from collections import defaultdict
from itertools import combinations, product
from typing import Any, Iterable, Iterator, Mapping, Sequence
import hashlib
import json
import math

class DomainError(ValueError):
    """Input lies outside the domain of the requested geometric operation."""

class BudgetExceeded(RuntimeError):
    """A finite symbolic-computation budget has been exhausted."""


def rational(value: Any) -> Q:
    if isinstance(value, Q):
        return value
    if isinstance(value, float):
        if not math.isfinite(value):
            raise DomainError('non-finite input')
        return Q(str(value))
    return Q(value)


@dataclass(frozen=True, order=True)
class Vec2:
    x: Q
    y: Q
    def __post_init__(self):
        object.__setattr__(self, 'x', rational(self.x))
        object.__setattr__(self, 'y', rational(self.y))
    def __add__(self, other: 'Vec2') -> 'Vec2':
        return Vec2(self.x + other.x, self.y + other.y)
    def __sub__(self, other: 'Vec2') -> 'Vec2':
        return Vec2(self.x - other.x, self.y - other.y)
    def __neg__(self) -> 'Vec2':
        return Vec2(-self.x, -self.y)
    def __mul__(self, value: Any) -> 'Vec2':
        a = rational(value)
        return Vec2(a * self.x, a * self.y)
    __rmul__ = __mul__
    def __truediv__(self, value: Any) -> 'Vec2':
        a = rational(value)
        if not a:
            raise ZeroDivisionError('zero vector divisor')
        return Vec2(self.x / a, self.y / a)
    def dot(self, other: 'Vec2') -> Q:
        return self.x * other.x + self.y * other.y
    def cross(self, other: 'Vec2') -> Q:
        return self.x * other.y - self.y * other.x
    def norm2(self) -> Q:
        return self.dot(self)
    def rotate90(self) -> 'Vec2':
        return Vec2(-self.y, self.x)
    def as_tuple(self) -> tuple[Q, Q]:
        return self.x, self.y
    def as_float(self) -> tuple[float, float]:
        return float(self.x), float(self.y)


def determinant(a: Vec2, b: Vec2, c: Vec2) -> Q:
    return (b-a).cross(c-a)


def midpoint(a: Vec2, b: Vec2) -> Vec2:
    return (a+b) / 2


def area2(a: Vec2, b: Vec2, c: Vec2) -> Q:
    return determinant(a, b, c)


def squared_distance(a: Vec2, b: Vec2) -> Q:
    return (a-b).norm2()


def collinear(a: Vec2, b: Vec2, c: Vec2) -> bool:
    return a != b and a != c and b != c and area2(a,b,c) == 0


def parallel(a: Vec2,b: Vec2,c: Vec2,d: Vec2) -> bool:
    return a != b and c != d and (b-a).cross(d-c) == 0


def perpendicular(a: Vec2,b: Vec2,c: Vec2,d: Vec2) -> bool:
    return a != b and c != d and (b-a).dot(d-c) == 0


@dataclass(frozen=True)
class Line:
    a: Q
    b: Q
    c: Q
    def __post_init__(self):
        for key in ('a','b','c'):
            object.__setattr__(self,key,rational(getattr(self,key)))
        if self.a==0 and self.b==0:
            raise DomainError('zero normal cannot define a line')
    @classmethod
    def through(cls,p: Vec2,q: Vec2) -> 'Line':
        if p == q:
            raise DomainError('line through identical points')
        a=q.y-p.y; b=p.x-q.x; c=-(a*p.x+b*p.y)
        return cls(a,b,c).normalized()
    def normalized(self) -> 'Line':
        den=math.lcm(*(v.denominator for v in (self.a,self.b,self.c)))
        ai,bi,ci=(int(v*den) for v in (self.a,self.b,self.c))
        g=math.gcd(math.gcd(abs(ai),abs(bi)),abs(ci))
        ai//=g;bi//=g;ci//=g
        if (ai,bi)<(0,0):
            ai,bi,ci=-ai,-bi,-ci
        return Line(Q(ai),Q(bi),Q(ci))
    def evaluate(self,p: Vec2) -> Q:
        return self.a*p.x+self.b*p.y+self.c
    def contains(self,p: Vec2) -> bool:
        return self.evaluate(p)==0
    def direction(self) -> Vec2:
        return Vec2(-self.b,self.a)
    def intersect(self,other: 'Line') -> Vec2:
        determinant=self.a*other.b-other.a*self.b
        if not determinant:
            raise DomainError('parallel or identical lines')
        x=(self.b*other.c-other.b*self.c)/determinant
        y=(self.c*other.a-other.c*self.a)/determinant
        return Vec2(x,y)
    def projection(self,p: Vec2) -> Vec2:
        den=self.a*self.a+self.b*self.b
        t=self.evaluate(p)/den
        return Vec2(p.x-t*self.a,p.y-t*self.b)
    def reflect(self,p: Vec2) -> Vec2:
        foot=self.projection(p)
        return 2*foot-p
    def is_parallel(self, other: 'Line') -> bool:
        return self.a*other.b==self.b*other.a
    def is_perpendicular(self, other: 'Line') -> bool:
        return self.a*other.a+self.b*other.b==0


@dataclass(frozen=True)
class Circle:
    center: Vec2
    radius2: Q
    def __post_init__(self):
        object.__setattr__(self, 'radius2', rational(self.radius2))
        if self.radius2 <= 0:
            raise DomainError('circle radius must be positive')
    @classmethod
    def through(cls,a: Vec2,b: Vec2,c: Vec2) -> 'Circle':
        if determinant(a,b,c)==0:
            raise DomainError('collinear circumcircle')
        u=b-a;v=c-a
        rhs1=(b.norm2()-a.norm2())/2
        rhs2=(c.norm2()-a.norm2())/2
        den=u.cross(v)
        x=(rhs1*v.y-u.y*rhs2)/den
        y=(u.x*rhs2-rhs1*v.x)/den
        center=Vec2(x,y)
        return cls(center,squared_distance(a,center))
    def contains(self,p: Vec2) -> bool:
        return squared_distance(self.center,p)==self.radius2
    def power(self,p: Vec2) -> Q:
        return squared_distance(p,self.center)-self.radius2
    def radical_axis(self,other: 'Circle') -> Line:
        # |p-o1|²-r1² = |p-o2|²-r2²
        if self.center==other.center:
            raise DomainError('concentric circles do not define a radical axis')
        a=2*(other.center.x-self.center.x)
        b=2*(other.center.y-self.center.y)
        c=(self.center.norm2()-self.radius2)- (other.center.norm2()-other.radius2)
        return Line(a,b,c).normalized()
    def squared_distance_from_center(self,p: Vec2) -> Q:
        return squared_distance(self.center,p)


def radical_center(a: Circle,b: Circle,c: Circle) -> Vec2:
    return a.radical_axis(b).intersect(a.radical_axis(c))


def circle_line_intersections(circle: Circle,line: Line) -> tuple[Vec2,...]:
    foot=line.projection(circle.center)
    rem=circle.radius2-squared_distance(circle.center,foot)
    if rem < 0:
        return ()
    if rem == 0:
        return (foot,)
    d=line.direction(); scale2=rem/d.norm2()
    num=scale2.numerator;den=scale2.denominator
    s_num=math.isqrt(num);s_den=math.isqrt(den)
    if s_num*s_num!=num or s_den*s_den!=den:
        raise DomainError('irrational intersection coordinates; use numerical construction')
    v=d*Q(s_num,s_den)
    return tuple(sorted((foot-v,foot+v)))


def circles_intersect_exact(a: Circle,b: Circle) -> tuple[Vec2,...]:
    if a.center==b.center:
        if a.radius2==b.radius2:
            raise DomainError('infinitely many circle intersection points')
        return ()
    return circle_line_intersections(a,a.radical_axis(b))


@dataclass(frozen=True)
class Inversion:
    center: Vec2
    radius2: Q
    def __post_init__(self):
        object.__setattr__(self,'radius2',rational(self.radius2))
        if self.radius2<=0:
            raise DomainError('inversion radius squared must be positive')
    def point(self,p: Vec2) -> Vec2:
        d=p-self.center
        if d.norm2()==0:
            raise DomainError('inversion undefined at its center')
        return self.center+d*(self.radius2/d.norm2())
    def line(self,line: Line) -> 'Line | Circle':
        # A line not passing through inversion center becomes a circle
        # through inversion center.  Foot of origin maps to diameter endpoint.
        if line.contains(self.center):
            return line
        foot=line.projection(self.center)
        image=self.point(foot)
        center=midpoint(self.center,image)
        return Circle(center,squared_distance(center,self.center))
    def circle(self,circle: Circle) -> 'Circle | Line':
        o=circle.center-self.center
        power=o.norm2()-circle.radius2
        if power == 0:
            # Inversion of a circle through inversion center is a line.
            return Line(2*o.x,2*o.y,-self.radius2-2*o.dot(self.center)).normalized()
        center=self.center+o*(self.radius2/power)
        rr=self.radius2*self.radius2*circle.radius2/(power*power)
        return Circle(center,rr)
    def is_involution(self,p: Vec2) -> bool:
        return self.point(self.point(p))==p


def directed_ratio(a: Vec2,b: Vec2,c: Vec2) -> Q:
    # Only defined when A,B,C collinear; (C-A)/(B-A), signed.
    u=b-a; v=c-a
    if u.norm2()==0 or u.cross(v)!=0:
        raise DomainError('directed ratio requires nondegenerate collinear points')
    return u.dot(v)/u.norm2()


def cross_ratio(a: Vec2,b: Vec2,c: Vec2,d: Vec2) -> Q:
    if a==b or c==d or a==d or b==c:
        raise DomainError('non-distinct points in denominator')
    ab=Line.through(a,b)
    if any(not ab.contains(p) for p in (c,d)):
        raise DomainError('cross-ratio points must be collinear')
    # (AC/BC) / (AD/BD) signed; use a coordinate along line.
    u=b-a
    t=lambda p: u.dot(p-a)/u.norm2()
    tc,td=t(c),t(d)
    if tc==1 or td==0:
        raise DomainError('cross ratio undefined')
    return (tc/(tc-1))/(td/(td-1))


@dataclass(frozen=True)
class HPoint:
    x: Q
    y: Q
    z: Q
    def __post_init__(self):
        for k in ('x','y','z'):
            object.__setattr__(self,k,rational(getattr(self,k)))
        if self.x==self.y==self.z==0:
            raise DomainError('homogeneous zero point')
    @classmethod
    def from_affine(cls,p: Vec2) -> 'HPoint':
        return cls(p.x,p.y,Q(1))
    def affine(self) -> Vec2:
        if not self.z:
            raise DomainError('point at infinity')
        return Vec2(self.x/self.z,self.y/self.z)
    def cross(self,other: 'HPoint') -> 'HLine':
        return HLine(self.y*other.z-self.z*other.y,
                     self.z*other.x-self.x*other.z,
                     self.x*other.y-self.y*other.x)
    def normalized(self) -> 'HPoint':
        arr=(self.x,self.y,self.z)
        den=math.lcm(*(v.denominator for v in arr))
        a=[int(v*den) for v in arr];g=math.gcd(*a)
        a=[x//g for x in a]
        if next(x for x in a if x)!=abs(next(x for x in a if x)):
            a=[-v for v in a]
        return HPoint(*a)


@dataclass(frozen=True)
class HLine:
    a: Q
    b: Q
    c: Q
    def __post_init__(self):
        for k in ('a','b','c'):
            object.__setattr__(self,k,rational(getattr(self,k)))
        if self.a==self.b==self.c==0:
            raise DomainError('homogeneous zero line')
    def intersection(self,other: 'HLine') -> HPoint:
        p=HPoint(self.b*other.c-self.c*other.b,
                 self.c*other.a-self.a*other.c,
                 self.a*other.b-self.b*other.a)
        return p.normalized()
    def contains(self,p: HPoint) -> bool:
        return self.a*p.x+self.b*p.y+self.c*p.z==0
    def normalized(self) -> 'HLine':
        arr=(self.a,self.b,self.c)
        den=math.lcm(*(v.denominator for v in arr))
        a=[int(v*den) for v in arr];g=math.gcd(*a)
        a=[x//g for x in a]
        if next(x for x in a if x)<0:
            a=[-v for v in a]
        return HLine(*a)


@dataclass(frozen=True)
class Mat3:
    data: tuple[tuple[Q,Q,Q],tuple[Q,Q,Q],tuple[Q,Q,Q]]
    def __post_init__(self):
        if len(self.data)!=3 or any(len(row)!=3 for row in self.data):
            raise DomainError('3x3 matrix required')
        object.__setattr__(self,'data',tuple(tuple(map(rational,r)) for r in self.data))
    @classmethod
    def identity(cls):
        return cls(((1,0,0),(0,1,0),(0,0,1)))
    def point(self,p: HPoint) -> HPoint:
        v=(p.x,p.y,p.z)
        return HPoint(*(sum(a*b for a,b in zip(row,v)) for row in self.data)).normalized()
    def __matmul__(self,other: 'Mat3') -> 'Mat3':
        return Mat3(tuple(tuple(sum(self.data[i][k]*other.data[k][j] for k in range(3))
                              for j in range(3)) for i in range(3)))
    def determinant(self) -> Q:
        a,b,c=self.data
        return a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0])
    def invert(self) -> 'Mat3':
        d=self.determinant()
        if not d:raise DomainError('singular projective transform')
        a=self.data
        def minor(i,j):
            inds=[k for k in range(3) if k!=i]
            jnds=[k for k in range(3) if k!=j]
            return (a[inds[0]][jnds[0]]*a[inds[1]][jnds[1]]-
                    a[inds[0]][jnds[1]]*a[inds[1]][jnds[0]])
        cof=tuple(tuple((-1)**(i+j)*minor(i,j) for j in range(3)) for i in range(3))
        return Mat3(tuple(tuple(cof[j][i]/d for j in range(3)) for i in range(3)))


def segment_intersection(a:Vec2,b:Vec2,c:Vec2,d:Vec2,proper=False)->Vec2|None:
    if a==b or c==d:
        raise DomainError('zero segment')
    try:
        p=Line.through(a,b).intersect(Line.through(c,d))
    except DomainError:
        return None
    def within(x,lo,hi):
        if proper:return min(lo,hi)<x<max(lo,hi) or lo==hi==x
        return min(lo,hi)<=x<=max(lo,hi)
    if all((within(p.x,a.x,b.x),within(p.y,a.y,b.y),
            within(p.x,c.x,d.x),within(p.y,c.y,d.y))):
        if proper and p in (a,b,c,d):return None
        return p
    return None


def convex_hull(points: Sequence[Vec2]) -> tuple[Vec2,...]:
    pts=sorted(set(points))
    if len(pts)<3:return tuple(pts)
    def half(items):
        out=[]
        for p in items:
            while len(out)>1 and (out[-1]-out[-2]).cross(p-out[-1])<=0:
                out.pop()
            out.append(p)
        return out
    return tuple(half(pts)[:-1]+half(pts[::-1])[:-1])


def polygon_area2(vertices: Sequence[Vec2]) -> Q:
    if len(vertices)<3:raise DomainError('at least three vertices required')
    return sum(a.cross(b) for a,b in zip(vertices,(*vertices[1:],vertices[0])))


def point_inside_convex_polygon(p: Vec2,vertices: Sequence[Vec2],strict=False) -> bool:
    if len(vertices)<3:raise DomainError('polygon requires three vertices')
    signs=[(b-a).cross(p-a) for a,b in zip(vertices,(*vertices[1:],vertices[0]))]
    return (all(v>0 for v in signs) or all(v<0 for v in signs)) if strict else (
        all(v>=0 for v in signs) or all(v<=0 for v in signs))


def is_convex_polygon(vertices: Sequence[Vec2],strict=True) -> bool:
    if len(vertices)<3 or len(set(vertices))!=len(vertices):return False
    turns=[(vertices[(i+1)%len(vertices)]-vertices[i]).cross(
           vertices[(i+2)%len(vertices)]-vertices[(i+1)%len(vertices)]) for i in range(len(vertices))]
    return all(v>0 for v in turns) or all(v<0 for v in turns) if strict else (
        all(v>=0 for v in turns) or all(v<=0 for v in turns))


# Exact multivariate polynomial ring Q[x_0, ..., x_(n-1)]
Monomial = tuple[int,...]


@dataclass(frozen=True)
class Polynomial:
    nvars: int
    terms: tuple[tuple[Monomial,Q],...]
    def __post_init__(self):
        if self.nvars<1:raise DomainError('at least one variable required')
        d=defaultdict(Q)
        for m,c in self.terms:
            if len(m)!=self.nvars or any(not isinstance(x,int) or x<0 for x in m):
                raise DomainError('invalid monomial exponent vector')
            d[tuple(m)]+=rational(c)
        object.__setattr__(self,'terms',tuple(sorted((m,c) for m,c in d.items() if c)))
    @classmethod
    def from_dict(cls,nvars:int,data:Mapping[Monomial,Any]) -> 'Polynomial':
        return cls(nvars,tuple(data.items()))
    @classmethod
    def constant(cls,nvars:int,v:Any) -> 'Polynomial':
        q=rational(v)
        return cls.from_dict(nvars,{(0,)*nvars:q} if q else {})
    @classmethod
    def variable(cls,nvars:int,i:int) -> 'Polynomial':
        if not 0<=i<nvars:raise IndexError(i)
        v=[0]*nvars;v[i]=1
        return cls.from_dict(nvars,{tuple(v):Q(1)})
    def __bool__(self):return bool(self.terms)
    def as_dict(self):return dict(self.terms)
    def _coerce(self,other: Any)->'Polynomial':
        if isinstance(other,Polynomial):
            if self.nvars!=other.nvars:raise DomainError('different polynomial rings')
            return other
        return Polynomial.constant(self.nvars,other)
    def __add__(self,other:Any)->'Polynomial':
        y=self._coerce(other);d=defaultdict(Q,self.terms)
        for m,v in y.terms:d[m]+=v
        return Polynomial.from_dict(self.nvars,d)
    __radd__=__add__
    def __neg__(self)->'Polynomial':
        return Polynomial(self.nvars,tuple((m,-v) for m,v in self.terms))
    def __sub__(self,other:Any)->'Polynomial':return self+(-self._coerce(other))
    def __rsub__(self,other:Any)->'Polynomial':return self._coerce(other)+(-self)
    def __mul__(self,other:Any)->'Polynomial':
        y=self._coerce(other);d=defaultdict(Q)
        for (a,av),(b,bv) in product(self.terms,y.terms):
            d[tuple(x+y for x,y in zip(a,b))]+=av*bv
        return Polynomial.from_dict(self.nvars,d)
    __rmul__=__mul__
    def __pow__(self,exponent:int)->'Polynomial':
        if not isinstance(exponent,int) or exponent<0:raise DomainError('negative polynomial exponent')
        out=Polynomial.constant(self.nvars,1);base=self
        while exponent:
            if exponent&1:out=out*base
            base=base*base;exponent>>=1
        return out
    def scale(self,c:Any)->'Polynomial':return self*self._coerce(c)
    def derivative(self,index:int)->'Polynomial':
        if not 0<=index<self.nvars:raise IndexError(index)
        d=defaultdict(Q)
        for m,c in self.terms:
            if m[index]:
                q=list(m);q[index]-=1;d[tuple(q)]+=c*m[index]
        return Polynomial.from_dict(self.nvars,d)
    def eval(self,values:Sequence[Any])->Q:
        if len(values)!=self.nvars:raise DomainError('invalid number of evaluation points')
        v=tuple(map(rational,values))
        return sum(c*math.prod(x**e for x,e in zip(v,m)) for m,c in self.terms)
    def leading(self)->tuple[Monomial,Q]:
        if not self.terms:raise DomainError('zero polynomial has no leading monomial')
        return max(self.terms,key=lambda x:(sum(x[0]),x[0]))
    def normalized(self)->'Polynomial':
        return self.scale(1/self.leading()[1]) if self else self
    def multiply_monomial(self,m:Monomial,coef:Any=1)->'Polynomial':
        if len(m)!=self.nvars or any(x<0 for x in m):raise DomainError('invalid monomial')
        q=rational(coef)
        return Polynomial.from_dict(self.nvars,{tuple(x+y for x,y in zip(a,m)):v*q for a,v in self.terms})
    def divided_remainder(self,divisors:Sequence['Polynomial'],max_steps=10000):
        """Multivariate division, returning quotient list and exact remainder."""
        div=tuple(self._coerce(d) for d in divisors)
        if any(not f for f in div):raise ZeroDivisionError('zero divisor')
        q=[Polynomial.constant(self.nvars,0) for _ in div]
        r=Polynomial.constant(self.nvars,0);p=self;step=0
        while p:
            if step>=max_steps:raise BudgetExceeded('polynomial reduction exceeds budget')
            step+=1;m,c=p.leading();advanced=False
            for i,d in enumerate(div):
                n,coeff=d.leading()
                if all(x>=y for x,y in zip(m,n)):
                    delta=tuple(x-y for x,y in zip(m,n))
                    t=Polynomial.constant(self.nvars,c/coeff).multiply_monomial(delta)
                    q[i]=q[i]+t;p=p-t*d;advanced=True;break
            if not advanced:
                t=Polynomial.from_dict(self.nvars,{m:c});r=r+t;p=p-t
        return tuple(q),r
    def __str__(self):
        if not self.terms:return '0'
        pieces=[]
        for m,c in sorted(self.terms,reverse=True):
            mon=''.join(f'x{i}'+(f'^{e}' if e!=1 else '') for i,e in enumerate(m) if e)
            pieces.append(f'{c}*{mon}' if mon else str(c))
        return ' + '.join(pieces)


def monomial_lcm(a:Monomial,b:Monomial)->Monomial:
    if len(a)!=len(b):raise DomainError('incompatible monomials')
    return tuple(max(x,y) for x,y in zip(a,b))


def s_polynomial(f:Polynomial,g:Polynomial)->Polynomial:
    fm,fc=f.leading();gm,gc=g.leading();mm=monomial_lcm(fm,gm)
    d1=tuple(x-y for x,y in zip(mm,fm));d2=tuple(x-y for x,y in zip(mm,gm))
    return f.multiply_monomial(d1,1/fc)-g.multiply_monomial(d2,1/gc)


@dataclass(frozen=True)
class GroebnerResult:
    basis: tuple[Polynomial,...]
    pairs_examined:int
    reductions:int
    exhausted:bool


def groebner_basis(polys:Sequence[Polynomial],max_pairs=150,max_terms=2000,max_steps=10000)->GroebnerResult:
    if not polys: return GroebnerResult((),0,0,False)
    n=polys[0].nvars
    if any(p.nvars!=n for p in polys):raise DomainError('incompatible polynomial rings')
    basis=[p.normalized() for p in polys if p]
    pairs=list(combinations(range(len(basis)),2));count=0;reductions=0
    while pairs:
        if count>=max_pairs:
            return GroebnerResult(tuple(basis),count,reductions,True)
        i,j=pairs.pop(0);count+=1
        f=basis[i];g=basis[j]
        # Buchberger product criterion for relatively prime leading terms.
        fm,_=f.leading();gm,_=g.leading()
        if all(min(a,b)==0 for a,b in zip(fm,gm)):continue
        sp=s_polynomial(f,g)
        if len(sp.terms)>max_terms:
            return GroebnerResult(tuple(basis),count,reductions,True)
        _,r=sp.divided_remainder(basis,max_steps=max_steps);reductions+=1
        if r:
            r=r.normalized()
            if r in basis:continue
            index=len(basis)
            pairs.extend((i,index) for i in range(index))
            basis.append(r)
    return GroebnerResult(tuple(basis),count,reductions,False)


def prove_polynomial_membership(goal:Polynomial,axioms:Sequence[Polynomial],max_pairs=150):
    gb=groebner_basis(axioms,max_pairs=max_pairs)
    if gb.exhausted:return False,gb,'budget_exhausted'
    if not gb.basis:return not goal,gb,'empty_ideal'
    _,rem=goal.divided_remainder(gb.basis)
    return not rem,gb,'exact_remainder_zero' if not rem else 'not_derivable_by_this_basis'


def symbolic_collinearity(n=6):
    if n<6:raise DomainError('at least 6 coordinate variables')
    x=[Polynomial.variable(n,i) for i in range(n)]
    return (x[2]-x[0])*(x[5]-x[1])-(x[3]-x[1])*(x[4]-x[0])


def symbolic_perpendicular(n=8):
    if n<8:raise DomainError('at least 8 coordinate variables')
    x=[Polynomial.variable(n,i) for i in range(n)]
    return (x[2]-x[0])*(x[6]-x[4])+(x[3]-x[1])*(x[7]-x[5])


def symbolic_parallel(n=8):
    if n<8:raise DomainError('at least 8 coordinate variables')
    x=[Polynomial.variable(n,i) for i in range(n)]
    return (x[2]-x[0])*(x[7]-x[5])-(x[3]-x[1])*(x[6]-x[4])


def symbolic_congruence(n=8):
    if n<8:raise DomainError('at least 8 coordinate variables')
    x=[Polynomial.variable(n,i) for i in range(n)]
    return ((x[2]-x[0])**2+(x[3]-x[1])**2)-((x[6]-x[4])**2+(x[7]-x[5])**2)


def symbolic_midpoint(n=6):
    if n<6:raise DomainError('at least 6 coordinate variables')
    x=[Polynomial.variable(n,i) for i in range(n)]
    return (2*x[0]-x[2]-x[4],2*x[1]-x[3]-x[5])


@dataclass(frozen=True)
class ExactGeometryCertificate:
    """Certificate that a finite coordinate identity is true, NOT universal."""
    operation:str
    inputs:dict[str,tuple[str,str]]
    output:dict[str,str]
    def json(self)->str:
        return json.dumps({'operation':self.operation,'inputs':self.inputs,
                           'output':self.output},sort_keys=True,ensure_ascii=False)
    @staticmethod
    def pack_points(operation:str,inputs:dict[str,Vec2],outputs:dict[str,Q|Vec2]):
        fmt=lambda v:f'{v.numerator}/{v.denominator}'
        ins={k:(fmt(v.x),fmt(v.y)) for k,v in inputs.items()}
        out={}
        for k,v in outputs.items():
            if isinstance(v,Vec2):out[k]=fmt(v.x)+','+fmt(v.y)
            else:out[k]=fmt(rational(v))
        return ExactGeometryCertificate(operation,ins,out)


def exact_geometry_fingerprint(points:Mapping[str,Vec2],invariants:Sequence[str]=())->str:
    data={k:(str(v.x),str(v.y)) for k,v in sorted(points.items())}
    raw=json.dumps({'points':data,'invariants':sorted(invariants)},sort_keys=True)
    return hashlib.sha256(raw.encode()).hexdigest()


__all__ = [name for name in globals() if not name.startswith('_') and name not in {
    'Any','Iterable','Iterator','Mapping','Sequence','Q','defaultdict','combinations','product',
    'hashlib','json','math','dataclass'}]
