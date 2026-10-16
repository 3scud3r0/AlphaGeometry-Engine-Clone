"""Independent regression tests for the model-free certified prover."""
from __future__ import annotations
from pathlib import Path
from fractions import Fraction as Q
import copy
import json
import pytest
from geoforge_upgrade_suite.geometry_exact import Polynomial
from geoforge_upgrade_suite.deterministic_ideal import (ExactIdealEngine,IdealBudget,
    certificate_to_json,verify_certificate_json,polynomial_to_object)
from geoforge_upgrade_suite.deterministic_solver import (ExactFactEvaluator,GuardLedger,
    DeterministicGeometrySolver,DeterministicBudget,IndependentResultChecker,
    exact_counterexample)
from geoforge_upgrade_suite.exact_constructions import (SPoint,ConstructionStep,
    ExactConstructionExecutor,verify_construction_trace,foot,orthocenter,
    circumcenter,circle_line_intersection,circle_circle_intersection,
    ConstructionUnavailable)
from geoforge_upgrade_suite.saturation_solver import (SaturatedGeometryProver,
    SaturationCertificateChecker,nonzero_guard_expression)
from geoforge_upgrade_suite.symbolic_coordinates import CoordinatePredicateCompiler

HERE=Path(__file__).resolve().parents[2]


def test_ideal_witness_two_generators():
    x=Polynomial.variable(2,0);y=Polynomial.variable(2,1)
    facts=(x-y,y-1)
    result=ExactIdealEngine().membership(facts,x-1)
    assert result.status=='proved'
    assert result.certificate.verify()
    assert verify_certificate_json(certificate_to_json(result.certificate))


def test_ideal_witness_groebner_spair():
    x=Polynomial.variable(2,0);y=Polynomial.variable(2,1)
    result=ExactIdealEngine().membership((x*y-1,y-x),x*x-1)
    assert result.status=='proved'
    assert result.explored_pairs>0
    assert result.certificate.verify()


def test_unprovable_polynomial_refuses_certificate():
    x=Polynomial.variable(2,0)
    result=ExactIdealEngine().membership((x-1,),x-2)
    assert result.status=='unknown'
    assert result.certificate is None


def test_zero_polynomial_is_proved():
    x=Polynomial.variable(2,0)
    result=ExactIdealEngine().membership((x-1,),x-x)
    assert result.status=='proved'
    assert result.certificate.verify()


def test_ideal_tampering_fails():
    x=Polynomial.variable(2,0);axiom=x-3
    r=ExactIdealEngine().membership((axiom,),x*x-9)
    raw=json.loads(certificate_to_json(r.certificate))
    raw['multipliers'][0]['terms'].append([[0,0],'1'])
    assert not verify_certificate_json(json.dumps(raw))


def test_exhausted_budget_does_not_prove():
    x=Polynomial.variable(2,0);y=Polynomial.variable(2,1)
    eng=ExactIdealEngine(IdealBudget(max_pairs=1,seconds=1))
    result=eng.membership((x*y-1,y-x),x*x-1)
    assert result.status in ('resource_exhausted','proved')
    if result.status=='proved':assert result.certificate.verify()


def test_guard_noncollinear_implies_pairwise_distinct():
    ledger=GuardLedger(('ncoll a b c',))
    for a,b in (('a','b'),('a','c'),('b','c')):
        assert ledger.entails('distinct '+a+' '+b)
    assert not ledger.entails('distinct x y')


def test_guard_midpoints_share_vertex():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c'))
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert not ledger.contradictions


def test_guard_detects_trivial_contradiction():
    ledger=GuardLedger(('overlap a b','distinct a b'))
    assert ledger.contradictions


def test_coordinate_exact_predicates():
    e=ExactFactEvaluator({'a':(0,0),'b':(3,0),'c':(0,4),'d':(3,4),'m':('3/2',0)})
    assert e.check('ncoll a b c')
    assert e.check('midp m a b')
    assert e.check('perp a b a c')
    assert e.check('para a b c d')
    assert e.check('cong a b c d')
    assert not e.check('perp a b c d')


def test_rational_exact_counterexample():
    hs=['para a b c d']
    example=exact_counterexample(hs,'perp a b c d',attempts=300)
    assert example is not None
    evaluator=ExactFactEvaluator(example['coordinates'])
    assert evaluator.all_hold(hs)
    assert not evaluator.check('perp a b c d')


def test_solver_midline_proof_is_replayed():
    s=DeterministicGeometrySolver(DeterministicBudget(seconds=2),source_path=HERE/'geoforge.py')
    out=s.prove(['midp d a b','midp e a c','ncoll a b c'],'para d e b c')
    assert out.status=='proved'
    assert IndependentResultChecker(HERE/'geoforge.py').verify(out)


