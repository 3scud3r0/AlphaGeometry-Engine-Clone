"""Formal multiplicative metric relations (requires positive, nonzero segments)."""
from fractions import Fraction
from .sparse_exact import RationalLinearSystem

def undirected_segment(a,b):
    if a==b: raise ValueError("zero segment has no logarithm")
    return "L:"+":".join(sorted((a,b)))

class LogLengthAR:
    def __init__(self):
        self.system=RationalLinearSystem()
        self.nonzero=set()
    def allow_segment(self,a,b):
        if a==b: raise ValueError("zero segment")
        self.nonzero.add(undirected_segment(a,b))
    def _ensure(self,*segments):
        for a,b in segments:
            key=undirected_segment(a,b)
            if key not in self.nonzero:
                raise ValueError("nonzero length not established: "+key)
    def add_equal(self,name,a,b,c,d):
        self._ensure((a,b),(c,d))
        self.system.add(name,{undirected_segment(a,b):1,undirected_segment(c,d):-1})
    def equal(self,a,b,c,d):
        self._ensure((a,b),(c,d))
        return self.system.entail({undirected_segment(a,b):1,undirected_segment(c,d):-1})
    def add_ratio_equality(self,name,s1,s2,s3,s4):
        self._ensure(s1,s2,s3,s4)
        pairs=[s1,s2,s3,s4]
        vector={}
        for (a,b),coef in zip(pairs,(1,-1,-1,1)):
            var=undirected_segment(a,b)
            vector[var]=vector.get(var,0)+coef
        self.system.add(name,vector)
