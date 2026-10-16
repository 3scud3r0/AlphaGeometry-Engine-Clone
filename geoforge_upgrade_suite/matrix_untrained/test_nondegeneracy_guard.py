# GENERATED, DETERMINISTIC, NO TRAINED MODEL USED.
# Source generator: geoforge_upgrade_suite/generate_untrained_matrix.py
from fractions import Fraction as Q
from geoforge_upgrade_suite.geometry_exact import Vec2,Polynomial,Line
from geoforge_upgrade_suite.exact_constructions import SPoint,foot,line_intersection
from geoforge_upgrade_suite.deterministic_ideal import ExactIdealEngine,certificate_to_json,verify_certificate_json
from geoforge_upgrade_suite.deterministic_solver import ExactFactEvaluator,GuardLedger

def test_nondegeneracy_guard_0000():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0001():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0002():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0003():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0004():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0005():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0006():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0007():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0008():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0009():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0010():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0011():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0012():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0013():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0014():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0015():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0016():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0017():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0018():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0019():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0020():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0021():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0022():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0023():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0024():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0025():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0026():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0027():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0028():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0029():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0030():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0031():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0032():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0033():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0034():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0035():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0036():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0037():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0038():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0039():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0040():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0041():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0042():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0043():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0044():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0045():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0046():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0047():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0048():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0049():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0050():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0051():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0052():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0053():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0054():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0055():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0056():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0057():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0058():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0059():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0060():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0061():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0062():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0063():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0064():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0065():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0066():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0067():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0068():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0069():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0070():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0071():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0072():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0073():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0074():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0075():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0076():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0077():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0078():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0079():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0080():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0081():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0082():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0083():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0084():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0085():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0086():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0087():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0088():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0089():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0090():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0091():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0092():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0093():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0094():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0095():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0096():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0097():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0098():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0099():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0100():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0101():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0102():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0103():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0104():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0105():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0106():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0107():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0108():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0109():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0110():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0111():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0112():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0113():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0114():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0115():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0116():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0117():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0118():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0119():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0120():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0121():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0122():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0123():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0124():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0125():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0126():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0127():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0128():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0129():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0130():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0131():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0132():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0133():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0134():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0135():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0136():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0137():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0138():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0139():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0140():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0141():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0142():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0143():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0144():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0145():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0146():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0147():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0148():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0149():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0150():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0151():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0152():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0153():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0154():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0155():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0156():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0157():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0158():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0159():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0160():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0161():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0162():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0163():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0164():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0165():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0166():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0167():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0168():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0169():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0170():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0171():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0172():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0173():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0174():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0175():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0176():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0177():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0178():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0179():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0180():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0181():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0182():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0183():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0184():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0185():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0186():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0187():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0188():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0189():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0190():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0191():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0192():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0193():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0194():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0195():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0196():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0197():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0198():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0199():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0200():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0201():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0202():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0203():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0204():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0205():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0206():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0207():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0208():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0209():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0210():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0211():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0212():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0213():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0214():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0215():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0216():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0217():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0218():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0219():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0220():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0221():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0222():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0223():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0224():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0225():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0226():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0227():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0228():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0229():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0230():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0231():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0232():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0233():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0234():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0235():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0236():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0237():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0238():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0239():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0240():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0241():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0242():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0243():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0244():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0245():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0246():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0247():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0248():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0249():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0250():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0251():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0252():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0253():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0254():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0255():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0256():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0257():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0258():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0259():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0260():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0261():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0262():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0263():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0264():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0265():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0266():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0267():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0268():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0269():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0270():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0271():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0272():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0273():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0274():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0275():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0276():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0277():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0278():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0279():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0280():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0281():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0282():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0283():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0284():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0285():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0286():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0287():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0288():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0289():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0290():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0291():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0292():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0293():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0294():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0295():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0296():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0297():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0298():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0299():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0300():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0301():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0302():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0303():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0304():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0305():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0306():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0307():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0308():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0309():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0310():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0311():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0312():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0313():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0314():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0315():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0316():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0317():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0318():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0319():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0320():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0321():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0322():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0323():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0324():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0325():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0326():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0327():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0328():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0329():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0330():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0331():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0332():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0333():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0334():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0335():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0336():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0337():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0338():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0339():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0340():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0341():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0342():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0343():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0344():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0345():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0346():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0347():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0348():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0349():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0350():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0351():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0352():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0353():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0354():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0355():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0356():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0357():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0358():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0359():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0360():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0361():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0362():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0363():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0364():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0365():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0366():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0367():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0368():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0369():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0370():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0371():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0372():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0373():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0374():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0375():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0376():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0377():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0378():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0379():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0380():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0381():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0382():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0383():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0384():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0385():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0386():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0387():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0388():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0389():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0390():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0391():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0392():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0393():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0394():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0395():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0396():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0397():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0398():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0399():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0400():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0401():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0402():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0403():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0404():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0405():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0406():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0407():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0408():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0409():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0410():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0411():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0412():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0413():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0414():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0415():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0416():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0417():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0418():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0419():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0420():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0421():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0422():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0423():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0424():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0425():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0426():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0427():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0428():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0429():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0430():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0431():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0432():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0433():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0434():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0435():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0436():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0437():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0438():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0439():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0440():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0441():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0442():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0443():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0444():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0445():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0446():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0447():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0448():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0449():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0450():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0451():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0452():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0453():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0454():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0455():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0456():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0457():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0458():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0459():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0460():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0461():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0462():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0463():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0464():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0465():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0466():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0467():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0468():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0469():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0470():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0471():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0472():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0473():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0474():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0475():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0476():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0477():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0478():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0479():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0480():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0481():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0482():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0483():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0484():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0485():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0486():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0487():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0488():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0489():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0490():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0491():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0492():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0493():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0494():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0495():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0496():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0497():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0498():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0499():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0500():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0501():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0502():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0503():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0504():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0505():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0506():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0507():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0508():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0509():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0510():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0511():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0512():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0513():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0514():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0515():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0516():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0517():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0518():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0519():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0520():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0521():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0522():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0523():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0524():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0525():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0526():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0527():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0528():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0529():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0530():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0531():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0532():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0533():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0534():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0535():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0536():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0537():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0538():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0539():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0540():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0541():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0542():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0543():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0544():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0545():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0546():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0547():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0548():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0549():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0550():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0551():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0552():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0553():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0554():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0555():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0556():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0557():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0558():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0559():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0560():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0561():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0562():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0563():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0564():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0565():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0566():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0567():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0568():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0569():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0570():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0571():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0572():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0573():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0574():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0575():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0576():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0577():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0578():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0579():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0580():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0581():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0582():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0583():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0584():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0585():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0586():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0587():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0588():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0589():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0590():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0591():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0592():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0593():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0594():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0595():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0596():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0597():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0598():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

def test_nondegeneracy_guard_0599():
    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')

