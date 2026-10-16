"""Independent small proof kernel: checks axioms and instantiated rules only."""
from dataclasses import dataclass
from geoforge_core.ast import Predicate
from geoforge_core.canonical import canonical
from geoforge_core.type_system import check_predicate, GeometryTypeError
from .ddar2_rules import default_rules
from .rule_compiler import match_rule

@dataclass(frozen=True)
class ProofStep:
    conclusion: Predicate
    rule: str
    parents: tuple[Predicate,...] = ()

@dataclass(frozen=True)
class Proof:
    premises: tuple[Predicate,...]
    goal: Predicate
    steps: tuple[ProofStep,...]

class ProofKernel:
    def __init__(self,rules=None):
        self.rules={r.name:r for r in (default_rules() if rules is None else rules)}
    def check(self,proof):
        # Reject malformed facts even when a forged certificate repeats one
        # verbatim as a supposed premise.
        try:
            for p in (*proof.premises,proof.goal):
                check_predicate(p)
            for step in proof.steps:
                check_predicate(step.conclusion)
                for parent in step.parents: check_predicate(parent)
        except (GeometryTypeError,ValueError,TypeError):
            return False
        known={canonical(p) for p in proof.premises}
        for step in proof.steps:
            claim=canonical(step.conclusion)
            if step.rule=="premise":
                if claim not in known: return False
                continue
            if step.rule not in self.rules: return False
            parents=tuple(canonical(p) for p in step.parents)
            if not all(p in known for p in parents): return False
            rule=self.rules[step.rule]
            justified=any(canonical(goal)==claim and set(used)==set(parents)
                          for goal,used in match_rule(rule,parents))
            if not justified: return False
            known.add(claim)
        return canonical(proof.goal) in known
