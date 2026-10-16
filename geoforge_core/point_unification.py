"""Explicit named-point equivalence with guarded merges."""
class PointEquivalence:
    def __init__(self):
        self.parent = {}
    def find(self, point):
        self.parent.setdefault(point, point)
        if self.parent[point] != point:
            self.parent[point] = self.find(self.parent[point])
        return self.parent[point]
    def merge(self, a, b, *, justified=False):
        if not justified:
            raise ValueError("point equality requires a certified premise or theorem")
        a, b = self.find(a), self.find(b)
        self.parent[max(a,b)] = min(a,b)
    def same(self, a, b):
        return self.find(a) == self.find(b)
    def class_members(self, point):
        root = self.find(point)
        return frozenset(p for p in self.parent if self.find(p) == root)
