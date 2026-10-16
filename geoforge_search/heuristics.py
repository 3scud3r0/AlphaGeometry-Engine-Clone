"""Deterministic, interpretable auxiliary prioritization."""
def score_candidate(candidate,goal_points=(),existing_relations=()):
    touched=set(candidate.inputs)
    relevant=len(touched.intersection(goal_points))
    repetitive=sum(1 for r in existing_relations if getattr(r,"points",None) and touched.issubset(r.points))
    complexity={"midpoint":1,"line_intersection":2}.get(candidate.kind,3)
    return 2*relevant-complexity-0.1*repetitive

def rank_candidates(candidates,goal_points=()):
    return sorted(candidates,key=lambda c:(-score_candidate(c,goal_points),c.kind,c.inputs))
