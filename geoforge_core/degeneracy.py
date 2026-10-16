"""Exact nonzero-length and orientation guards."""
from fractions import Fraction

def separated(a, b):
    return tuple(a) != tuple(b)

def noncollinear(a, b, c):
    ax, ay = map(Fraction,a); bx, by=map(Fraction,b); cx,cy=map(Fraction,c)
    return (bx-ax)*(cy-ay)-(by-ay)*(cx-ax) != 0

def require_distinct(*points):
    if len({tuple(p) for p in points}) != len(points):
        raise ValueError("coincident points in a non-degenerate construction")
    return True

def require_nondegenerate_triangle(a,b,c):
    require_distinct(a,b,c)
    if not noncollinear(a,b,c):
        raise ValueError("degenerate triangle")
    return True
