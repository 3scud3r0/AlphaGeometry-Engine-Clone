#!/usr/bin/env python3
"""One-command regression gate for deterministic, training-free GeoForge.

quick  : local substantive proof tests + transparent mini-benchmark + sample;
stress : previous full regression suite + all 5400 generated matrix cases +
         independently replayed benchmark proofs/counterexamples.
The 12 mini-cases are NOT the IMO/AG2 benchmark.
"""
from __future__ import annotations
from pathlib import Path
import argparse,json,subprocess,sys,time

ROOT=Path(__file__).resolve().parent
PKG=ROOT/'geoforge_upgrade_suite'


def run(args,timeout):
    start=time.monotonic()
    try:
        p=subprocess.run([sys.executable,*args],cwd=ROOT,
                         capture_output=True,text=True,timeout=timeout)
        return {'passed':p.returncode==0,'return_code':p.returncode,
                'elapsed_s':round(time.monotonic()-start,4),
                'stdout_tail':p.stdout[-2000:],'stderr_tail':p.stderr[-1000:]}
    except subprocess.TimeoutExpired as ex:
        return {'passed':False,'return_code':None,'timed_out':True,
                'elapsed_s':round(time.monotonic()-start,4),
                'error':f'timed out after {timeout} seconds'}


def main(argv=None):
    p=argparse.ArgumentParser()
    p.add_argument('--mode',choices=('quick','stress'),default='quick')
    p.add_argument('--out',default=str(ROOT/'RELATORIO_BENCHMARK_SEM_TREINO.json'))
    a=p.parse_args(argv)
    jobs=[('core', ['-m','pytest','-q',str(PKG/'tests'/'test_deterministic_solver.py')],60),
          ('matrix_sample',['-m','pytest','-q',str(PKG/'matrix_untrained'),
                            '-k','_0000 or _0001 or _0100'],60),
          ('mini_benchmark',['-m','geoforge_upgrade_suite.deterministic_benchmark',
                            '--source',str(ROOT/'geoforge.py'),
                            '--out',str(PKG/'deterministic_benchmark_report.json')],90)]
    if a.mode=='stress':
        jobs=[('all_existing_tests',['-m','pytest','-q',str(PKG/'tests')],120),
              ('full_matrix',['-m','pytest','-q',str(PKG/'matrix_untrained')],180),
              jobs[-1]]
    results={name:run(arg,limit) for name,arg,limit in jobs}
    mini=PKG/'deterministic_benchmark_report.json'
    details=json.loads(mini.read_text()) if mini.exists() else None
    manifest=json.loads((PKG/'matrix_untrained'/'manifest.json').read_text())
    report={'schema':'geoforge-untrained-regression-v1','mode':a.mode,
            'status':'passed' if all(v['passed'] for v in results.values()) else 'failed',
            'runs':results,'matrix_test_definitions':manifest['cases'],
            'mini_benchmark':{'cases':details['total'],'passed':details['passed'],
                              'official_AG2_comparison':False} if details else None,
            'cannot_claim':['No 30/30 official evaluation was executed.',
              'A finite bounded prover may return UNKNOWN for hard theorems.',
              'Generated cases test exact identities, not olympiad solve-rate.',
              'Proof correctness requires independently checked side conditions.']}
    Path(a.out).write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding='utf8')
    print(json.dumps({'status':report['status'],'mode':a.mode,
                      'runs':{k:{'passed':v['passed'],'time_s':v['elapsed_s']}
                              for k,v in results.items()},
                      'mini_benchmark':report['mini_benchmark'],
                      'report':a.out},indent=2,ensure_ascii=False))
    return 0 if report['status']=='passed' else 1

if __name__=='__main__':raise SystemExit(main())
