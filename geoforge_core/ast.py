"""Immutable, serializable geometry syntax tree with explicit point identities."""
from dataclasses import dataclass, field
from fractions import Fraction
from typing import Union

Number = Union[int, Fraction]

@dataclass(frozen=True, order=True)
class Point:
    name: str
    def __post_init__(self):
        if not self.name or not (self.name[0].isalpha() or self.name[0] == "_"):
            raise ValueError("invalid point name")

@dataclass(frozen=True)
class Expr:
    """Affine scalar expression: sum(coeff * variable) + constant."""
    coefficients: tuple[tuple[str, Fraction], ...] = ()
    constant: Fraction = Fraction(0)
    def __post_init__(self):
        normalized = {}
        for k, v in self.coefficients:
            normalized[k] = normalized.get(k, Fraction(0)) + Fraction(v)
        object.__setattr__(self, "coefficients", tuple(sorted((k, v) for k, v in normalized.items() if v)))
        object.__setattr__(self, "constant", Fraction(self.constant))
    def __add__(self, other):
        if isinstance(other, (int, Fraction)):
            other = Expr((), Fraction(other))
        return Expr(self.coefficients + other.coefficients, self.constant + other.constant)
    def __neg__(self):
        return Expr(tuple((k, -v) for k, v in self.coefficients), -self.constant)
    def __sub__(self, other):
        return self + -other
    def scale(self, coefficient):
        c = Fraction(coefficient)
        return Expr(tuple((k, c*v) for k, v in self.coefficients), c*self.constant)

@dataclass(frozen=True)
class Predicate:
    kind: str
    points: tuple[str, ...] = ()
    constants: tuple[Fraction, ...] = ()
    def __post_init__(self):
        if not self.kind.isidentifier():
            raise ValueError("invalid predicate identifier")
        object.__setattr__(self, "points", tuple(self.points))
        object.__setattr__(self, "constants", tuple(Fraction(c) for c in self.constants))
    def serialize(self):
        return " ".join((self.kind,) + self.points + tuple(str(c) for c in self.constants))

@dataclass(frozen=True)
class Construction:
    point: str
    relations: tuple[Predicate, ...]
    def __post_init__(self):
        if not self.point or not self.relations:
            raise ValueError("construction requires point and conditions")

@dataclass(frozen=True)
class Problem:
    premises: tuple[Predicate, ...]
    goal: Predicate
    constructions: tuple[Construction, ...] = ()
    coordinates: tuple[tuple[str, Fraction, Fraction], ...] = ()
    def points(self):
        return frozenset(x for p in self.premises + (self.goal,) for x in p.points)
    def serialize(self):
        lines = [p.serialize() for p in self.premises]
        return " ; ".join(lines) + " ? " + self.goal.serialize()
