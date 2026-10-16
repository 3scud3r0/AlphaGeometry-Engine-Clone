"""Bounded real-closed-field reasoning for formulas accepted by SymPy.

This is not CAD and never treats 'unknown' as 'true'.
"""
from dataclasses import dataclass

@dataclass(frozen=True)
class Decision:
    status: str
    reason: str=""

def univariate_forall_nonnegative(expr,variable):
    import sympy as sp
    f=sp.Poly(expr,variable,domain="QQ")
    if f.is_zero: return Decision("proved")
    # Exact proof from SOS or a constant, not sampled positivity.
    if f.degree()==0:
        return Decision("proved" if f.all_coeffs()[0]>=0 else "refuted")
    if f.degree()==2:
        a,b,c=f.all_coeffs()
        if a>0 and 4*a*c-b*b>=0: return Decision("proved")
        if a<0: return Decision("refuted","unbounded below")
    return Decision("unknown","general CAD not integrated")
