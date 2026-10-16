#!/usr/bin/env python3
"""CLI for the independently checkable, intentionally small modular rule kernel."""
import argparse
import json
from pathlib import Path
from geoforge_core.parser_ag2 import parse_predicate
from geoforge_core.canonical import canonical
from geoforge_prover.closure import ClosureEngine
from geoforge_prover.proof_kernel import Proof,ProofStep,ProofKernel
from geoforge_prover.certificates import dump,verify_json

def solve(givens,goal):
    assumptions=tuple(parse_predicate(s) for s in givens)
    target=parse_predicate(goal)
    engine=ClosureEngine(assumptions)
    graph=engine.run()
    if not graph.contains(target):return None
    steps=[]
    visited=set()
    def walk(fact):
        fact=canonical(fact)
        if fact in visited:return
        source,parents=graph.reasons[fact]
        for parent in parents:walk(parent)
        visited.add(fact)
        if source!="premise":
            steps.append(ProofStep(fact,source,parents))
    walk(target)
    proof=Proof(assumptions,target,tuple(steps))
    if not ProofKernel().check(proof):
        raise RuntimeError("internal proof failed independent verification")
    return proof

def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    commands=parser.add_subparsers(dest="command",required=True)
    solvep=commands.add_parser("prove")
    solvep.add_argument("--given",action="append",default=[])
    solvep.add_argument("--goal",required=True)
    solvep.add_argument("--out",required=False)
    checkp=commands.add_parser("check")
    checkp.add_argument("--path",required=True)
    official=commands.add_parser("reference",help="Run vendored official AG2 DDAR symbolic core")
    official.add_argument("--file",required=True,help="Formal AG2 problem with diagram coordinates")
    official.add_argument("--timeout",type=float,default=30.)
    args=parser.parse_args(argv)
    if args.command=="reference":
        from geoforge_prover.ddar2_reference import prove_with_reference
        from dataclasses import asdict
        text=Path(args.file).read_text(encoding="utf-8")
        outcome=asdict(prove_with_reference(text,timeout=args.timeout))
        print(json.dumps(outcome,sort_keys=True))
        return 0 if outcome["result"]=="deduced" else 2

    if args.command=="check":
        good=verify_json(Path(args.path).read_text(encoding="utf-8"))
        print(json.dumps({"verified":good}))
        return 0 if good else 2
    proof=solve(args.given,args.goal)
    if proof is None:
        print(json.dumps({"status":"unknown","reason":"subset rules did not derive goal"}))
        return 2
    blob=dump(proof)
    if args.out:Path(args.out).write_text(blob,encoding="utf-8")
    print(json.dumps({"status":"proved","verified":verify_json(blob),"certificate":json.loads(blob)}))
    return 0

if __name__=="__main__":
    raise SystemExit(main())
