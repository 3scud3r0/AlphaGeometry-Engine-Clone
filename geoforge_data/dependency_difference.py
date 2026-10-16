"""Dependency DAG pruning; cannot certify mathematical necessity of auxiliaries."""
def ancestors(definitions, roots):
    active=set(roots)
    todo=list(roots)
    while todo:
        name=todo.pop()
        for parent in definitions.get(name,()):
            if parent not in active:
                active.add(parent);todo.append(parent)
    return frozenset(active)

def auxiliary_candidates(definitions,goal_points,proof_points):
    goal_anc=ancestors(definitions,goal_points)
    proof_anc=ancestors(definitions,proof_points)
    return frozenset(proof_anc-goal_anc)

def reverse_topological_prune(definitions,goal_points,proof_points):
    used=ancestors(definitions,goal_points)|ancestors(definitions,proof_points)
    return {k:tuple(v) for k,v in definitions.items() if k in used}
