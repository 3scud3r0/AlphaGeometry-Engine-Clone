"""Non-neural transparent value baseline used before learning a ranking policy."""
def proof_progress_score(new_facts,goal,previous_facts=()):
    if goal in new_facts:return 1.0
    before=set(previous_facts);new=set(new_facts)-before
    if not new:return 0.0
    g=set(goal.points)
    return min(0.95,sum(len(set(p.points)&g) for p in new)/(4.0*len(new)+1))
