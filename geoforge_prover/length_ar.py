"""Linear additive segment-length constraints, separate from log-length algebra."""
from fractions import Fraction
from .sparse_exact import RationalLinearSystem

def distvar(a,b):
    if a==b: raise ValueError("zero length")
    return "D:"+":".join(sorted((a,b)))

class AdditiveLengthAR:
    def __init__(self):
        self.system=RationalLinearSystem()
    def add(self, name, terms, constant=0):
        row={"__constant__":-Fraction(constant)}
        for (a,b),coef in terms:
            key=distvar(a,b)
            row[key]=row.get(key,Fraction())+Fraction(coef)
        self.system.add(name,row)
    def entails(self,terms,constant=0):
        row={"__constant__":-Fraction(constant)}
        for (a,b),coef in terms:
            key=distvar(a,b)
            row[key]=row.get(key,Fraction())+Fraction(coef)
        return self.system.entail(row)
