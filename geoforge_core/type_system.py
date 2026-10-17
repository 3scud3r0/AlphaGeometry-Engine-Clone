"""Conservative predicate arity and non-degeneracy checks."""
from .ast import Predicate

ARITY = {
    "coll": 3, "ncoll":3, "para":4, "npara":4, "perp":4,
    "cong":4, "cyclic":4, "midp":3, "eqangle":8, "eqratio":8,
    "simtri":6, "overlap":2, "noverlap":2,
    "sameclock":6, "lessthan":4, "circle":4,
}
EXPRESSION_PREDICATES = frozenset({"angeq", "distmeq", "distseq", "aconst", "rconst", "acompute", "rcompute"})

class GeometryTypeError(ValueError):
    pass

def check_predicate(predicate: Predicate):
    if not isinstance(predicate, Predicate):
        raise GeometryTypeError("expected Predicate")
    if predicate.kind in ARITY and len(predicate.points) != ARITY[predicate.kind]:
        raise GeometryTypeError(f"{predicate.kind}: expected {ARITY[predicate.kind]} points")
    if predicate.kind not in ARITY and predicate.kind not in EXPRESSION_PREDICATES:
        raise GeometryTypeError(f"unsupported predicate: {predicate.kind}")
    if predicate.kind in ARITY and predicate.constants:
        raise GeometryTypeError(f"{predicate.kind}: unexpected numeric constants")
    # Preserve the same non-degeneracy semantics as the exact evaluator.
    # These declarations cannot be satisfied in a Euclidean realization.
    k, p = predicate.kind, predicate.points
    if k in ("para", "perp", "npara") and len(p) == 4:
        if p[0] == p[1] or p[2] == p[3]:
            raise GeometryTypeError(f"{k}: zero-length line direction")
    if k == "cyclic" and len(p) == 4 and len(set(p)) != 4:
        raise GeometryTypeError("cyclic: repeated points")
    if k == "ncoll" and len(p) == 3 and len(set(p)) != 3:
        raise GeometryTypeError("ncoll: repeated points")
    if k == "noverlap" and len(p) == 2 and p[0] == p[1]:
        raise GeometryTypeError("noverlap: a point cannot differ from itself")
    if k == "eqratio" and len(p) == 8:
        if any(p[i] == p[i + 1] for i in range(0, 8, 2)):
            raise GeometryTypeError("eqratio: zero-length segment")
    if any(not x.isidentifier() for x in predicate.points):
        raise GeometryTypeError("invalid point symbol")
    return predicate

def check_problem(problem):
    for pred in problem.premises + (problem.goal,):
        check_predicate(pred)
    return problem
