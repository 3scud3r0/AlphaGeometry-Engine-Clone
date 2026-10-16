"""Indexed symbolic facts; coordinates never prove a predicate."""
from collections import defaultdict
from .ast import Predicate
from .canonical import canonical
from .point_unification import PointEquivalence

class GeometryGraph:
    def __init__(self, premises=()):
        self.facts = set()
        self.by_kind = defaultdict(set)
        self.by_point = defaultdict(set)
        self.reasons = {}
        self.points = PointEquivalence()
        for premise in premises:
            self.add(premise, "premise")
    def add(self, fact, source=None, parents=()):
        fact = canonical(fact)
        if fact in self.facts:
            return False
        if source is None:
            raise ValueError("a fact needs a provenance")
        self.facts.add(fact)
        self.by_kind[fact.kind].add(fact)
        for p in fact.points:
            self.by_point[p].add(fact)
        self.reasons[fact] = (source, tuple(parents))
        if fact.kind == "overlap" and source == "premise":
            self.points.merge(*fact.points, justified=True)
        return True
    def contains(self, fact):
        return canonical(fact) in self.facts
    def lookup(self, kind, containing=()):
        candidates = self.by_kind.get(kind, set())
        for p in containing:
            candidates = candidates.intersection(self.by_point.get(p, set()))
        return tuple(sorted(candidates, key=lambda x:x.serialize()))
    def dependencies(self, fact):
        fact = canonical(fact)
        seen = set()
        def walk(f):
            if f in seen: return
            seen.add(f)
            for parent in self.reasons[f][1]:
                walk(canonical(parent))
        walk(fact)
        return frozenset(seen)
