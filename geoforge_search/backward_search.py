"""Backward rule decomposition into explicit, unproved subgoals."""
from geoforge_core.ast import Predicate
from geoforge_core.canonical import canonical
from geoforge_prover.ddar2_rules import default_rules

def backward_subgoals(goal,rules=None):
    out=[]
    for rule in (default_rules() if rules is None else rules):
        # Unify schematic conclusion with actual goal. Variables in the conclusion
        # must be bound; unbound premise names are existential, not asserted facts.
        pattern=rule.conclusion
        if goal.kind!=pattern.kind or len(goal.points)!=len(pattern.points):continue
        mapping={}
        ok=True
        for a,b in zip(pattern.points,goal.points):
            if a in mapping and mapping[a]!=b:ok=False;break
            mapping[a]=b
        if not ok:continue
        if all(all(x in mapping for x in premise.points) for premise in rule.premises):
            out.append((rule.name,tuple(canonical(Predicate(p.kind,tuple(mapping[x] for x in p.points),p.constants)) for p in rule.premises)))
    return tuple(out)
