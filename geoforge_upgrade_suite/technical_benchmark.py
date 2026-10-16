#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Benchmark instrumentation and conservative AG2 capability evidence.

A generated test passing is a local correctness observation, NEVER evidence
that public AlphaGeometry2 Olympiad accuracy has been reproduced.
"""
from __future__ import annotations
from dataclasses import dataclass,field
from pathlib import Path
from collections import Counter,defaultdict
from typing import Any,Callable,Mapping,Sequence
import ast
import csv
import hashlib
import json
import os
import platform
import statistics
import subprocess
import sys
import time
import tracemalloc


@dataclass(frozen=True)
class Measurement:
    name:str
    iterations:int
    elapsed_s:float
    throughput:float
    peak_bytes:int
    errors:tuple[str,...]
    def report(self):return dict(self.__dict__)


class BenchmarkHarness:
    def __init__(self,seed=0):self.seed=int(seed)
    def run(self,name:str,fn:Callable,iterations:int=10,fail_fast=False):
        if iterations<1:raise ValueError('iteration count must be positive')
        errors=[];tracemalloc.start();start=time.perf_counter()
        for i in range(iterations):
            try:fn(i)
            except Exception as ex:
                errors.append(type(ex).__name__+': '+str(ex))
                if fail_fast:break
        elapsed=time.perf_counter()-start
        _,peak=tracemalloc.get_traced_memory();tracemalloc.stop()
        return Measurement(name,iterations,elapsed,
                 iterations/max(1.e-12,elapsed),peak,tuple(errors[:20]))


class SourceInventory:
    def __init__(self,root):self.root=Path(root)
    def files(self):
        yield from sorted(self.root.rglob('*.py'))
    def summarize(self):
        result=[]
        for file in self.files():
            if '__pycache__' in file.parts:continue
            text=file.read_text(encoding='utf-8')
            try:
                tree=ast.parse(text);classes=[x.name for x in tree.body if isinstance(x,ast.ClassDef)]
                funcs=[x.name for x in tree.body if isinstance(x,(ast.FunctionDef,ast.AsyncFunctionDef))]
                syntax=True
            except SyntaxError:
                classes=[];funcs=[];syntax=False
            result.append({'file':str(file.relative_to(self.root)),
              'lines':len(text.splitlines()),'nonempty':sum(bool(x.strip()) for x in text.splitlines()),
              'bytes':len(text.encode()),'classes':len(classes),'functions':len(funcs),
              'syntax':syntax,'sha256':hashlib.sha256(text.encode()).hexdigest()})
        return {'files':result,'total_lines':sum(x['lines'] for x in result),
           'total_nonempty':sum(x['nonempty'] for x in result),
           'total_classes':sum(x['classes'] for x in result),
           'total_functions':sum(x['functions'] for x in result)}


class CapabilityEvidenceRegistry:
    """Explicit evidence attachment, with no automatic symbol-based passes."""
    VALID={'verified_subset','needs_official_benchmark','not_tested',
           'blocked_external','failed','not_implemented'}
    def __init__(self):self.items={}
    def record(self,requirement_id:int,status:str,test_names:Sequence[str],notes:str):
        if not 1<=requirement_id<=450:raise ValueError('requirement out of range')
        if status not in self.VALID:raise ValueError('invalid evidence status')
        if status=='verified_subset' and not test_names:
            raise ValueError('verified_subset requires test evidence')
        self.items[requirement_id]={'id':requirement_id,'status':status,
                      'tests':tuple(test_names),'notes':notes}
    def export(self):return {'schema':'geoforge-upgrade-evidence-v1',
                             'requirements':[self.items[i] for i in sorted(self.items)]}


class ExternalBenchmarkGuard:
    """Checks datasets and writes BLOCKED instead of counterfeit solve rates."""
    REQUIRED=('imo_ag_30.txt','imo_ag_50.txt','imosl_ag_30.txt','jgex_ag_231.txt')
    def __init__(self,data_dir=None):self.data_dir=Path(data_dir) if data_dir else None
    def inspect(self):
        checks={}
        for name in self.REQUIRED:
            path=self.data_dir/name if self.data_dir else None
            if path and path.exists() and path.stat().st_size>0:
                checks[name]={'status':'PRESENT_NOT_EXECUTED','path':str(path)}
            else:
                checks[name]={'status':'BLOCKED_DATASET_MISSING'}
        return checks


class ReproducibilityStamp:
    @staticmethod
    def manifest(root,benchmarks=None):
        inventory=SourceInventory(root).summarize()
        return {'schema':'geoforge-upgrade-run-v1','python':sys.version,
           'platform':platform.platform(),'files':inventory,
           'external_benchmarks':ExternalBenchmarkGuard(benchmarks).inspect(),
           'claims':{'official_AG2_parity':'not_measured',
              '30_of_30_IMO_AG_30':'not_measured',
              'all_seven_phases_complete':False}}
    @staticmethod
    def write(path,report):
        target=Path(path);target.parent.mkdir(parents=True,exist_ok=True)
        target.write_text(json.dumps(report,indent=2,ensure_ascii=False,sort_keys=True),encoding='utf8')


class RegressionComparison:
    @staticmethod
    def compare(before:Mapping,after:Mapping):
        old={x['file']:x for x in before['files']}
        new={x['file']:x for x in after['files']}
        changed=[n for n in new if n in old and new[n]['sha256']!=old[n]['sha256']]
        added=[n for n in new if n not in old]
        removed=[n for n in old if n not in new]
        return {'added':sorted(added),'removed':sorted(removed),
                'modified':sorted(changed),
                'line_difference':after['total_lines']-before['total_lines']}


class BenchmarkCommand:
    """Controlled subprocess execution. Does NOT execute shell commands."""
    def run(self,argv:Sequence[str],timeout=90.,cwd=None):
        if not argv or timeout<=0:raise ValueError('invalid command')
        try:
            done=subprocess.run(list(argv),cwd=cwd,timeout=timeout,
                     text=True,capture_output=True,check=False)
            return {'returncode':done.returncode,'stdout':done.stdout[-20000:],
                    'stderr':done.stderr[-20000:],'timed_out':False}
        except subprocess.TimeoutExpired as ex:
            return {'returncode':124,'stdout':str(ex.stdout or '')[-20000:],
                    'stderr':str(ex.stderr or '')[-20000:],'timed_out':True}


__all__=[name for name in globals() if not name.startswith('_') and name not in {
    'dataclass','field','Path','Counter','defaultdict','Any','Callable','Mapping','Sequence',
    'ast','csv','hashlib','json','os','platform','statistics','subprocess','sys','time','tracemalloc'}]
