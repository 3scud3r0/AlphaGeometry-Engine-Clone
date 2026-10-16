"""Isolated execution of Google's vendored AlphaGeometry 2 symbolic DDAR reference.

Upstream deducibility is NOT a formal proof certificate; the user-provided
diagram and premise validity are assumed by the reference. No model training.
"""
from __future__ import annotations
import argparse
from dataclasses import dataclass, asdict
import json
from pathlib import Path
import subprocess
import sys

_VENDOR = Path(__file__).resolve().parent.parent / "vendor" / "alphageometry2_symbolic"
_SENTINEL = "__GEOFORGE_AG2_RESULT__="
_REFERENCE_CODE = r"""
import json,sys
from parse import AGProblem
from ddar import DDAR
p=json.loads(sys.stdin.read())
try:
    prob=AGProblem.parse(p["formal_problem"])
    if prob.goal is None:
        raise ValueError("formal input lacks goal")
    engine=DDAR(prob.points)
    for fact in prob.preds: engine.force_pred(fact)
    engine.deduction_closure()
    out={"result":"deduced" if engine.check_pred(prob.goal) else "unknown",
         "num_points":len(prob.points),"num_premises":len(prob.preds)}
except Exception as exc:
    out={"result":"error","exception":type(exc).__name__,"detail":str(exc)[:800]}
print("__GEOFORGE_AG2_RESULT__="+json.dumps(out,sort_keys=True))
"""
_EXAMPLES_CODE = r"""
from test import problems_without_aux,problems_with_aux
import json
print("__GEOFORGE_AG2_RESULT__="+json.dumps({
"without_aux":list(problems_without_aux.items()),
"with_aux":list(problems_with_aux.items())}))
"""

@dataclass(frozen=True)
class ReferenceResult:
    result: str
    num_points: int | None = None
    num_premises: int | None = None
    exception: str | None = None
    detail: str = ""

def _invoke(script: str, stdin: str = "", timeout: float = 30.) -> dict:
    if timeout <= 0: raise ValueError("timeout must be positive")
    required=("ddar.py","elimination.py","numericals.py","parse.py")
    if not all((_VENDOR / name).is_file() for name in required):
        return {"result":"unavailable","detail":"vendored AG2 DDAR core is missing"}
    try:
        completed=subprocess.run([sys.executable,"-c",script],input=stdin,
                                 text=True,encoding="utf-8",cwd=str(_VENDOR),
                                 capture_output=True,timeout=timeout,check=False)
    except subprocess.TimeoutExpired:
        return {"result":"timeout","detail":"AG2 DDAR exceeded time budget"}
    matches=[line.split(_SENTINEL,1)[1] for line in completed.stdout.splitlines()
             if _SENTINEL in line]
    if not matches:
        return {"result":"error","detail":
                f"subprocess exit={completed.returncode}, stderr={completed.stderr[-800:]}"}
    try:
        return json.loads(matches[-1])
    except json.JSONDecodeError as exc:
        return {"result":"error","detail":"invalid DDAR process response: "+str(exc)}

def prove_with_reference(formal_problem: str, *, timeout: float = 30.) -> ReferenceResult:
    """Return deduced/unknown/timeout/error/unavailable (NOT independent certificate)."""
    if not isinstance(formal_problem,str) or "?" not in formal_problem:
        raise ValueError("expected AG2 formal problem containing ? goal")
    raw=_invoke(_REFERENCE_CODE,json.dumps({"formal_problem":formal_problem}),timeout)
    return ReferenceResult(**{k:v for k,v in raw.items()
                              if k in ReferenceResult.__dataclass_fields__})

def official_examples(*, timeout: float = 10.) -> dict:
    raw=_invoke(_EXAMPLES_CODE,timeout=timeout)
    if raw.get("result") in ("error","unavailable","timeout"):
        raise RuntimeError(raw.get("detail",raw["result"]))
    return {"without_aux":tuple(tuple(x) for x in raw["without_aux"]),
            "with_aux":tuple(tuple(x) for x in raw["with_aux"])}

def evaluate_examples(*, limit: int = 3, timeout: float = 30.) -> dict:
    if limit < 1: raise ValueError("limit must be positive")
    examples=official_examples()
    items=list(examples["without_aux"][:limit])
    details=[{"id":name,**asdict(prove_with_reference(src,timeout=timeout))}
             for name,src in items]
    return {"tested":len(details),
            "deduced":sum(x["result"]=="deduced" for x in details),
            "results":details,
            "source":"vendored upstream examples, NOT complete IMO-AG-30 benchmark"}

def main(argv=None):
    ap=argparse.ArgumentParser(description=__doc__)
    commands=ap.add_subparsers(dest="command",required=True)
    p=commands.add_parser("prove")
    arg=p.add_mutually_exclusive_group(required=True)
    arg.add_argument("--problem")
    arg.add_argument("--file")
    p.add_argument("--timeout",type=float,default=30.)
    e=commands.add_parser("examples")
    e.add_argument("--limit",type=int,default=3)
    e.add_argument("--timeout",type=float,default=30.)
    ns=ap.parse_args(argv)
    if ns.command=="prove":
        source=Path(ns.file).read_text(encoding="utf-8") if ns.file else ns.problem
        result=asdict(prove_with_reference(source,timeout=ns.timeout))
        print(json.dumps(result,ensure_ascii=False,sort_keys=True))
        return 0 if result["result"]=="deduced" else 2
    result=evaluate_examples(limit=ns.limit,timeout=ns.timeout)
    print(json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2))
    return 0 if result["tested"]==result["deduced"] else 2

if __name__=="__main__":
    raise SystemExit(main())
