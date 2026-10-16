"""Check typed formalizations; semantic equivalence to prose is not automated."""
from dataclasses import dataclass
from geoforge_core.type_system import check_problem
@dataclass(frozen=True)
class FormalizationReview:
    syntax_ok:bool
    semantic_equivalence_confirmed:bool
    concerns:tuple[str,...]=()

def review(problem):
    try:check_problem(problem)
    except ValueError as exc:return FormalizationReview(False,False,(str(exc),))
    return FormalizationReview(True,False,("Human or independent semantic review required",))
