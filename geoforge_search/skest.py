"""Proof-gated workspace inspired by shared-knowledge tree search.

Not a reproduction of AG2 SKEST: this module forbids sharing uncertified lemmas.
"""
from geoforge_core.canonical import canonical
from geoforge_prover.proof_kernel import ProofKernel

class VerifiedWorkspace:
    def __init__(self, kernel=None):
        self.kernel=kernel or ProofKernel()
        self.proofs={}
    def publish(self,proof):
        if not self.kernel.check(proof):return False
        goal=canonical(proof.goal)
        premises=frozenset(canonical(p) for p in proof.premises)
        self.proofs[(goal,premises)]=proof
        return True
    def available(self,fact,premises):
        given=frozenset(canonical(p) for p in premises)
        target=canonical(fact)
        return tuple(p for (conclusion,required),p in self.proofs.items()
                     if conclusion==target and required.issubset(given))
