"""S1 proven facts, S2 goal-assumption consequences, S3 numeric candidates.

A hypothetical goal and a numerically observed fact are never promoted to
an unconditional proof merely by appearing in an analysis string.
"""
from dataclasses import dataclass
@dataclass(frozen=True)
class Analysis:
    premise_proven:frozenset
    goal_conditional:frozenset
    numerical_candidates:frozenset
    def format(self):
        s1=self.premise_proven
        return "\n".join([
            "PROVEN: "+"; ".join(sorted(map(str,s1))),
            "GOAL_ASSUMED_ONLY: "+"; ".join(sorted(map(str,self.goal_conditional-s1))),
            "NUMERIC_UNPROVEN: "+"; ".join(sorted(map(str,self.numerical_candidates-self.goal_conditional-s1))),
        ])
