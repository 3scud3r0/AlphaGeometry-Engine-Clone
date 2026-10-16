"""Delegate polynomial proof search to existing exact solver; no unsound promotion."""
from geoforge_upgrade_suite.symbolic_coordinates import AlgebraicCoordinateProver, CoordinatePredicateCompiler
from geoforge_upgrade_suite.deterministic_solver import DeterministicGeometrySolver
__all__=["AlgebraicCoordinateProver","CoordinatePredicateCompiler","DeterministicGeometrySolver"]
