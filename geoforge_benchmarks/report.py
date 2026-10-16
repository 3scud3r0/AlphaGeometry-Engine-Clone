"""Reproducible run accounting; unverified claims are not scored as solved."""
from dataclasses import dataclass
import json

@dataclass(frozen=True)
class Result:
    problem_id:str
    status:str
    seconds:float
    certificate_verified:bool=False

def summarize(results):
    rows=tuple(results)
    accepted=[r for r in rows if r.status=="proved" and r.certificate_verified]
    return {"total":len(rows),"certified_solved":len(accepted),
            "fraction":len(accepted)/len(rows) if rows else None,
            "unverified_proof_claims":sum(r.status=="proved" and not r.certificate_verified for r in rows),
            "total_seconds":sum(max(0.,r.seconds) for r in rows)}

def save_json(summary,path):
    with open(path,"w",encoding="utf-8") as handle:
        json.dump(summary,handle,indent=2,sort_keys=True)
