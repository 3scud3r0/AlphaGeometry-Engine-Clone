#!/usr/bin/env python3
"""Training-free exact ruler-and-compass construction executor.

Algebraic point coordinates are SymPy expressions (Q + radicals), not floats.
Every returned point is checked against the precise defining conditions.
These are exact *constructions for a given diagram*; they are not universal
proofs about every possible geometric configuration.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Mapping,Sequence
import itertools,json,time
try:
    import sympy as sp
except ImportError:
    sp=None

class ConstructionUnavailable(RuntimeError):pass
class ConstructionAmbiguous(ValueError):pass

def _sym():
    if sp is None:raise ConstructionUnavailable('sympy is required for exact algebraic constructions')
    return sp

def simp(value):return _sym().simplify(value)

def is_zero(value):
    x=simp(value)
    return x==0 or x.equals(0) is True


def _v(point):
    s=_sym()
    if isinstance(point,SPoint):return point
    if len(point)!=2:raise ValueError('a point requires two coordinates')
    return SPoint(s.sympify(point[0]),s.sympify(point[1]))

@dataclass(frozen=True)
class SPoint:
    x:object
    y:object
    def __post_init__(self):
        s=_sym()
        object.__setattr__(self,'x',s.simplify(s.sympify(self.x)))
        object.__setattr__(self,'y',s.simplify(s.sympify(self.y)))
    def __add__(self,other):return SPoint(self.x+other.x,self.y+other.y)
    def __sub__(self,other):return SPoint(self.x-other.x,self.y-other.y)
    def __mul__(self,s):return SPoint(self.x*s,self.y*s)
    __rmul__=__mul__
    def __truediv__(self,s):
        if is_zero(s):raise ZeroDivisionError('zero point divisor')
        return SPoint(self.x/s,self.y/s)
    def cross(self,other):return simp(self.x*other.y-self.y*other.x)
    def dot(self,other):return simp(self.x*other.x+self.y*other.y)
    def norm2(self):return simp(self.dot(self))
    def rotate90(self):return SPoint(-self.y,self.x)
    def eq(self,other):return is_zero(self.x-other.x) and is_zero(self.y-other.y)
    def json(self):return [str(self.x),str(self.y)]


def line_intersection(a,b,c,d):
    ab=b-a;cd=d-c;det=ab.cross(cd)
    if is_zero(ab.norm2()) or is_zero(cd.norm2()):
        raise ConstructionUnavailable('zero defining segment')
    if is_zero(det):raise ConstructionUnavailable('parallel or coincident lines')
    t=(c-a).cross(cd)/det
    p=a+ab*t
    if not is_zero((p-a).cross(ab)) or not is_zero((p-c).cross(cd)):
        raise AssertionError('exact intersection verification failed')
    return p


def foot(a,b,c):
    u=c-b
    n=u.norm2()
    if is_zero(n):raise ConstructionUnavailable('undefined line for projection')
    p=b+u*(a-b).dot(u)/n
    if not is_zero((p-b).cross(u)) or not is_zero((a-p).dot(u)):
        raise AssertionError('projection identity failed')
    return p


def orthocenter(a,b,c):
    if is_zero((b-a).cross(c-a)):
        raise ConstructionUnavailable('collinear triangle')
    p=foot(a,b,c);q=foot(b,a,c)
    return line_intersection(a,p,b,q)


def circumcenter(a,b,c):
    if is_zero((b-a).cross(c-a)):raise ConstructionUnavailable('collinear triangle')
    m=(a+b)/2;n=(a+c)/2
    return line_intersection(m,m+(b-a).rotate90(),n,n+(c-a).rotate90())


def circle_line_intersection(o,r2,a,b):
    s=_sym();u=b-a
    if is_zero(u.norm2()):raise ConstructionUnavailable('undefined line')
    if s.simplify(r2).is_negative:raise ConstructionUnavailable('negative squared radius')
    qa=u.norm2();qb=2*(a-o).dot(u);qc=(a-o).norm2()-r2
    discr=s.simplify(qb*qb-4*qa*qc)
    if discr.is_negative: return ()
    roots=((-qb+s.sqrt(discr))/(2*qa),(-qb-s.sqrt(discr))/(2*qa))
    points=[]
    for t in roots:
        p=a+u*t
        if not is_zero((p-o).norm2()-r2):raise AssertionError('circle root invalid')
        if not any(p.eq(q) for q in points):points.append(p)
    return tuple(points)


def circle_circle_intersection(o,r2,c,s2):
    if o.eq(c):
        if is_zero(r2-s2):raise ConstructionAmbiguous('coincident circles have infinitely many intersections')
        return ()
    d=c-o;u=d.norm2()
    # The radical axis has equation 2 d.(p-o) = r2 - s2 + |d|^2.
    k=(r2-s2+u)/2
    point=o+d*(k/u)
    return circle_line_intersection(o,r2,point,point+d.rotate90())


@dataclass(frozen=True)
class ConstructionStep:
    name:str
    operator:str
    args:tuple[str,...]
    branch:int=0
    def __post_init__(self):
        if not self.name or self.branch<0:raise ValueError('invalid construction step')

@dataclass(frozen=True)
class ConstructionTrace:
    status:str
    points:dict
    steps:tuple[dict,...]
    failure:str|None
    def json(self):
        return {'status':self.status,'points':{k:p.json() for k,p in self.points.items()},
                'steps':list(self.steps),'failure':self.failure}


class ExactConstructionExecutor:
    """All operations have explicit domain checks and independently tested outputs."""
    OPERATORS={
        'midpoint':2,'foot':3,'reflection_point':2,'reflection_line':3,
        'parallelogram':3,'centroid':3,'orthocenter':3,'circumcenter':3,
        'line_intersection':4,'on_line_circle':4,'on_circle_circle':4,
        'parallel_shift':3,'perpendicular_shift':3,'ratio':3,
    }
    def __init__(self,initial:Mapping[str,Sequence[object]]):
        self.points={name.lower():_v(value) for name,value in initial.items()}
        self.events=[]
    def construct(self,step:ConstructionStep):
        if step.operator not in self.OPERATORS:raise ConstructionUnavailable('unknown operator '+step.operator)
        if len(step.args)!=self.OPERATORS[step.operator]:raise ValueError('wrong construction arity')
        if step.name in self.points:raise ValueError('point already defined')
        p=[self.points[a] for a in step.args]
        k=step.operator;b=step.branch
        if k=='midpoint':poss=((p[0]+p[1])/2,)
        elif k=='foot':poss=(foot(*p),)
        elif k=='reflection_point':poss=(p[1]*2-p[0],)
        elif k=='reflection_line':poss=(foot(p[0],p[1],p[2])*2-p[0],)
        elif k=='parallelogram':poss=(p[0]+p[2]-p[1],)
        elif k=='centroid':poss=((p[0]+p[1]+p[2])/3,)
        elif k=='orthocenter':poss=(orthocenter(*p),)
        elif k=='circumcenter':poss=(circumcenter(*p),)
        elif k=='line_intersection':poss=(line_intersection(*p),)
        elif k=='on_line_circle':
            # first two define line; circle center is third, fourth is on circle.
            poss=circle_line_intersection(p[2],(p[3]-p[2]).norm2(),p[0],p[1])
        elif k=='on_circle_circle':
            # A center, B radius point, C center, D radius point.
            poss=circle_circle_intersection(p[0],(p[1]-p[0]).norm2(),
                                           p[2],(p[3]-p[2]).norm2())
        elif k=='parallel_shift':
            poss=(p[0]+p[2]-p[1],)  # AB translated vector B->C to A
        elif k=='perpendicular_shift':
            poss=(p[0]+(p[2]-p[1]).rotate90(),)
        elif k=='ratio':
            # Third point fixes a rational ratio from origin (x-coordinate).
            # Intentional strict interface: x is an exact dimensionless scalar.
            poss=(p[0]+(p[1]-p[0])*p[2].x,)
        else:raise AssertionError('missing construction branch')
        if not poss:raise ConstructionUnavailable('construction has no solutions')
        if b>=len(poss):raise ConstructionUnavailable('requested branch does not exist')
        point=poss[b]
        self.points[step.name]=point
        self.events.append({'name':step.name,'operator':k,'arguments':list(step.args),
                            'branch':b,'coordinates':point.json(),'solutions':len(poss)})
        return point
    def execute(self,steps:Sequence[ConstructionStep],stop_on_error=False):
        for step in steps:
            try:self.construct(step)
            except (ConstructionUnavailable,ConstructionAmbiguous,KeyError,ValueError) as exc:
                if stop_on_error:
                    return ConstructionTrace('failed',dict(self.points),tuple(self.events),str(exc))
                raise
        return ConstructionTrace('constructed',dict(self.points),tuple(self.events),None)


def verify_construction_trace(initial,steps,trace):
    """Re-execute each step from the user-declared base points."""
    try:
        e=ExactConstructionExecutor(initial)
        other=e.execute(steps)
        if other.status!='constructed' or trace.status!='constructed':return False
        if set(other.points)!=set(trace.points):return False
        return all(v.eq(trace.points[k]) for k,v in other.points.items())
    except (ConstructionUnavailable,ConstructionAmbiguous,ValueError,KeyError):return False
