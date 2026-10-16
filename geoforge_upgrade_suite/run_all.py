#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Unified local regression gate: legacy benchmark + new functionality.

Exit nonzero if either test suite fails. Official AG2 benchmark remains
BLOCKED unless user supplies the benchmark and official implementation.
"""
from __future__ import annotations
from pathlib import Path
import argparse
import json
import subprocess
import sys
import time
ROOT=Path(__file__).resolve().parent
PROJECT=ROOT.parent
sys.path.insert(0,str(ROOT))
from progress_evidence import load_progress
from technical_benchmark import ReproducibilityStamp,BenchmarkCommand


def run(mode='quick',out=None):
    if mode not in ('quick','stress'):raise ValueError('invalid run mode')
    dest=Path(out) if out else ROOT/'execucao_atual'
    dest.mkdir(parents=True,exist_ok=True)
    jobs=(
        ('new_tests',[sys.executable,'-m','pytest','-q',str(ROOT/'tests')]+
            (['-k','not stress_matrix'] if mode=='quick' else []),180),
        ('phase1',[sys.executable,str(PROJECT/'geoforge.py'),'phase1-test'],70),
        ('phase23',[sys.executable,str(PROJECT/'geoforge.py'),'phase23-test'],70),
        ('old_audit',[sys.executable,str(PROJECT/'geoforge_7fases_benchmark.py'),
             '--mode','quick' if mode=='quick' else 'standard','--gate',
             '--out',str(dest/'auditoria_antiga')],110),
    )
    records=[]
    for name,cmd,timeout in jobs:
        started=time.monotonic()
        result=BenchmarkCommand().run(cmd,timeout=timeout,cwd=str(PROJECT))
        result['name']=name;result['elapsed_s']=round(time.monotonic()-started,4)
        (dest/(name+'.log')).write_text(result['stdout']+'\n'+result['stderr'],encoding='utf8')
        records.append({'name':name,'passed':result['returncode']==0,
             'returncode':result['returncode'],'elapsed_s':result['elapsed_s'],
             'timed_out':result['timed_out']})
        if result['returncode']!=0:break
    passed=all(r['passed'] for r in records) and len(records)==len(jobs)
    baseline=dest/'auditoria_antiga'/'relatorio_7fases.json'
    newer=dest/'new_tests.log'
    if baseline.is_file() and newer.is_file():
        progress=load_progress(ROOT,baseline,newer)
        (dest/'progresso_450.json').write_text(json.dumps(progress,indent=2,
                                             ensure_ascii=False),encoding='utf8')
        status=progress['status_counts']
    else:status={}
    reproducibility=ReproducibilityStamp.manifest(PROJECT)
    (dest/'ambiente.json').write_text(json.dumps(reproducibility,indent=2,
                                          ensure_ascii=False),encoding='utf8')
    summary={'schema':'geoforge-full-gate-v5','passed':passed,'mode':mode,
         'steps':records,'milestone_status':status,
         'official_AG2_parity':'NOT_MEASURED',
         'official_IMO30':'BLOCKED_WITHOUT_DATASET_AND_NEURAL_MODEL'}
    (dest/'resumo.json').write_text(json.dumps(summary,indent=2,
                                 ensure_ascii=False),encoding='utf8')
    print(json.dumps(summary,ensure_ascii=False,indent=2))
    return 0 if passed else 1


def main(argv=None):
    p=argparse.ArgumentParser(description='Run full GeoForge regression gate')
    p.add_argument('--mode',choices=('quick','stress'),default='quick')
    p.add_argument('--out')
    a=p.parse_args(argv)
    return run(a.mode,a.out)


if __name__=='__main__':raise SystemExit(main())
