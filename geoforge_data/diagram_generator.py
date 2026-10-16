"""Deterministic diagram generation, with rejection statistics."""
from dataclasses import dataclass
import random
from geoforge_upgrade_suite.geometry_exact import Vec2,area2

@dataclass(frozen=True)
class GeneratedTriangle:
    points: tuple
    seed: int

def triangle(seed,range_bound=10,max_attempts=100):
    rng=random.Random(seed)
    for _ in range(max_attempts):
        p=tuple(Vec2(rng.randint(-range_bound,range_bound),
                     rng.randint(-range_bound,range_bound)) for _ in range(3))
        if len(set(p))==3 and area2(*p)!=0:
            return GeneratedTriangle(p,seed)
    raise ValueError("could not sample nondegenerate triangle")

def triangle_stream(seed,count):
    for i in range(count):
        yield triangle(seed+i)
