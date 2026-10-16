"""Render only independently checked proof sequences."""
from geoforge_prover.proof_kernel import ProofKernel

def explain(proof):
    if not ProofKernel().check(proof):
        raise ValueError("cannot explain an invalid proof as proven")
    lines=["Premissas: "+", ".join(p.serialize() for p in proof.premises)]
    for i,step in enumerate(proof.steps,1):
        lines.append(f"{i}. {step.conclusion.serialize()} [{step.rule}]")
    lines.append("Conclusão certificada: "+proof.goal.serialize())
    return "\n".join(lines)
