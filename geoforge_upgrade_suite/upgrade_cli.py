#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""One entrypoint for the honest GeoForge research extension.

Usage:
  python geoforge_upgrade_suite/upgrade_cli.py test --mode quick
  python geoforge_upgrade_suite/upgrade_cli.py test --mode stress
  python geoforge_upgrade_suite/upgrade_cli.py search --given 'midp d a b' \
    --given 'midp e a c' --given 'ncoll a b c' --goal 'para d e b c'
  python geoforge_upgrade_suite/upgrade_cli.py formalize --text '...'
  python geoforge_upgrade_suite/upgrade_cli.py symbolic --given ... --goal ...
  python geoforge_upgrade_suite/upgrade_cli.py inventory
"""
from __future__ import annotations
from pathlib import Path
import argparse
import json
import subprocess
import sys
import time
import traceback

ROOT=Path(__file__).resolve().parent
PARENT=ROOT.parent
sys.path.insert(0,str(ROOT))

from technical_benchmark import (SourceInventory,ExternalBenchmarkGuard,
    ReproducibilityStamp,BenchmarkCommand)
from reasoning_search import (load_engine,CertifiedSearchEnsemble,Budget,
    ProofGapAnalyzer)
from symbolic_coordinates import AlgebraicCoordinateProver
from formal_language import NLToDSLTranslator
from neural_baseline import (GeometryTokenizer,TransformerConfig,
    GeometryTransformer,NeuralTrainer,TrainingConfig,ProofTextDataset,require_torch)


def dump(data):print(json.dumps(data,ensure_ascii=False,indent=2,default=str))


def cmd_test(a):
    timeout=60 if a.mode=='quick' else 180
    args=[sys.executable,'-m','pytest','-q',str(ROOT/'tests')]
    if a.mode=='quick':args.extend(['-k','not stress_matrix'])
    result=BenchmarkCommand().run(args,timeout=timeout,cwd=str(ROOT))
    dump({'status':'passed' if result['returncode']==0 else 'failed',
          'command':args,'stdout':result['stdout'][-2000:],
          'stderr':result['stderr'][-3000:],'timed_out':result['timed_out']})
    return result['returncode']


def cmd_search(a):
    core=load_engine(str(PARENT/'geoforge.py'))
    coords={}
    if a.coordinates:
        obj=json.loads(Path(a.coordinates).read_text(encoding='utf8'))
        coords={k:tuple(v) for k,v in obj.items()}
    budget=Budget(seconds=a.timeout,max_nodes=a.nodes,max_auxiliary_points=a.depth,
        max_facts=a.maxfacts,beam_width=a.beam)
    outcome=CertifiedSearchEnsemble(core,budget,seed=a.seed).solve(
        a.given,a.goal,coordinates=coords,n_trees=a.trees)
    dump(outcome.report())
    return 0 if outcome.status=='certified' else 1


def cmd_formalize(a):
    dsl,parsed=NLToDSLTranslator().translate(a.text)
    dump({'dsl':dsl,'analysis':parsed.to_dict()})
    return 0 if parsed.is_complete() else 2


def cmd_symbolic(a):
    try:
        result=AlgebraicCoordinateProver(max_pairs=a.pairs,max_points=a.maxpoints).prove(
              a.given,a.goal)
    except Exception as ex:
        dump({'status':'error','error':type(ex).__name__+': '+str(ex)})
        return 2
    dump(result.to_dict())
    return 0 if result.status=='polynomial_identity_proven' else 1


def cmd_analysis(a):
    core=load_engine(str(PARENT/'geoforge.py'))
    dump(ProofGapAnalyzer(core).compare(a.given,a.goal,timeout=a.timeout))
    return 0


def cmd_train_demo(a):
    require_torch()
    texts=(
       'given midp d a b given midp e a c prove para d e b c',
       'given midp m a b prove cong m a m b',
       'given perp a b c d given perp e f c d prove para a b e f',
       'given cyclic a b c d prove eqangle c a c b d a d b',
    )
    tokenizer=GeometryTokenizer.fit(texts)
    config=TransformerConfig(len(tokenizer.vocab),context=36,dim=32,heads=4,
          layers=1,experts=a.experts,top_k=min(2,a.experts) if a.experts else 2)
    model=GeometryTransformer(config)
    cfg=TrainingConfig(steps=a.steps,batch=4,seed=a.seed)
    trainer=NeuralTrainer(model,cfg)
    result=trainer.train(ProofTextDataset(texts,tokenizer,config.context))
    if a.save:
        trainer.save_checkpoint(a.save,tokenizer,{'status':'research_baseline_not_ag2'})
    dump({'training':result,'parameter_count':sum(p.numel() for p in model.parameters()),
          'note':'Training on toy samples does not measure geometry generalization.'})
    return 0


def cmd_prove_deterministic(a):
    """Neural-free portfolio: proofs, exact counterexamples or unknown."""
    from .deterministic_solver import (DeterministicGeometrySolver,
        DeterministicBudget,IndependentResultChecker)
    budget=DeterministicBudget(seconds=a.timeout,max_points=a.maxpoints,
        max_pairs=a.pairs,max_basis=a.basis,max_terms=a.terms,
        sample_attempts=a.samples)
    coords=json.loads(Path(a.coordinates).read_text(encoding='utf8')) if a.coordinates else None
    outcome=DeterministicGeometrySolver(budget,source_path=PARENT/'geoforge.py',seed=a.seed).prove(
        a.given,a.goal,provided_coordinates=coords)
    report=outcome.to_dict()
    report['certificate_replayed']=IndependentResultChecker(PARENT/'geoforge.py').verify(outcome)
    if a.out:Path(a.out).write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
    dump(report)
    return 0 if outcome.status in ('proved','counterexample') and report['certificate_replayed'] else 1


def cmd_check_deterministic(a):
    from .deterministic_solver import IndependentResultChecker
    try:
        report=json.loads(Path(a.path).read_text(encoding='utf8'))
        accepted=IndependentResultChecker(PARENT/'geoforge.py').verify(report)
    except (ValueError,KeyError,TypeError) as exc:
        accepted=False
    dump({'verified':accepted,'file':a.path})
    return 0 if accepted else 1


def cmd_construct_exact(a):
    from .exact_constructions import ExactConstructionExecutor,ConstructionStep
    doc=json.loads(Path(a.input).read_text(encoding='utf8'))
    operations=[ConstructionStep(name=s['name'],operator=s['operator'],
                args=tuple(s['args']),branch=int(s.get('branch',0))) for s in doc['steps']]
    trace=ExactConstructionExecutor(doc['points']).execute(operations,stop_on_error=True)
    obj=trace.json()
    if a.out:Path(a.out).write_text(json.dumps(obj,ensure_ascii=False,indent=2),encoding='utf8')
    dump(obj)
    return 0 if trace.status=='constructed' else 1


def cmd_inventory(a):
    report=ReproducibilityStamp.manifest(PARENT,a.official)
    if a.out:ReproducibilityStamp.write(a.out,report)
    lines=report['files']
    dump({'total_lines':lines['total_lines'],'nonempty':lines['total_nonempty'],
          'files':len(lines['files']),'classes':lines['total_classes'],
          'functions':lines['total_functions'],
          'external':report['external_benchmarks'],
          'claims':report['claims']})
    return 0


def main(argv=None):
    parser=argparse.ArgumentParser(description='GeoForge extended research suite')
    sub=parser.add_subparsers(dest='mode',required=True)
    test=sub.add_parser('test');test.add_argument('--mode',choices=('quick','stress'),default='quick')
    test.set_defaults(func=cmd_test)
    search=sub.add_parser('search')
    search.add_argument('--given',action='append',default=[])
    search.add_argument('--goal',required=True)
    search.add_argument('--coordinates')
    search.add_argument('--timeout',type=float,default=5)
    search.add_argument('--nodes',type=int,default=100)
    search.add_argument('--maxfacts',type=int,default=1500)
    search.add_argument('--trees',type=int,default=3)
    search.add_argument('--depth',type=int,default=2)
    search.add_argument('--beam',type=int,default=12)
    search.add_argument('--seed',type=int,default=42)
    search.set_defaults(func=cmd_search)
    formal=sub.add_parser('formalize');formal.add_argument('--text',required=True)
    formal.set_defaults(func=cmd_formalize)
    symbolic=sub.add_parser('symbolic')
    symbolic.add_argument('--given',action='append',default=[])
    symbolic.add_argument('--goal',required=True)
    symbolic.add_argument('--pairs',type=int,default=120)
    symbolic.add_argument('--maxpoints',type=int,default=10)
    symbolic.set_defaults(func=cmd_symbolic)
    analysis=sub.add_parser('analysis')
    analysis.add_argument('--given',action='append',default=[])
    analysis.add_argument('--goal',required=True)
    analysis.add_argument('--timeout',type=float,default=5)
    analysis.set_defaults(func=cmd_analysis)
    train=sub.add_parser('train-demo')
    train.add_argument('--steps',type=int,default=8)
    train.add_argument('--experts',type=int,default=0)
    train.add_argument('--seed',type=int,default=42)
    train.add_argument('--save')
    train.set_defaults(func=cmd_train_demo)
    inv=sub.add_parser('inventory');inv.add_argument('--official')
    inv.add_argument('--out');inv.set_defaults(func=cmd_inventory)
    deterministic=sub.add_parser('prove-deterministic',
        help='Resolve sem rede neural, exige certificado exato ou contraexemplo racional')
    deterministic.add_argument('--given',action='append',default=[])
    deterministic.add_argument('--goal',required=True)
    deterministic.add_argument('--timeout',type=float,default=8)
    deterministic.add_argument('--maxpoints',type=int,default=9)
    deterministic.add_argument('--pairs',type=int,default=180)
    deterministic.add_argument('--basis',type=int,default=80)
    deterministic.add_argument('--terms',type=int,default=3000)
    deterministic.add_argument('--samples',type=int,default=150)
    deterministic.add_argument('--coordinates')
    deterministic.add_argument('--seed',type=int,default=1729)
    deterministic.add_argument('--out')
    deterministic.set_defaults(func=cmd_prove_deterministic)
    checker=sub.add_parser('check-deterministic',help='Verifica independentemente um certificado JSON')
    checker.add_argument('--path',required=True)
    checker.set_defaults(func=cmd_check_deterministic)
    construct=sub.add_parser('construct-exact',help='Executa construções algébricas exatas a partir de JSON')
    construct.add_argument('--input',required=True)
    construct.add_argument('--out')
    construct.set_defaults(func=cmd_construct_exact)
    a=parser.parse_args(argv)
    return a.func(a)


if __name__=='__main__':raise SystemExit(main())
