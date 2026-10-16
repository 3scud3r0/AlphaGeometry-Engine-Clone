# GENERATED, DETERMINISTIC, NO TRAINED MODEL USED.
# Source generator: geoforge_upgrade_suite/generate_untrained_matrix.py
from fractions import Fraction as Q
from geoforge_upgrade_suite.geometry_exact import Vec2,Polynomial,Line
from geoforge_upgrade_suite.exact_constructions import SPoint,foot,line_intersection
from geoforge_upgrade_suite.deterministic_ideal import ExactIdealEngine,certificate_to_json,verify_certificate_json
from geoforge_upgrade_suite.deterministic_solver import ExactFactEvaluator,GuardLedger

def test_rational_angle_0000():
    q=1;r=2;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0001():
    q=2;r=3;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0002():
    q=3;r=4;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0003():
    q=4;r=5;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0004():
    q=5;r=6;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0005():
    q=6;r=7;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0006():
    q=7;r=8;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0007():
    q=8;r=9;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0008():
    q=9;r=10;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0009():
    q=10;r=11;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0010():
    q=11;r=12;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0011():
    q=12;r=13;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0012():
    q=13;r=14;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0013():
    q=14;r=2;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0014():
    q=15;r=3;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0015():
    q=16;r=4;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0016():
    q=17;r=5;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0017():
    q=1;r=6;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0018():
    q=2;r=7;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0019():
    q=3;r=8;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0020():
    q=4;r=9;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0021():
    q=5;r=10;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0022():
    q=6;r=11;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0023():
    q=7;r=12;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0024():
    q=8;r=13;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0025():
    q=9;r=14;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0026():
    q=10;r=2;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0027():
    q=11;r=3;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0028():
    q=12;r=4;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0029():
    q=13;r=5;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0030():
    q=14;r=6;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0031():
    q=15;r=7;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0032():
    q=16;r=8;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0033():
    q=17;r=9;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0034():
    q=1;r=10;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0035():
    q=2;r=11;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0036():
    q=3;r=12;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0037():
    q=4;r=13;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0038():
    q=5;r=14;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0039():
    q=6;r=2;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0040():
    q=7;r=3;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0041():
    q=8;r=4;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0042():
    q=9;r=5;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0043():
    q=10;r=6;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0044():
    q=11;r=7;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0045():
    q=12;r=8;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0046():
    q=13;r=9;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0047():
    q=14;r=10;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0048():
    q=15;r=11;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0049():
    q=16;r=12;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0050():
    q=17;r=13;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0051():
    q=1;r=14;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0052():
    q=2;r=2;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0053():
    q=3;r=3;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0054():
    q=4;r=4;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0055():
    q=5;r=5;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0056():
    q=6;r=6;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0057():
    q=7;r=7;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0058():
    q=8;r=8;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0059():
    q=9;r=9;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0060():
    q=10;r=10;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0061():
    q=11;r=11;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0062():
    q=12;r=12;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0063():
    q=13;r=13;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0064():
    q=14;r=14;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0065():
    q=15;r=2;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0066():
    q=16;r=3;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0067():
    q=17;r=4;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0068():
    q=1;r=5;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0069():
    q=2;r=6;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0070():
    q=3;r=7;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0071():
    q=4;r=8;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0072():
    q=5;r=9;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0073():
    q=6;r=10;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0074():
    q=7;r=11;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0075():
    q=8;r=12;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0076():
    q=9;r=13;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0077():
    q=10;r=14;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0078():
    q=11;r=2;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0079():
    q=12;r=3;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0080():
    q=13;r=4;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0081():
    q=14;r=5;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0082():
    q=15;r=6;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0083():
    q=16;r=7;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0084():
    q=17;r=8;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0085():
    q=1;r=9;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0086():
    q=2;r=10;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0087():
    q=3;r=11;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0088():
    q=4;r=12;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0089():
    q=5;r=13;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0090():
    q=6;r=14;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0091():
    q=7;r=2;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0092():
    q=8;r=3;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0093():
    q=9;r=4;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0094():
    q=10;r=5;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0095():
    q=11;r=6;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0096():
    q=12;r=7;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0097():
    q=13;r=8;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0098():
    q=14;r=9;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0099():
    q=15;r=10;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0100():
    q=16;r=11;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0101():
    q=17;r=12;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0102():
    q=1;r=13;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0103():
    q=2;r=14;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0104():
    q=3;r=2;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0105():
    q=4;r=3;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0106():
    q=5;r=4;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0107():
    q=6;r=5;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0108():
    q=7;r=6;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0109():
    q=8;r=7;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0110():
    q=9;r=8;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0111():
    q=10;r=9;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0112():
    q=11;r=10;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0113():
    q=12;r=11;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0114():
    q=13;r=12;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0115():
    q=14;r=13;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0116():
    q=15;r=14;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0117():
    q=16;r=2;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0118():
    q=17;r=3;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0119():
    q=1;r=4;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0120():
    q=2;r=5;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0121():
    q=3;r=6;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0122():
    q=4;r=7;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0123():
    q=5;r=8;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0124():
    q=6;r=9;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0125():
    q=7;r=10;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0126():
    q=8;r=11;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0127():
    q=9;r=12;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0128():
    q=10;r=13;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0129():
    q=11;r=14;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0130():
    q=12;r=2;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0131():
    q=13;r=3;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0132():
    q=14;r=4;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0133():
    q=15;r=5;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0134():
    q=16;r=6;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0135():
    q=17;r=7;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0136():
    q=1;r=8;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0137():
    q=2;r=9;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0138():
    q=3;r=10;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0139():
    q=4;r=11;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0140():
    q=5;r=12;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0141():
    q=6;r=13;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0142():
    q=7;r=14;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0143():
    q=8;r=2;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0144():
    q=9;r=3;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0145():
    q=10;r=4;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0146():
    q=11;r=5;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0147():
    q=12;r=6;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0148():
    q=13;r=7;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0149():
    q=14;r=8;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0150():
    q=15;r=9;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0151():
    q=16;r=10;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0152():
    q=17;r=11;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0153():
    q=1;r=12;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0154():
    q=2;r=13;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0155():
    q=3;r=14;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0156():
    q=4;r=2;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0157():
    q=5;r=3;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0158():
    q=6;r=4;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0159():
    q=7;r=5;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0160():
    q=8;r=6;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0161():
    q=9;r=7;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0162():
    q=10;r=8;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0163():
    q=11;r=9;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0164():
    q=12;r=10;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0165():
    q=13;r=11;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0166():
    q=14;r=12;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0167():
    q=15;r=13;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0168():
    q=16;r=14;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0169():
    q=17;r=2;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0170():
    q=1;r=3;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0171():
    q=2;r=4;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0172():
    q=3;r=5;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0173():
    q=4;r=6;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0174():
    q=5;r=7;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0175():
    q=6;r=8;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0176():
    q=7;r=9;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0177():
    q=8;r=10;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0178():
    q=9;r=11;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0179():
    q=10;r=12;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0180():
    q=11;r=13;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0181():
    q=12;r=14;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0182():
    q=13;r=2;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0183():
    q=14;r=3;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0184():
    q=15;r=4;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0185():
    q=16;r=5;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0186():
    q=17;r=6;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0187():
    q=1;r=7;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0188():
    q=2;r=8;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0189():
    q=3;r=9;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0190():
    q=4;r=10;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0191():
    q=5;r=11;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0192():
    q=6;r=12;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0193():
    q=7;r=13;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0194():
    q=8;r=14;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0195():
    q=9;r=2;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0196():
    q=10;r=3;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0197():
    q=11;r=4;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0198():
    q=12;r=5;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0199():
    q=13;r=6;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0200():
    q=14;r=7;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0201():
    q=15;r=8;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0202():
    q=16;r=9;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0203():
    q=17;r=10;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0204():
    q=1;r=11;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0205():
    q=2;r=12;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0206():
    q=3;r=13;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0207():
    q=4;r=14;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0208():
    q=5;r=2;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0209():
    q=6;r=3;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0210():
    q=7;r=4;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0211():
    q=8;r=5;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0212():
    q=9;r=6;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0213():
    q=10;r=7;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0214():
    q=11;r=8;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0215():
    q=12;r=9;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0216():
    q=13;r=10;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0217():
    q=14;r=11;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0218():
    q=15;r=12;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0219():
    q=16;r=13;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0220():
    q=17;r=14;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0221():
    q=1;r=2;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0222():
    q=2;r=3;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0223():
    q=3;r=4;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0224():
    q=4;r=5;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0225():
    q=5;r=6;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0226():
    q=6;r=7;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0227():
    q=7;r=8;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0228():
    q=8;r=9;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0229():
    q=9;r=10;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0230():
    q=10;r=11;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0231():
    q=11;r=12;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0232():
    q=12;r=13;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0233():
    q=13;r=14;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0234():
    q=14;r=2;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0235():
    q=15;r=3;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0236():
    q=16;r=4;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0237():
    q=17;r=5;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0238():
    q=1;r=6;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0239():
    q=2;r=7;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0240():
    q=3;r=8;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0241():
    q=4;r=9;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0242():
    q=5;r=10;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0243():
    q=6;r=11;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0244():
    q=7;r=12;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0245():
    q=8;r=13;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0246():
    q=9;r=14;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0247():
    q=10;r=2;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0248():
    q=11;r=3;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0249():
    q=12;r=4;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0250():
    q=13;r=5;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0251():
    q=14;r=6;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0252():
    q=15;r=7;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0253():
    q=16;r=8;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0254():
    q=17;r=9;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0255():
    q=1;r=10;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0256():
    q=2;r=11;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0257():
    q=3;r=12;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0258():
    q=4;r=13;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0259():
    q=5;r=14;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0260():
    q=6;r=2;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0261():
    q=7;r=3;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0262():
    q=8;r=4;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0263():
    q=9;r=5;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0264():
    q=10;r=6;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0265():
    q=11;r=7;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0266():
    q=12;r=8;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0267():
    q=13;r=9;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0268():
    q=14;r=10;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0269():
    q=15;r=11;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0270():
    q=16;r=12;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0271():
    q=17;r=13;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0272():
    q=1;r=14;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0273():
    q=2;r=2;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0274():
    q=3;r=3;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0275():
    q=4;r=4;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0276():
    q=5;r=5;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0277():
    q=6;r=6;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0278():
    q=7;r=7;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0279():
    q=8;r=8;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0280():
    q=9;r=9;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0281():
    q=10;r=10;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0282():
    q=11;r=11;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0283():
    q=12;r=12;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0284():
    q=13;r=13;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0285():
    q=14;r=14;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0286():
    q=15;r=2;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0287():
    q=16;r=3;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0288():
    q=17;r=4;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0289():
    q=1;r=5;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0290():
    q=2;r=6;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0291():
    q=3;r=7;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0292():
    q=4;r=8;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0293():
    q=5;r=9;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0294():
    q=6;r=10;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0295():
    q=7;r=11;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0296():
    q=8;r=12;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0297():
    q=9;r=13;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0298():
    q=10;r=14;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0299():
    q=11;r=2;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0300():
    q=12;r=3;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0301():
    q=13;r=4;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0302():
    q=14;r=5;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0303():
    q=15;r=6;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0304():
    q=16;r=7;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0305():
    q=17;r=8;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0306():
    q=1;r=9;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0307():
    q=2;r=10;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0308():
    q=3;r=11;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0309():
    q=4;r=12;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0310():
    q=5;r=13;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0311():
    q=6;r=14;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0312():
    q=7;r=2;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0313():
    q=8;r=3;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0314():
    q=9;r=4;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0315():
    q=10;r=5;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0316():
    q=11;r=6;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0317():
    q=12;r=7;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0318():
    q=13;r=8;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0319():
    q=14;r=9;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0320():
    q=15;r=10;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0321():
    q=16;r=11;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0322():
    q=17;r=12;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0323():
    q=1;r=13;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0324():
    q=2;r=14;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0325():
    q=3;r=2;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0326():
    q=4;r=3;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0327():
    q=5;r=4;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0328():
    q=6;r=5;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0329():
    q=7;r=6;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0330():
    q=8;r=7;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0331():
    q=9;r=8;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0332():
    q=10;r=9;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0333():
    q=11;r=10;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0334():
    q=12;r=11;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0335():
    q=13;r=12;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0336():
    q=14;r=13;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0337():
    q=15;r=14;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0338():
    q=16;r=2;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0339():
    q=17;r=3;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0340():
    q=1;r=4;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0341():
    q=2;r=5;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0342():
    q=3;r=6;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0343():
    q=4;r=7;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0344():
    q=5;r=8;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0345():
    q=6;r=9;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0346():
    q=7;r=10;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0347():
    q=8;r=11;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0348():
    q=9;r=12;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0349():
    q=10;r=13;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0350():
    q=11;r=14;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0351():
    q=12;r=2;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0352():
    q=13;r=3;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0353():
    q=14;r=4;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0354():
    q=15;r=5;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0355():
    q=16;r=6;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0356():
    q=17;r=7;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0357():
    q=1;r=8;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0358():
    q=2;r=9;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0359():
    q=3;r=10;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0360():
    q=4;r=11;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0361():
    q=5;r=12;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0362():
    q=6;r=13;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0363():
    q=7;r=14;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0364():
    q=8;r=2;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0365():
    q=9;r=3;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0366():
    q=10;r=4;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0367():
    q=11;r=5;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0368():
    q=12;r=6;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0369():
    q=13;r=7;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0370():
    q=14;r=8;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0371():
    q=15;r=9;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0372():
    q=16;r=10;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0373():
    q=17;r=11;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0374():
    q=1;r=12;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0375():
    q=2;r=13;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0376():
    q=3;r=14;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0377():
    q=4;r=2;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0378():
    q=5;r=3;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0379():
    q=6;r=4;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0380():
    q=7;r=5;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0381():
    q=8;r=6;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0382():
    q=9;r=7;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0383():
    q=10;r=8;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0384():
    q=11;r=9;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0385():
    q=12;r=10;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0386():
    q=13;r=11;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0387():
    q=14;r=12;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0388():
    q=15;r=13;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0389():
    q=16;r=14;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0390():
    q=17;r=2;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0391():
    q=1;r=3;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0392():
    q=2;r=4;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0393():
    q=3;r=5;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0394():
    q=4;r=6;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0395():
    q=5;r=7;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0396():
    q=6;r=8;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0397():
    q=7;r=9;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0398():
    q=8;r=10;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0399():
    q=9;r=11;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0400():
    q=10;r=12;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0401():
    q=11;r=13;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0402():
    q=12;r=14;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0403():
    q=13;r=2;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0404():
    q=14;r=3;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0405():
    q=15;r=4;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0406():
    q=16;r=5;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0407():
    q=17;r=6;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0408():
    q=1;r=7;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0409():
    q=2;r=8;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0410():
    q=3;r=9;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0411():
    q=4;r=10;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0412():
    q=5;r=11;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0413():
    q=6;r=12;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0414():
    q=7;r=13;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0415():
    q=8;r=14;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0416():
    q=9;r=2;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0417():
    q=10;r=3;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0418():
    q=11;r=4;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0419():
    q=12;r=5;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0420():
    q=13;r=6;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0421():
    q=14;r=7;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0422():
    q=15;r=8;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0423():
    q=16;r=9;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0424():
    q=17;r=10;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0425():
    q=1;r=11;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0426():
    q=2;r=12;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0427():
    q=3;r=13;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0428():
    q=4;r=14;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0429():
    q=5;r=2;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0430():
    q=6;r=3;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0431():
    q=7;r=4;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0432():
    q=8;r=5;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0433():
    q=9;r=6;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0434():
    q=10;r=7;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0435():
    q=11;r=8;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0436():
    q=12;r=9;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0437():
    q=13;r=10;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0438():
    q=14;r=11;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0439():
    q=15;r=12;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0440():
    q=16;r=13;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0441():
    q=17;r=14;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0442():
    q=1;r=2;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0443():
    q=2;r=3;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0444():
    q=3;r=4;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0445():
    q=4;r=5;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0446():
    q=5;r=6;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0447():
    q=6;r=7;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0448():
    q=7;r=8;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0449():
    q=8;r=9;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0450():
    q=9;r=10;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0451():
    q=10;r=11;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0452():
    q=11;r=12;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0453():
    q=12;r=13;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0454():
    q=13;r=14;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0455():
    q=14;r=2;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0456():
    q=15;r=3;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0457():
    q=16;r=4;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0458():
    q=17;r=5;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0459():
    q=1;r=6;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0460():
    q=2;r=7;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0461():
    q=3;r=8;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0462():
    q=4;r=9;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0463():
    q=5;r=10;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0464():
    q=6;r=11;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0465():
    q=7;r=12;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0466():
    q=8;r=13;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0467():
    q=9;r=14;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0468():
    q=10;r=2;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0469():
    q=11;r=3;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0470():
    q=12;r=4;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0471():
    q=13;r=5;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0472():
    q=14;r=6;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0473():
    q=15;r=7;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0474():
    q=16;r=8;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0475():
    q=17;r=9;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0476():
    q=1;r=10;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0477():
    q=2;r=11;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0478():
    q=3;r=12;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0479():
    q=4;r=13;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0480():
    q=5;r=14;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0481():
    q=6;r=2;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0482():
    q=7;r=3;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0483():
    q=8;r=4;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0484():
    q=9;r=5;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0485():
    q=10;r=6;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0486():
    q=11;r=7;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0487():
    q=12;r=8;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0488():
    q=13;r=9;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0489():
    q=14;r=10;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0490():
    q=15;r=11;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0491():
    q=16;r=12;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0492():
    q=17;r=13;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0493():
    q=1;r=14;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0494():
    q=2;r=2;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0495():
    q=3;r=3;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0496():
    q=4;r=4;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0497():
    q=5;r=5;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0498():
    q=6;r=6;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0499():
    q=7;r=7;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0500():
    q=8;r=8;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0501():
    q=9;r=9;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0502():
    q=10;r=10;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0503():
    q=11;r=11;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0504():
    q=12;r=12;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0505():
    q=13;r=13;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0506():
    q=14;r=14;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0507():
    q=15;r=2;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0508():
    q=16;r=3;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0509():
    q=17;r=4;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0510():
    q=1;r=5;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0511():
    q=2;r=6;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0512():
    q=3;r=7;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0513():
    q=4;r=8;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0514():
    q=5;r=9;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0515():
    q=6;r=10;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0516():
    q=7;r=11;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0517():
    q=8;r=12;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0518():
    q=9;r=13;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0519():
    q=10;r=14;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0520():
    q=11;r=2;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0521():
    q=12;r=3;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0522():
    q=13;r=4;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0523():
    q=14;r=5;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0524():
    q=15;r=6;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0525():
    q=16;r=7;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0526():
    q=17;r=8;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0527():
    q=1;r=9;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0528():
    q=2;r=10;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0529():
    q=3;r=11;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0530():
    q=4;r=12;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0531():
    q=5;r=13;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0532():
    q=6;r=14;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0533():
    q=7;r=2;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0534():
    q=8;r=3;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0535():
    q=9;r=4;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0536():
    q=10;r=5;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0537():
    q=11;r=6;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0538():
    q=12;r=7;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0539():
    q=13;r=8;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0540():
    q=14;r=9;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0541():
    q=15;r=10;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0542():
    q=16;r=11;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0543():
    q=17;r=12;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0544():
    q=1;r=13;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0545():
    q=2;r=14;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0546():
    q=3;r=2;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0547():
    q=4;r=3;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0548():
    q=5;r=4;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0549():
    q=6;r=5;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0550():
    q=7;r=6;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0551():
    q=8;r=7;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0552():
    q=9;r=8;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0553():
    q=10;r=9;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0554():
    q=11;r=10;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0555():
    q=12;r=11;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0556():
    q=13;r=12;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0557():
    q=14;r=13;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0558():
    q=15;r=14;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0559():
    q=16;r=2;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0560():
    q=17;r=3;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0561():
    q=1;r=4;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0562():
    q=2;r=5;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0563():
    q=3;r=6;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0564():
    q=4;r=7;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0565():
    q=5;r=8;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0566():
    q=6;r=9;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0567():
    q=7;r=10;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0568():
    q=8;r=11;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0569():
    q=9;r=12;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0570():
    q=10;r=13;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0571():
    q=11;r=14;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0572():
    q=12;r=2;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0573():
    q=13;r=3;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0574():
    q=14;r=4;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0575():
    q=15;r=5;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0576():
    q=16;r=6;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0577():
    q=17;r=7;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0578():
    q=1;r=8;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0579():
    q=2;r=9;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0580():
    q=3;r=10;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0581():
    q=4;r=11;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0582():
    q=5;r=12;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0583():
    q=6;r=13;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0584():
    q=7;r=14;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0585():
    q=8;r=2;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0586():
    q=9;r=3;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0587():
    q=10;r=4;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0588():
    q=11;r=5;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0589():
    q=12;r=6;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0590():
    q=13;r=7;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0591():
    q=14;r=8;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0592():
    q=15;r=9;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0593():
    q=16;r=10;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0594():
    q=17;r=11;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0595():
    q=1;r=12;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0596():
    q=2;r=13;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0597():
    q=3;r=14;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0598():
    q=4;r=2;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

def test_rational_angle_0599():
    q=5;r=3;p={'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')

