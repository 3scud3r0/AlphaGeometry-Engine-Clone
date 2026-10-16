"""Exact rational constructions with explicit failure on ambiguities."""
from fractions import Fraction
from geoforge_upgrade_suite.geometry_exact import Vec2, Line, midpoint, squared_distance

def rational_point(x, y):
    return Vec2(Fraction(x), Fraction(y))

def intersect_lines(a, b, c, d):
    from .degeneracy import require_distinct
    require_distinct((a.x,a.y),(b.x,b.y))
    require_distinct((c.x,c.y),(d.x,d.y))
    return Line.through(a,b).intersect(Line.through(c,d))

def midpoint_point(a,b):
    return midpoint(a,b)

def reflect_point_about_point(a,center):
    return center*2-a

def perpendicular_foot(a,b,c):
    from geoforge_upgrade_suite.geometry_exact import Line
    return Line.through(b,c).projection(a)

def evaluate_midpoint(a,b,c):
    return squared_distance(a, midpoint(b,c)) == 0

class ConstructionRegistry:
    def __init__(self):
        self.builders = {"midpoint": midpoint_point, "line_intersection": intersect_lines,
                         "point_reflection":reflect_point_about_point,
                         "perpendicular_foot":perpendicular_foot}
    def build(self, kind, *args):
        if kind not in self.builders:
            raise ValueError(f"unsupported exact construction: {kind}")
        return self.builders[kind](*args)
