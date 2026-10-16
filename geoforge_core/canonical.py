"""Sound syntactic symmetries; not an unconstrained geometry isomorphism."""
from .ast import Predicate

def canonical(predicate):
    p = predicate.points
    k = predicate.kind
    if k in ("coll", "ncoll", "cyclic"):
        p = tuple(sorted(p))
    elif k in ("para", "perp", "cong", "npara", "lessthan") and len(p) == 4:
        a,b,c,d = p
        if k == "lessthan":
            p = tuple(sorted((a,b))) + tuple(sorted((c,d)))
        else:
            p = min((tuple(sorted((a,b))) + tuple(sorted((c,d))),
                     tuple(sorted((c,d))) + tuple(sorted((a,b)))))
    elif k in ("overlap", "noverlap"):
        p = tuple(sorted(p))
    elif k == "midp":
        p = (p[0],) + tuple(sorted(p[1:]))
    return Predicate(k, p, predicate.constants)

def alpha_rename(predicate, mapping):
    return canonical(Predicate(predicate.kind, tuple(mapping.get(p, p) for p in predicate.points), predicate.constants))
