"""Declarative rule matcher over typed predicates, without text eval."""
from geoforge_core.ast import Predicate
from geoforge_core.canonical import canonical

def match(pattern,fact,subst):
    if pattern.kind!=fact.kind or len(pattern.points)!=len(fact.points):
        return None
    subst=dict(subst)
    for a,b in zip(pattern.points,fact.points):
        if a in subst and subst[a]!=b: return None
        subst[a]=b
    return subst

def instantiate(pattern,mapping):
    return canonical(Predicate(pattern.kind,tuple(mapping[x] for x in pattern.points),pattern.constants))

def match_rule(rule,facts):
    """Generate (conclusion, premises) where each premise occurs in known facts."""
    facts=tuple(facts)
    def rec(index,subst,parents):
        if index==len(rule.premises):
            yield instantiate(rule.conclusion,subst),tuple(parents)
            return
        pred=rule.premises[index]
        for fact in facts:
            sub=match(pred,fact,subst)
            if sub is not None:
                yield from rec(index+1,sub,parents+[fact])
    yield from rec(0,{},[])
