"""Diagram constraint construction: numerical candidates, NOT formal proofs."""
from dataclasses import dataclass
import numpy as np

@dataclass(frozen=True)
class DiagramResult:
    status: str
    coordinates: tuple = ()
    maximum_residual: float = float("inf")

def fit_diagram(initial, equations, *, max_nfev=2000, tolerance=1e-8):
    from scipy.optimize import least_squares
    x = np.asarray(initial, dtype=float).reshape(-1)
    def residual(v):
        return np.asarray([fn(v) for fn in equations], dtype=float).reshape(-1)
    if not len(equations):
        return DiagramResult("candidate", tuple(float(k) for k in x), 0.0)
    result = least_squares(residual, x, max_nfev=max_nfev)
    values = residual(result.x)
    error = float(np.max(np.abs(values))) if values.size else 0.
    return DiagramResult("candidate" if error<=tolerance else "unresolved",
                         tuple(float(k) for k in result.x), error)
