"""Conservative forward closure with exact provenance and resource budgets."""
from geoforge_core.geometry_graph import GeometryGraph
from .ddar2_rules import default_rules
from .rule_compiler import match_rule

class ClosureEngine:
    def __init__(self,premises=(),rules=None,maxfacts=1000,maxrounds=12):
        self.graph=GeometryGraph(premises)
        self.rules=tuple(default_rules() if rules is None else rules)
        self.maxfacts=maxfacts
        self.maxrounds=maxrounds
    def run(self):
        for _ in range(self.maxrounds):
            changed=0
            for rule in self.rules:
                for goal,parents in match_rule(rule,self.graph.facts):
                    if len(self.graph.facts)>=self.maxfacts:
                        return self.graph
                    changed += bool(self.graph.add(goal,rule.name,parents))
            if not changed: break
        return self.graph
