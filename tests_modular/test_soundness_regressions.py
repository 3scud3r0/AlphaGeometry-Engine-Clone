"""Adversarial soundness regressions for the modular and exact GeoForge paths.

Each case exercises a previously unsafe inference or a malformed declaration.
These are correctness tests, not IMO/AG2 solved-problem benchmarks.
"""
from fractions import Fraction
from itertools import permutations

import pytest

from geoforge_core.ast import Predicate
from geoforge_core.canonical import canonical
from geoforge_core.type_system import GeometryTypeError
from geoforge_modular_cli import solve
from geoforge_prover.proof_kernel import Proof, ProofKernel
from geoforge_prover.rule_compiler import match
from geoforge_upgrade_suite.deterministic_solver import (
    DeterministicBudget,
    DeterministicGeometrySolver,
    ExactFactEvaluator,
    GuardLedger,
    IndependentResultChecker,
)
from geoforge_upgrade_suite.symbolic_coordinates import CoordinatePredicateCompiler


def test_collinearity_is_invariant_under_point_order_and_repetition():
    ev = ExactFactEvaluator({"a": (0, 0), "b": (1, 0)})
    forms = set(permutations(("a", "a", "b")))
    assert all(ev.check("coll " + " ".join(args)) for args in forms)
    assert len({canonical(Predicate("coll", args)) for args in forms}) == 1
    assert not GuardLedger(("coll a a b",)).entails("distinct a b")


def test_cyclic_goal_requires_distinct_points_in_addition_to_equation():
    comp = CoordinatePredicateCompiler(("a", "b", "c", "d"))
    equation = comp.compile("cyclic", ("a", "b", "c", "d"))
    assert "ncoll a b c" in equation.nondegeneracy
    assert {
        "distinct a b",
        "distinct a c",
        "distinct a d",
        "distinct b c",
        "distinct b d",
        "distinct c d",
    }.issubset(set(equation.nondegeneracy))


def test_overlapping_fourth_point_cannot_be_proved_cyclic():
    hypotheses = ("ncoll a b c", "overlap d a")
    coordinates = {"a": (0, 0), "b": (1, 0), "c": (0, 1), "d": (0, 0)}
    solver = DeterministicGeometrySolver(
        DeterministicBudget(seconds=2.0, max_pairs=24, max_basis=36, max_terms=900)
    )
    outcome = solver.prove(hypotheses, "cyclic a b c d", provided_coordinates=coordinates)
    assert outcome.status == "counterexample"
    assert IndependentResultChecker().verify(outcome)
    assert not ExactFactEvaluator(coordinates).check("cyclic a b c d")


@pytest.mark.parametrize(
    "premise",
    (
        "cyclic a a b c",
        "para a a b c",
        "perp a b c c",
        "distinct a a",
        "eqratio a a b c d e f g",
    ),
)
def test_self_contradictory_nondegeneracy_rejected(premise):
    solver = DeterministicGeometrySolver(DeterministicBudget(seconds=1))
    result = solver.prove((premise,), "cong a b a b")
    assert result.status == "invalid_problem"


def test_valid_midline_proof_remains_accepted():
    givens = ("midp d a b", "midp e a c", "ncoll a b c")
    cert = solve(givens, "para d e b c")
    assert cert is not None
    assert ProofKernel().check(cert)


def test_rule_matching_cannot_drop_numeric_constants():
    schematic = Predicate("para", ("a", "b", "c", "d"))
    malformed = Predicate("para", ("a", "b", "c", "d"), (Fraction(1),))
    assert match(schematic, malformed, {}) is None


def test_modular_cli_rejects_extra_numeric_arguments():
    with pytest.raises(GeometryTypeError):
        solve(("para a b c d 1",), "para a b c d")


def test_independent_kernel_rejects_malformed_assumption_certificate():
    bad = Predicate("cong", ("a", "b", "c", "d"), (Fraction(5),))
    assert not ProofKernel().check(Proof((bad,), bad, ()))
