#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GeoForge Seven-Phase Audit and Benchmark Suite.

Independent, stdlib-first executable QA + capability gap registry.

Usage:
  python geoforge_7fases_benchmark.py --mode quick
  python geoforge_7fases_benchmark.py --mode standard --out auditoria
  python geoforge_7fases_benchmark.py --mode full --official-dir /path/to/alphageometry2
  python geoforge_7fases_benchmark.py --mode full --imo30 /path/to/imo_ag_30.txt
  python geoforge_7fases_benchmark.py --mode standard --gate

Principles:
* PASS requires execution of an actual assertion against the target implementation.
* A matching symbol is NOT sufficient for PASS: it is PARTIAL, pending semantic tests.
* NO_EVIDENCE is not equivalent to a mathematical proof of absence.
* Optional externally sourced benchmarks become BLOCKED/NOT_RUN unless files provided.
* Do not interpret high local synthetic accuracy as IMO/AG2 parity.
* Runs are deterministic when the referenced functions are deterministic.
* Results may be exported as JSON, Markdown, HTML, JUnit XML, and per-requirement CSV.
* Scope includes 450 engineering milestones from the seven-phase plan; entries can
  be satisfied by different implementations if evidence is explicitly added below.
* This suite uses the local file, never downloads/untrusted-executes arbitrary code.
"""
from __future__ import annotations

import argparse
import ast
import contextlib
import copy
import csv
import dataclasses
from dataclasses import dataclass, field
from datetime import datetime, timezone
import gzip
import hashlib
import html
import importlib.util
import io
import json
import math
import os
from pathlib import Path
import random
import shutil
import statistics
import subprocess
import sys
import tempfile
import time
import traceback
import xml.etree.ElementTree as ET

SUITE_VERSION = '1.0.0'
OFFICIAL_REFS = {
 'AG2_code': 'https://github.com/google-deepmind/alphageometry2',
 'AG2_test': 'https://github.com/google-deepmind/alphageometry2/blob/main/test.py',
 'AG1_code': 'https://github.com/google-deepmind/alphageometry',
 'AG2_paper': 'https://www.jmlr.org/papers/volume26/25-1654/25-1654.pdf',
}
PHASE_NAMES = {
 1: 'Linguagem, grafo, álgebra exata e certificação',
 2: 'DDAR2, construções, numerics e lugares geométricos',
 3: 'Geração sintética, datasets e cobertura',
 4: 'Modelo neural, SKEST e análise simbólica',
 5: 'Infraestrutura, benchmark e avaliação externa',
 6: 'Matemática avançada e estratégias de pesquisa',
 7: 'Formalização natural, diagramas e interface',
}

# A ordem é a dos IDs originais. Todas as entradas aparecem no CSV/relatório.
# Inclui alvos avançados não implementados no GeoForge: isso é intencional.
CAPABILITY_SECTIONS = {
 '001-025': '''GeometryLexer|GeometryParser|GeometryAST|GeometryTypeChecker|GeometryCanonicalizer|aconst|rconst|acompute|rcompute|angeq|distmeq|distseq|sameclock|noverlap|overlap|lessthan|cyclic_with_center|LinearExpression|LocusExpression|FreePointPlaceholder|NonConstructiveStatement|GoalNormalizer|VariableScope|DSLSerializer|AG1AG2Compatibility''',
 '026-050': '''ConstructionRegistry|LineLineIntersection|LineCircleIntersection|CircleCircleIntersection|IntersectionBranchResolver|ParallelLineConstructor|PerpendicularLineConstructor|AngleBisectorConstructor|PerpendicularBisectorConstructor|TriangleCenterConstructor|CircleConstructor|TangentConstructor|MidpointAndRatioConstructor|ReflectionConstructor|RotationConstructor|HomothetyConstructor|SimilarityConstructor|EquilateralTriangleConstructor|MultiConstraintConstruction|ImplicitGeometrySolver|ConstructionDependencyGraph|ConstructionExistenceChecker|ConstructionUniquenessChecker|ConstructionEquivalenceChecker|AuxiliaryPointValidator''',
 '051-073': '''PointNode|LineNode|CircleNode|SegmentNode|AngleNode|TriangleNode|PredicateNode|ConstructionNode|ProofDependencyNode|IncidenceIndex|ParallelClassIndex|PerpendicularityIndex|EqualLengthIndex|CyclicPointIndex|CongruenceIndex|SimilarityIndex|GeometryUnionFind|DoublePointEngine|SymbolicPointSubstitution|IncrementalFactPropagation|ContradictionDetector|GraphStateHasher|PersistentGeometryState''',
 '074-097': '''ExactRational|SparseLinearExpression|AngleEquationSystem|AngleModuloPiSolver|AngleConstantSolver|LogDistanceEquationSystem|DistanceEquationSystem|RatioEquationSystem|ExactGaussianElimination|IncrementalRowReduction|SparseMatrixBackend|AlgebraicNormalForm|EquationEntailment|AlgebraicProofTrace|AlgebraicContradictionCheck|ZeroLengthGuard|AngleDegeneracyGuard|ExactConstantRepresentation|PolynomialEquationInterface|AlgebraicDependencyPruner|ModularArithmeticAccelerator|ModularResultCertification|NativeLinearAlgebraBackend|AlgebraDifferentialTests''',
 '098-122': '''DeductiveRuleRegistry|DDAR1CompatibilityRules|DDAR2RuleSet|RuleConditionChecker|TheoremInstantiationEngine|SemiNaiveDeduction|IndexedRuleMatching|SimilarityShapeHasher|CyclicAngleHasher|TriangleCongruenceEngine|TriangleSimilarityEngine|CircleTheoremEngine|TriangleCenterTheorems|MidpointTheorems|ParallelismTheorems|PerpendicularityTheorems|TangentChordTheorems|GeneralizedCentralAngleTheorem|InscribedAngleTheorems|ChordEqualityTheorems|TriangleAngleBisectorTheorems|PointEqualityDeduction|GoalDirectedInference|DeductiveFixedPointEngine|InferenceCompletenessAudit''',
 '123-144': '''GeometryConstraintCompiler|EquationResidualBuilder|InequalityResidualBuilder|RandomDiagramInitializer|ConstructiveDiagramInitializer|HeuristicDiagramInitializer|LocusBasedInitializer|MultipleDiagramCandidates|DifferentiableGeometryLoss|AdamGeometryOptimizer|GaussNewtonSolver|LevenbergMarquardtSolver|NonDegeneracyLoss|ScaleNormalization|TopologyConstraintEvaluator|MultipleSolutionHandler|NumericalStabilityMonitor|AdaptivePrecisionEvaluator|IntervalGeometryValidator|DiagramBranchExplorer|ConstraintSatisfactionVerifier|DiagramEnsemble''',
 '145-161': '''MovingPoint|FixedPoint|MovementDependency|LocusCircleThroughPoint|LocusFixedRadiusCircle|LocusLineThroughPoint|LocusPerpendicularBisector|LocusParallelLine|LocusPerpendicularLine|LocusPointOnFixedLine|LocusPointOnFixedCircle|LocusFixedDistance|LocusFixedDirection|LocusFixedAngle|MovementDependencyClosure|LocusTheoremGenerator|LocusProofVerifier''',
 '162-182': '''ProofStep|ProofCertificate|ProofChecker|AxiomRegistry|TheoremRuleValidator|AlgebraicCertificateVerifier|ConstructionCertificateVerifier|NonDegeneracyCertificate|TopologicalCertificate|ProofDependencyDAG|ProofTraceback|ProofMinimizer|AuxiliaryPointMinimizer|ProofLengthOptimizer|InvalidProofDetector|NumericalCounterexampleFinder|ProofAssumptionAudit|ProofPrettyPrinter|ProofJSONExporter|FormalAssistantBridge|ProofReplayEngine''',
 '183-210': '''RandomGeometryGenerator2|LargeDiagramSampler|ConstructionDistributionSampler|TheoremCandidateExtractor|DeepProofGenerator|AuxiliaryConstructionExtractor|DependencyDifference2|ReverseTopologicalPruning|PremiseMinimizer|GoalDiversitySampler|LocusProblemSampler|ComputeValueProblemSampler|NonConstructiveProblemSampler|MultiAuxiliaryProblemSampler|DifficultyEstimator|CurriculumDatasetBuilder|AuxiliaryBalanceSampler|ProofComplexityBalancer|GeometricFamilyDeduplicator|GraphIsomorphismDeduplicator|DatasetContaminationDetector|IndependentValidationSplit|SyntheticDataQualityGate|ShardedDatasetWriter|StreamingDatasetReader|DistributedDataGenerator|DatasetCheckpointing|DatasetStatistics''',
 '211-235': '''GPUTransformerBackend|TransformerDecoder2|SparseMixtureOfExperts|ExpertRouter|ExpertLoadBalancer|EfficientAttention|KVCache|LongContextManager|DynamicGeometryTokenizer|ProofReferenceTokenizer|GeometryStructuredEmbedding|FullProofLanguageModeling|AuxiliaryPointPredictionHead|MathematicalPretrainingAdapter|MultimodalGeometryEncoder|MixedPrecisionTraining|DistributedTraining|GradientAccumulation|TrainingScheduler|TrainingCheckpointManager|ModelEvaluationSuite|ModelEnsemble|NeuralInferenceServer|ModelDistillation|InferenceQuantization''',
 '236-270': '''SearchState|SearchTree|BeamSearch2|SharedKnowledgeWorkspace|CrossTreeKnowledgeTransfer|InterestingFactExtractor|SharedFactProofValidator|SharedFactDependencyFilter|MultipleModelSearch|SingleAuxiliaryTree|MultiAuxiliaryTree|OperatorBalancedTree|DeepNarrowSearch|ShallowWideSearch|SearchStrategyScheduler|AsynchronousNeuralWorkers|AsynchronousDDARWorkers|DistributedJobQueue|DynamicWorkerAllocation|SearchTranspositionTable|SearchStateCanonicalizer|SearchBranchPruner|ProofProgressScorer|CandidateNoveltyScorer|AuxiliaryConstructionRanker|TopKSampler|TemperatureSampler|GrammarConstrainedDecoder|MultiSampleDecoder|AdaptiveSearchBudget|GlobalSearchDeadline|SearchMemoryManager|SearchReplayLogger|SearchEnsembleController|CertifiedProofTermination''',
 '271-280': '''PremiseDeductionAnalyzer|GoalAssumptionAnalyzer|NumericalRelationDiscoverer|AnalysisSetDifferencer|AnalysisSerializer|AnalysisContextEncoder|NumericalFactConfidenceFilter|GoalConditionIsolation|AnalysisContextCompressor|AnalysisAblationEvaluator''',
 '281-295': '''NaturalLanguageGeometryParser|MathematicalEntityRecognizer|GeometricRelationExtractor|GoalExtractor|GeometricCoreferenceResolver|TopologyLanguageParser|NLToDSLTranslator|FormalizationCandidateGenerator|FormalizationConsensusEngine|FormalizationConsistencyChecker|FormalizationCounterexampleTester|TextDiagramConsistencyChecker|MultilingualProblemInterface|LaTeXGeometryParser|NaturalLanguageProofGenerator''',
 '296-319': '''InversionGeometryEngine|InversionTheoremLibrary|RadicalAxisEngine|RadicalCenterTheorems|CirclePowerEngine|MiquelTheoremEngine|ProjectiveGeometryEngine|HomogeneousCoordinateSystem|CrossRatioEngine|HarmonicDivisionEngine|PascalTheoremEngine|DesarguesTheoremEngine|PolynomialGeometryCompiler|GroebnerBasisEngine|WuMethodEngine|PolynomialIdealReasoner|AlgebraicCoordinateProver|ComplexPlaneGeometryEngine|VectorGeometryEngine|TrigonometricIdentityEngine|SymbolicEquationSubstitution|NonlinearEquationSolver|HybridProverRouter|CrossMethodLemmaExchange''',
 '320-338': '''GeometryInequalityAST|OrderReasoningEngine|TriangleInequalityEngine|GeometricAMGMEngine|SumOfSquaresProver|RealAlgebraicInequalitySolver|BetweennessReasoner|ConvexityReasoner|InsideOutsideReasoner|OrientedAngleInequalityEngine|GeometricInequalityRuleLibrary|QuantifiedGeometryLogic|ParametricPointFamilies|InductionProofEngine|Geometry3DLanguage|SpatialIncidenceEngine|SpatialAngleDistanceEngine|SpatialTransformationEngine|DimensionAwareProofChecker''',
 '339-358': '''HierarchicalProofPlanner|SubgoalGenerator|BackwardChainingEngine|BidirectionalProofSearch|LemmaDiscoveryEngine|AuxiliaryConstructionPolicy|NeuralValueFunction|MonteCarloTreeSearch|ProofGuidedReinforcementLearning|SymbolicRewardModel|FailedSearchLearning|HardProblemReplayBuffer|CounterexampleGuidedSearch|SearchDiversificationPolicy|AdaptiveComputeAllocator|RecursiveProblemDecomposer|ProofStrategyPortfolio|VerifiedLemmaMemory|NovelTheoremMiner|AutomatedStrategySelection''',
 '359-378': '''DistributedExecutionCoordinator|DDARWorkerPool|NeuralInferenceWorkerPool|GPUModelServing|DynamicBatchingEngine|NativeGeometryCore|PythonNativeBindings|SharedFactDatabase|TransactionalProofStorage|DistributedCache|MemoryMappedDataset|DistributedCheckpointing|WorkerFaultRecovery|ResourceQuotaManager|ClusterTelemetry|PerformanceProfiler|ProofSearchTraceDatabase|ExperimentReproducibilityManager|ContainerizedDeployment|InferenceCostOptimizer''',
 '379-412': '''GeometryUnitTests|ConstructionPropertyTests|DeductionRuleTests|AlgebraicSoundnessTests|DegeneracyRegressionTests|OrientationRegressionTests|NumericVsSymbolicTests|ProofCertificateTests|AG1DifferentialTests|AG2DDARDifferentialTests|IMOAG30Benchmark|IMOAG50Benchmark|IMOSLAG30Benchmark|JGEXAG231Benchmark|ExternalGeometryBenchmarkAdapter|UnseenProblemBenchmark|BenchmarkContaminationAudit|FormalizationCoverageReport|DiagramConstructionReport|DDAROnlySolveRate|NeuralOnlyAblation|NeuroSymbolicSolveRate|SearchStrategyAblation|ComputationalBudgetParity|ProofVerificationRate|FalsePositiveCounter|SolverFailureClassifier|PerProblemDiagnosticReport|ConfidenceIntervalEvaluator|MultipleSeedBenchmark|DeterministicReplay|AdversarialGeometryTestSuite|ContinuousIntegration|PerformanceRegressionDetector''',
 '413-450': '''ARITY: linguagem extensível|CONS: catálogo unificado com AGS|num_check: proteger degenerescência|LinSys: certificação algébrica exata|stmt_rows: equações AG2|_prove: semântica e hipóteses|Closure: núcleo DDAR2|Closure.add: checar premissas|_merge: limitar perda de completude|r_simtri: assinatura de triângulos|r_simtri_ang: orientação exata|r_cycang: assinatura angular|Closure.close: ponto fixo|Closure.explain: certificados|Cfg: suportar diagramas maiores|build_diagram: geometria complexa|make_records: diversidade de objetivos|_one_goal: auxiliares e prova|_dedupe_bucket: dedupe estrutural|VOCAB: expansão robusta|cmd_tokenize: nomes/constantes|Model: backend GPU e cache|AdamW: treinamento distribuído|cmd_train: aceleração GPU|parse_defs: construções compostas|parse_goal: objetivos AG2|realize: restrições múltiplas|add_aux: auxiliares compostos|lm_propose: grammar constrained|lm_propose: correção do contexto|solve: SKEST|solve: deadline global|cmd_eval: avaliação externa|AGS: construções AG2|ag_build: não construtivo e overlap|ag_goal: objetivos gerais|cmd_agbench: buscar e provar|cmd_selftest: regressão profunda''',
}

def phase_of(identifier: int) -> int:
    if 413 <= identifier <= 450:
        if identifier in (413, 416, 417, 418, 422, 426): return 1
        if identifier in (414,415,419,420,421,423,424,425,438,439,440,446,447,448):return 2
        if identifier in (427,428,429,430,431,433):return 3
        if identifier in (432,434,435,436,441,442,443,444):return 4
        return 5
    if 1 <= identifier <= 25 or 51 <= identifier <= 97 or 162 <= identifier <= 182: return 1
    if 26 <= identifier <= 50 or 98 <= identifier <= 161: return 2
    if 183 <= identifier <= 210: return 3
    if 211 <= identifier <= 280: return 4
    if 359 <= identifier <= 412: return 5
    if 296 <= identifier <= 358: return 6
    if 281 <= identifier <= 295: return 7
    raise ValueError(identifier)

# Equivalence is only used to discover evidence of code presence (PARTIAL).
# Not a guarantee that the capability is correctly implemented.
SYMBOL_ALIASES = {
 8: ('GEOMETRY_REGISTRY',), 9: ('GEOMETRY_REGISTRY',), 10: ('GEOMETRY_REGISTRY',),
 11: ('GEOMETRY_REGISTRY',), 12: ('GEOMETRY_REGISTRY',),
 13: ('GEOMETRY_REGISTRY',), 14: ('GEOMETRY_REGISTRY',), 15: ('GeometryGraph',),
 16: ('GEOMETRY_REGISTRY',), 17: ('GEOMETRY_REGISTRY',), 24: ('GeometryDSLSerializer',),
 25: ('AG1AG2Compatibility',),
 26: ('ConstructionSolver2',), 27: ('ConstructionSolver2',),
 28: ('ConstructionSolver2',), 29: ('ConstructionSolver2',),
 30: ('ConstructionSolver2',), 31: ('ConstructionSolver2',),
 32: ('ConstructionSolver2',), 33: ('ConstructionSolver2',),
 34: ('ConstructionSolver2',), 36: ('ConstructionSolver2',),
 38: ('ConstructionSolver2',), 39: ('ConstructionSolver2',),
 44: ('ConstructionSolver2',),45: ('NumericalConstraintSolver2',),
 47: ('ConstructionSolver2',), 48: ('ConstructionSolver2',),
 51: ('PointNode',), 52: ('LineNode',), 53: ('CircleNode',),
 61: ('GeometryGraph',), 62: ('PerpendicularityIndex',),
 63: ('GeometryGraph',), 64: ('GeometryGraph',),
 66: ('GeometryGraph',), 67: ('GeometryUnionFind',), 68: ('GeometryGraph',),
 70: ('CertifiedDDAR2Engine',), 71: ('GeometryAssumptionConsistency',),
 74: ('ExactLinearSystem',), 75: ('LinearExpression',),
 77: ('AngleLattice',), 78: ('AngleLattice',),
 82: ('ExactLinearSystem',), 83: ('ExactLinearSystem',),
 84: ('ExactLinearSystem',), 88: ('GeometryAssumptionConsistency',),
 89: ('NonDegeneracyGuard',), 90: ('NonDegeneracyGuard',),
 93: ('ProofMinimizer',),
 98: ('CertifiedDDAR2Engine',),99: ('CertifiedDDAR2Engine',),
 100: ('CertifiedDDAR2Engine',),101: ('ProofCheckerV2',),
 102: ('ProofCheckerV2',),103: ('CertifiedDDAR2Engine',),
 104: ('CertifiedDDAR2Engine',), 106: ('CertifiedDDAR2Engine',),
 108: ('CertifiedDDAR2Engine',), 109: ('CertifiedDDAR2Engine',),
 111: ('CertifiedDDAR2Engine',),112: ('CertifiedDDAR2Engine',),
 113: ('CertifiedDDAR2Engine',), 116: ('CertifiedDDAR2Engine',),
 119: ('FullerCertifiedDDAR2Engine',), 121: ('CertifiedDDAR2Engine',),
 123: ('NumericalConstraintSolver2',),124: ('NumericalConstraintSolver2',),
 125: ('NumericalConstraintSolver2',),126: ('build_diagram',),
 127: ('ConstructionSolver2',),129: ('ConstructionSolver2',),
 130: ('NumericalConstraintSolver2',),133: ('NumericalConstraintSolver2',),
 134: ('NumericalConstraintSolver2',),136: ('_residual_geometric_extended',),
 140: ('NumericalGeometryGuard',),143: ('NumericalConstraintSolver2',),
 146: ('MovingPointDependency',), 147: ('MovingPointDependency',),
 148: ('MovingPointDependency',),159: ('MovingPointDependency',),
 161: ('LocusConstructionProver',),
 165: ('GeometryAssumptionConsistency',),166: ('ProofCheckerV2',),
 168: ('ConstructionSolver2',),169: ('NonDegeneracyGuard',),
 171: ('ProofDependencyDAG',), 172: ('ProofDependencyDAG',),
 175: ('ProofCheckerV2',), 178: ('ProofCheckerV2',),
 179: ('ProofCertificate',),
 183: ('Phase3GeneratorAdvanced',),184: ('Phase3Config',),
 185: ('StochasticSyntheticFactory',),186: ('RandomDiagramProofMiner',),
 187: ('RandomDiagramProofMiner',), 188: ('RandomDiagramProofMiner',),
 189: ('_ancestors',), 190: ('ProofMinimizer',),
 191: ('ProofMinimizer',),192: ('StochasticSyntheticFactory',),
 193: ('LocusConstructionProver',),194: ('GeometryTemplateFactory',),
 195: ('GeometryParser2',),197: ('Phase3Config',),
 198: ('Phase3Config',),199: ('Phase3Config',),
 200: ('Phase3Config',),201: ('GeometryStructureFingerprint',),
 202: ('GeometryStructureFingerprint',),204: ('Phase3DatasetWriter',),
 205: ('Phase3DatasetAuditor',),206: ('Phase3DatasetWriter',),
 207: ('Phase3DatasetAuditor',),208: ('Phase3DatasetWriter',),
 209: ('Phase3DatasetWriter',),210: ('Phase3DatasetAuditor',),
 212: ('Model',), 217: ('Model',), 222: ('Model',),
 229: ('cmd_train',),230: ('Model',),231: ('cmd_eval',),
 238: ('solve',), 245: ('solve',), 264: ('lm_propose',),
 281: ('GeometryParser',), 282: ('GeometryParser',),
 284: ('GeometryParser',), 287: ('GeometryParser',),
 291: ('NumericalCounterexampleFinder',),
 318: ('PolynomialEquationInterface',),
 324: ('PolynomialEquationInterface',),
 346: ('solve',), 347: ('cmd_train',), 351: ('NumericalCounterexampleFinder',),
 367: ('ProofCertificate',), 368: ('GraphStateHasher',),
 369: ('cmd_tokenize',), 371: ('Phase3DatasetWriter',),
 372: ('Phase3DatasetWriter',), 374: ('cmd_bench',),
 379: ('cmd_phase1_test',), 380: ('cmd_phase23_test',),
 381: ('cmd_phase23_test',), 382: ('cmd_phase1_test',),
 383: ('cmd_phase1_test',), 385: ('num_check',),
 386: ('ProofCheckerV2',), 390: ('cmd_agbench',),
 393: ('cmd_agbench',), 396: ('AG2PublicProblemParser',),
 397: ('cmd_agbench',), 398: ('cmd_agbench',),
 403: ('ProofCheckerV2',), 405: ('Phase3DatasetAuditor',),
 406: ('cmd_phase3_verify',), 409: ('Phase3DatasetWriter',),
 410: ('cmd_phase1_test',), 411: ('cmd_phase23_test',),
 412: ('cmd_bench',),
}

# Existing functions are only evidence of partial implementation, never full coverage.
LEGACY_SYMBOL_TARGETS = {
413:'GEOMETRY_REGISTRY',414:'ConstructionSolver2',415:'NumericalGeometryGuard',
416:'ExactLinearSystem',417:'stmt_rows',418:'_prove',419:'CertifiedDDAR2Engine',
420:'CertifiedDDAR2Engine',421:'_merge',422:'r_simtri',423:'r_simtri_ang',
424:'r_cycang',425:'CertifiedDDAR2Engine',426:'ProofCertificate',
427:'Phase3Config',428:'build_diagram',429:'make_records',430:'_one_goal',
431:'GeometryStructureFingerprint',432:'VOCAB',433:'cmd_tokenize',434:'Model',
435:'AdamW',436:'cmd_train',437:'GeometryParser2',438:'AG2PublicProblemParser',
439:'NumericalConstraintSolver2',440:'ConstructionSolver2',441:'lm_propose',
442:'lm_propose',443:'solve',444:'solve',445:'cmd_eval',446:'AGS',
447:'AG2OfficialCoreBridge',448:'ag_goal',449:'cmd_agbench',450:'cmd_selftest'
}

@dataclass
class Capability:
    id: int
    phase: int
    name: str
    symbols: tuple[str,...]
    status: str
    evidence: str
    next_action: str
    tests: list[str] = field(default_factory=list)


def make_catalog(symbols: set[str]) -> list[Capability]:
    entries = []
    for section, raw in CAPABILITY_SECTIONS.items():
        a,b = map(int,section.split('-'))
        names=[s.strip() for s in raw.strip().split('|')]
        assert len(names)==b-a+1, (section, len(names), b-a+1)
        for i, name in zip(range(a,b+1), names):
            aliases = (LEGACY_SYMBOL_TARGETS[i],) if i in LEGACY_SYMBOL_TARGETS else SYMBOL_ALIASES.get(i,(name,))
            present = tuple(a for a in aliases if a in symbols)
            status='PARTIAL' if present else 'MISSING'
            evidence=('Símbolo(s) encontrados: '+', '.join(present)+'; sem teste semântico suficiente.'
                      if present else 'Sem implementação equivalente identificável pela inspeção estática.')
            action=('Criar teste semântico independente, documentação de contrato e diferencial oficial.'
                    if present else 'Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência.')
            entries.append(Capability(i,phase_of(i),name,aliases,status,evidence,action))
    assert len(entries)==450 and [x.id for x in entries]==list(range(1,451))
    return entries

@dataclass
class Case:
    id: str
    phase: int
    group: str
    description: str
    level: str
    fn: object
    related: tuple[int,...] = ()
    seconds_limit: float = 30.0

@dataclass
class CaseResult:
    id: str
    phase: int
    group: str
    description: str
    status: str
    elapsed_seconds: float
    details: str = ''
    related: tuple[int,...] = ()

@dataclass
class Context:
    module: object
    source: Path
    tmp: Path
    mode: str
    seed: int
    args: object
    extras: dict = field(default_factory=dict)

CASES: list[Case]=[]
def case(id, phase, group, description, level='quick', related=(),seconds_limit=30):
    def decoration(fn):
        CASES.append(Case(id,phase,group,description,level,fn,tuple(related),seconds_limit))
        return fn
    return decoration

def must(value, message='assertion falhou'):
    if not value: raise AssertionError(message)
    return value

def expect_error(typ, f, message='entrada inválida foi aceita'):
    try: f()
    except typ: return
    except Exception as e: raise AssertionError(f'exceção errada: {type(e).__name__} {e}') from e
    raise AssertionError(message)

def obj(ctx, string):
    return ctx.module.GeometryParser().fact(string)

def run_cli(ctx, args, expect_return=0, timeout=30):
    p=subprocess.run([sys.executable,str(ctx.source),*args],cwd=str(ctx.tmp),
                     capture_output=True,text=True,encoding='utf8',errors='replace',
                     timeout=timeout, env={**os.environ,'PYTHONHASHSEED':'17','NO_COLOR':'1'})
    must(p.returncode==expect_return,
        f'CLI {args[0]}: status {p.returncode} (esperado {expect_return}); stdout={p.stdout[-1200:]}; stderr={p.stderr[-1200:]}')
    return p.stdout

# PHASE 1: AST, exact algebra, graph, proof system
@case('F1-001',1,'DSL','Tokenização de identificadores e operadores',related=(1,))
def f1_lex(ctx):
    t=ctx.module.GeometryLexer().tokenize('a b c = triangle ; d = midp a b ; prove para d e b c')
    must(t.count(';')==2 and 'triangle' in t and 'midp' in t and '=' in t)

@case('F1-002',1,'DSL','Parser formal de problema completo',related=(2,3))
def f1_ast(ctx):
    p=ctx.module.GeometryParser().parse('a b c = triangle ; d = midp a b ; given ncoll a b c ; prove coll a b d')
    must(len(p.constructions)==2 and len(p.hypotheses)==1 and p.goal.kind=='coll')

@case('F1-003',1,'DSL','Rejeita predicado e aridade desconhecidos')
def f1_invalid_pred(ctx):
    parser=ctx.module.GeometryParser()
    expect_error(ctx.module.GeometrySyntaxError,lambda:parser.fact('nao_existe a b'))
    expect_error(ctx.module.GeometrySyntaxError,lambda:parser.fact('midp a b'))

@case('F1-004',1,'DSL','Rejeita construção que referencia ponto ainda inexistente',related=(4,))
def f1_typecheck(ctx):
    p=ctx.module.GeometryParser();t=ctx.module.GeometryTypeChecker()
    must(t.validate(p.parse('a b c = triangle ; d = midp a b ; prove midp d a b')))
    expect_error(ctx.module.GeometrySyntaxError,lambda:t.validate(p.parse('a b c = triangle ; d = midp a q')))

@case('F1-005',1,'DSL','Roundtrip serialização AST')
def f1_roundtrip(ctx):
    p=ctx.module.GeometryParser()
    x=p.parse('a b c = triangle ; d = midp a b ; given ncoll a b c ; prove coll d a b')
    ds=ctx.module.GeometryDSLSerializer();must(ds.loads(ds.dumps(x)).to_dict()==x.to_dict())

@case('F1-006',1,'DSL','Nomes repetidos e redefinição de pontos')
def f1_duplicate(ctx):
    p=ctx.module.GeometryParser()
    expect_error(ctx.module.GeometrySyntaxError,lambda: ctx.module.GeometryTypeChecker().validate(
        p.parse('a b c = triangle ; a = midp a b')))

@case('F1-007',1,'DSL','Expressões com frações e operações formais',related=(18,))
def f1_expr(ctx):
    F=ctx.module.Fraction; E=ctx.module.LinearExpression
    must(ctx.module.LinearExpressionParser().parse('2*AB-CD+3/2*EF-1/3') ==
         E({'AB':2,'CD':-1,'EF':F(3,2)},F(-1,3)))
    expect_error(ctx.module.GeometrySyntaxError,lambda:ctx.module.LinearExpressionParser().parse('x**2'))

@case('F1-008',1,'Grafo','Union-find reflexividade, simetria e transitividade',related=(67,))
def f1_unionfind(ctx):
    u=ctx.module.GeometryUnionFind()
    u.union('a','b');u.union('b','c')
    must(u.find('a')==u.find('c') and u.find('c')!=u.find('d'))

@case('F1-009',1,'Grafo','Pontos coincidentes e indexação',related=(15,))
def f1_graph(ctx):
    g=ctx.module.GeometryGraph()
    g.add_fact(obj(ctx,'overlap a b'))
    must(g.equivalent_points('a','b') and not g.equivalent_points('a','c'))
    must(len(g.facts_of_kind('overlap'))==1)

@case('F1-010',1,'Grafo','Hash de estado determinístico e persistência',related=(72,73))
def f1_hash(ctx):
    x=ctx.module.GeometryGraph();y=ctx.module.GeometryGraph()
    facts=['coll a b c','midp d a b','distinct c d']
    for s in facts:x.add_fact(obj(ctx,s))
    for s in reversed(facts):y.add_fact(obj(ctx,s))
    must(ctx.module.GraphStateHasher.hash(x)==ctx.module.GraphStateHasher.hash(y))
    ps=ctx.module.PersistentGeometryState(delta=('a',)).add(('b',)); must(set(ps.facts())=={'a','b'})

@case('F1-011',1,'Álgebra','Sistema racional: consequência exata e testemunho',related=(74,82,86))
def f1_rational(ctx):
    E=ctx.module.ExactLinearSystem();E.add({'x':2,'y':1},'eq1');E.add({'y':1},'eq2')
    ok,coeff=E.prove({'x':2}); must(ok and E.check_witness({'x':2},coeff))
    must(not E.prove({'z':1})[0])

@case('F1-012',1,'Álgebra','Rejeita falso testemunho racional')
def f1_fake_rational(ctx):
    E=ctx.module.ExactLinearSystem();E.add({'x':1},'eq1')
    must(not E.check_witness({'y':1},{'eq1':1}))

@case('F1-013',1,'Álgebra','Ângulos: não divide congruências sem justificativa',related=(77,))
def f1_angle(ctx):
    a=ctx.module.AngleLattice();a.add({'x':2},'double')
    must(not a.prove({'x':1})[0], '2x=0 (mod pi) NÃO implica x=0 (mod pi)')
    a.add({'x':1,'K':-1},'right');ok,w=a.prove({'x':2})
    must(ok and a.check_witness({'x':2},w))

@case('F1-014',1,'Álgebra','Auditoria diferencial algébrica aleatória',level='standard',related=(97,))
def f1_differential(ctx):
    must(ctx.module.AlgebraDifferentialTests.run(30 if ctx.mode=='standard' else 100,seed=ctx.seed))

@case('F1-015',1,'Certificados','Teorema da base média: certificado válido',related=(162,163,164))
def f1_cert_valid(ctx):
    p=lambda s:obj(ctx,s)
    giv=tuple(map(p,('midp d a b','midp e a c','ncoll a b c')))
    goal=p('para d e b c');st=ctx.module.ProofStep(goal,'midline',giv[:2]);c=ctx.module.ProofCertificate(giv,goal,(st,))
    must(ctx.module.ProofCheckerV2().verify(c)[0])
    ctx.extras['midline_cert']=c

@case('F1-016',1,'Certificados','Rejeita certificado sem hipótese de não-colinearidade')
def f1_cert_missing_guard(ctx):
    p=lambda s:obj(ctx,s)
    giv=tuple(map(p,('midp d a b','midp e a c')))
    goal=p('para d e b c');c=ctx.module.ProofCertificate(giv,goal,(ctx.module.ProofStep(goal,'midline',giv),))
    must(not ctx.module.ProofCheckerV2().verify(c)[0])

@case('F1-017',1,'Certificados','Rejeita conclusão adulterada')
def f1_forged_conclusion(ctx):
    p=lambda s:obj(ctx,s)
    giv=tuple(map(p,('midp d a b','midp e a c','ncoll a b c')))
    goal=p('perp d e b c');c=ctx.module.ProofCertificate(giv,goal,(ctx.module.ProofStep(goal,'midline',giv[:2]),))
    must(not ctx.module.ProofCheckerV2().verify(c)[0])

@case('F1-018',1,'Certificados','Rejeita nome de regra inexistente')
def f1_fake_rule(ctx):
    p=lambda s:obj(ctx,s)
    giv=tuple(map(p,('midp d a b','midp e a c','ncoll a b c')))
    goal=p('para d e b c');c=ctx.module.ProofCertificate(giv,goal,(ctx.module.ProofStep(goal,'magic_rule',giv[:2]),))
    must(not ctx.module.ProofCheckerV2().verify(c)[0])

@case('F1-019',1,'Certificados','Rejeita dependência que não consta como fato conhecido')
def f1_fake_dependency(ctx):
    p=lambda s:obj(ctx,s)
    giv=tuple(map(p,('midp d a b','ncoll a b c')))
    goal=p('para d e b c');c=ctx.module.ProofCertificate(giv,goal,(
       ctx.module.ProofStep(goal,'midline',(p('midp d a b'),p('midp e a c'))),))
    must(not ctx.module.ProofCheckerV2().verify(c)[0])

@case('F1-020',1,'Certificados','JSON roundtrip + replay',related=(180,182))
def f1_json(ctx):
    p=lambda s:obj(ctx,s)
    giv=tuple(map(p,('midp d a b','midp e a c','ncoll a b c')))
    goal=p('para d e b c');c=ctx.module.ProofCertificate(giv,goal,(ctx.module.ProofStep(goal,'midline',giv[:2]),))
    t=ctx.tmp/'proof_valid.json';ctx.module.ProofJSONExporter.dump(c,t)
    must(ctx.module.ProofReplayEngine().replay(t)[0])
    must(ctx.module.ProofCertificate.from_dict(json.loads(t.read_text())).to_dict()==c.to_dict())

@case('F1-021',1,'Certificados','Verificador independente em outro processo')
def f1_cli_valid(ctx):
    p=lambda s:obj(ctx,s)
    giv=tuple(map(p,('midp d a b','midp e a c','ncoll a b c')))
    goal=p('para d e b c');c=ctx.module.ProofCertificate(giv,goal,(ctx.module.ProofStep(goal,'midline',giv[:2]),))
    t=ctx.tmp/'cli_valid.json';ctx.module.ProofJSONExporter.dump(c,t)
    out=run_cli(ctx,['check-proof','--file',str(t)],timeout=15)
    must(json.loads(out)['verified'] is True)

@case('F1-022',1,'Certificados','CLI retorna erro para prova falsificada')
def f1_cli_bad(ctx):
    p=lambda s:obj(ctx,s)
    giv=tuple(map(p,('midp d a b','midp e a c','ncoll a b c')))
    goal=p('perp d e b c');c=ctx.module.ProofCertificate(giv,goal,(ctx.module.ProofStep(goal,'midline',giv[:2]),))
    t=ctx.tmp/'cli_bad.json';ctx.module.ProofJSONExporter.dump(c,t)
    out=run_cli(ctx,['check-proof','--file',str(t)],expect_return=1,timeout=15)
    must(json.loads(out)['verified'] is False)

@case('F1-023',1,'Certificados','Premissas contraditórias são rejeitadas')
def f1_contradiction(ctx):
    c=ctx.module.GeometryAssumptionConsistency
    must(not c.check((obj(ctx,'coll a b c'),obj(ctx,'ncoll a b c')))[0])

@case('F1-024',1,'Numérico','Segmento nulo não pode produzir paralelismo')
def f1_deg_para(ctx):
    must(not ctx.module.num_check(('para','a','a','b','c'),
                                  {'a':(0.,0.),'b':(1.,0.),'c':(0.,1.)}))

@case('F1-025',1,'Numérico','Segmento nulo não pode produzir perpendicularidade')
def f1_deg_perp(ctx):
    must(not ctx.module.num_check(('perp','a','a','b','c'),
                                  {'a':(0.,0.),'b':(1.,0.),'c':(0.,1.)}))

@case('F1-026',1,'Numérico','Pontos coincidentes não definem colinearidade válida')
def f1_deg_coll(ctx):
    must(not ctx.module.num_check(('coll','a','a','b'),{'a':(0.,0.),'b':(1.,0.)}))

@case('F1-027',1,'Numérico','Verifica relações geométricas legítimas')
def f1_numeric_true(ctx):
    C={'a':(0.,0.),'b':(4.,0.),'c':(0.,3.),'d':(2.,0.)}
    must(ctx.module.num_check(('midp','d','a','b'),C))
    must(ctx.module.num_check(('perp','a','b','a','c'),C))

@case('F1-028',1,'CLI','Comando oficial phase1-test',level='standard')
def f1_selftest(ctx):
    text=run_cli(ctx,['phase1-test'],timeout=20)
    must('PASSARAM' in text)

# PHASE 2: constructions, DDAR subset, numeric optimization, locus
@case('F2-001',2,'Construções','Interseção de duas retas com solução única',related=(27,44))
def f2_ll(ctx):
    m=ctx.module;s=m.ConstructionSolver2()
    C={'a':(0.,0.),'b':(4.,0.),'c':(2.,-4.),'q':(0.,2.)}
    constraints=[m.ConstructionConstraint('on_line',('a','b')),m.ConstructionConstraint('on_line',('c','q'))]
    x=s.construct('x',constraints,C).point
    must(abs(x[0]-2/3)<1e-7 and abs(x[1])<1e-7)

@case('F2-002',2,'Construções','Interseção reta-círculo com dois ramos',related=(28,30))
def f2_lc(ctx):
    m=ctx.module;C={'o':(0.,0.),'p':(2.,0.),'a':(-4.,0.),'b':(4.,0.)}
    r=m.ConstructionSolver2().construct('x',(
       m.ConstructionConstraint('on_circle',('o','p')),
       m.ConstructionConstraint('on_line',('a','b'))),C,allow_overlap=True)
    must(len(r.candidates)==2)
    must(all(abs(abs(x[0])-2)<1e-8 and abs(x[1])<1e-8 for x in r.candidates))

@case('F2-003',2,'Construções','Ambiguidade de interseção exige escolha explícita',related=(48,))
def f2_ambiguous(ctx):
    m=ctx.module;C={'o':(0.,0.),'p':(2.,0.),'a':(-4.,0.),'b':(4.,0.)}
    constraints=[m.ConstructionConstraint('on_circle',('o','p')),m.ConstructionConstraint('on_line',('a','b'))]
    expect_error(m.GeometrySyntaxError,lambda:m.ConstructionSolver2().construct(
       'x',constraints,C,allow_overlap=True,require_unique=True))

@case('F2-004',2,'Construções','Ponto médio exato na representação numérica',related=(38,))
def f2_midpoint(ctx):
    m=ctx.module;C={'a':(0.,0.),'b':(4.,2.)}
    x=m.ConstructionSolver2().construct('x',[m.ConstructionConstraint('midpoint',('a','b'))],
                                       C,allow_overlap=True).point
    must(m.dist(x,(2.,1.))<1e-8)

@case('F2-005',2,'Construções','Parser de construção composta',related=(44,))
def f2_multi_parse(ctx):
    m=ctx.module;p=m.GeometryParser2().parse(
        'a b c = triangle ; x = on_line a b, on_circle c a ; prove coll x a b')
    must(p.instructions[0][1][0].operator=='on_line')
    must(p.instructions[0][1][1].operator=='on_circle')

@case('F2-006',2,'Construções','Realização de construção composta')
def f2_multi_realize(ctx):
    m=ctx.module;p=m.GeometryParser2().parse(
        'a b c = triangle ; x = on_line a b, on_circle c a ; prove coll x a b')
    C=m.GeometryParser2().realize(p,{'a':(0.,0.),'b':(4.,0.),'c':(1.,2.)},seed=0)
    must(abs(C['x'][1])<1e-8)

@case('F2-007',2,'Numérico','Resolvedor de restrições não lineares com ponto médio',level='standard',related=(131,132,133,134))
def f2_optimize(ctx):
    m=ctx.module;s=m.NumericalConstraintSolver2(max_iterations=45,restarts=2)
    result=s.solve({'a':(0.,0.),'b':(4.,0.),'m':(3.,2.)},('a','b'),(obj(ctx,'midp m a b'),))
    must(result.success and m.dist(result.coordinates['m'],(2.,0.))<1e-5)

@case('F2-008',2,'Locus','Prova condicionada de lugar geométrico retilíneo',related=(161,))
def f2_locus(ctx):
    m=ctx.module
    constraints=[m.ConstructionConstraint('on_line',('a','b'))]
    must(m.LocusConstructionProver().verify(obj(ctx,'coll x a b'),'x',constraints,
                                           ('a','b'),(obj(ctx,'distinct a b'),)))

@case('F2-009',2,'DDAR2','Base média com hipóteses explícitas',related=(111,112))
def f2_midline(ctx):
    m=ctx.module;giv=list(map(lambda s:obj(ctx,s),('midp d a b','midp e a c','ncoll a b c')))
    goal=obj(ctx,'para d e b c')
    engine=m.CertifiedDDAR2Engine(giv,maxfacts=200).close()
    cert=engine.certificate(goal)
    must(cert is not None and m.ProofCheckerV2().verify(cert)[0])

@case('F2-010',2,'DDAR2','Duas perpendiculares à mesma reta implicam paralelas')
def f2_perp_pair(ctx):
    m=ctx.module; giv=['perp a b c d','perp c d e f','distinct a b','distinct c d','distinct e f']
    engine=m.CertifiedDDAR2Engine(tuple(map(lambda x:obj(ctx,x),giv)),maxfacts=100).close()
    goal=obj(ctx,'para a b e f');cert=engine.certificate(goal)
    must(cert is not None and m.ProofCheckerV2().verify(cert)[0])

@case('F2-011',2,'DDAR2','Círculo por quatro pontos equidistantes do centro')
def f2_circle(ctx):
    m=ctx.module
    family,C,assumptions,goal=m.GeometryTemplateFactory(10).build('circle_center')
    cert=m.CertifiedDDAR2Engine(assumptions,maxfacts=350).close().certificate(goal)
    must(cert is not None and m.ProofCheckerV2().verify(cert)[0])

@case('F2-012',2,'DDAR2','Famílias de provas: cobertura real em sementes distintas',level='standard')
def f2_families(ctx):
    m=ctx.module;families=m.GeometryTemplateFactory.families
    must(len(families)>=10)
    seen=set()
    for seed in (0,3):
        for family in families:
            _,C,hyp,goal=m.GeometryTemplateFactory(seed).build(family)
            cert=m.CertifiedDDAR2Engine(hyp,maxfacts=600).close().certificate(goal)
            must(cert is not None and m.ProofCheckerV2().verify(cert)[0],f'{family} seed={seed}')
            must(m.num_check(goal.legacy,C),f'invalid numeric goal {family}')
            seen.add(family)
    ctx.extras['families_tested']=len(seen)

@case('F2-013',2,'DDAR2','Prova longa de midline encadeada',level='standard')
def f2_chain(ctx):
    m=ctx.module;name,C,hyp,goal=m.GeometryTemplateFactory(14).build('double_midline')
    cert=m.CertifiedDDAR2Engine(hyp,maxfacts=700).close().certificate(goal)
    must(cert is not None and len(cert.steps)>=2 and m.ProofCheckerV2().verify(cert)[0])

@case('F2-014',2,'DDAR2','Rejeita regra de Thales sem não-colinearidade')
def f2_forged_thales(ctx):
    m=ctx.module;giv=tuple(map(lambda s:obj(ctx,s),('midp m a c','perp a b b c')))
    goal=obj(ctx,'cong m a m b');cert=m.ProofCertificate(giv,goal,
                           (m.ProofStep(goal,'thales',giv),))
    must(not m.ProofCheckerV2().verify(cert)[0])

@case('F2-015',2,'DDAR2','Substituição de pontos coincidentes não cria fatos falsos',level='standard')
def f2_overlap(ctx):
    m=ctx.module
    hyp=tuple(map(lambda s:obj(ctx,s),('overlap a b','distinct a c','distinct b c','coll a c d')))
    eng=m.FullerCertifiedDDAR2Engine(hyp,maxfacts=250).close(max_steps=600)
    for st in eng.steps:
        must(eng.checker._rule(st, set(hyp)|{x.conclusion for x in eng.steps}),str(st))
    must(eng.certificate(obj(ctx,'overlap a b')) is not None)

@case('F2-016',2,'DDAR2','CLI ddar2-certified + arquivo de certificado',level='standard')
def f2_cli(ctx):
    cert_path=ctx.tmp/'ddar2_cert.json'
    output=run_cli(ctx,['ddar2-certified','--given','midp d a b','--given','midp e a c',
                 '--given','ncoll a b c','--goal','para d e b c','--out',str(cert_path)], timeout=25)
    must(json.loads(output)['solved'] is True)
    must(json.loads(run_cli(ctx,['check-proof','--file',str(cert_path)],timeout=15))['verified'])

@case('F2-017',2,'Integração AG2','Parser reconhece formato de problema oficial',level='standard')
def f2_ag2_import(ctx):
    m=ctx.module
    sample='a@0_0 = ; b@2_0 = ; c@0_1 = ncoll a b c ? perp a b a c'
    o=m.AG2PublicProblemParser().parse(sample)
    must(o is not None and len(o.points)==3 and o.goal is not None)

@case('F2-018',2,'CLI','Comando phase23-test',level='full',seconds_limit=100)
def f2_cli_legacy(ctx):
    out=run_cli(ctx,['phase23-test'],timeout=100)
    must('OK' in out)

# PHASE 3: synthetic generation, manifest, tamper detection, resume
@case('F3-001',3,'Gerador','Registros sintéticos possuem objetivo e prova verificada',related=(183,205))
def f3_record(ctx):
    m=ctx.module
    config=m.Phase3Config(count=1,seed=ctx.seed,max_points=12)
    rec=m.Phase3Generator(config).next_record('midline')
    cert=m.ProofCertificate.from_dict(rec['proof'])
    must(m.ProofCheckerV2().verify(cert)[0]);must(obj(ctx,rec['problem']['goal']).legacy==cert.goal.legacy)

@case('F3-002',3,'Gerador','Cadeia sintética de várias inferências',related=(187,))
def f3_chain(ctx):
    m=ctx.module
    rec=m.Phase3Generator(m.Phase3Config(count=1,seed=31,max_points=12)).next_record('double_midline')
    cert=m.ProofCertificate.from_dict(rec['proof'])
    must(len(cert.steps)>=2 and m.ProofCheckerV2().verify(cert)[0])

@case('F3-003',3,'Gerador','Fingerprints canônicos independem da ordem das hipóteses',related=(201,))
def f3_hash(ctx):
    m=ctx.module; _,_,hyp,goal=m.GeometryTemplateFactory(42).build('midline')
    k=m.GeometryStructureFingerprint.key(hyp,goal)
    must(k==m.GeometryStructureFingerprint.key(tuple(reversed(hyp)),goal))

@case('F3-004',3,'Gerador','Templating distribuído por famílias com sementes diferentes')
def f3_families(ctx):
    m=ctx.module;generator=m.GeometryTemplateFactory(11)
    must(len(set(generator.families))==len(generator.families))
    for fam in generator.families[:5]:
        _,C,hyp,goal=generator.build(fam)
        must(m.num_check(goal.legacy,C),fam)

@case('F3-005',3,'Dataset','Escreve e audita shards com provas certificadas',level='standard',related=(206,209,210))
def f3_dataset(ctx):
    m=ctx.module;p=ctx.tmp/'dataset'
    cfg=m.Phase3Config(count=17,seed=71,max_points=12,workers=1)
    result=m.Phase3DatasetWriter(p,shard_size=5).write(cfg,unique='exact')
    r=m.Phase3DatasetAuditor.verify(p)
    must(r['total']>0 and r['valid']==r['total'] and not r['errors'],str(r.get('errors',[])[:2]))
    must(r['total']==sum(result['counts'].values()))
    ctx.extras['dataset_path']=str(p)
    ctx.extras['dataset_count']=r['total']
    ctx.extras['dataset_manifest']=result

@case('F3-006',3,'Dataset','Manifesto registra hash SHA-256 de cada shard',level='standard')
def f3_manifest(ctx):
    m=ctx.module;p=Path(ctx.extras.get('dataset_path',ctx.tmp/'data_manifest'))
    if not p.exists():
        m.Phase3DatasetWriter(p,shard_size=5).write(m.Phase3Config(count=5,seed=2),unique='exact')
    x=json.loads((p/'phase3_manifest.json').read_text())
    must(len(x['files'])>0)
    for filename in x['files']:
        actual=hashlib.sha256((p/filename).read_bytes()).hexdigest()
        must(x['sha256'][filename]==actual)

@case('F3-007',3,'Dataset','Alterar shard é detectado na auditoria',level='standard')
def f3_tamper(ctx):
    m=ctx.module;p=ctx.tmp/'tampered'
    m.Phase3DatasetWriter(p,shard_size=8).write(m.Phase3Config(count=6,seed=22),unique='exact')
    data=json.loads((p/'phase3_manifest.json').read_text())
    file=p/data['files'][0]
    b=bytearray(file.read_bytes());b[-3] ^= 7;file.write_bytes(b)
    try:rep=m.Phase3DatasetAuditor.verify(p)
    except (ValueError,OSError,EOFError,gzip.BadGzipFile):return
    must(rep['errors'] or rep['valid']<rep['total'],'auditor NÃO percebeu alteração do shard')

@case('F3-008',3,'Dataset','Retomada mantém dados anteriores e atualiza manifesto',level='standard',related=(209,))
def f3_resume(ctx):
    m=ctx.module;p=ctx.tmp/'resume'
    w=m.Phase3DatasetWriter(p,shard_size=6)
    one=w.write(m.Phase3Config(count=7,seed=32),unique='exact')
    two=w.write(m.Phase3Config(count=10,seed=32),unique='exact',resume=True)
    must(two['generated']==10 and two['generated']>one['generated'])
    rep=m.Phase3DatasetAuditor.verify(p)
    must(rep['valid']==rep['total'] and not rep['errors'])

@case('F3-009',3,'Dataset','Sem modo resume, diretório existente não é sobrescrito',level='standard')
def f3_no_overwrite(ctx):
    m=ctx.module;p=ctx.tmp/'overwrite'
    w=m.Phase3DatasetWriter(p,shard_size=8)
    w.write(m.Phase3Config(count=4,seed=39),unique='exact')
    expect_error(FileExistsError,lambda:w.write(m.Phase3Config(count=4,seed=39),unique='exact'))

@case('F3-010',3,'Dataset','Determinismo entre processos e hash randomization',level='full',seconds_limit=90,related=(208,))
def f3_parallel(ctx):
    # Cuidado: datasets paralelos são iguais apenas se configurações e seeds coincidirem.
    def run(workers,hashseed):
        folder=ctx.tmp/f'data_{workers}_{hashseed}'
        env={**os.environ,'PYTHONHASHSEED':str(hashseed),'NO_COLOR':'1'}
        p=subprocess.run([sys.executable,str(ctx.source),'phase3-gen','--out',str(folder),
            '--n','18','--seed','137','--max-points','12','--workers',str(workers),
            '--shard-size','6'],stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,
            timeout=90,env=env)
        must(p.returncode==0,str(p.stderr[-500:])); return folder
    a=run(1,1);b=run(2,999)
    ma=json.loads((a/'phase3_manifest.json').read_text()); mb=json.loads((b/'phase3_manifest.json').read_text())
    must(ma['sha256']==mb['sha256'],'shards não são idênticos entre configurações de processos')

@case('F3-011',3,'Dataset','Confere distribuição por famílias',level='standard')
def f3_coverage(ctx):
    p=Path(ctx.extras.get('dataset_path',ctx.tmp/'dataset'))
    m=ctx.module
    if not p.exists():m.Phase3DatasetWriter(p,shard_size=8).write(m.Phase3Config(count=17,seed=71))
    manifest=json.loads((p/'phase3_manifest.json').read_text())
    families=set()
    for name in manifest['files']:
        with gzip.open(p/name,'rt',encoding='utf8') as f:
            families.update(json.loads(line)['family'] for line in f)
    must(len(families)>=8,f'somente {len(families)} famílias')
    ctx.extras['observed_families']=sorted(families)

@case('F3-012',3,'Dataset','Provas e hipóteses verificadas no arquivo de saída',level='standard')
def f3_full_audit(ctx):
    m=ctx.module;p=Path(ctx.extras.get('dataset_path',ctx.tmp/'dataset'))
    if not p.exists():m.Phase3DatasetWriter(p,shard_size=5).write(m.Phase3Config(count=17,seed=71))
    r=m.Phase3DatasetAuditor.verify(p)
    must(r['valid']==r['total'] and r['errors']==[],str(r['errors'][:3]))

@case('F3-013',3,'CLI','Geração CLI e auditoria CLI',level='standard')
def f3_cli(ctx):
    p=ctx.tmp/'cli_ds'
    a=run_cli(ctx,['phase3-gen','--out',str(p),'--n','8','--seed','61',
                   '--workers','1','--shard-size','4'],timeout=35)
    x=json.loads(a);must(x['generated']==8)
    b=json.loads(run_cli(ctx,['phase3-verify','--out',str(p)],timeout=20))
    must(not b['errors'] and b['total']==b['reported'])

@case('F3-014',3,'Gerador','Minerador estocástico não inventa prova',level='full',seconds_limit=90)
def f3_miner(ctx):
    m=ctx.module
    defs,coords,hyp,goal,cert=m.RandomDiagramProofMiner(19,max_points=11,maxfacts=500,budget_s=.3).next(seed=19,attempts=50)
    must(m.ProofCheckerV2().verify(cert)[0])
    must(m.num_check(goal.legacy,coords))

# PHASES 4-7: critical negative evidence and optional integration (no fake passes)
@case('F4-001',4,'Modelo','Transformer pequeno: forward shape e gradientes finitos',level='standard')
def f4_forward(ctx):
    m=ctx.module
    must(m.np is not None,'NumPy indisponível')
    model=m.Model(V=24,T=8,d=16,L=1,H=2,seed=11)
    ids=m.np.arange(16,dtype=m.np.int64).reshape(2,8)%24
    logits,_=model.forward(ids,keep=True)
    must(logits.shape==(2,8,24) and bool(m.np.isfinite(logits).all()))
    loss,grads=model.loss_grad(ids,(ids+1)%24,m.np.ones((2,8),dtype=m.np.float32))
    must(math.isfinite(loss) and all(bool(m.np.isfinite(t).all()) for t in grads.values()))
    ctx.extras['tiny_neural_params']=model.nparams()

@case('F4-002',4,'Modelo','Salva/carrega pesos sem alterar inferência',level='standard')
def f4_save(ctx):
    m=ctx.module; must(m.np is not None)
    model=m.Model(V=24,T=8,d=16,L=1,H=2,seed=11)
    ids=m.np.array([[1,2,3,4,5,6,7,8]],dtype=m.np.int64)
    logits,_=model.forward(ids,keep=False)
    path=ctx.tmp/'tiny_model.npz';model.save(path)
    new=m.Model.load(path);out,_=new.forward(ids,keep=False)
    must(bool(m.np.allclose(logits,out,atol=1e-8,rtol=1e-8)))

@case('F4-003',4,'Busca','Solver dedutivo pequeno: resposta possui estado explícito',level='full',seconds_limit=40)
def f4_solver(ctx):
    m=ctx.module
    answer=m.solve('a b c = triangle ; d = midp a b ; e = midp a c',
                   'para d e b c',mode='ddar',seed=3,budget=.5,maxfacts=150)
    must(isinstance(answer,dict),str(answer))

@case('F5-001',5,'CLI','Ajuda registra comandos de todas as fases atuais')
def f5_cli(ctx):
    out=run_cli(ctx,['--help'],timeout=10)
    for command in ('phase1-test','phase23-test','phase3-gen','phase3-verify','ddar2-certified','ag2-parse','ag2-official'):
        must(command in out,command)

@case('F5-002',5,'Auditoria','Inventário cobre os 450 marcos e as sete fases')
def f5_catalog(ctx):
    for f in range(1,8):must(any(x.phase==f for x in ctx.extras['catalog']))
    must([x.id for x in ctx.extras['catalog']]==list(range(1,451)))

@case('F5-003',5,'Referência','Registra benchmarks oficiais e separa metas aspiracionais')
def f5_references(ctx):
    must(len(OFFICIAL_REFS)>=3)
    must(ctx.extras['published_reference']['IMO-AG-30']['AG2']==30)
    must(ctx.extras['published_reference']['IMO-AG-50']['AG2']==42)

@case('F6-001',6,'Exploratório','Detecta interface polinomial (sem certificar implementação completa)',level='standard')
def f6_polynomial(ctx):
    must(hasattr(ctx.module,'PolynomialEquationInterface'))
    # O suporte a consequências polinomiais é limitado; registramos sua presença,
    # sem declarar paridade com Wu/Gröbner ou com desigualdades reais.

@case('F7-001',7,'Formalização','Parser aceita DSL existente sem inferir NL não suportada')
def f7_parse(ctx):
    p=ctx.module.GeometryParser().parse('given midp d a b ; prove coll d a b')
    must(p.goal.kind=='coll' and p.hypotheses[0].kind=='midp')

# Parametrized multi-seed and adversarial checks. These are separate test IDs,
# so a future regression pinpoints the exact theorem, geometry and random seed.

def _register_generated_cases():
    # Test every supported synthetic template under several random seeds.
    def make_family_test(fam,seed):
        def t(ctx):
            m=ctx.module
            _,C,hyp,goal=m.GeometryTemplateFactory(seed).build(fam)
            engine=m.CertifiedDDAR2Engine(hyp,maxfacts=800).close()
            cert=engine.certificate(goal)
            must(cert is not None,f'{fam} seed {seed} sem prova')
            must(m.ProofCheckerV2().verify(cert)[0])
            must(m.num_check(goal.legacy,C))
        return t
    # The family registry is statically known from the supplied GeoForge.
    families=('midline','parallel_transitive','perp_pair','para_perp','thales',
              'thales_converse','circle_center','double_midline',
              'parallel_perpendicular_chain','circle_angle_chain',
              'parallelogram_perpendicular_chain','midpoint_parallelogram')
    for i,fam in enumerate(families,1):
        for seed in (0,7,23,101):
            CASES.append(Case(f'F2-THEOREM-{i:02d}-{seed:03d}',2,'Teoremas',
                f'Prova certificada e numérica de {fam}, seed {seed}',
                'standard',make_family_test(fam,seed)))
    # Affine transforms preserve midpoints, collinearity and parallelism.
    # This exercises mathematical invariance, not just one coordinate diagram.
    for index in range(16):
        def metamorphic(ctx,index=index):
            m=ctx.module
            rng=random.Random(909+index)
            _,C,hyp,goal=m.GeometryTemplateFactory(10+index).build('midline')
            theta=rng.uniform(-math.pi,math.pi);co=math.cos(theta);si=math.sin(theta)
            k=rng.uniform(.3,6);tx=rng.uniform(-50,50);ty=rng.uniform(-50,50)
            rotated={n:(k*(co*x-si*y)+tx,k*(si*x+co*y)+ty) for n,(x,y) in C.items()}
            must(m.num_check(goal.legacy,rotated))
            for f in hyp:
                if f.kind in m.MK:must(m.num_check(f.legacy,rotated),str(f))
        CASES.append(Case(f'F2-META-{index:02d}',2,'Metamorfismo',
            f'Rotação, escala e translação de base média ({index})',
            'standard',metamorphic))
    # Certificadores must NEVER accept an unrelated conclusion merely because
    # assumptions are geometrically plausible.
    for index,wrong in enumerate((
        'perp d e b c','para d e a c','cong d e b c','midp d e c',
        'cyclic a b c d','perp a b a c','coll d b c','eqratio a b c d a c b d',
    ),1):
        def mutation(ctx,wrong=wrong):
            m=ctx.module
            given=tuple(obj(ctx,s) for s in ('midp d a b','midp e a c','ncoll a b c'))
            goal=obj(ctx,wrong)
            cert=m.ProofCertificate(given,goal,(m.ProofStep(goal,'midline',given[:2]),))
            must(not m.ProofCheckerV2().verify(cert)[0], 'certificador aceitou prova adulterada')
        CASES.append(Case(f'F1-MUT-{index:02d}',1,'Mutação',
             f'Certificado de base média alterado para {wrong}',
             'standard',mutation))
    # Independent random alpha-equation witnesses. The explicit witness checker
    # must always reject the zero combination for a non-zero target.
    for index in range(12):
        def algebra_mutation(ctx,index=index):
            m=ctx.module;R=random.Random(1500+index)
            E=m.ExactLinearSystem()
            x=R.randint(1,9);y=R.randint(1,7)
            E.add({'x':x,'y':y},'row1')
            E.add({'y':1},'row2')
            ok,w=E.prove({'x':x})
            must(ok and E.check_witness({'x':x},w))
            must(not E.check_witness({'z':1},{'row1':0,'row2':0}))
        CASES.append(Case(f'F1-ALG-{index:02d}',1,'Álgebra',
            f'Testemunho racional aleatório {index}',
            'standard',algebra_mutation))
_register_generated_cases()

@case('F3-STRESS-001',3,'Carga','128 tentativas sintéticas e auditoria completa de shards',level='stress',seconds_limit=240)
def f3_stress_dataset(ctx):
    m=ctx.module;p=ctx.tmp/'stress_128'
    result=m.Phase3DatasetWriter(p,shard_size=32).write(
       m.Phase3Config(count=128,seed=734,max_points=14,workers=2),unique='exact')
    rep=m.Phase3DatasetAuditor.verify(p)
    must(rep['total']>0 and rep['valid']==rep['total'] and not rep['errors'])
    ctx.extras['stress_128_dataset_records']=rep['total']

@case('F1-STRESS-001',1,'Carga','Auditoria algébrica diferencial ampliada (800 ensaios)',level='stress')
def f1_stress_algebra(ctx):
    must(ctx.module.AlgebraDifferentialTests.run(800,seed=ctx.seed))

@case('F2-STRESS-001',2,'Carga','Cobertura de 12 famílias em 30 sementes adversariais',level='stress',seconds_limit=120)
def f2_stress_families(ctx):
    m=ctx.module
    for seed in range(30):
        for family in m.GeometryTemplateFactory.families:
            _,coords,given,goal=m.GeometryTemplateFactory(seed).build(family)
            cert=m.CertifiedDDAR2Engine(given,maxfacts=600).close().certificate(goal)
            must(cert is not None and m.ProofCheckerV2().verify(cert)[0],f'{family}, {seed}')
            must(m.num_check(goal.legacy,coords),f'goal inválido {family}, {seed}')

# ---------- Optional reference benchmarks, required for an honest external claim ----------
def optional_target_checks(args):
    options=[('imo30','IMO-AG-30',1,30,30),('imo50','IMO-AG-50',2,50,42),
             ('imosl30','IMOSL-AG-30',3,30,20),('jgex231','JGEX-AG-231',4,231,None)]
    return options


PUBLISHED_REFERENCE = {
 'IMO-AG-30': {'AG2':30,'total':30,'note':'AlphaGeometry 2 completo, artigo JMLR'},
 'IMO-AG-50': {'AG2':42,'total':50,'note':'AlphaGeometry 2 completo, artigo JMLR'},
 'IMOSL-AG-30': {'AG2':20,'total':30,'note':'AlphaGeometry 2 completo, artigo JMLR'},
 'JGEX-AG-231': {'AG1':228,'total':231,'note':'AlphaGeometry 1 completo; sem referência AG2 publicada diretamente comparável'},
}

LEVELS={'quick': {'quick'},'standard': {'quick','standard'},
        'full': {'quick','standard','full'},'stress': {'quick','standard','full','stress'}}
# Before ANY capability is tagged COMPLETE, require explicit, independent,
# multi-case acceptance tests. Add entries only with tested contracts and
# officially compatible conformance fixtures. Default is deliberately empty:
# no requirement can become COMPLETE just because a class exists or one demo passes.
# Example for a future fully validated component (DO NOT UNCOMMENT without tests):
# REQUIREMENT_ACCEPTANCE = {27: ('F2-001','F2-001-DEGENERATE','F2-001-EXACT')}
REQUIREMENT_ACCEPTANCE: dict[int, tuple[str,...]] = {}

STATUS_SYMBOL = {
 'PASS':'PASS', 'FAIL':'FAIL', 'BLOCKED':'BLOCKED','COMPLETE':'COMPLETE',
 'PARTIAL':'PARTIAL', 'MISSING':'MISSING', 'NOT_RUN':'NOT_RUN',
 'VERIFIED_SUBSET':'VERIFIED_SUBSET', 'ERROR':'ERROR'
}


def load_geoforge(source:Path):
    name='geoforge_benchmark_subject'
    spec=importlib.util.spec_from_file_location(name,str(source))
    if spec is None or spec.loader is None:raise RuntimeError('não foi possível importar '+str(source))
    module=importlib.util.module_from_spec(spec)
    sys.modules[name]=module
    spec.loader.exec_module(module)
    return module


def extract_symbols(path:Path):
    source=path.read_text(encoding='utf-8')
    tree=ast.parse(source,filename=str(path))
    symbols=set()
    for node in ast.walk(tree):
        if isinstance(node,(ast.FunctionDef,ast.AsyncFunctionDef,ast.ClassDef)):
            symbols.add(node.name)
            if isinstance(node,ast.ClassDef):
                for subnode in node.body:
                    if isinstance(subnode,(ast.FunctionDef,ast.AsyncFunctionDef)):
                        symbols.add(node.name+'.'+subnode.name)
        elif isinstance(node,ast.Assign):
            for target in node.targets:
                if isinstance(target,ast.Name):symbols.add(target.id)
        elif isinstance(node,ast.AnnAssign) and isinstance(node.target,ast.Name):
            symbols.add(node.target.id)
    return symbols


def execute_case(case:Case, ctx:Context) -> CaseResult:
    start=time.monotonic()
    try:
        value=case.fn(ctx)
        if value is False: raise AssertionError('teste retornou False')
        status='PASS'; detail='Verificações comportamentais concluídas.'
    except (subprocess.TimeoutExpired,TimeoutError) as ex:
        status='FAIL';detail='Tempo limite excedido: '+str(ex)
    except Exception as ex:
        status='FAIL';detail=f'{type(ex).__name__}: {ex}\n'+traceback.format_exc(limit=3)
    return CaseResult(case.id,case.phase,case.group,case.description,status,
                      round(time.monotonic()-start,5),detail,case.related)


def benchmark_micro(ctx:Context, iterations:int):
    m=ctx.module
    data={}
    def timeit(label,action,n):
        elapsed=[]
        for _ in range(n):
            t=time.perf_counter();action();elapsed.append(time.perf_counter()-t)
        data[label]={'samples':n,'median_ms':round(statistics.median(elapsed)*1000,4),
                     'p95_ms':round(sorted(elapsed)[max(0,math.ceil(n*.95)-1)]*1000,4),
                     'ops_per_sec':round(n/max(1.e-9,sum(elapsed)),2)}
    p=m.GeometryParser()
    timeit('parser_fact',lambda:p.fact('eqangle a b a c d e d f'),iterations)
    def proof():
        given=tuple(map(p.fact,('midp d a b','midp e a c','ncoll a b c')))
        goal=p.fact('para d e b c')
        cert=m.ProofCertificate(given,goal,(m.ProofStep(goal,'midline',given[:2]),))
        assert m.ProofCheckerV2().verify(cert)[0]
    timeit('certified_proof_check',proof,max(3,iterations//3))
    def deduction():
        giv=tuple(map(p.fact,('midp d a b','midp e a c','ncoll a b c')))
        goal=p.fact('para d e b c')
        engine=m.CertifiedDDAR2Engine(giv,maxfacts=120).close()
        cert=engine.certificate(goal)
        assert cert is not None and m.ProofCheckerV2().verify(cert)[0]
    timeit('symbolic_ddar_midline',deduction,max(3,iterations//8))
    return data


def optional_benchmarks(ctx:Context):
    a=ctx.args
    rows=[]
    for key,label,phase,total,reference in optional_target_checks(a):
        filename=getattr(a,key)
        if not filename:
            rows.append({'id':key,'name':label,'status':'BLOCKED','solved':None,'total':total,
                'reason':'Dataset externo não fornecido; nenhuma taxa de sucesso é presumida.',
                'reference':reference})
            continue
        path=Path(filename)
        if not path.is_file():
            rows.append({'id':key,'name':label,'status':'BLOCKED','solved':None,'total':total,
                'reason':'Arquivo informado não existe: '+str(path),'reference':reference})
            continue
        if key not in ('imo30','jgex231'):
            rows.append({'id':key,'name':label,'status':'BLOCKED','solved':None,'total':total,
                'reason':'O CLI agbench do GeoForge utiliza formato AG1; este conjunto necessita adaptador formal AG2 e protocolo validado.',
                'reference':reference})
            continue
        if ctx.mode not in ('full','stress'):
            rows.append({'id':key,'name':label,'status':'NOT_RUN','solved':None,'total':total,
                'reason':'Benchmark externo pesado exige --mode full ou stress.','reference':reference})
            continue
        limit=min(a.max_external_problems,total)
        cmd=[sys.executable,str(ctx.source),'agbench','--file',str(path.resolve()),
             '--timeout',str(a.problem_timeout),'--tries',str(a.diagram_tries),'--limit',str(limit)]
        try:
            run=subprocess.run(cmd,text=True,capture_output=True,timeout=a.external_timeout,
                               cwd=str(ctx.tmp),env={**os.environ,'NO_COLOR':'1'})
            log_path=ctx.tmp/f'{key}_raw.log'
            log_path.write_text(run.stdout+'\nSTDERR:\n'+run.stderr,encoding='utf8')
            rows.append({'id':key,'name':label,'status':'PARTIAL' if run.returncode==0 else 'FAIL',
               'solved':None,'total':total,'reference':reference,
               'reason':f'Rodou o adaptador AG1 em {limit}/{total} casos; resultado bruto armazenado, '
                        'mas não contabilizado como prova AG2 (falta certificação independente).',
               'raw_log':str(log_path)})
        except subprocess.TimeoutExpired:
            rows.append({'id':key,'name':label,'status':'FAIL','solved':None,'total':total,
                        'reason':'Tempo limite total do benchmark excedido.','reference':reference})
    official=Path(a.official_dir).resolve() if a.official_dir else None
    if official is None or not all((official/f).is_file() for f in ('ddar.py','parse.py','elimination.py','numericals.py','test.py')):
        rows.append({'id':'ddar2_official','name':'Teste diferencial oficial DDAR2','status':'BLOCKED',
                     'reason':'Checkout do DDAR2 oficial não fornecido ou incompleto (--official-dir).',
                     'solved':None,'total':None})
    elif ctx.mode not in ('full','stress'):
        rows.append({'id':'ddar2_official','name':'Teste diferencial oficial DDAR2','status':'NOT_RUN',
                     'reason':'Configuração existente, mas requer --mode full.',
                     'solved':None,'total':None})
    else:
        try:
            p=subprocess.run([sys.executable,'test.py'],cwd=official,capture_output=True,
                text=True,timeout=a.external_timeout)
            rawfile=ctx.tmp/'dd ag2 official raw.log';rawfile.write_text(p.stdout+'\n'+p.stderr,encoding='utf8')
            rows.append({'id':'ddar2_official','name':'Teste de referência DDAR2 oficial',
                         'status':'PARTIAL' if p.returncode==0 else 'FAIL',
                         'reason':'Teste oficial executado; comparar resultados caso a caso ainda exige adaptador e fixtures alinhados.',
                         'solved':None,'total':None,'raw_log':str(rawfile)})
        except (subprocess.TimeoutExpired,OSError) as e:
            rows.append({'id':'ddar2_official','name':'Teste DDAR2 oficial','status':'FAIL',
                         'reason':str(e),'solved':None,'total':None})
    return rows


def derive_capability_evidence(catalog, results):
    byid={x.id:x for x in catalog}
    for t in results:
        for rid in t.related:
            if rid not in byid:continue
            cap=byid[rid]; cap.tests.append(t.id)
            if t.status=='FAIL':
                cap.status='FAIL'
                cap.evidence+=' Teste comportamental FALHOU: '+t.id+'.'
                cap.next_action='Corrigir a falha do teste '+t.id+' e impedir regressão.'
            elif t.status=='PASS' and cap.status not in ('FAIL',):
                # Um teste funcional valida SOMENTE o comportamento testado, não a
                # implementação integral de uma grande capacidade.
                cap.status='VERIFIED_SUBSET'
                cap.evidence+=' Teste específico passou: '+t.id+'. Cobertura completa não demonstrada.'
                cap.next_action='Expandir para toda a semântica, incluir casos adversariais e comparar com referências externas.'
    test_by_id={r.id:r for r in results}
    for cap in catalog:
        required=REQUIREMENT_ACCEPTANCE.get(cap.id,())
        if required and all(t in test_by_id and test_by_id[t].status=='PASS' for t in required):
            cap.status='COMPLETE'
            cap.evidence+=' Todos os testes de aceitação definidos foram executados e passaram: '+', '.join(required)
            cap.next_action='Manter testes diferenciais, adversariais e benchmarks atualizados.'
    return catalog


def classify_phase(catalog,tests):
    data={}
    for phase,name in PHASE_NAMES.items():
        caps=[x for x in catalog if x.phase==phase]
        runs=[x for x in tests if x.phase==phase]
        ccounts={label:sum(x.status==label for x in caps) for label in ('COMPLETE','VERIFIED_SUBSET','PARTIAL','MISSING','FAIL')}
        counts={label:sum(x.status==label for x in runs) for label in ('PASS','FAIL','BLOCKED','NOT_RUN')}
        data[str(phase)]={'name':name,'capabilities':len(caps),
                          'capability_status':ccounts,'test_status':counts,
                          'functional_test_pass_rate':round(counts['PASS']/(counts['PASS']+counts['FAIL']),4)
                          if counts['PASS']+counts['FAIL'] else None,
                          'completion_percent_certified':round(ccounts['COMPLETE']/len(caps)*100,2) if caps else 0.0,
                          'interpretation':('Capacidades certificadas pelos critérios explícitos.' if ccounts['COMPLETE']==len(caps) else 'A fase não foi certificada integralmente; testes de subconjunto não bastam.')}
    return data


def compare_baseline(report,baseline_path):
    if not baseline_path:return None
    old=json.loads(Path(baseline_path).read_text(encoding='utf8'))
    orig={v['id']:v for v in old.get('tests',[])}
    reg=[];fixed=[]
    for test in report['tests']:
        old_test=orig.get(test['id'])
        if not old_test:continue
        if old_test['status']=='PASS' and test['status']=='FAIL':reg.append(test['id'])
        if old_test['status']!='PASS' and test['status']=='PASS':fixed.append(test['id'])
    return {'baseline_path':str(baseline_path),'regressions':reg,'improvements':fixed}


def serialize(catalog,tests,other,measures,source,args,started,finished,extras):
    testsdata=[dataclasses.asdict(v) for v in tests]
    capsdata=[dataclasses.asdict(v) for v in catalog]
    counts={k:sum(x.status==k for x in tests) for k in ('PASS','FAIL','BLOCKED','NOT_RUN')}
    external_by_id={b.get('id'):b for b in other}
    ag2_verified=all(
       external_by_id.get(code,{}).get('status')=='PASS' and
       external_by_id[code].get('solved',-1)>=PUBLISHED_REFERENCE[label]['AG2'] and
       external_by_id[code].get('certified_proofs',-1)>=external_by_id[code].get('solved',0) and
       external_by_id[code].get('protocol')=='AG2-certified-compatible'
       for code,label in (('imo30','IMO-AG-30'),('imo50','IMO-AG-50'),('imosl30','IMOSL-AG-30')))
    report={
      'suite':'GeoForge 7 fases — verificação independente','version':SUITE_VERSION,
      'started_utc':started,'completed_utc':finished,
      'target_file':str(source.resolve()), 'target_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
      'mode':args.mode,'seed':args.seed,'host':{'python':sys.version.split()[0],'platform':sys.platform},
      'summary':{'requirements_total':len(catalog),'requirements_verified_in_full':sum(c.status=='COMPLETE' for c in catalog),
         'requirements_functional_subsets':sum(c.status=='VERIFIED_SUBSET' for c in catalog),
         'requirements_partial_symbols':sum(c.status=='PARTIAL' for c in catalog),
         'requirements_no_evidence':sum(c.status=='MISSING' for c in catalog),
         'requirements_failed':sum(c.status=='FAIL' for c in catalog),
         'tests_executed':counts['PASS']+counts['FAIL'],
         'tests_passed':counts['PASS'],'tests_failed':counts['FAIL'],
         'tests_blocked':counts['BLOCKED'],'tests_not_run':counts['NOT_RUN'],
         'ag2_parity_verified':ag2_verified,
         'seven_phases_complete':ag2_verified and all(c.status=='COMPLETE' for c in catalog) and not any(t.status=='FAIL' for t in tests)},
      'phases':classify_phase(catalog,tests),
      'tests':testsdata,'requirements':capsdata,'external_benchmarks':other,
      'performance':measures,'published_references':PUBLISHED_REFERENCE,
      'official_urls':OFFICIAL_REFS,
      'caveats':[
          'Ausência de símbolo é indício, não prova absoluta de ausência de funcionalidade.',
          'Presença de classe/rotina não certifica comportamento nem equivalência ao AG2.',
          'Passagem dos testes sintéticos não certifica desempenho em IMO, IMOSL ou JGEX.',
          'O repositório público do AG2 publica o núcleo DDAR, não todos os pesos e a busca neural.',
          'Completar 450 itens de engenharia não garante 100% de problemas matemáticos inéditos.'
      ],
      'runtime_metrics':{k:v for k,v in extras.items() if isinstance(v,(int,float,str,list,dict)) and k not in ('catalog', 'dataset_manifest','dataset_path')}
    }
    return report


def generate_markdown(r):
    s=r['summary']; ph=r['phases']
    lines=[f'# Auditoria das 7 fases do GeoForge', '',
      f'**Arquivo:** `{r["target_file"]}`',
      f'**SHA-256:** `{r["target_sha256"]}`',
      f'**Data UTC:** {r["completed_utc"]} · **Modo:** {r["mode"]}', '',
      '## Resultado verificável', '',
      f'- Testes funcionais: **{s["tests_passed"]} passaram / {s["tests_executed"]} executados**.',
      f'- Falhas funcionais: **{s["tests_failed"]}**.',
      f'- Testes não executados por modo/dependência: **{s["tests_not_run"] + s["tests_blocked"]}**.',
      f'- Inventário de marcos: **{s["requirements_total"]}**.',
      f'- Com comportamento testado apenas parcialmente: **{s["requirements_functional_subsets"]}**.',
      f'- Com símbolo identificado sem comprovação integral: **{s["requirements_partial_symbols"]}**.',
      f'- Sem evidência estática encontrada: **{s["requirements_no_evidence"]}**.',
      f'- Marcos com testes falhando: **{s["requirements_failed"]}**.',
      f'- Paridade AG2 comprovada: **{"SIM" if s["ag2_parity_verified"] else "NÃO"}**. Todas as fases concluídas: **{"SIM" if s["seven_phases_complete"] else "NÃO"}**.', '',
      '### Progresso por fase (não é porcentagem de conclusão)', '',
      '| Fase | Nome | Testes passaram | Falharam | Marcos com evidência funcional | Só símbolo | Sem evidência |',
      '|---:|---|---:|---:|---:|---:|---:|']
    for k,v in ph.items():
        c=v['capability_status'];t=v['test_status']
        lines.append(f'| {k} | {v["name"]} | {t["PASS"]} | {t["FAIL"]} | {c["VERIFIED_SUBSET"]} | {c["PARTIAL"]} | {c["MISSING"]} |')
    lines.extend(['', '## Tarefas de maior prioridade', '',
       'Estas lacunas vêm de testes executados, ausências de evidência ou benchmarks não fornecidos.'])
    failed=[t for t in r['tests'] if t['status']=='FAIL']
    for t in failed:
        lines.append(f'- **Falha {t["id"]}:** {t["description"]}. `{t["details"].splitlines()[0][:300]}`')
    if not failed:lines.append('- Nenhum teste executado apresentou falha funcional neste modo.')
    for phase in range(1,8):
        caps=[c for c in r['requirements'] if c['phase']==phase and c['status']=='MISSING']
        for cap in caps[:8]:
            lines.append(f'- **Fase {phase}, #{cap["id"]:03d} {cap["name"]}:** {cap["next_action"]}')
        if len(caps)>8: lines.append(f'- Fase {phase}: outras **{len(caps)-8}** capacidades sem evidência estão no CSV.')
    lines.extend(['', '## Benchmarks externos', '',
                  '| Benchmark | Resultado | Evidência ausente / observação |',
                  '|---|---|---|'])
    for b in r['external_benchmarks']:
        lines.append(f'| {b["name"]} | **{b["status"]}** | {str(b.get("reason", "")).replace("|","/")} |')
    lines.extend(['', '## Microbenchmarks locais (NÃO olímpicos)', '',
                  '| Operação | Amostras | Mediana (ms) | P95 (ms) | Ops/s |',
                  '|---|---:|---:|---:|---:|'])
    for name,v in r['performance'].items():
        lines.append(f'| {name} | {v["samples"]} | {v["median_ms"]} | {v["p95_ms"]} | {v["ops_per_sec"]} |')
    lines.extend(['', '## Falhas e testes não realizados', ''])
    for t in r['tests']:
        if t['status']!='PASS':
            lines.append(f'- [{t["status"]}] {t["id"]}: {t["description"]}. {t["details"].splitlines()[0] if t["details"] else ""}')
    lines.extend(['', '## Referências externas', ''])
    lines.extend(f'- [{k}]({v})' for k,v in r['official_urls'].items())
    lines.extend(['', '## Interpretação obrigatória', ''])
    lines.extend('- '+c for c in r['caveats'])
    lines.extend(['', '## Inventário COMPLETO de 450 requisitos (por fase)', ''])
    for phase in range(1,8):
        lines.append(f'### Fase {phase}: {PHASE_NAMES[phase]}')
        lines.append('')
        lines.append('| ID | Requisito | Estado | Próxima ação |')
        lines.append('|---:|---|---|---|')
        for cap in r['requirements']:
            if cap['phase']!=phase:continue
            next_action=cap['next_action'].replace('|','/')
            lines.append(f'| {cap["id"]:03d} | {cap["name"].replace("|","/")} | {cap["status"]} | {next_action} |')
        lines.append('')
    return '\n'.join(lines)+'\n'


def generate_html(report):
    markdown=generate_markdown(report)
    # HTML without third-party dependencies, details have safe escaping.
    badges={'PASS':'#146c43','FAIL':'#ae2424','PARTIAL':'#855d12',
           'VERIFIED_SUBSET':'#1b6d83','MISSING':'#755e5e','BLOCKED':'#786b2e','NOT_RUN':'#5d6675'}
    table_rows=[]
    for p in report['requirements']:
        col=badges.get(p['status'],'#555')
        table_rows.append('<tr data-phase="{}" data-status="{}"><td>{:03d}</td><td>{}</td>'
                          '<td><span style="color:{};font-weight:600">{}</span></td><td>{}</td><td>{}</td></tr>'.format(
              p['phase'],html.escape(p['status']),p['id'],html.escape(p['name']),col,
              html.escape(p['status']),html.escape(p['evidence']),html.escape(p['next_action'])))
    tests='\n'.join('<tr><td>{}</td><td>F{}</td><td>{}</td><td>{}</td><td>{:.3f}s</td></tr>'.format(
              html.escape(t['id']),t['phase'],html.escape(t['description']),html.escape(t['status']),t['elapsed_seconds'])
                    for t in report['tests'])
    return f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>GeoForge · Auditoria 7 fases</title><style>
:root{{color-scheme:light dark}}body{{font:14px/1.6 system-ui,Arial,sans-serif;max-width:1500px;margin:32px auto;padding:0 22px}}
h1{{font-size:26px}}h2{{margin-top:40px}}table{{border-collapse:collapse;width:100%;font-size:12px}}
th,td{{padding:8px 12px;text-align:left;border-bottom:1px solid #9995;vertical-align:top}}th{{position:sticky;top:0;background:Canvas}}
nav{{display:flex;gap:12px;align-items:center;flex-wrap:wrap;padding:12px;background:Canvas;position:sticky;top:0}}
input,select{{padding:8px;min-height:32px}}.numbers{{display:grid;grid-template-columns:repeat(auto-fit,minmax(145px,1fr));gap:12px}}
.number{{padding:15px;border:1px solid #8886;border-radius:10px}}.value{{font-size:26px;font-weight:700}}
small{{opacity:.65}}tr:hover{{background:#8881}}code{{overflow-wrap:anywhere}}
</style></head><body>
<h1>GeoForge · Auditoria das 7 fases</h1>
<p><strong>Arquivo:</strong> {html.escape(report['target_file'])}<br><strong>SHA-256:</strong> <code>{report['target_sha256']}</code><br>
<strong>Modo:</strong> {report['mode']} · <strong>Data:</strong> {report['completed_utc']}</p>
<div class="numbers">
<div class="number"><small>Testes passaram</small><div class="value">{report['summary']['tests_passed']}</div></div>
<div class="number"><small>Testes falharam</small><div class="value">{report['summary']['tests_failed']}</div></div>
<div class="number"><small>Marcos rastreados</small><div class="value">450</div></div>
<div class="number"><small>Paridade AlphaGeometry 2</small><div class="value">{'SIM' if report['summary']['ag2_parity_verified'] else 'NÃO'}</div></div></div>
<h2>Inventário de capacidades e o que falta</h2>
<nav><label>Filtrar <input id="q" placeholder="Buscar nome / ID / lacuna" oninput="filter()"></label>
<label>Fase <select id="phase" onchange="filter()"><option value="all">Todas</option>{''.join(f'<option value="{i}">Fase {i}</option>' for i in range(1,8))}</select></label>
<label>Estado <select id="status" onchange="filter()"><option value="all">Todos</option>{''.join(f'<option>{x}</option>' for x in ('MISSING','PARTIAL','VERIFIED_SUBSET','COMPLETE','FAIL'))}</select></label></nav>
<table id="catalog"><thead><tr><th>ID</th><th>Capacidade</th><th>Estado</th><th>Evidência</th><th>Próxima implementação</th></tr></thead><tbody>{''.join(table_rows)}</tbody></table>
<h2>Testes funcionais</h2><table><thead><tr><th>ID</th><th>Fase</th><th>Descrição</th><th>Status</th><th>Tempo</th></tr></thead><tbody>{tests}</tbody></table>
<p><strong>Aviso:</strong> presença de função não é prova de equivalência funcional. Um teste local não garante 30/30 na IMO.</p>
<script>function filter(){{let q=document.getElementById('q').value.toLowerCase(),p=document.getElementById('phase').value,s=document.getElementById('status').value;for(let tr of document.querySelectorAll('#catalog tbody tr'))tr.hidden=!((p==='all'||tr.dataset.phase===p)&&(s==='all'||tr.dataset.status===s)&&tr.innerText.toLowerCase().includes(q));}}</script>
</body></html>'''


def export_junit(tests,path):
    root=ET.Element('testsuite',{'name':'geoforge-seven-phases',
                     'tests':str(len(tests)),'failures':str(sum(t.status=='FAIL' for t in tests)),
                     'skipped':str(sum(t.status in ('NOT_RUN','BLOCKED') for t in tests)),
                     'time':str(round(sum(t.elapsed_seconds for t in tests),3))})
    for t in tests:
        case_node=ET.SubElement(root,'testcase',{'name':t.id+' '+t.description,
                  'classname':f'geoforge.phase{t.phase}.{t.group}',
                  'time':str(t.elapsed_seconds)})
        if t.status=='FAIL':ET.SubElement(case_node,'failure',{'message':t.details[:200]}).text=t.details
        elif t.status in ('NOT_RUN','BLOCKED'):ET.SubElement(case_node,'skipped',{'message':t.details[:200]})
    ET.ElementTree(root).write(path,encoding='utf-8',xml_declaration=True)


def export_reports(report,out_path,results):
    out_path.mkdir(parents=True,exist_ok=True)
    (out_path/'relatorio_7fases.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
    (out_path/'O_QUE_FALTA_7FASES.md').write_text(generate_markdown(report),encoding='utf8')
    (out_path/'painel_7fases.html').write_text(generate_html(report),encoding='utf8')
    with (out_path/'requisitos_450.csv').open('w',encoding='utf-8-sig',newline='') as f:
        keys=['id','phase','name','status','evidence','next_action','symbols','tests']
        wr=csv.DictWriter(f,fieldnames=keys);wr.writeheader()
        for entry in report['requirements']:
            w={**entry,'symbols':', '.join(entry['symbols']),'tests':', '.join(entry['tests'])}; wr.writerow(w)
    with (out_path/'testes_executados.csv').open('w',encoding='utf-8-sig',newline='') as f:
        keys=['id','phase','group','description','status','elapsed_seconds','details','related']
        wr=csv.DictWriter(f,fieldnames=keys);wr.writeheader()
        for x in report['tests']:
            wr.writerow({**x,'related':','.join(map(str,x['related']))})
    export_junit(results,out_path/'junit_7fases.xml')


def parse_args(argv=None):
    ap=argparse.ArgumentParser(description='Benchmark permanente dos 450 requisitos e 7 fases GeoForge')
    ap.add_argument('--geoforge',type=Path,default=Path(__file__).with_name('geoforge.py'))
    ap.add_argument('--out',type=Path,default=Path(__file__).with_name('auditoria_geoforge_7fases'))
    ap.add_argument('--mode',choices=tuple(LEVELS),default='standard')
    ap.add_argument('--seed',type=int,default=20261016)
    ap.add_argument('--gate',action='store_true',help='status != 0 se algum teste executado falhar')
    ap.add_argument('--require-100',action='store_true',help='requer validação INTEGRAL (incluindo benchmarks externos); deve falhar no estado atual')
    ap.add_argument('--baseline',type=Path,help='JSON anterior: identifica regressões (PASS -> outro status)')
    ap.add_argument('--fail-on-regression',action='store_true')
    ap.add_argument('--no-microbench',action='store_true')
    ap.add_argument('--imo30',type=Path,help='arquivo de benchmark IMO_AG_30 em formato AG1')
    ap.add_argument('--imo50',type=Path,help='arquivo de problemas IMO_AG_50 formalizados')
    ap.add_argument('--imosl30',type=Path,help='arquivo de problemas IMOSL_AG_30 formalizados')
    ap.add_argument('--jgex231',type=Path,help='arquivo JGEX_AG_231 em formato AG1')
    ap.add_argument('--official-dir',type=Path,help='checkout público DDAR2 da Google DeepMind')
    ap.add_argument('--max-external-problems',type=int,default=4)
    ap.add_argument('--diagram-tries',type=int,default=2)
    ap.add_argument('--problem-timeout',type=float,default=2)
    ap.add_argument('--external-timeout',type=float,default=90)
    ap.add_argument('--list-cases',action='store_true')
    return ap.parse_args(argv)


def main(argv=None):
    a=parse_args(argv)
    if a.list_cases:
        for t in CASES:print(f'{t.id:8} F{t.phase} [{t.level:8}] {t.description}')
        print('Casos: ',len(CASES),'| Requisitos rastreados: 450')
        return 0
    start=datetime.now(timezone.utc).isoformat()
    source=a.geoforge.expanduser().resolve()
    if not source.is_file():
        print('Arquivo GeoForge não encontrado: '+str(source),file=sys.stderr);return 2
    a.out.mkdir(parents=True,exist_ok=True)
    catalog=make_catalog(extract_symbols(source))
    # Workdir temporário removido após exportar os relatórios e métricas.
    with tempfile.TemporaryDirectory(prefix='geoforge_7ph_') as temporary:
        tmp=Path(temporary)
        try:m=load_geoforge(source)
        except Exception as e:
            print(f'Falha ao importar o GeoForge: {e}',file=sys.stderr)
            (a.out/'FALHA_IMPORTACAO.txt').write_text(traceback.format_exc(),encoding='utf8')
            return 2
        ctx=Context(m,source,tmp,a.mode,a.seed,a,
             {'catalog':catalog,'published_reference':PUBLISHED_REFERENCE})
        tests=[]
        levels=LEVELS[a.mode]
        print(f'GeoForge 7 fases | {source.name} | modo {a.mode} | casos {len(CASES)} | requisitos 450',flush=True)
        for test in CASES:
            if test.level not in levels:
                tests.append(CaseResult(test.id,test.phase,test.group,test.description,'NOT_RUN',0.,
                            f'Exige nível {test.level}; execução selecionada: {a.mode}.',test.related))
                continue
            result=execute_case(test,ctx);tests.append(result)
            print(f'  [{result.status:8}] {result.id} (F{result.phase}) {result.elapsed_seconds:.3f}s {result.description}',flush=True)
            if result.status=='FAIL':print('             '+result.details.splitlines()[0][:240],flush=True)
        catalog=derive_capability_evidence(catalog,tests)
        try:benchmarks=optional_benchmarks(ctx)
        except Exception as ex:
            benchmarks=[{'id':'external_suite','name':'Benchmarks externos','status':'FAIL',
              'reason':str(ex),'total':None,'solved':None}]
        performance={}
        if not a.no_microbench:
            try:performance=benchmark_micro(ctx,10 if a.mode=='quick' else 35)
            except Exception as ex:
                performance={'microbench_error':{'samples':0,'median_ms':0.,'p95_ms':0.,'ops_per_sec':0.,'reason':str(ex)}}
        finish=datetime.now(timezone.utc).isoformat()
        report=serialize(catalog,tests,benchmarks,performance,source,a,start,finish,ctx.extras)
        report['baseline_comparison']=compare_baseline(report,a.baseline)
        export_reports(report,a.out,tests)
    summary=report['summary']
    print('\nRESUMO: ',summary['tests_passed'],'/',summary['tests_executed'],'testes passaram;',
          summary['tests_failed'],'falhas |',summary['requirements_no_evidence'],
          'itens sem evidência | completude AG2: NÃO',flush=True)
    for filename in ('O_QUE_FALTA_7FASES.md','painel_7fases.html','requisitos_450.csv','relatorio_7fases.json','junit_7fases.xml'):
        print('  '+str(a.out/filename))
    has_regressions=bool(report['baseline_comparison'] and report['baseline_comparison']['regressions'])
    if a.require_100 and not report['summary']['seven_phases_complete']:return 3
    if a.gate and summary['tests_failed']:return 1
    if a.fail_on_regression and has_regressions:return 4
    return 0

if __name__=='__main__':
    raise SystemExit(main())
