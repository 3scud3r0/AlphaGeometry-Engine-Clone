"""Movement dependency analysis; geometric locus claims need proof obligations."""
from dataclasses import dataclass

@dataclass(frozen=True)
class MovementResult:
    fixed: frozenset[str]
    moving: frozenset[str]
    undecidable: frozenset[str]

def movement_closure(dependencies, free_points):
    free_points = set(free_points)
    moving = set(free_points)
    changed = True
    while changed:
        before = len(moving)
        for name, args in dependencies.items():
            if any(p in moving for p in args):
                moving.add(name)
        changed = len(moving) != before
    fixed = set(dependencies) - moving
    return MovementResult(frozenset(fixed), frozenset(moving), frozenset())

def fixed_distance_candidate(a,b,movement):
    return a in movement.fixed and b in movement.fixed