def test_solver_refuted_claim_is_replayed():
    s=DeterministicGeometrySolver(DeterministicBudget(seconds=2),source_path=HERE/'geoforge.py')
    out=s.prove(['para a b c d'],'perp a b c d')
    assert out.status=='counterexample'
    assert IndependentResultChecker(HERE/'geoforge.py').verify(out)


def test_solver_rejects_tampered_goal():
    s=DeterministicGeometrySolver(DeterministicBudget(seconds=2),source_path=HERE/'geoforge.py')
    out=s.prove(['midp d a b','midp e a c','ncoll a b c'],'para d e b c')
    altered=out.to_dict();altered['goal']='perp d e b c'
    assert not IndependentResultChecker(HERE/'geoforge.py').verify(altered)


def test_solver_refuses_contradictory_premises():
    out=DeterministicGeometrySolver().prove(['overlap a b','distinct a b'],'cong a b a b')
    assert out.status=='invalid_problem'
    assert not IndependentResultChecker().verify(out)


def test_circle_line_radical_result():
    p=circle_line_intersection(SPoint(0,0),9,SPoint(-5,0),SPoint(5,0))
    assert len(p)==2
    assert {str(q.x) for q in p}=={'-3','3'}


def test_circle_circle_radical_axis():
    p=circle_circle_intersection(SPoint(0,0),5,SPoint(2,0),5)
    assert len(p)==2
    assert all(q.x==1 for q in p)
    assert {str(q.y) for q in p}=={'-2','2'}


def test_orthocenter_and_circumcenter_exact():
    a,b,c=SPoint(0,0),SPoint(4,0),SPoint(0,4)
    assert orthocenter(a,b,c).eq(a)
    assert circumcenter(a,b,c).eq(SPoint(2,2))


def test_undefined_circle_construction_fails():
    assert circle_circle_intersection(SPoint(0,0),1,SPoint(6,0),1)==()


def test_construction_trace_replay():
    initial={'a':(0,0),'b':(4,0),'c':(0,4)}
    steps=[ConstructionStep('m','midpoint',('a','b')),
           ConstructionStep('h','orthocenter',('a','b','c')),
           ConstructionStep('o','circumcenter',('a','b','c'))]
    trace=ExactConstructionExecutor(initial).execute(steps)
    assert verify_construction_trace(initial,steps,trace)
    assert trace.points['o'].eq(SPoint(2,2))


def test_fake_trace_is_rejected():
    initial={'a':(0,0),'b':(4,0)}
    steps=[ConstructionStep('m','midpoint',('a','b'))]
    trace=ExactConstructionExecutor(initial).execute(steps)
    trace.points['m']=SPoint(999,999)
    assert not verify_construction_trace(initial,steps,trace)


def test_saturation_checker_rejects_unjustified_guard():
    c=CoordinatePredicateCompiler(('a','b'))
    assert nonzero_guard_expression(c,'distinct a b')
    with pytest.raises(Exception):
        nonzero_guard_expression(c,'nonsense a b')


def test_identity_certificate_binds_source_axioms():
    s=DeterministicGeometrySolver(DeterministicBudget(seconds=3),source_path=None)
    out=s.prove(['midp m a b'],'cong m a m b')
    assert out.status=='proved'
    assert out.method=='polynomial_certificate'
    assert IndependentResultChecker().verify(out)
    falsified=out.to_dict();falsified['hypotheses']=['midp m a c']
    assert not IndependentResultChecker().verify(falsified)


def test_cyclic_rejects_repeated_points():
    e=ExactFactEvaluator({'a':(0,0),'b':(1,0),'c':(0,1),'d':(0,1)})
    assert not e.check('cyclic a b c d')


def test_fast_affine_tactic_witness():
    from geoforge_upgrade_suite.affine_certificate import AffineIdealTactic
    x=Polynomial.variable(2,0);y=Polynomial.variable(2,1)
    out=AffineIdealTactic().prove((x-y,y-2),x*x-4)
    assert out.status=='proved'
    assert out.certificate.verify()


def test_affine_tactic_ignores_nonlinear_sources():
    from geoforge_upgrade_suite.affine_certificate import AffineIdealTactic
    x=Polynomial.variable(2,0);y=Polynomial.variable(2,1)
    out=AffineIdealTactic().prove((x*x-1,y-2),x*x-1)
    assert out.status=='unknown'


def test_affine_tactic_never_certifies_inconsistent_linear_constraints():
    from geoforge_upgrade_suite.affine_certificate import AffineIdealTactic
    x=Polynomial.variable(2,0)
    out=AffineIdealTactic().prove((x-1,x-2),x*x-1)
    assert out.status=='inconsistent_linear_equations'
    assert out.certificate is None
