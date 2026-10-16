# GENERATED, DETERMINISTIC, NO TRAINED MODEL USED.
# Source generator: geoforge_upgrade_suite/generate_untrained_matrix.py
from fractions import Fraction as Q
from geoforge_upgrade_suite.geometry_exact import Vec2,Polynomial,Line
from geoforge_upgrade_suite.exact_constructions import SPoint,foot,line_intersection
from geoforge_upgrade_suite.deterministic_ideal import ExactIdealEngine,certificate_to_json,verify_certificate_json
from geoforge_upgrade_suite.deterministic_solver import ExactFactEvaluator,GuardLedger

def test_vector_midpoint_0000():
    a=Vec2(Q(1),Q(2));b=Vec2(Q(1),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0001():
    a=Vec2(Q(2),Q(3));b=Vec2(Q(2),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0002():
    a=Vec2(Q(3),Q(4));b=Vec2(Q(3),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0003():
    a=Vec2(Q(4),Q(5));b=Vec2(Q(4),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0004():
    a=Vec2(Q(5),Q(6));b=Vec2(Q(5),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0005():
    a=Vec2(Q(6),Q(7));b=Vec2(Q(6),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0006():
    a=Vec2(Q(7),Q(8));b=Vec2(Q(7),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0007():
    a=Vec2(Q(8),Q(9));b=Vec2(Q(8),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0008():
    a=Vec2(Q(9),Q(10));b=Vec2(Q(9),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0009():
    a=Vec2(Q(10),Q(11));b=Vec2(Q(10),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0010():
    a=Vec2(Q(11),Q(12));b=Vec2(Q(11),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0011():
    a=Vec2(Q(12),Q(13));b=Vec2(Q(12),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0012():
    a=Vec2(Q(13),Q(14));b=Vec2(Q(13),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0013():
    a=Vec2(Q(14),Q(2));b=Vec2(Q(14),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0014():
    a=Vec2(Q(15),Q(3));b=Vec2(Q(15),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0015():
    a=Vec2(Q(16),Q(4));b=Vec2(Q(16),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0016():
    a=Vec2(Q(17),Q(5));b=Vec2(Q(17),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0017():
    a=Vec2(Q(1),Q(6));b=Vec2(Q(18),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0018():
    a=Vec2(Q(2),Q(7));b=Vec2(Q(19),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0019():
    a=Vec2(Q(3),Q(8));b=Vec2(Q(20),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0020():
    a=Vec2(Q(4),Q(9));b=Vec2(Q(21),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0021():
    a=Vec2(Q(5),Q(10));b=Vec2(Q(22),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0022():
    a=Vec2(Q(6),Q(11));b=Vec2(Q(23),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0023():
    a=Vec2(Q(7),Q(12));b=Vec2(Q(1),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0024():
    a=Vec2(Q(8),Q(13));b=Vec2(Q(2),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0025():
    a=Vec2(Q(9),Q(14));b=Vec2(Q(3),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0026():
    a=Vec2(Q(10),Q(2));b=Vec2(Q(4),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0027():
    a=Vec2(Q(11),Q(3));b=Vec2(Q(5),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0028():
    a=Vec2(Q(12),Q(4));b=Vec2(Q(6),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0029():
    a=Vec2(Q(13),Q(5));b=Vec2(Q(7),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0030():
    a=Vec2(Q(14),Q(6));b=Vec2(Q(8),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0031():
    a=Vec2(Q(15),Q(7));b=Vec2(Q(9),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0032():
    a=Vec2(Q(16),Q(8));b=Vec2(Q(10),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0033():
    a=Vec2(Q(17),Q(9));b=Vec2(Q(11),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0034():
    a=Vec2(Q(1),Q(10));b=Vec2(Q(12),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0035():
    a=Vec2(Q(2),Q(11));b=Vec2(Q(13),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0036():
    a=Vec2(Q(3),Q(12));b=Vec2(Q(14),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0037():
    a=Vec2(Q(4),Q(13));b=Vec2(Q(15),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0038():
    a=Vec2(Q(5),Q(14));b=Vec2(Q(16),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0039():
    a=Vec2(Q(6),Q(2));b=Vec2(Q(17),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0040():
    a=Vec2(Q(7),Q(3));b=Vec2(Q(18),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0041():
    a=Vec2(Q(8),Q(4));b=Vec2(Q(19),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0042():
    a=Vec2(Q(9),Q(5));b=Vec2(Q(20),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0043():
    a=Vec2(Q(10),Q(6));b=Vec2(Q(21),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0044():
    a=Vec2(Q(11),Q(7));b=Vec2(Q(22),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0045():
    a=Vec2(Q(12),Q(8));b=Vec2(Q(23),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0046():
    a=Vec2(Q(13),Q(9));b=Vec2(Q(1),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0047():
    a=Vec2(Q(14),Q(10));b=Vec2(Q(2),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0048():
    a=Vec2(Q(15),Q(11));b=Vec2(Q(3),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0049():
    a=Vec2(Q(16),Q(12));b=Vec2(Q(4),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0050():
    a=Vec2(Q(17),Q(13));b=Vec2(Q(5),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0051():
    a=Vec2(Q(1),Q(14));b=Vec2(Q(6),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0052():
    a=Vec2(Q(2),Q(2));b=Vec2(Q(7),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0053():
    a=Vec2(Q(3),Q(3));b=Vec2(Q(8),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0054():
    a=Vec2(Q(4),Q(4));b=Vec2(Q(9),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0055():
    a=Vec2(Q(5),Q(5));b=Vec2(Q(10),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0056():
    a=Vec2(Q(6),Q(6));b=Vec2(Q(11),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0057():
    a=Vec2(Q(7),Q(7));b=Vec2(Q(12),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0058():
    a=Vec2(Q(8),Q(8));b=Vec2(Q(13),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0059():
    a=Vec2(Q(9),Q(9));b=Vec2(Q(14),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0060():
    a=Vec2(Q(10),Q(10));b=Vec2(Q(15),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0061():
    a=Vec2(Q(11),Q(11));b=Vec2(Q(16),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0062():
    a=Vec2(Q(12),Q(12));b=Vec2(Q(17),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0063():
    a=Vec2(Q(13),Q(13));b=Vec2(Q(18),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0064():
    a=Vec2(Q(14),Q(14));b=Vec2(Q(19),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0065():
    a=Vec2(Q(15),Q(2));b=Vec2(Q(20),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0066():
    a=Vec2(Q(16),Q(3));b=Vec2(Q(21),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0067():
    a=Vec2(Q(17),Q(4));b=Vec2(Q(22),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0068():
    a=Vec2(Q(1),Q(5));b=Vec2(Q(23),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0069():
    a=Vec2(Q(2),Q(6));b=Vec2(Q(1),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0070():
    a=Vec2(Q(3),Q(7));b=Vec2(Q(2),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0071():
    a=Vec2(Q(4),Q(8));b=Vec2(Q(3),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0072():
    a=Vec2(Q(5),Q(9));b=Vec2(Q(4),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0073():
    a=Vec2(Q(6),Q(10));b=Vec2(Q(5),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0074():
    a=Vec2(Q(7),Q(11));b=Vec2(Q(6),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0075():
    a=Vec2(Q(8),Q(12));b=Vec2(Q(7),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0076():
    a=Vec2(Q(9),Q(13));b=Vec2(Q(8),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0077():
    a=Vec2(Q(10),Q(14));b=Vec2(Q(9),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0078():
    a=Vec2(Q(11),Q(2));b=Vec2(Q(10),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0079():
    a=Vec2(Q(12),Q(3));b=Vec2(Q(11),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0080():
    a=Vec2(Q(13),Q(4));b=Vec2(Q(12),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0081():
    a=Vec2(Q(14),Q(5));b=Vec2(Q(13),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0082():
    a=Vec2(Q(15),Q(6));b=Vec2(Q(14),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0083():
    a=Vec2(Q(16),Q(7));b=Vec2(Q(15),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0084():
    a=Vec2(Q(17),Q(8));b=Vec2(Q(16),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0085():
    a=Vec2(Q(1),Q(9));b=Vec2(Q(17),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0086():
    a=Vec2(Q(2),Q(10));b=Vec2(Q(18),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0087():
    a=Vec2(Q(3),Q(11));b=Vec2(Q(19),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0088():
    a=Vec2(Q(4),Q(12));b=Vec2(Q(20),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0089():
    a=Vec2(Q(5),Q(13));b=Vec2(Q(21),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0090():
    a=Vec2(Q(6),Q(14));b=Vec2(Q(22),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0091():
    a=Vec2(Q(7),Q(2));b=Vec2(Q(23),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0092():
    a=Vec2(Q(8),Q(3));b=Vec2(Q(1),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0093():
    a=Vec2(Q(9),Q(4));b=Vec2(Q(2),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0094():
    a=Vec2(Q(10),Q(5));b=Vec2(Q(3),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0095():
    a=Vec2(Q(11),Q(6));b=Vec2(Q(4),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0096():
    a=Vec2(Q(12),Q(7));b=Vec2(Q(5),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0097():
    a=Vec2(Q(13),Q(8));b=Vec2(Q(6),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0098():
    a=Vec2(Q(14),Q(9));b=Vec2(Q(7),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0099():
    a=Vec2(Q(15),Q(10));b=Vec2(Q(8),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0100():
    a=Vec2(Q(16),Q(11));b=Vec2(Q(9),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0101():
    a=Vec2(Q(17),Q(12));b=Vec2(Q(10),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0102():
    a=Vec2(Q(1),Q(13));b=Vec2(Q(11),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0103():
    a=Vec2(Q(2),Q(14));b=Vec2(Q(12),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0104():
    a=Vec2(Q(3),Q(2));b=Vec2(Q(13),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0105():
    a=Vec2(Q(4),Q(3));b=Vec2(Q(14),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0106():
    a=Vec2(Q(5),Q(4));b=Vec2(Q(15),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0107():
    a=Vec2(Q(6),Q(5));b=Vec2(Q(16),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0108():
    a=Vec2(Q(7),Q(6));b=Vec2(Q(17),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0109():
    a=Vec2(Q(8),Q(7));b=Vec2(Q(18),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0110():
    a=Vec2(Q(9),Q(8));b=Vec2(Q(19),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0111():
    a=Vec2(Q(10),Q(9));b=Vec2(Q(20),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0112():
    a=Vec2(Q(11),Q(10));b=Vec2(Q(21),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0113():
    a=Vec2(Q(12),Q(11));b=Vec2(Q(22),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0114():
    a=Vec2(Q(13),Q(12));b=Vec2(Q(23),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0115():
    a=Vec2(Q(14),Q(13));b=Vec2(Q(1),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0116():
    a=Vec2(Q(15),Q(14));b=Vec2(Q(2),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0117():
    a=Vec2(Q(16),Q(2));b=Vec2(Q(3),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0118():
    a=Vec2(Q(17),Q(3));b=Vec2(Q(4),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0119():
    a=Vec2(Q(1),Q(4));b=Vec2(Q(5),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0120():
    a=Vec2(Q(2),Q(5));b=Vec2(Q(6),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0121():
    a=Vec2(Q(3),Q(6));b=Vec2(Q(7),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0122():
    a=Vec2(Q(4),Q(7));b=Vec2(Q(8),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0123():
    a=Vec2(Q(5),Q(8));b=Vec2(Q(9),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0124():
    a=Vec2(Q(6),Q(9));b=Vec2(Q(10),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0125():
    a=Vec2(Q(7),Q(10));b=Vec2(Q(11),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0126():
    a=Vec2(Q(8),Q(11));b=Vec2(Q(12),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0127():
    a=Vec2(Q(9),Q(12));b=Vec2(Q(13),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0128():
    a=Vec2(Q(10),Q(13));b=Vec2(Q(14),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0129():
    a=Vec2(Q(11),Q(14));b=Vec2(Q(15),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0130():
    a=Vec2(Q(12),Q(2));b=Vec2(Q(16),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0131():
    a=Vec2(Q(13),Q(3));b=Vec2(Q(17),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0132():
    a=Vec2(Q(14),Q(4));b=Vec2(Q(18),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0133():
    a=Vec2(Q(15),Q(5));b=Vec2(Q(19),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0134():
    a=Vec2(Q(16),Q(6));b=Vec2(Q(20),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0135():
    a=Vec2(Q(17),Q(7));b=Vec2(Q(21),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0136():
    a=Vec2(Q(1),Q(8));b=Vec2(Q(22),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0137():
    a=Vec2(Q(2),Q(9));b=Vec2(Q(23),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0138():
    a=Vec2(Q(3),Q(10));b=Vec2(Q(1),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0139():
    a=Vec2(Q(4),Q(11));b=Vec2(Q(2),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0140():
    a=Vec2(Q(5),Q(12));b=Vec2(Q(3),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0141():
    a=Vec2(Q(6),Q(13));b=Vec2(Q(4),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0142():
    a=Vec2(Q(7),Q(14));b=Vec2(Q(5),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0143():
    a=Vec2(Q(8),Q(2));b=Vec2(Q(6),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0144():
    a=Vec2(Q(9),Q(3));b=Vec2(Q(7),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0145():
    a=Vec2(Q(10),Q(4));b=Vec2(Q(8),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0146():
    a=Vec2(Q(11),Q(5));b=Vec2(Q(9),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0147():
    a=Vec2(Q(12),Q(6));b=Vec2(Q(10),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0148():
    a=Vec2(Q(13),Q(7));b=Vec2(Q(11),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0149():
    a=Vec2(Q(14),Q(8));b=Vec2(Q(12),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0150():
    a=Vec2(Q(15),Q(9));b=Vec2(Q(13),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0151():
    a=Vec2(Q(16),Q(10));b=Vec2(Q(14),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0152():
    a=Vec2(Q(17),Q(11));b=Vec2(Q(15),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0153():
    a=Vec2(Q(1),Q(12));b=Vec2(Q(16),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0154():
    a=Vec2(Q(2),Q(13));b=Vec2(Q(17),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0155():
    a=Vec2(Q(3),Q(14));b=Vec2(Q(18),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0156():
    a=Vec2(Q(4),Q(2));b=Vec2(Q(19),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0157():
    a=Vec2(Q(5),Q(3));b=Vec2(Q(20),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0158():
    a=Vec2(Q(6),Q(4));b=Vec2(Q(21),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0159():
    a=Vec2(Q(7),Q(5));b=Vec2(Q(22),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0160():
    a=Vec2(Q(8),Q(6));b=Vec2(Q(23),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0161():
    a=Vec2(Q(9),Q(7));b=Vec2(Q(1),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0162():
    a=Vec2(Q(10),Q(8));b=Vec2(Q(2),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0163():
    a=Vec2(Q(11),Q(9));b=Vec2(Q(3),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0164():
    a=Vec2(Q(12),Q(10));b=Vec2(Q(4),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0165():
    a=Vec2(Q(13),Q(11));b=Vec2(Q(5),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0166():
    a=Vec2(Q(14),Q(12));b=Vec2(Q(6),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0167():
    a=Vec2(Q(15),Q(13));b=Vec2(Q(7),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0168():
    a=Vec2(Q(16),Q(14));b=Vec2(Q(8),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0169():
    a=Vec2(Q(17),Q(2));b=Vec2(Q(9),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0170():
    a=Vec2(Q(1),Q(3));b=Vec2(Q(10),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0171():
    a=Vec2(Q(2),Q(4));b=Vec2(Q(11),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0172():
    a=Vec2(Q(3),Q(5));b=Vec2(Q(12),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0173():
    a=Vec2(Q(4),Q(6));b=Vec2(Q(13),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0174():
    a=Vec2(Q(5),Q(7));b=Vec2(Q(14),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0175():
    a=Vec2(Q(6),Q(8));b=Vec2(Q(15),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0176():
    a=Vec2(Q(7),Q(9));b=Vec2(Q(16),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0177():
    a=Vec2(Q(8),Q(10));b=Vec2(Q(17),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0178():
    a=Vec2(Q(9),Q(11));b=Vec2(Q(18),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0179():
    a=Vec2(Q(10),Q(12));b=Vec2(Q(19),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0180():
    a=Vec2(Q(11),Q(13));b=Vec2(Q(20),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0181():
    a=Vec2(Q(12),Q(14));b=Vec2(Q(21),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0182():
    a=Vec2(Q(13),Q(2));b=Vec2(Q(22),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0183():
    a=Vec2(Q(14),Q(3));b=Vec2(Q(23),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0184():
    a=Vec2(Q(15),Q(4));b=Vec2(Q(1),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0185():
    a=Vec2(Q(16),Q(5));b=Vec2(Q(2),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0186():
    a=Vec2(Q(17),Q(6));b=Vec2(Q(3),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0187():
    a=Vec2(Q(1),Q(7));b=Vec2(Q(4),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0188():
    a=Vec2(Q(2),Q(8));b=Vec2(Q(5),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0189():
    a=Vec2(Q(3),Q(9));b=Vec2(Q(6),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0190():
    a=Vec2(Q(4),Q(10));b=Vec2(Q(7),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0191():
    a=Vec2(Q(5),Q(11));b=Vec2(Q(8),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0192():
    a=Vec2(Q(6),Q(12));b=Vec2(Q(9),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0193():
    a=Vec2(Q(7),Q(13));b=Vec2(Q(10),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0194():
    a=Vec2(Q(8),Q(14));b=Vec2(Q(11),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0195():
    a=Vec2(Q(9),Q(2));b=Vec2(Q(12),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0196():
    a=Vec2(Q(10),Q(3));b=Vec2(Q(13),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0197():
    a=Vec2(Q(11),Q(4));b=Vec2(Q(14),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0198():
    a=Vec2(Q(12),Q(5));b=Vec2(Q(15),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0199():
    a=Vec2(Q(13),Q(6));b=Vec2(Q(16),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0200():
    a=Vec2(Q(14),Q(7));b=Vec2(Q(17),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0201():
    a=Vec2(Q(15),Q(8));b=Vec2(Q(18),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0202():
    a=Vec2(Q(16),Q(9));b=Vec2(Q(19),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0203():
    a=Vec2(Q(17),Q(10));b=Vec2(Q(20),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0204():
    a=Vec2(Q(1),Q(11));b=Vec2(Q(21),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0205():
    a=Vec2(Q(2),Q(12));b=Vec2(Q(22),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0206():
    a=Vec2(Q(3),Q(13));b=Vec2(Q(23),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0207():
    a=Vec2(Q(4),Q(14));b=Vec2(Q(1),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0208():
    a=Vec2(Q(5),Q(2));b=Vec2(Q(2),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0209():
    a=Vec2(Q(6),Q(3));b=Vec2(Q(3),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0210():
    a=Vec2(Q(7),Q(4));b=Vec2(Q(4),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0211():
    a=Vec2(Q(8),Q(5));b=Vec2(Q(5),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0212():
    a=Vec2(Q(9),Q(6));b=Vec2(Q(6),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0213():
    a=Vec2(Q(10),Q(7));b=Vec2(Q(7),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0214():
    a=Vec2(Q(11),Q(8));b=Vec2(Q(8),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0215():
    a=Vec2(Q(12),Q(9));b=Vec2(Q(9),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0216():
    a=Vec2(Q(13),Q(10));b=Vec2(Q(10),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0217():
    a=Vec2(Q(14),Q(11));b=Vec2(Q(11),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0218():
    a=Vec2(Q(15),Q(12));b=Vec2(Q(12),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0219():
    a=Vec2(Q(16),Q(13));b=Vec2(Q(13),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0220():
    a=Vec2(Q(17),Q(14));b=Vec2(Q(14),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0221():
    a=Vec2(Q(1),Q(2));b=Vec2(Q(15),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0222():
    a=Vec2(Q(2),Q(3));b=Vec2(Q(16),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0223():
    a=Vec2(Q(3),Q(4));b=Vec2(Q(17),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0224():
    a=Vec2(Q(4),Q(5));b=Vec2(Q(18),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0225():
    a=Vec2(Q(5),Q(6));b=Vec2(Q(19),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0226():
    a=Vec2(Q(6),Q(7));b=Vec2(Q(20),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0227():
    a=Vec2(Q(7),Q(8));b=Vec2(Q(21),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0228():
    a=Vec2(Q(8),Q(9));b=Vec2(Q(22),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0229():
    a=Vec2(Q(9),Q(10));b=Vec2(Q(23),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0230():
    a=Vec2(Q(10),Q(11));b=Vec2(Q(1),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0231():
    a=Vec2(Q(11),Q(12));b=Vec2(Q(2),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0232():
    a=Vec2(Q(12),Q(13));b=Vec2(Q(3),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0233():
    a=Vec2(Q(13),Q(14));b=Vec2(Q(4),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0234():
    a=Vec2(Q(14),Q(2));b=Vec2(Q(5),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0235():
    a=Vec2(Q(15),Q(3));b=Vec2(Q(6),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0236():
    a=Vec2(Q(16),Q(4));b=Vec2(Q(7),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0237():
    a=Vec2(Q(17),Q(5));b=Vec2(Q(8),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0238():
    a=Vec2(Q(1),Q(6));b=Vec2(Q(9),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0239():
    a=Vec2(Q(2),Q(7));b=Vec2(Q(10),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0240():
    a=Vec2(Q(3),Q(8));b=Vec2(Q(11),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0241():
    a=Vec2(Q(4),Q(9));b=Vec2(Q(12),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0242():
    a=Vec2(Q(5),Q(10));b=Vec2(Q(13),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0243():
    a=Vec2(Q(6),Q(11));b=Vec2(Q(14),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0244():
    a=Vec2(Q(7),Q(12));b=Vec2(Q(15),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0245():
    a=Vec2(Q(8),Q(13));b=Vec2(Q(16),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0246():
    a=Vec2(Q(9),Q(14));b=Vec2(Q(17),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0247():
    a=Vec2(Q(10),Q(2));b=Vec2(Q(18),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0248():
    a=Vec2(Q(11),Q(3));b=Vec2(Q(19),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0249():
    a=Vec2(Q(12),Q(4));b=Vec2(Q(20),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0250():
    a=Vec2(Q(13),Q(5));b=Vec2(Q(21),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0251():
    a=Vec2(Q(14),Q(6));b=Vec2(Q(22),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0252():
    a=Vec2(Q(15),Q(7));b=Vec2(Q(23),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0253():
    a=Vec2(Q(16),Q(8));b=Vec2(Q(1),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0254():
    a=Vec2(Q(17),Q(9));b=Vec2(Q(2),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0255():
    a=Vec2(Q(1),Q(10));b=Vec2(Q(3),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0256():
    a=Vec2(Q(2),Q(11));b=Vec2(Q(4),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0257():
    a=Vec2(Q(3),Q(12));b=Vec2(Q(5),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0258():
    a=Vec2(Q(4),Q(13));b=Vec2(Q(6),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0259():
    a=Vec2(Q(5),Q(14));b=Vec2(Q(7),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0260():
    a=Vec2(Q(6),Q(2));b=Vec2(Q(8),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0261():
    a=Vec2(Q(7),Q(3));b=Vec2(Q(9),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0262():
    a=Vec2(Q(8),Q(4));b=Vec2(Q(10),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0263():
    a=Vec2(Q(9),Q(5));b=Vec2(Q(11),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0264():
    a=Vec2(Q(10),Q(6));b=Vec2(Q(12),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0265():
    a=Vec2(Q(11),Q(7));b=Vec2(Q(13),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0266():
    a=Vec2(Q(12),Q(8));b=Vec2(Q(14),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0267():
    a=Vec2(Q(13),Q(9));b=Vec2(Q(15),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0268():
    a=Vec2(Q(14),Q(10));b=Vec2(Q(16),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0269():
    a=Vec2(Q(15),Q(11));b=Vec2(Q(17),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0270():
    a=Vec2(Q(16),Q(12));b=Vec2(Q(18),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0271():
    a=Vec2(Q(17),Q(13));b=Vec2(Q(19),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0272():
    a=Vec2(Q(1),Q(14));b=Vec2(Q(20),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0273():
    a=Vec2(Q(2),Q(2));b=Vec2(Q(21),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0274():
    a=Vec2(Q(3),Q(3));b=Vec2(Q(22),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0275():
    a=Vec2(Q(4),Q(4));b=Vec2(Q(23),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0276():
    a=Vec2(Q(5),Q(5));b=Vec2(Q(1),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0277():
    a=Vec2(Q(6),Q(6));b=Vec2(Q(2),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0278():
    a=Vec2(Q(7),Q(7));b=Vec2(Q(3),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0279():
    a=Vec2(Q(8),Q(8));b=Vec2(Q(4),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0280():
    a=Vec2(Q(9),Q(9));b=Vec2(Q(5),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0281():
    a=Vec2(Q(10),Q(10));b=Vec2(Q(6),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0282():
    a=Vec2(Q(11),Q(11));b=Vec2(Q(7),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0283():
    a=Vec2(Q(12),Q(12));b=Vec2(Q(8),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0284():
    a=Vec2(Q(13),Q(13));b=Vec2(Q(9),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0285():
    a=Vec2(Q(14),Q(14));b=Vec2(Q(10),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0286():
    a=Vec2(Q(15),Q(2));b=Vec2(Q(11),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0287():
    a=Vec2(Q(16),Q(3));b=Vec2(Q(12),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0288():
    a=Vec2(Q(17),Q(4));b=Vec2(Q(13),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0289():
    a=Vec2(Q(1),Q(5));b=Vec2(Q(14),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0290():
    a=Vec2(Q(2),Q(6));b=Vec2(Q(15),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0291():
    a=Vec2(Q(3),Q(7));b=Vec2(Q(16),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0292():
    a=Vec2(Q(4),Q(8));b=Vec2(Q(17),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0293():
    a=Vec2(Q(5),Q(9));b=Vec2(Q(18),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0294():
    a=Vec2(Q(6),Q(10));b=Vec2(Q(19),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0295():
    a=Vec2(Q(7),Q(11));b=Vec2(Q(20),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0296():
    a=Vec2(Q(8),Q(12));b=Vec2(Q(21),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0297():
    a=Vec2(Q(9),Q(13));b=Vec2(Q(22),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0298():
    a=Vec2(Q(10),Q(14));b=Vec2(Q(23),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0299():
    a=Vec2(Q(11),Q(2));b=Vec2(Q(1),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0300():
    a=Vec2(Q(12),Q(3));b=Vec2(Q(2),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0301():
    a=Vec2(Q(13),Q(4));b=Vec2(Q(3),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0302():
    a=Vec2(Q(14),Q(5));b=Vec2(Q(4),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0303():
    a=Vec2(Q(15),Q(6));b=Vec2(Q(5),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0304():
    a=Vec2(Q(16),Q(7));b=Vec2(Q(6),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0305():
    a=Vec2(Q(17),Q(8));b=Vec2(Q(7),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0306():
    a=Vec2(Q(1),Q(9));b=Vec2(Q(8),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0307():
    a=Vec2(Q(2),Q(10));b=Vec2(Q(9),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0308():
    a=Vec2(Q(3),Q(11));b=Vec2(Q(10),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0309():
    a=Vec2(Q(4),Q(12));b=Vec2(Q(11),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0310():
    a=Vec2(Q(5),Q(13));b=Vec2(Q(12),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0311():
    a=Vec2(Q(6),Q(14));b=Vec2(Q(13),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0312():
    a=Vec2(Q(7),Q(2));b=Vec2(Q(14),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0313():
    a=Vec2(Q(8),Q(3));b=Vec2(Q(15),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0314():
    a=Vec2(Q(9),Q(4));b=Vec2(Q(16),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0315():
    a=Vec2(Q(10),Q(5));b=Vec2(Q(17),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0316():
    a=Vec2(Q(11),Q(6));b=Vec2(Q(18),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0317():
    a=Vec2(Q(12),Q(7));b=Vec2(Q(19),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0318():
    a=Vec2(Q(13),Q(8));b=Vec2(Q(20),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0319():
    a=Vec2(Q(14),Q(9));b=Vec2(Q(21),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0320():
    a=Vec2(Q(15),Q(10));b=Vec2(Q(22),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0321():
    a=Vec2(Q(16),Q(11));b=Vec2(Q(23),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0322():
    a=Vec2(Q(17),Q(12));b=Vec2(Q(1),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0323():
    a=Vec2(Q(1),Q(13));b=Vec2(Q(2),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0324():
    a=Vec2(Q(2),Q(14));b=Vec2(Q(3),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0325():
    a=Vec2(Q(3),Q(2));b=Vec2(Q(4),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0326():
    a=Vec2(Q(4),Q(3));b=Vec2(Q(5),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0327():
    a=Vec2(Q(5),Q(4));b=Vec2(Q(6),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0328():
    a=Vec2(Q(6),Q(5));b=Vec2(Q(7),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0329():
    a=Vec2(Q(7),Q(6));b=Vec2(Q(8),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0330():
    a=Vec2(Q(8),Q(7));b=Vec2(Q(9),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0331():
    a=Vec2(Q(9),Q(8));b=Vec2(Q(10),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0332():
    a=Vec2(Q(10),Q(9));b=Vec2(Q(11),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0333():
    a=Vec2(Q(11),Q(10));b=Vec2(Q(12),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0334():
    a=Vec2(Q(12),Q(11));b=Vec2(Q(13),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0335():
    a=Vec2(Q(13),Q(12));b=Vec2(Q(14),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0336():
    a=Vec2(Q(14),Q(13));b=Vec2(Q(15),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0337():
    a=Vec2(Q(15),Q(14));b=Vec2(Q(16),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0338():
    a=Vec2(Q(16),Q(2));b=Vec2(Q(17),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0339():
    a=Vec2(Q(17),Q(3));b=Vec2(Q(18),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0340():
    a=Vec2(Q(1),Q(4));b=Vec2(Q(19),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0341():
    a=Vec2(Q(2),Q(5));b=Vec2(Q(20),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0342():
    a=Vec2(Q(3),Q(6));b=Vec2(Q(21),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0343():
    a=Vec2(Q(4),Q(7));b=Vec2(Q(22),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0344():
    a=Vec2(Q(5),Q(8));b=Vec2(Q(23),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0345():
    a=Vec2(Q(6),Q(9));b=Vec2(Q(1),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0346():
    a=Vec2(Q(7),Q(10));b=Vec2(Q(2),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0347():
    a=Vec2(Q(8),Q(11));b=Vec2(Q(3),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0348():
    a=Vec2(Q(9),Q(12));b=Vec2(Q(4),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0349():
    a=Vec2(Q(10),Q(13));b=Vec2(Q(5),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0350():
    a=Vec2(Q(11),Q(14));b=Vec2(Q(6),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0351():
    a=Vec2(Q(12),Q(2));b=Vec2(Q(7),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0352():
    a=Vec2(Q(13),Q(3));b=Vec2(Q(8),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0353():
    a=Vec2(Q(14),Q(4));b=Vec2(Q(9),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0354():
    a=Vec2(Q(15),Q(5));b=Vec2(Q(10),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0355():
    a=Vec2(Q(16),Q(6));b=Vec2(Q(11),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0356():
    a=Vec2(Q(17),Q(7));b=Vec2(Q(12),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0357():
    a=Vec2(Q(1),Q(8));b=Vec2(Q(13),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0358():
    a=Vec2(Q(2),Q(9));b=Vec2(Q(14),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0359():
    a=Vec2(Q(3),Q(10));b=Vec2(Q(15),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0360():
    a=Vec2(Q(4),Q(11));b=Vec2(Q(16),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0361():
    a=Vec2(Q(5),Q(12));b=Vec2(Q(17),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0362():
    a=Vec2(Q(6),Q(13));b=Vec2(Q(18),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0363():
    a=Vec2(Q(7),Q(14));b=Vec2(Q(19),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0364():
    a=Vec2(Q(8),Q(2));b=Vec2(Q(20),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0365():
    a=Vec2(Q(9),Q(3));b=Vec2(Q(21),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0366():
    a=Vec2(Q(10),Q(4));b=Vec2(Q(22),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0367():
    a=Vec2(Q(11),Q(5));b=Vec2(Q(23),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0368():
    a=Vec2(Q(12),Q(6));b=Vec2(Q(1),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0369():
    a=Vec2(Q(13),Q(7));b=Vec2(Q(2),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0370():
    a=Vec2(Q(14),Q(8));b=Vec2(Q(3),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0371():
    a=Vec2(Q(15),Q(9));b=Vec2(Q(4),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0372():
    a=Vec2(Q(16),Q(10));b=Vec2(Q(5),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0373():
    a=Vec2(Q(17),Q(11));b=Vec2(Q(6),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0374():
    a=Vec2(Q(1),Q(12));b=Vec2(Q(7),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0375():
    a=Vec2(Q(2),Q(13));b=Vec2(Q(8),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0376():
    a=Vec2(Q(3),Q(14));b=Vec2(Q(9),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0377():
    a=Vec2(Q(4),Q(2));b=Vec2(Q(10),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0378():
    a=Vec2(Q(5),Q(3));b=Vec2(Q(11),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0379():
    a=Vec2(Q(6),Q(4));b=Vec2(Q(12),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0380():
    a=Vec2(Q(7),Q(5));b=Vec2(Q(13),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0381():
    a=Vec2(Q(8),Q(6));b=Vec2(Q(14),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0382():
    a=Vec2(Q(9),Q(7));b=Vec2(Q(15),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0383():
    a=Vec2(Q(10),Q(8));b=Vec2(Q(16),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0384():
    a=Vec2(Q(11),Q(9));b=Vec2(Q(17),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0385():
    a=Vec2(Q(12),Q(10));b=Vec2(Q(18),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0386():
    a=Vec2(Q(13),Q(11));b=Vec2(Q(19),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0387():
    a=Vec2(Q(14),Q(12));b=Vec2(Q(20),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0388():
    a=Vec2(Q(15),Q(13));b=Vec2(Q(21),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0389():
    a=Vec2(Q(16),Q(14));b=Vec2(Q(22),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0390():
    a=Vec2(Q(17),Q(2));b=Vec2(Q(23),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0391():
    a=Vec2(Q(1),Q(3));b=Vec2(Q(1),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0392():
    a=Vec2(Q(2),Q(4));b=Vec2(Q(2),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0393():
    a=Vec2(Q(3),Q(5));b=Vec2(Q(3),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0394():
    a=Vec2(Q(4),Q(6));b=Vec2(Q(4),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0395():
    a=Vec2(Q(5),Q(7));b=Vec2(Q(5),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0396():
    a=Vec2(Q(6),Q(8));b=Vec2(Q(6),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0397():
    a=Vec2(Q(7),Q(9));b=Vec2(Q(7),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0398():
    a=Vec2(Q(8),Q(10));b=Vec2(Q(8),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0399():
    a=Vec2(Q(9),Q(11));b=Vec2(Q(9),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0400():
    a=Vec2(Q(10),Q(12));b=Vec2(Q(10),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0401():
    a=Vec2(Q(11),Q(13));b=Vec2(Q(11),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0402():
    a=Vec2(Q(12),Q(14));b=Vec2(Q(12),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0403():
    a=Vec2(Q(13),Q(2));b=Vec2(Q(13),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0404():
    a=Vec2(Q(14),Q(3));b=Vec2(Q(14),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0405():
    a=Vec2(Q(15),Q(4));b=Vec2(Q(15),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0406():
    a=Vec2(Q(16),Q(5));b=Vec2(Q(16),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0407():
    a=Vec2(Q(17),Q(6));b=Vec2(Q(17),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0408():
    a=Vec2(Q(1),Q(7));b=Vec2(Q(18),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0409():
    a=Vec2(Q(2),Q(8));b=Vec2(Q(19),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0410():
    a=Vec2(Q(3),Q(9));b=Vec2(Q(20),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0411():
    a=Vec2(Q(4),Q(10));b=Vec2(Q(21),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0412():
    a=Vec2(Q(5),Q(11));b=Vec2(Q(22),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0413():
    a=Vec2(Q(6),Q(12));b=Vec2(Q(23),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0414():
    a=Vec2(Q(7),Q(13));b=Vec2(Q(1),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0415():
    a=Vec2(Q(8),Q(14));b=Vec2(Q(2),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0416():
    a=Vec2(Q(9),Q(2));b=Vec2(Q(3),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0417():
    a=Vec2(Q(10),Q(3));b=Vec2(Q(4),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0418():
    a=Vec2(Q(11),Q(4));b=Vec2(Q(5),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0419():
    a=Vec2(Q(12),Q(5));b=Vec2(Q(6),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0420():
    a=Vec2(Q(13),Q(6));b=Vec2(Q(7),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0421():
    a=Vec2(Q(14),Q(7));b=Vec2(Q(8),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0422():
    a=Vec2(Q(15),Q(8));b=Vec2(Q(9),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0423():
    a=Vec2(Q(16),Q(9));b=Vec2(Q(10),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0424():
    a=Vec2(Q(17),Q(10));b=Vec2(Q(11),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0425():
    a=Vec2(Q(1),Q(11));b=Vec2(Q(12),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0426():
    a=Vec2(Q(2),Q(12));b=Vec2(Q(13),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0427():
    a=Vec2(Q(3),Q(13));b=Vec2(Q(14),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0428():
    a=Vec2(Q(4),Q(14));b=Vec2(Q(15),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0429():
    a=Vec2(Q(5),Q(2));b=Vec2(Q(16),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0430():
    a=Vec2(Q(6),Q(3));b=Vec2(Q(17),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0431():
    a=Vec2(Q(7),Q(4));b=Vec2(Q(18),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0432():
    a=Vec2(Q(8),Q(5));b=Vec2(Q(19),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0433():
    a=Vec2(Q(9),Q(6));b=Vec2(Q(20),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0434():
    a=Vec2(Q(10),Q(7));b=Vec2(Q(21),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0435():
    a=Vec2(Q(11),Q(8));b=Vec2(Q(22),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0436():
    a=Vec2(Q(12),Q(9));b=Vec2(Q(23),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0437():
    a=Vec2(Q(13),Q(10));b=Vec2(Q(1),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0438():
    a=Vec2(Q(14),Q(11));b=Vec2(Q(2),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0439():
    a=Vec2(Q(15),Q(12));b=Vec2(Q(3),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0440():
    a=Vec2(Q(16),Q(13));b=Vec2(Q(4),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0441():
    a=Vec2(Q(17),Q(14));b=Vec2(Q(5),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0442():
    a=Vec2(Q(1),Q(2));b=Vec2(Q(6),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0443():
    a=Vec2(Q(2),Q(3));b=Vec2(Q(7),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0444():
    a=Vec2(Q(3),Q(4));b=Vec2(Q(8),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0445():
    a=Vec2(Q(4),Q(5));b=Vec2(Q(9),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0446():
    a=Vec2(Q(5),Q(6));b=Vec2(Q(10),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0447():
    a=Vec2(Q(6),Q(7));b=Vec2(Q(11),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0448():
    a=Vec2(Q(7),Q(8));b=Vec2(Q(12),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0449():
    a=Vec2(Q(8),Q(9));b=Vec2(Q(13),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0450():
    a=Vec2(Q(9),Q(10));b=Vec2(Q(14),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0451():
    a=Vec2(Q(10),Q(11));b=Vec2(Q(15),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0452():
    a=Vec2(Q(11),Q(12));b=Vec2(Q(16),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0453():
    a=Vec2(Q(12),Q(13));b=Vec2(Q(17),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0454():
    a=Vec2(Q(13),Q(14));b=Vec2(Q(18),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0455():
    a=Vec2(Q(14),Q(2));b=Vec2(Q(19),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0456():
    a=Vec2(Q(15),Q(3));b=Vec2(Q(20),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0457():
    a=Vec2(Q(16),Q(4));b=Vec2(Q(21),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0458():
    a=Vec2(Q(17),Q(5));b=Vec2(Q(22),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0459():
    a=Vec2(Q(1),Q(6));b=Vec2(Q(23),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0460():
    a=Vec2(Q(2),Q(7));b=Vec2(Q(1),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0461():
    a=Vec2(Q(3),Q(8));b=Vec2(Q(2),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0462():
    a=Vec2(Q(4),Q(9));b=Vec2(Q(3),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0463():
    a=Vec2(Q(5),Q(10));b=Vec2(Q(4),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0464():
    a=Vec2(Q(6),Q(11));b=Vec2(Q(5),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0465():
    a=Vec2(Q(7),Q(12));b=Vec2(Q(6),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0466():
    a=Vec2(Q(8),Q(13));b=Vec2(Q(7),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0467():
    a=Vec2(Q(9),Q(14));b=Vec2(Q(8),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0468():
    a=Vec2(Q(10),Q(2));b=Vec2(Q(9),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0469():
    a=Vec2(Q(11),Q(3));b=Vec2(Q(10),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0470():
    a=Vec2(Q(12),Q(4));b=Vec2(Q(11),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0471():
    a=Vec2(Q(13),Q(5));b=Vec2(Q(12),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0472():
    a=Vec2(Q(14),Q(6));b=Vec2(Q(13),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0473():
    a=Vec2(Q(15),Q(7));b=Vec2(Q(14),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0474():
    a=Vec2(Q(16),Q(8));b=Vec2(Q(15),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0475():
    a=Vec2(Q(17),Q(9));b=Vec2(Q(16),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0476():
    a=Vec2(Q(1),Q(10));b=Vec2(Q(17),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0477():
    a=Vec2(Q(2),Q(11));b=Vec2(Q(18),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0478():
    a=Vec2(Q(3),Q(12));b=Vec2(Q(19),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0479():
    a=Vec2(Q(4),Q(13));b=Vec2(Q(20),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0480():
    a=Vec2(Q(5),Q(14));b=Vec2(Q(21),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0481():
    a=Vec2(Q(6),Q(2));b=Vec2(Q(22),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0482():
    a=Vec2(Q(7),Q(3));b=Vec2(Q(23),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0483():
    a=Vec2(Q(8),Q(4));b=Vec2(Q(1),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0484():
    a=Vec2(Q(9),Q(5));b=Vec2(Q(2),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0485():
    a=Vec2(Q(10),Q(6));b=Vec2(Q(3),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0486():
    a=Vec2(Q(11),Q(7));b=Vec2(Q(4),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0487():
    a=Vec2(Q(12),Q(8));b=Vec2(Q(5),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0488():
    a=Vec2(Q(13),Q(9));b=Vec2(Q(6),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0489():
    a=Vec2(Q(14),Q(10));b=Vec2(Q(7),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0490():
    a=Vec2(Q(15),Q(11));b=Vec2(Q(8),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0491():
    a=Vec2(Q(16),Q(12));b=Vec2(Q(9),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0492():
    a=Vec2(Q(17),Q(13));b=Vec2(Q(10),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0493():
    a=Vec2(Q(1),Q(14));b=Vec2(Q(11),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0494():
    a=Vec2(Q(2),Q(2));b=Vec2(Q(12),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0495():
    a=Vec2(Q(3),Q(3));b=Vec2(Q(13),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0496():
    a=Vec2(Q(4),Q(4));b=Vec2(Q(14),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0497():
    a=Vec2(Q(5),Q(5));b=Vec2(Q(15),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0498():
    a=Vec2(Q(6),Q(6));b=Vec2(Q(16),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0499():
    a=Vec2(Q(7),Q(7));b=Vec2(Q(17),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0500():
    a=Vec2(Q(8),Q(8));b=Vec2(Q(18),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0501():
    a=Vec2(Q(9),Q(9));b=Vec2(Q(19),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0502():
    a=Vec2(Q(10),Q(10));b=Vec2(Q(20),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0503():
    a=Vec2(Q(11),Q(11));b=Vec2(Q(21),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0504():
    a=Vec2(Q(12),Q(12));b=Vec2(Q(22),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0505():
    a=Vec2(Q(13),Q(13));b=Vec2(Q(23),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0506():
    a=Vec2(Q(14),Q(14));b=Vec2(Q(1),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0507():
    a=Vec2(Q(15),Q(2));b=Vec2(Q(2),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0508():
    a=Vec2(Q(16),Q(3));b=Vec2(Q(3),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0509():
    a=Vec2(Q(17),Q(4));b=Vec2(Q(4),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0510():
    a=Vec2(Q(1),Q(5));b=Vec2(Q(5),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0511():
    a=Vec2(Q(2),Q(6));b=Vec2(Q(6),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0512():
    a=Vec2(Q(3),Q(7));b=Vec2(Q(7),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0513():
    a=Vec2(Q(4),Q(8));b=Vec2(Q(8),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0514():
    a=Vec2(Q(5),Q(9));b=Vec2(Q(9),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0515():
    a=Vec2(Q(6),Q(10));b=Vec2(Q(10),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0516():
    a=Vec2(Q(7),Q(11));b=Vec2(Q(11),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0517():
    a=Vec2(Q(8),Q(12));b=Vec2(Q(12),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0518():
    a=Vec2(Q(9),Q(13));b=Vec2(Q(13),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0519():
    a=Vec2(Q(10),Q(14));b=Vec2(Q(14),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0520():
    a=Vec2(Q(11),Q(2));b=Vec2(Q(15),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0521():
    a=Vec2(Q(12),Q(3));b=Vec2(Q(16),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0522():
    a=Vec2(Q(13),Q(4));b=Vec2(Q(17),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0523():
    a=Vec2(Q(14),Q(5));b=Vec2(Q(18),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0524():
    a=Vec2(Q(15),Q(6));b=Vec2(Q(19),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0525():
    a=Vec2(Q(16),Q(7));b=Vec2(Q(20),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0526():
    a=Vec2(Q(17),Q(8));b=Vec2(Q(21),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0527():
    a=Vec2(Q(1),Q(9));b=Vec2(Q(22),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0528():
    a=Vec2(Q(2),Q(10));b=Vec2(Q(23),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0529():
    a=Vec2(Q(3),Q(11));b=Vec2(Q(1),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0530():
    a=Vec2(Q(4),Q(12));b=Vec2(Q(2),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0531():
    a=Vec2(Q(5),Q(13));b=Vec2(Q(3),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0532():
    a=Vec2(Q(6),Q(14));b=Vec2(Q(4),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0533():
    a=Vec2(Q(7),Q(2));b=Vec2(Q(5),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0534():
    a=Vec2(Q(8),Q(3));b=Vec2(Q(6),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0535():
    a=Vec2(Q(9),Q(4));b=Vec2(Q(7),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0536():
    a=Vec2(Q(10),Q(5));b=Vec2(Q(8),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0537():
    a=Vec2(Q(11),Q(6));b=Vec2(Q(9),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0538():
    a=Vec2(Q(12),Q(7));b=Vec2(Q(10),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0539():
    a=Vec2(Q(13),Q(8));b=Vec2(Q(11),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0540():
    a=Vec2(Q(14),Q(9));b=Vec2(Q(12),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0541():
    a=Vec2(Q(15),Q(10));b=Vec2(Q(13),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0542():
    a=Vec2(Q(16),Q(11));b=Vec2(Q(14),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0543():
    a=Vec2(Q(17),Q(12));b=Vec2(Q(15),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0544():
    a=Vec2(Q(1),Q(13));b=Vec2(Q(16),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0545():
    a=Vec2(Q(2),Q(14));b=Vec2(Q(17),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0546():
    a=Vec2(Q(3),Q(2));b=Vec2(Q(18),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0547():
    a=Vec2(Q(4),Q(3));b=Vec2(Q(19),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0548():
    a=Vec2(Q(5),Q(4));b=Vec2(Q(20),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0549():
    a=Vec2(Q(6),Q(5));b=Vec2(Q(21),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0550():
    a=Vec2(Q(7),Q(6));b=Vec2(Q(22),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0551():
    a=Vec2(Q(8),Q(7));b=Vec2(Q(23),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0552():
    a=Vec2(Q(9),Q(8));b=Vec2(Q(1),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0553():
    a=Vec2(Q(10),Q(9));b=Vec2(Q(2),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0554():
    a=Vec2(Q(11),Q(10));b=Vec2(Q(3),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0555():
    a=Vec2(Q(12),Q(11));b=Vec2(Q(4),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0556():
    a=Vec2(Q(13),Q(12));b=Vec2(Q(5),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0557():
    a=Vec2(Q(14),Q(13));b=Vec2(Q(6),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0558():
    a=Vec2(Q(15),Q(14));b=Vec2(Q(7),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0559():
    a=Vec2(Q(16),Q(2));b=Vec2(Q(8),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0560():
    a=Vec2(Q(17),Q(3));b=Vec2(Q(9),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0561():
    a=Vec2(Q(1),Q(4));b=Vec2(Q(10),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0562():
    a=Vec2(Q(2),Q(5));b=Vec2(Q(11),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0563():
    a=Vec2(Q(3),Q(6));b=Vec2(Q(12),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0564():
    a=Vec2(Q(4),Q(7));b=Vec2(Q(13),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0565():
    a=Vec2(Q(5),Q(8));b=Vec2(Q(14),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0566():
    a=Vec2(Q(6),Q(9));b=Vec2(Q(15),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0567():
    a=Vec2(Q(7),Q(10));b=Vec2(Q(16),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0568():
    a=Vec2(Q(8),Q(11));b=Vec2(Q(17),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0569():
    a=Vec2(Q(9),Q(12));b=Vec2(Q(18),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0570():
    a=Vec2(Q(10),Q(13));b=Vec2(Q(19),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0571():
    a=Vec2(Q(11),Q(14));b=Vec2(Q(20),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0572():
    a=Vec2(Q(12),Q(2));b=Vec2(Q(21),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0573():
    a=Vec2(Q(13),Q(3));b=Vec2(Q(22),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0574():
    a=Vec2(Q(14),Q(4));b=Vec2(Q(23),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0575():
    a=Vec2(Q(15),Q(5));b=Vec2(Q(1),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0576():
    a=Vec2(Q(16),Q(6));b=Vec2(Q(2),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0577():
    a=Vec2(Q(17),Q(7));b=Vec2(Q(3),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0578():
    a=Vec2(Q(1),Q(8));b=Vec2(Q(4),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0579():
    a=Vec2(Q(2),Q(9));b=Vec2(Q(5),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0580():
    a=Vec2(Q(3),Q(10));b=Vec2(Q(6),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0581():
    a=Vec2(Q(4),Q(11));b=Vec2(Q(7),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0582():
    a=Vec2(Q(5),Q(12));b=Vec2(Q(8),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0583():
    a=Vec2(Q(6),Q(13));b=Vec2(Q(9),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0584():
    a=Vec2(Q(7),Q(14));b=Vec2(Q(10),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0585():
    a=Vec2(Q(8),Q(2));b=Vec2(Q(11),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0586():
    a=Vec2(Q(9),Q(3));b=Vec2(Q(12),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0587():
    a=Vec2(Q(10),Q(4));b=Vec2(Q(13),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0588():
    a=Vec2(Q(11),Q(5));b=Vec2(Q(14),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0589():
    a=Vec2(Q(12),Q(6));b=Vec2(Q(15),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0590():
    a=Vec2(Q(13),Q(7));b=Vec2(Q(16),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0591():
    a=Vec2(Q(14),Q(8));b=Vec2(Q(17),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0592():
    a=Vec2(Q(15),Q(9));b=Vec2(Q(18),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0593():
    a=Vec2(Q(16),Q(10));b=Vec2(Q(19),Q(6))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0594():
    a=Vec2(Q(17),Q(11));b=Vec2(Q(20),Q(7))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0595():
    a=Vec2(Q(1),Q(12));b=Vec2(Q(21),Q(1))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0596():
    a=Vec2(Q(2),Q(13));b=Vec2(Q(22),Q(2))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0597():
    a=Vec2(Q(3),Q(14));b=Vec2(Q(23),Q(3))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0598():
    a=Vec2(Q(4),Q(2));b=Vec2(Q(1),Q(4))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

def test_vector_midpoint_0599():
    a=Vec2(Q(5),Q(3));b=Vec2(Q(2),Q(5))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m

