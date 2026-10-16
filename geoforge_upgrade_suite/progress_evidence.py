#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Reconcile local verified subsets with the stable 450-milestone audit.

No amount of unit tests automatically changes COMPLETE or official solve rates.
Each local evidence entry names a regression test and an exact subset proved.
"""
from __future__ import annotations
from dataclasses import dataclass
from collections import Counter,defaultdict
from pathlib import Path
from typing import Mapping,Sequence
import ast
import json
import re
import sys

# Requirement: test basename (function), precise local subset.
EVIDENCE={
 39:('test_vectors_lines_exact','Exact line reflection operation, not full construction DSL'),
 74:('test_vectors_lines_exact','Rational arithmetic through fractions'),
 92:('test_polynomial_ideal_exact','Exact polynomial reduction interface'),
 201:('test_dataset_real_certificates_and_tamper','Exact duplicate check in versioned record schema'),
 206:('test_dataset_real_certificates_and_tamper','Atomic deterministic gzip shards'),
 207:('test_dataset_real_certificates_and_tamper','Streaming read of v5 shards'),
 212:('test_neural_tiny_train_and_checkpoint','Small causal Transformer trained on CPU'),
 213:('test_neural_moe_backward','Sparse MoE layer with backward pass'),
 214:('test_neural_moe_backward','Top-k expert router'),
 216:('test_neural_tiny_train_and_checkpoint','PyTorch causal attention, not GPU FlashAttention benchmark'),
 219:('test_tokenizer_and_grammar','Dynamic tokenizer for formal geometry token sequences'),
 222:('test_neural_tiny_train_and_checkpoint','Toy full sequence causal language modeling'),
 229:('test_neural_tiny_train_and_checkpoint','Simple LR warmup, not full distributed scheduler'),
 230:('test_neural_tiny_train_and_checkpoint','Safe local model checkpoint roundtrip'),
 236:('test_search_auxiliary_never_claims_unconditional','Bounded search state and certified termination'),
 237:('test_search_unknown_goal_finite','Small multi-queue tree traversal, not complete SKEST'),
 239:('test_shared_knowledge_requires_base_hypotheses','Certified workspace accepts only base-premise proofs'),
 242:('test_shared_knowledge_requires_base_hypotheses','Independent certificate verification before sharing'),
 243:('test_shared_knowledge_requires_base_hypotheses','Rejects mismatched assumptions, no unsound lemma sharing'),
 270:('test_search_auxiliary_never_claims_unconditional','Proves with independent certificate and labels conditional aux'),
 281:('test_natural_language_explicit_goals','Conservative deterministic PT/EN language subset'),
 283:('test_natural_language_explicit_goals','Extracts explicit midpoint/parallel/perpendicular predicates'),
 284:('test_natural_language_explicit_goals','Explicit goal extraction without inference'),
 287:('test_natural_language_explicit_goals','Natural-language-to-DSL subset'),
 290:('test_formal_language_unknown_is_not_hallucinated','Rejects unsupported text and reports missing goal'),
 293:('test_natural_language_explicit_goals','Portuguese and English rule patterns subset'),
 294:('test_natural_language_explicit_goals','Limited LaTeX parallel/perpendicular recognizer'),
 296:('test_inversion_circle_and_line','Exact rational point, line, circle inversion'),
 297:('test_inversion_circle_and_line','Inversion image identities; no complete theorem library'),
 298:('test_circumcircle_radical_axis','Exact radical axis of non-concentric circles'),
 299:('test_circumcircle_radical_axis','Radical center for independent radical axes'),
 300:('test_circumcircle_radical_axis','Exact point power computations'),
 302:('test_homogeneous_projection','Exact invertible projective 3x3 transformations subset'),
 303:('test_homogeneous_projection','Homogeneous points and line incidence'),
 304:('test_stress_matrix_ratio_0000','Exact cross ratio and affine invariance'),
 308:('test_coordinate_compilation','Polynomial encoding of geometry predicates'),
 309:('test_polynomial_ideal_exact','Small exact Buchberger basis membership'),
 311:('test_polynomial_ideal_exact','Polynomial ideal membership and exact reduction'),
 312:('test_coordinate_prover_simple','Exact polynomial implication with side conditions'),
 314:('test_vectors_lines_exact','Rational dot/cross vector operations'),
 327:('test_stress_matrix_convex_0000','Convex hull and orientation checks'),
 328:('test_stress_matrix_convex_0000','Exact inside-convex-polygon membership'),
 376:('test_seed_reproducibility','Deterministic data seeds and versioned manifests subset'),
 403:('test_dataset_real_certificates_and_tamper','Proof checker required for all output records'),
 410:('test_stress_matrix_inversion_0000','Integer-grid adversarial/metamorphic scenarios'),
}


class EvidenceTracker:
    def __init__(self,root:Path):
        self.root=root
    def _test_functions(self):
        found=set()
        for path in (self.root/'tests').glob('test_*.py'):
            tree=ast.parse(path.read_text(encoding='utf-8'))
            found.update(n.name for n in tree.body if isinstance(n,ast.FunctionDef))
        return found
    def generate(self,baseline:Mapping,all_tests_passed:bool):
        known_tests=self._test_functions()
        baseline_reqs={int(x['id']):x for x in baseline['requirements']}
        records=[]
        for rid,req in sorted(baseline_reqs.items()):
            original=req['status'];status=original
            entry=EVIDENCE.get(rid)
            if entry and entry[0] in known_tests and all_tests_passed:
                status='VERIFIED_SUBSET'
            records.append({'id':rid,'phase':req['phase'],'name':req['name'],
                'baseline_status':original,'new_status':status,
                'local_test':entry[0] if entry else None,
                'scope':entry[1] if entry else None})
        totals=Counter(x['new_status'] for x in records)
        return {'schema':'geoforge-capability-progress-v5',
          'tests_passed_for_new_evidence':all_tests_passed,
          'total_requirements':len(records),
          'new_tested_subsets':len([x for x in records if x['new_status']=='VERIFIED_SUBSET' and
                               x['baseline_status']!='VERIFIED_SUBSET']),
          'status_counts':dict(totals),
          'all_seven_phases_completed':False,
          'official_AG2_performance_verified':False,
          'requirements':records,
          'limitations':['VERIFIED_SUBSET != COMPLETE.',
            'No official AlphaGeometry2 DDAR differential tests have run.',
            'No AG2 SKEST/Gemini models or olympiad solve-rate comparison is claimed.',
            'Generated stress tests check algebraic invariants, not olympiad success.']}


def load_progress(root:Path,baseline_path:Path,tests_log:Path):
    baseline=json.loads(baseline_path.read_text(encoding='utf-8'))
    log=tests_log.read_text(encoding='utf-8')
    success=bool(re.search(r'\b\d+ passed\b',log)) and 'failed' not in log.lower()
    return EvidenceTracker(root).generate(baseline,success)


if __name__=='__main__':
    suite=Path(__file__).resolve().parent
    base=suite/'auditoria_450'/'relatorio_7fases.json'
    report=load_progress(suite,base,suite/'pytest_full.log')
    dest=suite/'progresso_450_v5.json'
    dest.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
    print(json.dumps({k:v for k,v in report.items() if k!='requirements'},
                  ensure_ascii=False,indent=2))
