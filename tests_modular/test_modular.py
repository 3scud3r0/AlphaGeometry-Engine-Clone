"""Regression tests for the new modules; not a DDAR2 parity benchmark."""
from fractions import Fraction
import json
import pytest
from geoforge_core.ast import Predicate,Expr
from geoforge_core.parser_ag2 import parse_predicate,parse_problem
from geoforge_core.geometry_graph import GeometryGraph
from geoforge_core.point_unification import PointEquivalence
from geoforge_core.degeneracy import noncollinear,require_nondegenerate_triangle
from geoforge_core.nonconstructive import solve_polynomials
from geoforge_core.loci import movement_closure
from geoforge_prover.sparse_exact import RationalLinearSystem
from geoforge_prover.angle_ar import AngleCongruenceSystem
from geoforge_prover.length_ar import AdditiveLengthAR
from geoforge_prover.loglength_ar import LogLengthAR
from geoforge_prover.proof_kernel import Proof,ProofStep,ProofKernel
from geoforge_prover.certificates import dump,load,verify_json
from geoforge_search.skest import VerifiedWorkspace
from geoforge_search.scheduler import Budget,BudgetExpired
from geoforge_data.dependency_difference import ancestors
from geoforge_data.quality_gate import CertificateQualityGate
from geoforge_benchmarks.report import Result,summarize
from geoforge_modular_cli import solve

def pred(text):return parse_predicate(text)
def example():
    given=("midp d a b","midp e a c","ncoll a b c")
    goal="para d e b c"
    return solve(given,goal)

def test_exact_ast_and_serialization():
    p=pred("aconst a b c 1/2")
    assert p.constants==(Fraction(1,2),)
    assert Expr((("x",Fraction(2)),("x",Fraction(-1))),Fraction(1)).coefficients==(("x",Fraction(1)),)

def test_problem_parser_and_type_errors():
    p=parse_problem("midp d a b ; midp e a c ; ncoll a b c ? para d e b c")
    assert len(p.premises)==3
    with pytest.raises(ValueError):
        parse_problem("midp d a b ? foo a")

def test_geometric_graph_and_no_arbitrary_inference():
    graph=GeometryGraph([pred("midp d a b")])
    assert graph.contains(pred("midp d b a"))
    with pytest.raises(ValueError):graph.add(pred("para d e b c"))

def test_point_equivalence_requires_justification():
    u=PointEquivalence()
    with pytest.raises(ValueError):u.merge("a","b")
    u.merge("a","b",justified=True)
    assert u.same("a","b")

def test_non_degeneracy_guards():
    assert noncollinear((0,0),(1,0),(0,1))
    with pytest.raises(ValueError):
        require_nondegenerate_triangle((0,0),(1,0),(2,0))

def test_sparse_witness_correct():
    s=RationalLinearSystem()
    s.add("p",{"x":1,"y":-1})
    s.add("q",{"y":1,"z":-1})
    w=s.entail({"x":1,"z":-1})
    assert w is not None
    assert s.verify_witness(s.original,{"x":1,"z":-1},w)
    assert s.entail({"x":1}) is None

def test_safe_angle_pivot():
    s=AngleCongruenceSystem()
    assert s.add({"theta":1})
    assert s.entails_zero_mod_pi({"theta":1})
    unsafe=AngleCongruenceSystem()
    assert unsafe.add({"theta":2}) is False
    assert not unsafe.entails_zero_mod_pi({"theta":1})

def test_lengths_require_nonzero_guard():
    ar=LogLengthAR()
    with pytest.raises(ValueError):ar.add_equal("x","a","b","c","d")
    for segment in (("a","b"),("c","d")):ar.allow_segment(*segment)
    ar.add_equal("x","a","b","c","d")
    assert ar.equal("a","b","c","d") is not None
    add=AdditiveLengthAR()
    add.add("one",[(("a","b"),1)],3)
    assert add.entails([(("a","b"),1)],3) is not None

def test_midline_derived_and_certified():
    p=example()
    assert p is not None
    assert ProofKernel().check(p)
    assert verify_json(dump(p))

def test_corrupt_proof_rejected():
    p=example()
    obj=json.loads(dump(p))
    obj["steps"][0]["conclusion"]="perp d e b c"
    assert not verify_json(json.dumps(obj))
    assert not CertificateQualityGate().validate("perp d e b c",dump(p))

def test_false_proof_no_rules():
    p=Proof((pred("ncoll a b c"),),pred("para d e b c"),
            (ProofStep(pred("para d e b c"),"midline",(pred("ncoll a b c"),)),))
    assert not ProofKernel().check(p)

def test_verified_workspace_not_leaking():
    p=example()
    ws=VerifiedWorkspace()
    assert ws.publish(p)
    assert ws.available(p.goal,p.premises)
    assert not ws.available(p.goal,())

def test_bounded_budget_and_movement():
    b=Budget(seconds=2,expansions=1)
    b.consume()
    with pytest.raises(BudgetExpired):b.consume()
    out=movement_closure({"b":("a",),"c":("b",),"d":("e",)},{"a"})
    assert {"a","b","c"}<=out.moving
    assert "d" in out.fixed

def test_dependency_difference_never_claims_necessity():
    assert ancestors({"c":("a","b"),"d":("c",)},["d"])==frozenset({"a","b","c","d"})

def test_external_benchmark_not_fake():
    result=summarize([Result("i","proved",1.0,True),Result("j","proved",2.0,False)])
    assert result["certified_solved"]==1
    assert result["unverified_proof_claims"]==1
