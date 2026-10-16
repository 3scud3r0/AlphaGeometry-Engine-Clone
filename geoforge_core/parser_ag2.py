"""Parser for a documented subset of AG2 predicate syntax.

Supports canonical predicate clauses and the AG2 point@x_y = ..., ? goal
layout. Rejects unknown operators instead of guessing their semantics.
"""
import re
from fractions import Fraction
from .ast import Predicate, Problem, Construction
from .type_system import ARITY, EXPRESSION_PREDICATES, check_problem

_IDENTIFIER = re.compile(r"^[A-Za-z_][A-Za-z_0-9]*$")
def parse_constant(text):
    if "pi/" in text:
        a, b = text.split("pi/", 1)
        return Fraction(int(a)*180, int(b))
    return Fraction(text)

def parse_predicate(text):
    parts = text.strip().split()
    if not parts:
        raise ValueError("empty predicate")
    kind = parts[0]
    points, constants = [], []
    for item in parts[1:]:
        if _IDENTIFIER.fullmatch(item):
            points.append(item)
        else:
            try: constants.append(parse_constant(item))
            except (ValueError, ZeroDivisionError) as exc:
                raise ValueError(f"invalid predicate argument {item!r}") from exc
    return Predicate(kind, tuple(points), tuple(constants))

def parse_problem(text):
    if "?" not in text:
        raise ValueError("problem must contain ? followed by a goal")
    source, goal = text.split("?", 1)
    premises, constructions, coords = [], [], []
    for clause in source.split(";"):
        clause = clause.strip()
        if not clause:
            continue
        if "=" not in clause:
            premises.extend(parse_predicate(p) for p in clause.split(",") if p.strip())
            continue
        lhs, rhs = clause.split("=", 1)
        names = lhs.split()
        if not names:
            raise ValueError("construction without point")
        for token in names:
            if "@" in token:
                point, xy = token.split("@", 1)
                x, y = xy.split("_", 1)
                coords.append((point, Fraction(x), Fraction(y)))
        preds = tuple(parse_predicate(p) for p in rhs.split(",") if p.strip())
        premises.extend(preds)
        if preds:
            for token in names:
                constructions.append(Construction(token.split("@", 1)[0], preds))
    result = Problem(tuple(premises), parse_predicate(goal), tuple(constructions), tuple(coords))
    return check_problem(result)
