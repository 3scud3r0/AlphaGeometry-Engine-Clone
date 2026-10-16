"""Finite exact geometry construction enumeration; candidates are NOT theorems."""
from dataclasses import dataclass
from itertools import combinations

@dataclass(frozen=True,order=True)
class Candidate:
    kind: str
    name: str
    inputs: tuple[str,...]

def enumerate_midpoints(points,used_names=(),prefix="aux"):
    used=set(points)|set(used_names)
    i=0
    for a,b in combinations(sorted(set(points)),2):
        while f"{prefix}{i}" in used: i+=1
        name=f"{prefix}{i}";used.add(name);i+=1
        yield Candidate("midpoint",name,(a,b))

def enumerate_line_intersections(points,limit=50):
    from itertools import combinations
    pairs=list(combinations(sorted(set(points)),2))
    emitted=0
    for (a,b),(c,d) in combinations(pairs,2):
        if len({a,b,c,d})<4:continue
        yield Candidate("line_intersection",f"auxI{emitted}",(a,b,c,d))
        emitted+=1
        if emitted>=limit:return
