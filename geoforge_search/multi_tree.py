"""Honest multi-strategy closure: only actual provable facts count."""
from dataclasses import dataclass
from geoforge_core.canonical import canonical
from geoforge_prover.closure import ClosureEngine

@dataclass(frozen=True)
class SearchReport:
    status: str
    rounds: int
    witnesses: tuple = ()

class SearchForest:
    def __init__(self,rule_sets,maxfacts=750):
        self.rule_sets=tuple(tuple(r) for r in rule_sets)
        self.maxfacts=maxfacts
    def prove(self,premises,goal):
        witnesses=[]
        for number,rules in enumerate(self.rule_sets):
            graph=ClosureEngine(premises,rules,maxfacts=self.maxfacts).run()
            if graph.contains(goal):
                return SearchReport("proved_in_subset",number+1,tuple(graph.dependencies(goal)))
            witnesses.append(len(graph.facts))
        return SearchReport("unknown",len(self.rule_sets),tuple(witnesses))
