"""Safe integer-pivot angle congruence elimination modulo pi.

Unlike ordinary elimination over Q, dividing 2*x ≡ 0 (mod pi) by two is
unsound. Only ±1 integer pivots are admitted.
"""
from fractions import Fraction

class AngleCongruenceSystem:
    def __init__(self):
        self.rows = {}
    def _reduce(self, expression, multiples=0):
        vec={k:int(v) for k,v in expression.items() if int(v)}
        constant=int(multiples)
        for pivot in sorted(self.rows):
            row, k=self.rows[pivot]
            coef=vec.get(pivot,0)
            if not coef: continue
            for key,value in row.items():
                vec[key]=vec.get(key,0)-coef*value
                if not vec[key]: del vec[key]
            constant -= coef*k
        return vec,constant
    def add(self, expression, multiples=0):
        if any(int(x)!=x for x in expression.values()):
            raise ValueError("integer coefficients required for angle congruences")
        vec,k=self._reduce(expression,multiples)
        pivots=[v for v in sorted(vec) if abs(vec[v])==1]
        if not pivots: return False
        pivot=pivots[0]; scale=vec[pivot]
        self.rows[pivot]=({v:c*scale for v,c in vec.items()},k*scale)
        return True
    def entails_zero_mod_pi(self, expression, multiples=0):
        vec,_=self._reduce(expression,multiples)
        return not vec
