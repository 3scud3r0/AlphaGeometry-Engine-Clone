"""JSON proof certificate schema v1; verifier checks each inference."""
import json
from geoforge_core.ast import Predicate
from .proof_kernel import Proof,ProofStep,ProofKernel

def dump(proof):
    return json.dumps({"schema":"geoforge.proof.v1",
        "premises":[p.serialize() for p in proof.premises],
        "goal":proof.goal.serialize(),
        "steps":[{"rule":s.rule,"conclusion":s.conclusion.serialize(),
                  "parents":[p.serialize() for p in s.parents]} for s in proof.steps]},sort_keys=True)

def load(blob):
    from geoforge_core.parser_ag2 import parse_predicate
    v=json.loads(blob)
    if v.get("schema")!="geoforge.proof.v1": raise ValueError("unknown certificate schema")
    return Proof(tuple(parse_predicate(x) for x in v["premises"]),
                 parse_predicate(v["goal"]),
                 tuple(ProofStep(parse_predicate(x["conclusion"]),x["rule"],
                       tuple(parse_predicate(y) for y in x["parents"])) for x in v["steps"]))

def verify_json(blob):
    return ProofKernel().check(load(blob))
