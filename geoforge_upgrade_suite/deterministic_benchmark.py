#!/usr/bin/env python3
"""Small transparent model-free theorem and counterexample benchmark.

NOT an IMO/AG2 benchmark. Every case specifies target semantics and optional
exact coordinates. In every case, a success is credited ONLY when the
independent checker replays the mathematical certificate/counterexample.
"""
from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
from .deterministic_solver import (DeterministicGeometrySolver,
       DeterministicBudget,IndependentResultChecker)
import argparse,json,time

@dataclass(frozen=True)
class Case:
    name:str
    hypotheses:tuple[str,...]
    goal:str
    expected:str
    witness:dict|None=None

CASES=(
    Case('base_media',('midp d a b','midp e a c','ncoll a b c'),
         'para d e b c','proved'),
    Case('ponto_medio_congruencia',('midp m a b',),
         'cong m a m b','proved'),
    Case('ponto_medio_simetria',('midp m a b',),
         'midp m b a','proved'),
    Case('perpendicular_gera_perpendicular',('perp a b c d',),
         'perp c d a b','proved'),
    Case('transitividade_paralelas',('para a b c d','para c d e f'),
         'para a b e f','proved'),
    Case('conciclicidade',('cyclic a b c d',),
         'eqangle c a c b d a d b','proved'),
    Case('base_nao_perpendicular',('ncoll a b c','midp d a b','midp e a c'),
         'perp d e b c','counterexample',
         {'a':(0,0),'b':(4,0),'c':(2,5),'d':(2,0),'e':(1,'5/2')}),
    Case('triangulo_nao_colinear',('ncoll a b c',),'coll a b c',
         'counterexample',{'a':(0,0),'b':(2,0),'c':(0,2)}),
    Case('paralelismo_nao_implica_perpendicularidade',('para a b c d',),
         'perp a b c d','counterexample',
         {'a':(0,0),'b':(2,0),'c':(0,1),'d':(3,1)}),
    Case('congruencia_nao_implica_paralelismo',('cong a b c d',),
         'para a b c d','counterexample',
         {'a':(0,0),'b':(3,0),'c':(0,0),'d':(0,3)}),
    Case('colinearidade_nao_implica_ortogonalidade',('coll a b c',),
         'perp a b a c','counterexample',
         {'a':(0,0),'b':(2,0),'c':(3,0)}),
    Case('ponto_medio_nao_e_extremidade',('midp m a b','distinct a b'),
         'overlap m a','counterexample',
         {'a':(0,0),'b':(4,0),'m':(2,0)}),
)


def evaluate(source:Path,timeout=2.5):
    results=[];start=time.monotonic()
    checker=IndependentResultChecker(source)
    solver=DeterministicGeometrySolver(
        DeterministicBudget(seconds=timeout,max_pairs=90,max_basis=50,
                            max_terms=1200,max_reductions=6000),source_path=source)
    for case in CASES:
        begin=time.monotonic()
        r=solver.prove(case.hypotheses,case.goal,provided_coordinates=case.witness)
        independent=checker.verify(r)
        passed=r.status==case.expected and independent
        results.append({'case':case.name,'expected':case.expected,'actual':r.status,
                        'method':r.method,'independent_verification':independent,
                        'passed':passed,'elapsed_s':round(time.monotonic()-begin,5),
                        'details':list(r.attempts)})
    return {'schema':'geoforge-untrained-benchmark-v1',
            'official_ag2_benchmark':False,
            'total':len(CASES),'passed':sum(x['passed'] for x in results),
            'failed':sum(not x['passed'] for x in results),
            'elapsed_s':round(time.monotonic()-start,5),'cases':results}


def main(argv=None):
    p=argparse.ArgumentParser();p.add_argument('--source',default='geoforge.py')
    p.add_argument('--timeout',type=float,default=2.5);p.add_argument('--out')
    a=p.parse_args(argv)
    report=evaluate(Path(a.source).resolve(),a.timeout)
    data=json.dumps(report,indent=2,ensure_ascii=False)
    print(data)
    if a.out:Path(a.out).write_text(data,encoding='utf-8')
    return 0 if report['failed']==0 else 1

if __name__=='__main__':raise SystemExit(main())
