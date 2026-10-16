"""Incremental exact elimination with linear-combination proof witnesses."""
from fractions import Fraction
from dataclasses import dataclass

def normalize(row):
    return {str(k): Fraction(v) for k,v in row.items() if Fraction(v)}

def add_rows(a,b,scale):
    out=dict(a)
    for k,v in b.items():
        out[k] = out.get(k,Fraction(0)) + Fraction(scale)*v
        if not out[k]: del out[k]
    return out

@dataclass(frozen=True)
class Witness:
    coefficients: tuple[tuple[str,Fraction], ...]
    def as_dict(self):
        return dict(self.coefficients)

class RationalLinearSystem:
    def __init__(self):
        self.basis = {}
        self.original = {}
    def add(self, name, vector):
        if name in self.original:
            raise ValueError("duplicate equation id")
        vec=normalize(vector)
        self.original[name]=vec
        combination={name:Fraction(1)}
        for pivot in sorted(self.basis):
            basis, proof=self.basis[pivot]
            if pivot not in vec: continue
            coefficient=vec[pivot]
            vec=add_rows(vec,basis,-coefficient)
            combination=add_rows(combination,proof,-coefficient)
        if not vec: return False
        pivot=min(vec)
        k=vec[pivot]
        self.basis[pivot]=({x:y/k for x,y in vec.items()},
                           {x:y/k for x,y in combination.items()})
        return True
    def entail(self,target):
        vec=normalize(target)
        witness={}
        for pivot in sorted(self.basis):
            row, proof=self.basis[pivot]
            if pivot not in vec: continue
            c=vec[pivot]
            vec=add_rows(vec,row,-c)
            witness=add_rows(witness,proof,c)
        if vec: return None
        return Witness(tuple(sorted(witness.items())))
    @staticmethod
    def verify_witness(original,target,witness):
        total={}
        for equation,coefficient in witness.as_dict().items():
            if equation not in original: return False
            total=add_rows(total,normalize(original[equation]),coefficient)
        return total==normalize(target)
