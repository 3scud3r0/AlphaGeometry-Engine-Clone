"""Certified simple rational and polynomial inequality checks."""
from fractions import Fraction

def triangle_inequality_squared(ab2,bc2,ac2):
    # Without exact square-root certificates this inequality remains unproved.
    from .quantifier_elimination import Decision
    if any(Fraction(x)<0 for x in (ab2,bc2,ac2)):
        return Decision("invalid")
    return Decision("unknown","square-root comparison requires an exact witness")

def rational_nonnegative(value):
    return Fraction(value)>=0
