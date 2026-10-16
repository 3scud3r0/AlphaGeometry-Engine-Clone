# GENERATED, DETERMINISTIC, NO TRAINED MODEL USED.
# Source generator: geoforge_upgrade_suite/generate_untrained_matrix.py
from fractions import Fraction as Q
from geoforge_upgrade_suite.geometry_exact import Vec2,Polynomial,Line
from geoforge_upgrade_suite.exact_constructions import SPoint,foot,line_intersection
from geoforge_upgrade_suite.deterministic_ideal import ExactIdealEngine,certificate_to_json,verify_certificate_json
from geoforge_upgrade_suite.deterministic_solver import ExactFactEvaluator,GuardLedger

def test_equal_lengths_0000():
    a=Vec2(Q(1),Q(2));b=Vec2(Q(2),Q(3))
    c=a+Vec2(Q(1),Q(-1));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0001():
    a=Vec2(Q(2),Q(3));b=Vec2(Q(4),Q(5))
    c=a+Vec2(Q(2),Q(-2));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0002():
    a=Vec2(Q(3),Q(4));b=Vec2(Q(6),Q(7))
    c=a+Vec2(Q(3),Q(-3));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0003():
    a=Vec2(Q(4),Q(5));b=Vec2(Q(8),Q(9))
    c=a+Vec2(Q(4),Q(-4));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0004():
    a=Vec2(Q(5),Q(6));b=Vec2(Q(10),Q(11))
    c=a+Vec2(Q(5),Q(-5));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0005():
    a=Vec2(Q(6),Q(7));b=Vec2(Q(12),Q(13))
    c=a+Vec2(Q(6),Q(-6));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0006():
    a=Vec2(Q(7),Q(8));b=Vec2(Q(14),Q(15))
    c=a+Vec2(Q(7),Q(-7));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0007():
    a=Vec2(Q(8),Q(9));b=Vec2(Q(16),Q(10))
    c=a+Vec2(Q(1),Q(-8));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0008():
    a=Vec2(Q(9),Q(10));b=Vec2(Q(18),Q(12))
    c=a+Vec2(Q(2),Q(-9));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0009():
    a=Vec2(Q(10),Q(11));b=Vec2(Q(20),Q(14))
    c=a+Vec2(Q(3),Q(-10));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0010():
    a=Vec2(Q(11),Q(12));b=Vec2(Q(22),Q(16))
    c=a+Vec2(Q(4),Q(-11));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0011():
    a=Vec2(Q(12),Q(13));b=Vec2(Q(24),Q(18))
    c=a+Vec2(Q(5),Q(-12));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0012():
    a=Vec2(Q(13),Q(14));b=Vec2(Q(26),Q(20))
    c=a+Vec2(Q(6),Q(-13));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0013():
    a=Vec2(Q(14),Q(2));b=Vec2(Q(28),Q(9))
    c=a+Vec2(Q(7),Q(-14));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0014():
    a=Vec2(Q(15),Q(3));b=Vec2(Q(30),Q(4))
    c=a+Vec2(Q(1),Q(-15));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0015():
    a=Vec2(Q(16),Q(4));b=Vec2(Q(32),Q(6))
    c=a+Vec2(Q(2),Q(-16));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0016():
    a=Vec2(Q(17),Q(5));b=Vec2(Q(34),Q(8))
    c=a+Vec2(Q(3),Q(-17));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0017():
    a=Vec2(Q(1),Q(6));b=Vec2(Q(19),Q(10))
    c=a+Vec2(Q(4),Q(-18));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0018():
    a=Vec2(Q(2),Q(7));b=Vec2(Q(21),Q(12))
    c=a+Vec2(Q(5),Q(-19));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0019():
    a=Vec2(Q(3),Q(8));b=Vec2(Q(23),Q(14))
    c=a+Vec2(Q(6),Q(-20));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0020():
    a=Vec2(Q(4),Q(9));b=Vec2(Q(25),Q(16))
    c=a+Vec2(Q(7),Q(-21));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0021():
    a=Vec2(Q(5),Q(10));b=Vec2(Q(27),Q(11))
    c=a+Vec2(Q(1),Q(-22));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0022():
    a=Vec2(Q(6),Q(11));b=Vec2(Q(29),Q(13))
    c=a+Vec2(Q(2),Q(-23));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0023():
    a=Vec2(Q(7),Q(12));b=Vec2(Q(8),Q(15))
    c=a+Vec2(Q(3),Q(-1));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0024():
    a=Vec2(Q(8),Q(13));b=Vec2(Q(10),Q(17))
    c=a+Vec2(Q(4),Q(-2));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0025():
    a=Vec2(Q(9),Q(14));b=Vec2(Q(12),Q(19))
    c=a+Vec2(Q(5),Q(-3));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0026():
    a=Vec2(Q(10),Q(2));b=Vec2(Q(14),Q(8))
    c=a+Vec2(Q(6),Q(-4));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0027():
    a=Vec2(Q(11),Q(3));b=Vec2(Q(16),Q(10))
    c=a+Vec2(Q(7),Q(-5));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0028():
    a=Vec2(Q(12),Q(4));b=Vec2(Q(18),Q(5))
    c=a+Vec2(Q(1),Q(-6));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0029():
    a=Vec2(Q(13),Q(5));b=Vec2(Q(20),Q(7))
    c=a+Vec2(Q(2),Q(-7));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0030():
    a=Vec2(Q(14),Q(6));b=Vec2(Q(22),Q(9))
    c=a+Vec2(Q(3),Q(-8));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0031():
    a=Vec2(Q(15),Q(7));b=Vec2(Q(24),Q(11))
    c=a+Vec2(Q(4),Q(-9));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0032():
    a=Vec2(Q(16),Q(8));b=Vec2(Q(26),Q(13))
    c=a+Vec2(Q(5),Q(-10));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0033():
    a=Vec2(Q(17),Q(9));b=Vec2(Q(28),Q(15))
    c=a+Vec2(Q(6),Q(-11));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0034():
    a=Vec2(Q(1),Q(10));b=Vec2(Q(13),Q(17))
    c=a+Vec2(Q(7),Q(-12));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0035():
    a=Vec2(Q(2),Q(11));b=Vec2(Q(15),Q(12))
    c=a+Vec2(Q(1),Q(-13));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0036():
    a=Vec2(Q(3),Q(12));b=Vec2(Q(17),Q(14))
    c=a+Vec2(Q(2),Q(-14));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0037():
    a=Vec2(Q(4),Q(13));b=Vec2(Q(19),Q(16))
    c=a+Vec2(Q(3),Q(-15));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0038():
    a=Vec2(Q(5),Q(14));b=Vec2(Q(21),Q(18))
    c=a+Vec2(Q(4),Q(-16));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0039():
    a=Vec2(Q(6),Q(2));b=Vec2(Q(23),Q(7))
    c=a+Vec2(Q(5),Q(-17));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0040():
    a=Vec2(Q(7),Q(3));b=Vec2(Q(25),Q(9))
    c=a+Vec2(Q(6),Q(-18));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0041():
    a=Vec2(Q(8),Q(4));b=Vec2(Q(27),Q(11))
    c=a+Vec2(Q(7),Q(-19));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0042():
    a=Vec2(Q(9),Q(5));b=Vec2(Q(29),Q(6))
    c=a+Vec2(Q(1),Q(-20));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0043():
    a=Vec2(Q(10),Q(6));b=Vec2(Q(31),Q(8))
    c=a+Vec2(Q(2),Q(-21));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0044():
    a=Vec2(Q(11),Q(7));b=Vec2(Q(33),Q(10))
    c=a+Vec2(Q(3),Q(-22));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0045():
    a=Vec2(Q(12),Q(8));b=Vec2(Q(35),Q(12))
    c=a+Vec2(Q(4),Q(-23));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0046():
    a=Vec2(Q(13),Q(9));b=Vec2(Q(14),Q(14))
    c=a+Vec2(Q(5),Q(-1));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0047():
    a=Vec2(Q(14),Q(10));b=Vec2(Q(16),Q(16))
    c=a+Vec2(Q(6),Q(-2));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0048():
    a=Vec2(Q(15),Q(11));b=Vec2(Q(18),Q(18))
    c=a+Vec2(Q(7),Q(-3));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0049():
    a=Vec2(Q(16),Q(12));b=Vec2(Q(20),Q(13))
    c=a+Vec2(Q(1),Q(-4));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0050():
    a=Vec2(Q(17),Q(13));b=Vec2(Q(22),Q(15))
    c=a+Vec2(Q(2),Q(-5));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0051():
    a=Vec2(Q(1),Q(14));b=Vec2(Q(7),Q(17))
    c=a+Vec2(Q(3),Q(-6));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0052():
    a=Vec2(Q(2),Q(2));b=Vec2(Q(9),Q(6))
    c=a+Vec2(Q(4),Q(-7));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0053():
    a=Vec2(Q(3),Q(3));b=Vec2(Q(11),Q(8))
    c=a+Vec2(Q(5),Q(-8));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0054():
    a=Vec2(Q(4),Q(4));b=Vec2(Q(13),Q(10))
    c=a+Vec2(Q(6),Q(-9));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0055():
    a=Vec2(Q(5),Q(5));b=Vec2(Q(15),Q(12))
    c=a+Vec2(Q(7),Q(-10));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0056():
    a=Vec2(Q(6),Q(6));b=Vec2(Q(17),Q(7))
    c=a+Vec2(Q(1),Q(-11));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0057():
    a=Vec2(Q(7),Q(7));b=Vec2(Q(19),Q(9))
    c=a+Vec2(Q(2),Q(-12));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0058():
    a=Vec2(Q(8),Q(8));b=Vec2(Q(21),Q(11))
    c=a+Vec2(Q(3),Q(-13));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0059():
    a=Vec2(Q(9),Q(9));b=Vec2(Q(23),Q(13))
    c=a+Vec2(Q(4),Q(-14));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0060():
    a=Vec2(Q(10),Q(10));b=Vec2(Q(25),Q(15))
    c=a+Vec2(Q(5),Q(-15));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0061():
    a=Vec2(Q(11),Q(11));b=Vec2(Q(27),Q(17))
    c=a+Vec2(Q(6),Q(-16));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0062():
    a=Vec2(Q(12),Q(12));b=Vec2(Q(29),Q(19))
    c=a+Vec2(Q(7),Q(-17));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0063():
    a=Vec2(Q(13),Q(13));b=Vec2(Q(31),Q(14))
    c=a+Vec2(Q(1),Q(-18));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0064():
    a=Vec2(Q(14),Q(14));b=Vec2(Q(33),Q(16))
    c=a+Vec2(Q(2),Q(-19));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0065():
    a=Vec2(Q(15),Q(2));b=Vec2(Q(35),Q(5))
    c=a+Vec2(Q(3),Q(-20));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0066():
    a=Vec2(Q(16),Q(3));b=Vec2(Q(37),Q(7))
    c=a+Vec2(Q(4),Q(-21));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0067():
    a=Vec2(Q(17),Q(4));b=Vec2(Q(39),Q(9))
    c=a+Vec2(Q(5),Q(-22));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0068():
    a=Vec2(Q(1),Q(5));b=Vec2(Q(24),Q(11))
    c=a+Vec2(Q(6),Q(-23));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0069():
    a=Vec2(Q(2),Q(6));b=Vec2(Q(3),Q(13))
    c=a+Vec2(Q(7),Q(-1));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0070():
    a=Vec2(Q(3),Q(7));b=Vec2(Q(5),Q(8))
    c=a+Vec2(Q(1),Q(-2));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0071():
    a=Vec2(Q(4),Q(8));b=Vec2(Q(7),Q(10))
    c=a+Vec2(Q(2),Q(-3));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0072():
    a=Vec2(Q(5),Q(9));b=Vec2(Q(9),Q(12))
    c=a+Vec2(Q(3),Q(-4));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0073():
    a=Vec2(Q(6),Q(10));b=Vec2(Q(11),Q(14))
    c=a+Vec2(Q(4),Q(-5));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0074():
    a=Vec2(Q(7),Q(11));b=Vec2(Q(13),Q(16))
    c=a+Vec2(Q(5),Q(-6));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0075():
    a=Vec2(Q(8),Q(12));b=Vec2(Q(15),Q(18))
    c=a+Vec2(Q(6),Q(-7));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0076():
    a=Vec2(Q(9),Q(13));b=Vec2(Q(17),Q(20))
    c=a+Vec2(Q(7),Q(-8));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0077():
    a=Vec2(Q(10),Q(14));b=Vec2(Q(19),Q(15))
    c=a+Vec2(Q(1),Q(-9));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0078():
    a=Vec2(Q(11),Q(2));b=Vec2(Q(21),Q(4))
    c=a+Vec2(Q(2),Q(-10));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0079():
    a=Vec2(Q(12),Q(3));b=Vec2(Q(23),Q(6))
    c=a+Vec2(Q(3),Q(-11));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0080():
    a=Vec2(Q(13),Q(4));b=Vec2(Q(25),Q(8))
    c=a+Vec2(Q(4),Q(-12));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0081():
    a=Vec2(Q(14),Q(5));b=Vec2(Q(27),Q(10))
    c=a+Vec2(Q(5),Q(-13));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0082():
    a=Vec2(Q(15),Q(6));b=Vec2(Q(29),Q(12))
    c=a+Vec2(Q(6),Q(-14));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0083():
    a=Vec2(Q(16),Q(7));b=Vec2(Q(31),Q(14))
    c=a+Vec2(Q(7),Q(-15));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0084():
    a=Vec2(Q(17),Q(8));b=Vec2(Q(33),Q(9))
    c=a+Vec2(Q(1),Q(-16));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0085():
    a=Vec2(Q(1),Q(9));b=Vec2(Q(18),Q(11))
    c=a+Vec2(Q(2),Q(-17));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0086():
    a=Vec2(Q(2),Q(10));b=Vec2(Q(20),Q(13))
    c=a+Vec2(Q(3),Q(-18));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0087():
    a=Vec2(Q(3),Q(11));b=Vec2(Q(22),Q(15))
    c=a+Vec2(Q(4),Q(-19));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0088():
    a=Vec2(Q(4),Q(12));b=Vec2(Q(24),Q(17))
    c=a+Vec2(Q(5),Q(-20));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0089():
    a=Vec2(Q(5),Q(13));b=Vec2(Q(26),Q(19))
    c=a+Vec2(Q(6),Q(-21));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0090():
    a=Vec2(Q(6),Q(14));b=Vec2(Q(28),Q(21))
    c=a+Vec2(Q(7),Q(-22));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0091():
    a=Vec2(Q(7),Q(2));b=Vec2(Q(30),Q(3))
    c=a+Vec2(Q(1),Q(-23));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0092():
    a=Vec2(Q(8),Q(3));b=Vec2(Q(9),Q(5))
    c=a+Vec2(Q(2),Q(-1));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0093():
    a=Vec2(Q(9),Q(4));b=Vec2(Q(11),Q(7))
    c=a+Vec2(Q(3),Q(-2));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0094():
    a=Vec2(Q(10),Q(5));b=Vec2(Q(13),Q(9))
    c=a+Vec2(Q(4),Q(-3));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0095():
    a=Vec2(Q(11),Q(6));b=Vec2(Q(15),Q(11))
    c=a+Vec2(Q(5),Q(-4));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0096():
    a=Vec2(Q(12),Q(7));b=Vec2(Q(17),Q(13))
    c=a+Vec2(Q(6),Q(-5));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0097():
    a=Vec2(Q(13),Q(8));b=Vec2(Q(19),Q(15))
    c=a+Vec2(Q(7),Q(-6));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0098():
    a=Vec2(Q(14),Q(9));b=Vec2(Q(21),Q(10))
    c=a+Vec2(Q(1),Q(-7));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0099():
    a=Vec2(Q(15),Q(10));b=Vec2(Q(23),Q(12))
    c=a+Vec2(Q(2),Q(-8));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0100():
    a=Vec2(Q(16),Q(11));b=Vec2(Q(25),Q(14))
    c=a+Vec2(Q(3),Q(-9));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0101():
    a=Vec2(Q(17),Q(12));b=Vec2(Q(27),Q(16))
    c=a+Vec2(Q(4),Q(-10));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0102():
    a=Vec2(Q(1),Q(13));b=Vec2(Q(12),Q(18))
    c=a+Vec2(Q(5),Q(-11));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0103():
    a=Vec2(Q(2),Q(14));b=Vec2(Q(14),Q(20))
    c=a+Vec2(Q(6),Q(-12));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0104():
    a=Vec2(Q(3),Q(2));b=Vec2(Q(16),Q(9))
    c=a+Vec2(Q(7),Q(-13));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0105():
    a=Vec2(Q(4),Q(3));b=Vec2(Q(18),Q(4))
    c=a+Vec2(Q(1),Q(-14));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0106():
    a=Vec2(Q(5),Q(4));b=Vec2(Q(20),Q(6))
    c=a+Vec2(Q(2),Q(-15));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0107():
    a=Vec2(Q(6),Q(5));b=Vec2(Q(22),Q(8))
    c=a+Vec2(Q(3),Q(-16));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0108():
    a=Vec2(Q(7),Q(6));b=Vec2(Q(24),Q(10))
    c=a+Vec2(Q(4),Q(-17));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0109():
    a=Vec2(Q(8),Q(7));b=Vec2(Q(26),Q(12))
    c=a+Vec2(Q(5),Q(-18));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0110():
    a=Vec2(Q(9),Q(8));b=Vec2(Q(28),Q(14))
    c=a+Vec2(Q(6),Q(-19));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0111():
    a=Vec2(Q(10),Q(9));b=Vec2(Q(30),Q(16))
    c=a+Vec2(Q(7),Q(-20));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0112():
    a=Vec2(Q(11),Q(10));b=Vec2(Q(32),Q(11))
    c=a+Vec2(Q(1),Q(-21));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0113():
    a=Vec2(Q(12),Q(11));b=Vec2(Q(34),Q(13))
    c=a+Vec2(Q(2),Q(-22));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0114():
    a=Vec2(Q(13),Q(12));b=Vec2(Q(36),Q(15))
    c=a+Vec2(Q(3),Q(-23));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0115():
    a=Vec2(Q(14),Q(13));b=Vec2(Q(15),Q(17))
    c=a+Vec2(Q(4),Q(-1));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0116():
    a=Vec2(Q(15),Q(14));b=Vec2(Q(17),Q(19))
    c=a+Vec2(Q(5),Q(-2));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0117():
    a=Vec2(Q(16),Q(2));b=Vec2(Q(19),Q(8))
    c=a+Vec2(Q(6),Q(-3));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0118():
    a=Vec2(Q(17),Q(3));b=Vec2(Q(21),Q(10))
    c=a+Vec2(Q(7),Q(-4));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0119():
    a=Vec2(Q(1),Q(4));b=Vec2(Q(6),Q(5))
    c=a+Vec2(Q(1),Q(-5));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0120():
    a=Vec2(Q(2),Q(5));b=Vec2(Q(8),Q(7))
    c=a+Vec2(Q(2),Q(-6));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0121():
    a=Vec2(Q(3),Q(6));b=Vec2(Q(10),Q(9))
    c=a+Vec2(Q(3),Q(-7));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0122():
    a=Vec2(Q(4),Q(7));b=Vec2(Q(12),Q(11))
    c=a+Vec2(Q(4),Q(-8));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0123():
    a=Vec2(Q(5),Q(8));b=Vec2(Q(14),Q(13))
    c=a+Vec2(Q(5),Q(-9));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0124():
    a=Vec2(Q(6),Q(9));b=Vec2(Q(16),Q(15))
    c=a+Vec2(Q(6),Q(-10));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0125():
    a=Vec2(Q(7),Q(10));b=Vec2(Q(18),Q(17))
    c=a+Vec2(Q(7),Q(-11));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0126():
    a=Vec2(Q(8),Q(11));b=Vec2(Q(20),Q(12))
    c=a+Vec2(Q(1),Q(-12));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0127():
    a=Vec2(Q(9),Q(12));b=Vec2(Q(22),Q(14))
    c=a+Vec2(Q(2),Q(-13));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0128():
    a=Vec2(Q(10),Q(13));b=Vec2(Q(24),Q(16))
    c=a+Vec2(Q(3),Q(-14));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0129():
    a=Vec2(Q(11),Q(14));b=Vec2(Q(26),Q(18))
    c=a+Vec2(Q(4),Q(-15));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0130():
    a=Vec2(Q(12),Q(2));b=Vec2(Q(28),Q(7))
    c=a+Vec2(Q(5),Q(-16));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0131():
    a=Vec2(Q(13),Q(3));b=Vec2(Q(30),Q(9))
    c=a+Vec2(Q(6),Q(-17));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0132():
    a=Vec2(Q(14),Q(4));b=Vec2(Q(32),Q(11))
    c=a+Vec2(Q(7),Q(-18));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0133():
    a=Vec2(Q(15),Q(5));b=Vec2(Q(34),Q(6))
    c=a+Vec2(Q(1),Q(-19));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0134():
    a=Vec2(Q(16),Q(6));b=Vec2(Q(36),Q(8))
    c=a+Vec2(Q(2),Q(-20));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0135():
    a=Vec2(Q(17),Q(7));b=Vec2(Q(38),Q(10))
    c=a+Vec2(Q(3),Q(-21));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0136():
    a=Vec2(Q(1),Q(8));b=Vec2(Q(23),Q(12))
    c=a+Vec2(Q(4),Q(-22));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0137():
    a=Vec2(Q(2),Q(9));b=Vec2(Q(25),Q(14))
    c=a+Vec2(Q(5),Q(-23));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0138():
    a=Vec2(Q(3),Q(10));b=Vec2(Q(4),Q(16))
    c=a+Vec2(Q(6),Q(-1));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0139():
    a=Vec2(Q(4),Q(11));b=Vec2(Q(6),Q(18))
    c=a+Vec2(Q(7),Q(-2));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0140():
    a=Vec2(Q(5),Q(12));b=Vec2(Q(8),Q(13))
    c=a+Vec2(Q(1),Q(-3));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0141():
    a=Vec2(Q(6),Q(13));b=Vec2(Q(10),Q(15))
    c=a+Vec2(Q(2),Q(-4));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0142():
    a=Vec2(Q(7),Q(14));b=Vec2(Q(12),Q(17))
    c=a+Vec2(Q(3),Q(-5));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0143():
    a=Vec2(Q(8),Q(2));b=Vec2(Q(14),Q(6))
    c=a+Vec2(Q(4),Q(-6));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0144():
    a=Vec2(Q(9),Q(3));b=Vec2(Q(16),Q(8))
    c=a+Vec2(Q(5),Q(-7));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0145():
    a=Vec2(Q(10),Q(4));b=Vec2(Q(18),Q(10))
    c=a+Vec2(Q(6),Q(-8));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0146():
    a=Vec2(Q(11),Q(5));b=Vec2(Q(20),Q(12))
    c=a+Vec2(Q(7),Q(-9));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0147():
    a=Vec2(Q(12),Q(6));b=Vec2(Q(22),Q(7))
    c=a+Vec2(Q(1),Q(-10));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0148():
    a=Vec2(Q(13),Q(7));b=Vec2(Q(24),Q(9))
    c=a+Vec2(Q(2),Q(-11));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0149():
    a=Vec2(Q(14),Q(8));b=Vec2(Q(26),Q(11))
    c=a+Vec2(Q(3),Q(-12));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0150():
    a=Vec2(Q(15),Q(9));b=Vec2(Q(28),Q(13))
    c=a+Vec2(Q(4),Q(-13));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0151():
    a=Vec2(Q(16),Q(10));b=Vec2(Q(30),Q(15))
    c=a+Vec2(Q(5),Q(-14));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0152():
    a=Vec2(Q(17),Q(11));b=Vec2(Q(32),Q(17))
    c=a+Vec2(Q(6),Q(-15));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0153():
    a=Vec2(Q(1),Q(12));b=Vec2(Q(17),Q(19))
    c=a+Vec2(Q(7),Q(-16));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0154():
    a=Vec2(Q(2),Q(13));b=Vec2(Q(19),Q(14))
    c=a+Vec2(Q(1),Q(-17));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0155():
    a=Vec2(Q(3),Q(14));b=Vec2(Q(21),Q(16))
    c=a+Vec2(Q(2),Q(-18));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0156():
    a=Vec2(Q(4),Q(2));b=Vec2(Q(23),Q(5))
    c=a+Vec2(Q(3),Q(-19));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0157():
    a=Vec2(Q(5),Q(3));b=Vec2(Q(25),Q(7))
    c=a+Vec2(Q(4),Q(-20));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0158():
    a=Vec2(Q(6),Q(4));b=Vec2(Q(27),Q(9))
    c=a+Vec2(Q(5),Q(-21));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0159():
    a=Vec2(Q(7),Q(5));b=Vec2(Q(29),Q(11))
    c=a+Vec2(Q(6),Q(-22));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0160():
    a=Vec2(Q(8),Q(6));b=Vec2(Q(31),Q(13))
    c=a+Vec2(Q(7),Q(-23));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0161():
    a=Vec2(Q(9),Q(7));b=Vec2(Q(10),Q(8))
    c=a+Vec2(Q(1),Q(-1));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0162():
    a=Vec2(Q(10),Q(8));b=Vec2(Q(12),Q(10))
    c=a+Vec2(Q(2),Q(-2));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0163():
    a=Vec2(Q(11),Q(9));b=Vec2(Q(14),Q(12))
    c=a+Vec2(Q(3),Q(-3));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0164():
    a=Vec2(Q(12),Q(10));b=Vec2(Q(16),Q(14))
    c=a+Vec2(Q(4),Q(-4));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0165():
    a=Vec2(Q(13),Q(11));b=Vec2(Q(18),Q(16))
    c=a+Vec2(Q(5),Q(-5));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0166():
    a=Vec2(Q(14),Q(12));b=Vec2(Q(20),Q(18))
    c=a+Vec2(Q(6),Q(-6));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0167():
    a=Vec2(Q(15),Q(13));b=Vec2(Q(22),Q(20))
    c=a+Vec2(Q(7),Q(-7));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0168():
    a=Vec2(Q(16),Q(14));b=Vec2(Q(24),Q(15))
    c=a+Vec2(Q(1),Q(-8));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0169():
    a=Vec2(Q(17),Q(2));b=Vec2(Q(26),Q(4))
    c=a+Vec2(Q(2),Q(-9));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0170():
    a=Vec2(Q(1),Q(3));b=Vec2(Q(11),Q(6))
    c=a+Vec2(Q(3),Q(-10));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0171():
    a=Vec2(Q(2),Q(4));b=Vec2(Q(13),Q(8))
    c=a+Vec2(Q(4),Q(-11));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0172():
    a=Vec2(Q(3),Q(5));b=Vec2(Q(15),Q(10))
    c=a+Vec2(Q(5),Q(-12));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0173():
    a=Vec2(Q(4),Q(6));b=Vec2(Q(17),Q(12))
    c=a+Vec2(Q(6),Q(-13));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0174():
    a=Vec2(Q(5),Q(7));b=Vec2(Q(19),Q(14))
    c=a+Vec2(Q(7),Q(-14));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0175():
    a=Vec2(Q(6),Q(8));b=Vec2(Q(21),Q(9))
    c=a+Vec2(Q(1),Q(-15));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0176():
    a=Vec2(Q(7),Q(9));b=Vec2(Q(23),Q(11))
    c=a+Vec2(Q(2),Q(-16));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0177():
    a=Vec2(Q(8),Q(10));b=Vec2(Q(25),Q(13))
    c=a+Vec2(Q(3),Q(-17));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0178():
    a=Vec2(Q(9),Q(11));b=Vec2(Q(27),Q(15))
    c=a+Vec2(Q(4),Q(-18));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0179():
    a=Vec2(Q(10),Q(12));b=Vec2(Q(29),Q(17))
    c=a+Vec2(Q(5),Q(-19));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0180():
    a=Vec2(Q(11),Q(13));b=Vec2(Q(31),Q(19))
    c=a+Vec2(Q(6),Q(-20));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0181():
    a=Vec2(Q(12),Q(14));b=Vec2(Q(33),Q(21))
    c=a+Vec2(Q(7),Q(-21));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0182():
    a=Vec2(Q(13),Q(2));b=Vec2(Q(35),Q(3))
    c=a+Vec2(Q(1),Q(-22));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0183():
    a=Vec2(Q(14),Q(3));b=Vec2(Q(37),Q(5))
    c=a+Vec2(Q(2),Q(-23));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0184():
    a=Vec2(Q(15),Q(4));b=Vec2(Q(16),Q(7))
    c=a+Vec2(Q(3),Q(-1));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0185():
    a=Vec2(Q(16),Q(5));b=Vec2(Q(18),Q(9))
    c=a+Vec2(Q(4),Q(-2));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0186():
    a=Vec2(Q(17),Q(6));b=Vec2(Q(20),Q(11))
    c=a+Vec2(Q(5),Q(-3));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0187():
    a=Vec2(Q(1),Q(7));b=Vec2(Q(5),Q(13))
    c=a+Vec2(Q(6),Q(-4));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0188():
    a=Vec2(Q(2),Q(8));b=Vec2(Q(7),Q(15))
    c=a+Vec2(Q(7),Q(-5));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0189():
    a=Vec2(Q(3),Q(9));b=Vec2(Q(9),Q(10))
    c=a+Vec2(Q(1),Q(-6));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0190():
    a=Vec2(Q(4),Q(10));b=Vec2(Q(11),Q(12))
    c=a+Vec2(Q(2),Q(-7));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0191():
    a=Vec2(Q(5),Q(11));b=Vec2(Q(13),Q(14))
    c=a+Vec2(Q(3),Q(-8));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0192():
    a=Vec2(Q(6),Q(12));b=Vec2(Q(15),Q(16))
    c=a+Vec2(Q(4),Q(-9));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0193():
    a=Vec2(Q(7),Q(13));b=Vec2(Q(17),Q(18))
    c=a+Vec2(Q(5),Q(-10));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0194():
    a=Vec2(Q(8),Q(14));b=Vec2(Q(19),Q(20))
    c=a+Vec2(Q(6),Q(-11));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0195():
    a=Vec2(Q(9),Q(2));b=Vec2(Q(21),Q(9))
    c=a+Vec2(Q(7),Q(-12));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0196():
    a=Vec2(Q(10),Q(3));b=Vec2(Q(23),Q(4))
    c=a+Vec2(Q(1),Q(-13));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0197():
    a=Vec2(Q(11),Q(4));b=Vec2(Q(25),Q(6))
    c=a+Vec2(Q(2),Q(-14));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0198():
    a=Vec2(Q(12),Q(5));b=Vec2(Q(27),Q(8))
    c=a+Vec2(Q(3),Q(-15));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0199():
    a=Vec2(Q(13),Q(6));b=Vec2(Q(29),Q(10))
    c=a+Vec2(Q(4),Q(-16));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0200():
    a=Vec2(Q(14),Q(7));b=Vec2(Q(31),Q(12))
    c=a+Vec2(Q(5),Q(-17));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0201():
    a=Vec2(Q(15),Q(8));b=Vec2(Q(33),Q(14))
    c=a+Vec2(Q(6),Q(-18));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0202():
    a=Vec2(Q(16),Q(9));b=Vec2(Q(35),Q(16))
    c=a+Vec2(Q(7),Q(-19));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0203():
    a=Vec2(Q(17),Q(10));b=Vec2(Q(37),Q(11))
    c=a+Vec2(Q(1),Q(-20));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0204():
    a=Vec2(Q(1),Q(11));b=Vec2(Q(22),Q(13))
    c=a+Vec2(Q(2),Q(-21));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0205():
    a=Vec2(Q(2),Q(12));b=Vec2(Q(24),Q(15))
    c=a+Vec2(Q(3),Q(-22));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0206():
    a=Vec2(Q(3),Q(13));b=Vec2(Q(26),Q(17))
    c=a+Vec2(Q(4),Q(-23));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0207():
    a=Vec2(Q(4),Q(14));b=Vec2(Q(5),Q(19))
    c=a+Vec2(Q(5),Q(-1));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0208():
    a=Vec2(Q(5),Q(2));b=Vec2(Q(7),Q(8))
    c=a+Vec2(Q(6),Q(-2));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0209():
    a=Vec2(Q(6),Q(3));b=Vec2(Q(9),Q(10))
    c=a+Vec2(Q(7),Q(-3));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0210():
    a=Vec2(Q(7),Q(4));b=Vec2(Q(11),Q(5))
    c=a+Vec2(Q(1),Q(-4));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0211():
    a=Vec2(Q(8),Q(5));b=Vec2(Q(13),Q(7))
    c=a+Vec2(Q(2),Q(-5));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0212():
    a=Vec2(Q(9),Q(6));b=Vec2(Q(15),Q(9))
    c=a+Vec2(Q(3),Q(-6));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0213():
    a=Vec2(Q(10),Q(7));b=Vec2(Q(17),Q(11))
    c=a+Vec2(Q(4),Q(-7));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0214():
    a=Vec2(Q(11),Q(8));b=Vec2(Q(19),Q(13))
    c=a+Vec2(Q(5),Q(-8));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0215():
    a=Vec2(Q(12),Q(9));b=Vec2(Q(21),Q(15))
    c=a+Vec2(Q(6),Q(-9));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0216():
    a=Vec2(Q(13),Q(10));b=Vec2(Q(23),Q(17))
    c=a+Vec2(Q(7),Q(-10));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0217():
    a=Vec2(Q(14),Q(11));b=Vec2(Q(25),Q(12))
    c=a+Vec2(Q(1),Q(-11));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0218():
    a=Vec2(Q(15),Q(12));b=Vec2(Q(27),Q(14))
    c=a+Vec2(Q(2),Q(-12));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0219():
    a=Vec2(Q(16),Q(13));b=Vec2(Q(29),Q(16))
    c=a+Vec2(Q(3),Q(-13));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0220():
    a=Vec2(Q(17),Q(14));b=Vec2(Q(31),Q(18))
    c=a+Vec2(Q(4),Q(-14));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0221():
    a=Vec2(Q(1),Q(2));b=Vec2(Q(16),Q(7))
    c=a+Vec2(Q(5),Q(-15));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0222():
    a=Vec2(Q(2),Q(3));b=Vec2(Q(18),Q(9))
    c=a+Vec2(Q(6),Q(-16));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0223():
    a=Vec2(Q(3),Q(4));b=Vec2(Q(20),Q(11))
    c=a+Vec2(Q(7),Q(-17));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0224():
    a=Vec2(Q(4),Q(5));b=Vec2(Q(22),Q(6))
    c=a+Vec2(Q(1),Q(-18));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0225():
    a=Vec2(Q(5),Q(6));b=Vec2(Q(24),Q(8))
    c=a+Vec2(Q(2),Q(-19));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0226():
    a=Vec2(Q(6),Q(7));b=Vec2(Q(26),Q(10))
    c=a+Vec2(Q(3),Q(-20));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0227():
    a=Vec2(Q(7),Q(8));b=Vec2(Q(28),Q(12))
    c=a+Vec2(Q(4),Q(-21));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0228():
    a=Vec2(Q(8),Q(9));b=Vec2(Q(30),Q(14))
    c=a+Vec2(Q(5),Q(-22));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0229():
    a=Vec2(Q(9),Q(10));b=Vec2(Q(32),Q(16))
    c=a+Vec2(Q(6),Q(-23));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0230():
    a=Vec2(Q(10),Q(11));b=Vec2(Q(11),Q(18))
    c=a+Vec2(Q(7),Q(-1));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0231():
    a=Vec2(Q(11),Q(12));b=Vec2(Q(13),Q(13))
    c=a+Vec2(Q(1),Q(-2));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0232():
    a=Vec2(Q(12),Q(13));b=Vec2(Q(15),Q(15))
    c=a+Vec2(Q(2),Q(-3));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0233():
    a=Vec2(Q(13),Q(14));b=Vec2(Q(17),Q(17))
    c=a+Vec2(Q(3),Q(-4));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0234():
    a=Vec2(Q(14),Q(2));b=Vec2(Q(19),Q(6))
    c=a+Vec2(Q(4),Q(-5));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0235():
    a=Vec2(Q(15),Q(3));b=Vec2(Q(21),Q(8))
    c=a+Vec2(Q(5),Q(-6));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0236():
    a=Vec2(Q(16),Q(4));b=Vec2(Q(23),Q(10))
    c=a+Vec2(Q(6),Q(-7));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0237():
    a=Vec2(Q(17),Q(5));b=Vec2(Q(25),Q(12))
    c=a+Vec2(Q(7),Q(-8));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0238():
    a=Vec2(Q(1),Q(6));b=Vec2(Q(10),Q(7))
    c=a+Vec2(Q(1),Q(-9));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0239():
    a=Vec2(Q(2),Q(7));b=Vec2(Q(12),Q(9))
    c=a+Vec2(Q(2),Q(-10));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0240():
    a=Vec2(Q(3),Q(8));b=Vec2(Q(14),Q(11))
    c=a+Vec2(Q(3),Q(-11));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0241():
    a=Vec2(Q(4),Q(9));b=Vec2(Q(16),Q(13))
    c=a+Vec2(Q(4),Q(-12));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0242():
    a=Vec2(Q(5),Q(10));b=Vec2(Q(18),Q(15))
    c=a+Vec2(Q(5),Q(-13));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0243():
    a=Vec2(Q(6),Q(11));b=Vec2(Q(20),Q(17))
    c=a+Vec2(Q(6),Q(-14));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0244():
    a=Vec2(Q(7),Q(12));b=Vec2(Q(22),Q(19))
    c=a+Vec2(Q(7),Q(-15));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0245():
    a=Vec2(Q(8),Q(13));b=Vec2(Q(24),Q(14))
    c=a+Vec2(Q(1),Q(-16));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0246():
    a=Vec2(Q(9),Q(14));b=Vec2(Q(26),Q(16))
    c=a+Vec2(Q(2),Q(-17));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0247():
    a=Vec2(Q(10),Q(2));b=Vec2(Q(28),Q(5))
    c=a+Vec2(Q(3),Q(-18));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0248():
    a=Vec2(Q(11),Q(3));b=Vec2(Q(30),Q(7))
    c=a+Vec2(Q(4),Q(-19));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0249():
    a=Vec2(Q(12),Q(4));b=Vec2(Q(32),Q(9))
    c=a+Vec2(Q(5),Q(-20));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0250():
    a=Vec2(Q(13),Q(5));b=Vec2(Q(34),Q(11))
    c=a+Vec2(Q(6),Q(-21));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0251():
    a=Vec2(Q(14),Q(6));b=Vec2(Q(36),Q(13))
    c=a+Vec2(Q(7),Q(-22));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0252():
    a=Vec2(Q(15),Q(7));b=Vec2(Q(38),Q(8))
    c=a+Vec2(Q(1),Q(-23));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0253():
    a=Vec2(Q(16),Q(8));b=Vec2(Q(17),Q(10))
    c=a+Vec2(Q(2),Q(-1));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0254():
    a=Vec2(Q(17),Q(9));b=Vec2(Q(19),Q(12))
    c=a+Vec2(Q(3),Q(-2));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0255():
    a=Vec2(Q(1),Q(10));b=Vec2(Q(4),Q(14))
    c=a+Vec2(Q(4),Q(-3));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0256():
    a=Vec2(Q(2),Q(11));b=Vec2(Q(6),Q(16))
    c=a+Vec2(Q(5),Q(-4));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0257():
    a=Vec2(Q(3),Q(12));b=Vec2(Q(8),Q(18))
    c=a+Vec2(Q(6),Q(-5));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0258():
    a=Vec2(Q(4),Q(13));b=Vec2(Q(10),Q(20))
    c=a+Vec2(Q(7),Q(-6));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0259():
    a=Vec2(Q(5),Q(14));b=Vec2(Q(12),Q(15))
    c=a+Vec2(Q(1),Q(-7));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0260():
    a=Vec2(Q(6),Q(2));b=Vec2(Q(14),Q(4))
    c=a+Vec2(Q(2),Q(-8));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0261():
    a=Vec2(Q(7),Q(3));b=Vec2(Q(16),Q(6))
    c=a+Vec2(Q(3),Q(-9));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0262():
    a=Vec2(Q(8),Q(4));b=Vec2(Q(18),Q(8))
    c=a+Vec2(Q(4),Q(-10));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0263():
    a=Vec2(Q(9),Q(5));b=Vec2(Q(20),Q(10))
    c=a+Vec2(Q(5),Q(-11));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0264():
    a=Vec2(Q(10),Q(6));b=Vec2(Q(22),Q(12))
    c=a+Vec2(Q(6),Q(-12));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0265():
    a=Vec2(Q(11),Q(7));b=Vec2(Q(24),Q(14))
    c=a+Vec2(Q(7),Q(-13));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0266():
    a=Vec2(Q(12),Q(8));b=Vec2(Q(26),Q(9))
    c=a+Vec2(Q(1),Q(-14));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0267():
    a=Vec2(Q(13),Q(9));b=Vec2(Q(28),Q(11))
    c=a+Vec2(Q(2),Q(-15));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0268():
    a=Vec2(Q(14),Q(10));b=Vec2(Q(30),Q(13))
    c=a+Vec2(Q(3),Q(-16));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0269():
    a=Vec2(Q(15),Q(11));b=Vec2(Q(32),Q(15))
    c=a+Vec2(Q(4),Q(-17));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0270():
    a=Vec2(Q(16),Q(12));b=Vec2(Q(34),Q(17))
    c=a+Vec2(Q(5),Q(-18));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0271():
    a=Vec2(Q(17),Q(13));b=Vec2(Q(36),Q(19))
    c=a+Vec2(Q(6),Q(-19));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0272():
    a=Vec2(Q(1),Q(14));b=Vec2(Q(21),Q(21))
    c=a+Vec2(Q(7),Q(-20));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0273():
    a=Vec2(Q(2),Q(2));b=Vec2(Q(23),Q(3))
    c=a+Vec2(Q(1),Q(-21));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0274():
    a=Vec2(Q(3),Q(3));b=Vec2(Q(25),Q(5))
    c=a+Vec2(Q(2),Q(-22));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0275():
    a=Vec2(Q(4),Q(4));b=Vec2(Q(27),Q(7))
    c=a+Vec2(Q(3),Q(-23));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0276():
    a=Vec2(Q(5),Q(5));b=Vec2(Q(6),Q(9))
    c=a+Vec2(Q(4),Q(-1));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0277():
    a=Vec2(Q(6),Q(6));b=Vec2(Q(8),Q(11))
    c=a+Vec2(Q(5),Q(-2));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0278():
    a=Vec2(Q(7),Q(7));b=Vec2(Q(10),Q(13))
    c=a+Vec2(Q(6),Q(-3));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0279():
    a=Vec2(Q(8),Q(8));b=Vec2(Q(12),Q(15))
    c=a+Vec2(Q(7),Q(-4));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0280():
    a=Vec2(Q(9),Q(9));b=Vec2(Q(14),Q(10))
    c=a+Vec2(Q(1),Q(-5));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0281():
    a=Vec2(Q(10),Q(10));b=Vec2(Q(16),Q(12))
    c=a+Vec2(Q(2),Q(-6));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0282():
    a=Vec2(Q(11),Q(11));b=Vec2(Q(18),Q(14))
    c=a+Vec2(Q(3),Q(-7));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0283():
    a=Vec2(Q(12),Q(12));b=Vec2(Q(20),Q(16))
    c=a+Vec2(Q(4),Q(-8));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0284():
    a=Vec2(Q(13),Q(13));b=Vec2(Q(22),Q(18))
    c=a+Vec2(Q(5),Q(-9));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0285():
    a=Vec2(Q(14),Q(14));b=Vec2(Q(24),Q(20))
    c=a+Vec2(Q(6),Q(-10));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0286():
    a=Vec2(Q(15),Q(2));b=Vec2(Q(26),Q(9))
    c=a+Vec2(Q(7),Q(-11));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0287():
    a=Vec2(Q(16),Q(3));b=Vec2(Q(28),Q(4))
    c=a+Vec2(Q(1),Q(-12));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0288():
    a=Vec2(Q(17),Q(4));b=Vec2(Q(30),Q(6))
    c=a+Vec2(Q(2),Q(-13));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0289():
    a=Vec2(Q(1),Q(5));b=Vec2(Q(15),Q(8))
    c=a+Vec2(Q(3),Q(-14));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0290():
    a=Vec2(Q(2),Q(6));b=Vec2(Q(17),Q(10))
    c=a+Vec2(Q(4),Q(-15));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0291():
    a=Vec2(Q(3),Q(7));b=Vec2(Q(19),Q(12))
    c=a+Vec2(Q(5),Q(-16));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0292():
    a=Vec2(Q(4),Q(8));b=Vec2(Q(21),Q(14))
    c=a+Vec2(Q(6),Q(-17));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0293():
    a=Vec2(Q(5),Q(9));b=Vec2(Q(23),Q(16))
    c=a+Vec2(Q(7),Q(-18));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0294():
    a=Vec2(Q(6),Q(10));b=Vec2(Q(25),Q(11))
    c=a+Vec2(Q(1),Q(-19));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0295():
    a=Vec2(Q(7),Q(11));b=Vec2(Q(27),Q(13))
    c=a+Vec2(Q(2),Q(-20));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0296():
    a=Vec2(Q(8),Q(12));b=Vec2(Q(29),Q(15))
    c=a+Vec2(Q(3),Q(-21));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0297():
    a=Vec2(Q(9),Q(13));b=Vec2(Q(31),Q(17))
    c=a+Vec2(Q(4),Q(-22));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0298():
    a=Vec2(Q(10),Q(14));b=Vec2(Q(33),Q(19))
    c=a+Vec2(Q(5),Q(-23));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0299():
    a=Vec2(Q(11),Q(2));b=Vec2(Q(12),Q(8))
    c=a+Vec2(Q(6),Q(-1));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0300():
    a=Vec2(Q(12),Q(3));b=Vec2(Q(14),Q(10))
    c=a+Vec2(Q(7),Q(-2));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0301():
    a=Vec2(Q(13),Q(4));b=Vec2(Q(16),Q(5))
    c=a+Vec2(Q(1),Q(-3));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0302():
    a=Vec2(Q(14),Q(5));b=Vec2(Q(18),Q(7))
    c=a+Vec2(Q(2),Q(-4));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0303():
    a=Vec2(Q(15),Q(6));b=Vec2(Q(20),Q(9))
    c=a+Vec2(Q(3),Q(-5));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0304():
    a=Vec2(Q(16),Q(7));b=Vec2(Q(22),Q(11))
    c=a+Vec2(Q(4),Q(-6));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0305():
    a=Vec2(Q(17),Q(8));b=Vec2(Q(24),Q(13))
    c=a+Vec2(Q(5),Q(-7));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0306():
    a=Vec2(Q(1),Q(9));b=Vec2(Q(9),Q(15))
    c=a+Vec2(Q(6),Q(-8));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0307():
    a=Vec2(Q(2),Q(10));b=Vec2(Q(11),Q(17))
    c=a+Vec2(Q(7),Q(-9));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0308():
    a=Vec2(Q(3),Q(11));b=Vec2(Q(13),Q(12))
    c=a+Vec2(Q(1),Q(-10));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0309():
    a=Vec2(Q(4),Q(12));b=Vec2(Q(15),Q(14))
    c=a+Vec2(Q(2),Q(-11));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0310():
    a=Vec2(Q(5),Q(13));b=Vec2(Q(17),Q(16))
    c=a+Vec2(Q(3),Q(-12));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0311():
    a=Vec2(Q(6),Q(14));b=Vec2(Q(19),Q(18))
    c=a+Vec2(Q(4),Q(-13));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0312():
    a=Vec2(Q(7),Q(2));b=Vec2(Q(21),Q(7))
    c=a+Vec2(Q(5),Q(-14));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0313():
    a=Vec2(Q(8),Q(3));b=Vec2(Q(23),Q(9))
    c=a+Vec2(Q(6),Q(-15));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0314():
    a=Vec2(Q(9),Q(4));b=Vec2(Q(25),Q(11))
    c=a+Vec2(Q(7),Q(-16));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0315():
    a=Vec2(Q(10),Q(5));b=Vec2(Q(27),Q(6))
    c=a+Vec2(Q(1),Q(-17));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0316():
    a=Vec2(Q(11),Q(6));b=Vec2(Q(29),Q(8))
    c=a+Vec2(Q(2),Q(-18));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0317():
    a=Vec2(Q(12),Q(7));b=Vec2(Q(31),Q(10))
    c=a+Vec2(Q(3),Q(-19));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0318():
    a=Vec2(Q(13),Q(8));b=Vec2(Q(33),Q(12))
    c=a+Vec2(Q(4),Q(-20));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0319():
    a=Vec2(Q(14),Q(9));b=Vec2(Q(35),Q(14))
    c=a+Vec2(Q(5),Q(-21));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0320():
    a=Vec2(Q(15),Q(10));b=Vec2(Q(37),Q(16))
    c=a+Vec2(Q(6),Q(-22));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0321():
    a=Vec2(Q(16),Q(11));b=Vec2(Q(39),Q(18))
    c=a+Vec2(Q(7),Q(-23));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0322():
    a=Vec2(Q(17),Q(12));b=Vec2(Q(18),Q(13))
    c=a+Vec2(Q(1),Q(-1));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0323():
    a=Vec2(Q(1),Q(13));b=Vec2(Q(3),Q(15))
    c=a+Vec2(Q(2),Q(-2));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0324():
    a=Vec2(Q(2),Q(14));b=Vec2(Q(5),Q(17))
    c=a+Vec2(Q(3),Q(-3));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0325():
    a=Vec2(Q(3),Q(2));b=Vec2(Q(7),Q(6))
    c=a+Vec2(Q(4),Q(-4));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0326():
    a=Vec2(Q(4),Q(3));b=Vec2(Q(9),Q(8))
    c=a+Vec2(Q(5),Q(-5));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0327():
    a=Vec2(Q(5),Q(4));b=Vec2(Q(11),Q(10))
    c=a+Vec2(Q(6),Q(-6));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0328():
    a=Vec2(Q(6),Q(5));b=Vec2(Q(13),Q(12))
    c=a+Vec2(Q(7),Q(-7));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0329():
    a=Vec2(Q(7),Q(6));b=Vec2(Q(15),Q(7))
    c=a+Vec2(Q(1),Q(-8));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0330():
    a=Vec2(Q(8),Q(7));b=Vec2(Q(17),Q(9))
    c=a+Vec2(Q(2),Q(-9));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0331():
    a=Vec2(Q(9),Q(8));b=Vec2(Q(19),Q(11))
    c=a+Vec2(Q(3),Q(-10));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0332():
    a=Vec2(Q(10),Q(9));b=Vec2(Q(21),Q(13))
    c=a+Vec2(Q(4),Q(-11));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0333():
    a=Vec2(Q(11),Q(10));b=Vec2(Q(23),Q(15))
    c=a+Vec2(Q(5),Q(-12));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0334():
    a=Vec2(Q(12),Q(11));b=Vec2(Q(25),Q(17))
    c=a+Vec2(Q(6),Q(-13));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0335():
    a=Vec2(Q(13),Q(12));b=Vec2(Q(27),Q(19))
    c=a+Vec2(Q(7),Q(-14));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0336():
    a=Vec2(Q(14),Q(13));b=Vec2(Q(29),Q(14))
    c=a+Vec2(Q(1),Q(-15));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0337():
    a=Vec2(Q(15),Q(14));b=Vec2(Q(31),Q(16))
    c=a+Vec2(Q(2),Q(-16));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0338():
    a=Vec2(Q(16),Q(2));b=Vec2(Q(33),Q(5))
    c=a+Vec2(Q(3),Q(-17));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0339():
    a=Vec2(Q(17),Q(3));b=Vec2(Q(35),Q(7))
    c=a+Vec2(Q(4),Q(-18));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0340():
    a=Vec2(Q(1),Q(4));b=Vec2(Q(20),Q(9))
    c=a+Vec2(Q(5),Q(-19));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0341():
    a=Vec2(Q(2),Q(5));b=Vec2(Q(22),Q(11))
    c=a+Vec2(Q(6),Q(-20));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0342():
    a=Vec2(Q(3),Q(6));b=Vec2(Q(24),Q(13))
    c=a+Vec2(Q(7),Q(-21));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0343():
    a=Vec2(Q(4),Q(7));b=Vec2(Q(26),Q(8))
    c=a+Vec2(Q(1),Q(-22));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0344():
    a=Vec2(Q(5),Q(8));b=Vec2(Q(28),Q(10))
    c=a+Vec2(Q(2),Q(-23));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0345():
    a=Vec2(Q(6),Q(9));b=Vec2(Q(7),Q(12))
    c=a+Vec2(Q(3),Q(-1));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0346():
    a=Vec2(Q(7),Q(10));b=Vec2(Q(9),Q(14))
    c=a+Vec2(Q(4),Q(-2));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0347():
    a=Vec2(Q(8),Q(11));b=Vec2(Q(11),Q(16))
    c=a+Vec2(Q(5),Q(-3));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0348():
    a=Vec2(Q(9),Q(12));b=Vec2(Q(13),Q(18))
    c=a+Vec2(Q(6),Q(-4));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0349():
    a=Vec2(Q(10),Q(13));b=Vec2(Q(15),Q(20))
    c=a+Vec2(Q(7),Q(-5));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0350():
    a=Vec2(Q(11),Q(14));b=Vec2(Q(17),Q(15))
    c=a+Vec2(Q(1),Q(-6));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0351():
    a=Vec2(Q(12),Q(2));b=Vec2(Q(19),Q(4))
    c=a+Vec2(Q(2),Q(-7));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0352():
    a=Vec2(Q(13),Q(3));b=Vec2(Q(21),Q(6))
    c=a+Vec2(Q(3),Q(-8));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0353():
    a=Vec2(Q(14),Q(4));b=Vec2(Q(23),Q(8))
    c=a+Vec2(Q(4),Q(-9));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0354():
    a=Vec2(Q(15),Q(5));b=Vec2(Q(25),Q(10))
    c=a+Vec2(Q(5),Q(-10));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0355():
    a=Vec2(Q(16),Q(6));b=Vec2(Q(27),Q(12))
    c=a+Vec2(Q(6),Q(-11));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0356():
    a=Vec2(Q(17),Q(7));b=Vec2(Q(29),Q(14))
    c=a+Vec2(Q(7),Q(-12));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0357():
    a=Vec2(Q(1),Q(8));b=Vec2(Q(14),Q(9))
    c=a+Vec2(Q(1),Q(-13));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0358():
    a=Vec2(Q(2),Q(9));b=Vec2(Q(16),Q(11))
    c=a+Vec2(Q(2),Q(-14));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0359():
    a=Vec2(Q(3),Q(10));b=Vec2(Q(18),Q(13))
    c=a+Vec2(Q(3),Q(-15));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0360():
    a=Vec2(Q(4),Q(11));b=Vec2(Q(20),Q(15))
    c=a+Vec2(Q(4),Q(-16));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0361():
    a=Vec2(Q(5),Q(12));b=Vec2(Q(22),Q(17))
    c=a+Vec2(Q(5),Q(-17));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0362():
    a=Vec2(Q(6),Q(13));b=Vec2(Q(24),Q(19))
    c=a+Vec2(Q(6),Q(-18));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0363():
    a=Vec2(Q(7),Q(14));b=Vec2(Q(26),Q(21))
    c=a+Vec2(Q(7),Q(-19));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0364():
    a=Vec2(Q(8),Q(2));b=Vec2(Q(28),Q(3))
    c=a+Vec2(Q(1),Q(-20));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0365():
    a=Vec2(Q(9),Q(3));b=Vec2(Q(30),Q(5))
    c=a+Vec2(Q(2),Q(-21));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0366():
    a=Vec2(Q(10),Q(4));b=Vec2(Q(32),Q(7))
    c=a+Vec2(Q(3),Q(-22));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0367():
    a=Vec2(Q(11),Q(5));b=Vec2(Q(34),Q(9))
    c=a+Vec2(Q(4),Q(-23));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0368():
    a=Vec2(Q(12),Q(6));b=Vec2(Q(13),Q(11))
    c=a+Vec2(Q(5),Q(-1));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0369():
    a=Vec2(Q(13),Q(7));b=Vec2(Q(15),Q(13))
    c=a+Vec2(Q(6),Q(-2));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0370():
    a=Vec2(Q(14),Q(8));b=Vec2(Q(17),Q(15))
    c=a+Vec2(Q(7),Q(-3));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0371():
    a=Vec2(Q(15),Q(9));b=Vec2(Q(19),Q(10))
    c=a+Vec2(Q(1),Q(-4));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0372():
    a=Vec2(Q(16),Q(10));b=Vec2(Q(21),Q(12))
    c=a+Vec2(Q(2),Q(-5));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0373():
    a=Vec2(Q(17),Q(11));b=Vec2(Q(23),Q(14))
    c=a+Vec2(Q(3),Q(-6));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0374():
    a=Vec2(Q(1),Q(12));b=Vec2(Q(8),Q(16))
    c=a+Vec2(Q(4),Q(-7));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0375():
    a=Vec2(Q(2),Q(13));b=Vec2(Q(10),Q(18))
    c=a+Vec2(Q(5),Q(-8));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0376():
    a=Vec2(Q(3),Q(14));b=Vec2(Q(12),Q(20))
    c=a+Vec2(Q(6),Q(-9));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0377():
    a=Vec2(Q(4),Q(2));b=Vec2(Q(14),Q(9))
    c=a+Vec2(Q(7),Q(-10));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0378():
    a=Vec2(Q(5),Q(3));b=Vec2(Q(16),Q(4))
    c=a+Vec2(Q(1),Q(-11));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0379():
    a=Vec2(Q(6),Q(4));b=Vec2(Q(18),Q(6))
    c=a+Vec2(Q(2),Q(-12));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0380():
    a=Vec2(Q(7),Q(5));b=Vec2(Q(20),Q(8))
    c=a+Vec2(Q(3),Q(-13));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0381():
    a=Vec2(Q(8),Q(6));b=Vec2(Q(22),Q(10))
    c=a+Vec2(Q(4),Q(-14));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0382():
    a=Vec2(Q(9),Q(7));b=Vec2(Q(24),Q(12))
    c=a+Vec2(Q(5),Q(-15));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0383():
    a=Vec2(Q(10),Q(8));b=Vec2(Q(26),Q(14))
    c=a+Vec2(Q(6),Q(-16));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0384():
    a=Vec2(Q(11),Q(9));b=Vec2(Q(28),Q(16))
    c=a+Vec2(Q(7),Q(-17));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0385():
    a=Vec2(Q(12),Q(10));b=Vec2(Q(30),Q(11))
    c=a+Vec2(Q(1),Q(-18));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0386():
    a=Vec2(Q(13),Q(11));b=Vec2(Q(32),Q(13))
    c=a+Vec2(Q(2),Q(-19));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0387():
    a=Vec2(Q(14),Q(12));b=Vec2(Q(34),Q(15))
    c=a+Vec2(Q(3),Q(-20));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0388():
    a=Vec2(Q(15),Q(13));b=Vec2(Q(36),Q(17))
    c=a+Vec2(Q(4),Q(-21));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0389():
    a=Vec2(Q(16),Q(14));b=Vec2(Q(38),Q(19))
    c=a+Vec2(Q(5),Q(-22));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0390():
    a=Vec2(Q(17),Q(2));b=Vec2(Q(40),Q(8))
    c=a+Vec2(Q(6),Q(-23));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0391():
    a=Vec2(Q(1),Q(3));b=Vec2(Q(2),Q(10))
    c=a+Vec2(Q(7),Q(-1));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0392():
    a=Vec2(Q(2),Q(4));b=Vec2(Q(4),Q(5))
    c=a+Vec2(Q(1),Q(-2));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0393():
    a=Vec2(Q(3),Q(5));b=Vec2(Q(6),Q(7))
    c=a+Vec2(Q(2),Q(-3));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0394():
    a=Vec2(Q(4),Q(6));b=Vec2(Q(8),Q(9))
    c=a+Vec2(Q(3),Q(-4));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0395():
    a=Vec2(Q(5),Q(7));b=Vec2(Q(10),Q(11))
    c=a+Vec2(Q(4),Q(-5));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0396():
    a=Vec2(Q(6),Q(8));b=Vec2(Q(12),Q(13))
    c=a+Vec2(Q(5),Q(-6));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0397():
    a=Vec2(Q(7),Q(9));b=Vec2(Q(14),Q(15))
    c=a+Vec2(Q(6),Q(-7));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0398():
    a=Vec2(Q(8),Q(10));b=Vec2(Q(16),Q(17))
    c=a+Vec2(Q(7),Q(-8));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0399():
    a=Vec2(Q(9),Q(11));b=Vec2(Q(18),Q(12))
    c=a+Vec2(Q(1),Q(-9));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0400():
    a=Vec2(Q(10),Q(12));b=Vec2(Q(20),Q(14))
    c=a+Vec2(Q(2),Q(-10));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0401():
    a=Vec2(Q(11),Q(13));b=Vec2(Q(22),Q(16))
    c=a+Vec2(Q(3),Q(-11));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0402():
    a=Vec2(Q(12),Q(14));b=Vec2(Q(24),Q(18))
    c=a+Vec2(Q(4),Q(-12));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0403():
    a=Vec2(Q(13),Q(2));b=Vec2(Q(26),Q(7))
    c=a+Vec2(Q(5),Q(-13));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0404():
    a=Vec2(Q(14),Q(3));b=Vec2(Q(28),Q(9))
    c=a+Vec2(Q(6),Q(-14));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0405():
    a=Vec2(Q(15),Q(4));b=Vec2(Q(30),Q(11))
    c=a+Vec2(Q(7),Q(-15));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0406():
    a=Vec2(Q(16),Q(5));b=Vec2(Q(32),Q(6))
    c=a+Vec2(Q(1),Q(-16));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0407():
    a=Vec2(Q(17),Q(6));b=Vec2(Q(34),Q(8))
    c=a+Vec2(Q(2),Q(-17));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0408():
    a=Vec2(Q(1),Q(7));b=Vec2(Q(19),Q(10))
    c=a+Vec2(Q(3),Q(-18));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0409():
    a=Vec2(Q(2),Q(8));b=Vec2(Q(21),Q(12))
    c=a+Vec2(Q(4),Q(-19));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0410():
    a=Vec2(Q(3),Q(9));b=Vec2(Q(23),Q(14))
    c=a+Vec2(Q(5),Q(-20));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0411():
    a=Vec2(Q(4),Q(10));b=Vec2(Q(25),Q(16))
    c=a+Vec2(Q(6),Q(-21));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0412():
    a=Vec2(Q(5),Q(11));b=Vec2(Q(27),Q(18))
    c=a+Vec2(Q(7),Q(-22));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0413():
    a=Vec2(Q(6),Q(12));b=Vec2(Q(29),Q(13))
    c=a+Vec2(Q(1),Q(-23));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0414():
    a=Vec2(Q(7),Q(13));b=Vec2(Q(8),Q(15))
    c=a+Vec2(Q(2),Q(-1));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0415():
    a=Vec2(Q(8),Q(14));b=Vec2(Q(10),Q(17))
    c=a+Vec2(Q(3),Q(-2));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0416():
    a=Vec2(Q(9),Q(2));b=Vec2(Q(12),Q(6))
    c=a+Vec2(Q(4),Q(-3));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0417():
    a=Vec2(Q(10),Q(3));b=Vec2(Q(14),Q(8))
    c=a+Vec2(Q(5),Q(-4));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0418():
    a=Vec2(Q(11),Q(4));b=Vec2(Q(16),Q(10))
    c=a+Vec2(Q(6),Q(-5));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0419():
    a=Vec2(Q(12),Q(5));b=Vec2(Q(18),Q(12))
    c=a+Vec2(Q(7),Q(-6));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0420():
    a=Vec2(Q(13),Q(6));b=Vec2(Q(20),Q(7))
    c=a+Vec2(Q(1),Q(-7));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0421():
    a=Vec2(Q(14),Q(7));b=Vec2(Q(22),Q(9))
    c=a+Vec2(Q(2),Q(-8));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0422():
    a=Vec2(Q(15),Q(8));b=Vec2(Q(24),Q(11))
    c=a+Vec2(Q(3),Q(-9));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0423():
    a=Vec2(Q(16),Q(9));b=Vec2(Q(26),Q(13))
    c=a+Vec2(Q(4),Q(-10));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0424():
    a=Vec2(Q(17),Q(10));b=Vec2(Q(28),Q(15))
    c=a+Vec2(Q(5),Q(-11));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0425():
    a=Vec2(Q(1),Q(11));b=Vec2(Q(13),Q(17))
    c=a+Vec2(Q(6),Q(-12));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0426():
    a=Vec2(Q(2),Q(12));b=Vec2(Q(15),Q(19))
    c=a+Vec2(Q(7),Q(-13));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0427():
    a=Vec2(Q(3),Q(13));b=Vec2(Q(17),Q(14))
    c=a+Vec2(Q(1),Q(-14));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0428():
    a=Vec2(Q(4),Q(14));b=Vec2(Q(19),Q(16))
    c=a+Vec2(Q(2),Q(-15));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0429():
    a=Vec2(Q(5),Q(2));b=Vec2(Q(21),Q(5))
    c=a+Vec2(Q(3),Q(-16));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0430():
    a=Vec2(Q(6),Q(3));b=Vec2(Q(23),Q(7))
    c=a+Vec2(Q(4),Q(-17));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0431():
    a=Vec2(Q(7),Q(4));b=Vec2(Q(25),Q(9))
    c=a+Vec2(Q(5),Q(-18));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0432():
    a=Vec2(Q(8),Q(5));b=Vec2(Q(27),Q(11))
    c=a+Vec2(Q(6),Q(-19));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0433():
    a=Vec2(Q(9),Q(6));b=Vec2(Q(29),Q(13))
    c=a+Vec2(Q(7),Q(-20));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0434():
    a=Vec2(Q(10),Q(7));b=Vec2(Q(31),Q(8))
    c=a+Vec2(Q(1),Q(-21));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0435():
    a=Vec2(Q(11),Q(8));b=Vec2(Q(33),Q(10))
    c=a+Vec2(Q(2),Q(-22));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0436():
    a=Vec2(Q(12),Q(9));b=Vec2(Q(35),Q(12))
    c=a+Vec2(Q(3),Q(-23));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0437():
    a=Vec2(Q(13),Q(10));b=Vec2(Q(14),Q(14))
    c=a+Vec2(Q(4),Q(-1));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0438():
    a=Vec2(Q(14),Q(11));b=Vec2(Q(16),Q(16))
    c=a+Vec2(Q(5),Q(-2));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0439():
    a=Vec2(Q(15),Q(12));b=Vec2(Q(18),Q(18))
    c=a+Vec2(Q(6),Q(-3));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0440():
    a=Vec2(Q(16),Q(13));b=Vec2(Q(20),Q(20))
    c=a+Vec2(Q(7),Q(-4));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0441():
    a=Vec2(Q(17),Q(14));b=Vec2(Q(22),Q(15))
    c=a+Vec2(Q(1),Q(-5));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0442():
    a=Vec2(Q(1),Q(2));b=Vec2(Q(7),Q(4))
    c=a+Vec2(Q(2),Q(-6));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0443():
    a=Vec2(Q(2),Q(3));b=Vec2(Q(9),Q(6))
    c=a+Vec2(Q(3),Q(-7));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0444():
    a=Vec2(Q(3),Q(4));b=Vec2(Q(11),Q(8))
    c=a+Vec2(Q(4),Q(-8));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0445():
    a=Vec2(Q(4),Q(5));b=Vec2(Q(13),Q(10))
    c=a+Vec2(Q(5),Q(-9));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0446():
    a=Vec2(Q(5),Q(6));b=Vec2(Q(15),Q(12))
    c=a+Vec2(Q(6),Q(-10));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0447():
    a=Vec2(Q(6),Q(7));b=Vec2(Q(17),Q(14))
    c=a+Vec2(Q(7),Q(-11));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0448():
    a=Vec2(Q(7),Q(8));b=Vec2(Q(19),Q(9))
    c=a+Vec2(Q(1),Q(-12));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0449():
    a=Vec2(Q(8),Q(9));b=Vec2(Q(21),Q(11))
    c=a+Vec2(Q(2),Q(-13));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0450():
    a=Vec2(Q(9),Q(10));b=Vec2(Q(23),Q(13))
    c=a+Vec2(Q(3),Q(-14));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0451():
    a=Vec2(Q(10),Q(11));b=Vec2(Q(25),Q(15))
    c=a+Vec2(Q(4),Q(-15));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0452():
    a=Vec2(Q(11),Q(12));b=Vec2(Q(27),Q(17))
    c=a+Vec2(Q(5),Q(-16));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0453():
    a=Vec2(Q(12),Q(13));b=Vec2(Q(29),Q(19))
    c=a+Vec2(Q(6),Q(-17));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0454():
    a=Vec2(Q(13),Q(14));b=Vec2(Q(31),Q(21))
    c=a+Vec2(Q(7),Q(-18));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0455():
    a=Vec2(Q(14),Q(2));b=Vec2(Q(33),Q(3))
    c=a+Vec2(Q(1),Q(-19));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0456():
    a=Vec2(Q(15),Q(3));b=Vec2(Q(35),Q(5))
    c=a+Vec2(Q(2),Q(-20));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0457():
    a=Vec2(Q(16),Q(4));b=Vec2(Q(37),Q(7))
    c=a+Vec2(Q(3),Q(-21));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0458():
    a=Vec2(Q(17),Q(5));b=Vec2(Q(39),Q(9))
    c=a+Vec2(Q(4),Q(-22));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0459():
    a=Vec2(Q(1),Q(6));b=Vec2(Q(24),Q(11))
    c=a+Vec2(Q(5),Q(-23));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0460():
    a=Vec2(Q(2),Q(7));b=Vec2(Q(3),Q(13))
    c=a+Vec2(Q(6),Q(-1));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0461():
    a=Vec2(Q(3),Q(8));b=Vec2(Q(5),Q(15))
    c=a+Vec2(Q(7),Q(-2));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0462():
    a=Vec2(Q(4),Q(9));b=Vec2(Q(7),Q(10))
    c=a+Vec2(Q(1),Q(-3));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0463():
    a=Vec2(Q(5),Q(10));b=Vec2(Q(9),Q(12))
    c=a+Vec2(Q(2),Q(-4));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0464():
    a=Vec2(Q(6),Q(11));b=Vec2(Q(11),Q(14))
    c=a+Vec2(Q(3),Q(-5));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0465():
    a=Vec2(Q(7),Q(12));b=Vec2(Q(13),Q(16))
    c=a+Vec2(Q(4),Q(-6));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0466():
    a=Vec2(Q(8),Q(13));b=Vec2(Q(15),Q(18))
    c=a+Vec2(Q(5),Q(-7));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0467():
    a=Vec2(Q(9),Q(14));b=Vec2(Q(17),Q(20))
    c=a+Vec2(Q(6),Q(-8));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0468():
    a=Vec2(Q(10),Q(2));b=Vec2(Q(19),Q(9))
    c=a+Vec2(Q(7),Q(-9));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0469():
    a=Vec2(Q(11),Q(3));b=Vec2(Q(21),Q(4))
    c=a+Vec2(Q(1),Q(-10));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0470():
    a=Vec2(Q(12),Q(4));b=Vec2(Q(23),Q(6))
    c=a+Vec2(Q(2),Q(-11));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0471():
    a=Vec2(Q(13),Q(5));b=Vec2(Q(25),Q(8))
    c=a+Vec2(Q(3),Q(-12));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0472():
    a=Vec2(Q(14),Q(6));b=Vec2(Q(27),Q(10))
    c=a+Vec2(Q(4),Q(-13));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0473():
    a=Vec2(Q(15),Q(7));b=Vec2(Q(29),Q(12))
    c=a+Vec2(Q(5),Q(-14));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0474():
    a=Vec2(Q(16),Q(8));b=Vec2(Q(31),Q(14))
    c=a+Vec2(Q(6),Q(-15));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0475():
    a=Vec2(Q(17),Q(9));b=Vec2(Q(33),Q(16))
    c=a+Vec2(Q(7),Q(-16));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0476():
    a=Vec2(Q(1),Q(10));b=Vec2(Q(18),Q(11))
    c=a+Vec2(Q(1),Q(-17));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0477():
    a=Vec2(Q(2),Q(11));b=Vec2(Q(20),Q(13))
    c=a+Vec2(Q(2),Q(-18));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0478():
    a=Vec2(Q(3),Q(12));b=Vec2(Q(22),Q(15))
    c=a+Vec2(Q(3),Q(-19));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0479():
    a=Vec2(Q(4),Q(13));b=Vec2(Q(24),Q(17))
    c=a+Vec2(Q(4),Q(-20));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0480():
    a=Vec2(Q(5),Q(14));b=Vec2(Q(26),Q(19))
    c=a+Vec2(Q(5),Q(-21));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0481():
    a=Vec2(Q(6),Q(2));b=Vec2(Q(28),Q(8))
    c=a+Vec2(Q(6),Q(-22));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0482():
    a=Vec2(Q(7),Q(3));b=Vec2(Q(30),Q(10))
    c=a+Vec2(Q(7),Q(-23));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0483():
    a=Vec2(Q(8),Q(4));b=Vec2(Q(9),Q(5))
    c=a+Vec2(Q(1),Q(-1));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0484():
    a=Vec2(Q(9),Q(5));b=Vec2(Q(11),Q(7))
    c=a+Vec2(Q(2),Q(-2));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0485():
    a=Vec2(Q(10),Q(6));b=Vec2(Q(13),Q(9))
    c=a+Vec2(Q(3),Q(-3));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0486():
    a=Vec2(Q(11),Q(7));b=Vec2(Q(15),Q(11))
    c=a+Vec2(Q(4),Q(-4));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0487():
    a=Vec2(Q(12),Q(8));b=Vec2(Q(17),Q(13))
    c=a+Vec2(Q(5),Q(-5));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0488():
    a=Vec2(Q(13),Q(9));b=Vec2(Q(19),Q(15))
    c=a+Vec2(Q(6),Q(-6));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0489():
    a=Vec2(Q(14),Q(10));b=Vec2(Q(21),Q(17))
    c=a+Vec2(Q(7),Q(-7));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0490():
    a=Vec2(Q(15),Q(11));b=Vec2(Q(23),Q(12))
    c=a+Vec2(Q(1),Q(-8));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0491():
    a=Vec2(Q(16),Q(12));b=Vec2(Q(25),Q(14))
    c=a+Vec2(Q(2),Q(-9));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0492():
    a=Vec2(Q(17),Q(13));b=Vec2(Q(27),Q(16))
    c=a+Vec2(Q(3),Q(-10));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0493():
    a=Vec2(Q(1),Q(14));b=Vec2(Q(12),Q(18))
    c=a+Vec2(Q(4),Q(-11));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0494():
    a=Vec2(Q(2),Q(2));b=Vec2(Q(14),Q(7))
    c=a+Vec2(Q(5),Q(-12));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0495():
    a=Vec2(Q(3),Q(3));b=Vec2(Q(16),Q(9))
    c=a+Vec2(Q(6),Q(-13));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0496():
    a=Vec2(Q(4),Q(4));b=Vec2(Q(18),Q(11))
    c=a+Vec2(Q(7),Q(-14));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0497():
    a=Vec2(Q(5),Q(5));b=Vec2(Q(20),Q(6))
    c=a+Vec2(Q(1),Q(-15));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0498():
    a=Vec2(Q(6),Q(6));b=Vec2(Q(22),Q(8))
    c=a+Vec2(Q(2),Q(-16));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0499():
    a=Vec2(Q(7),Q(7));b=Vec2(Q(24),Q(10))
    c=a+Vec2(Q(3),Q(-17));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0500():
    a=Vec2(Q(8),Q(8));b=Vec2(Q(26),Q(12))
    c=a+Vec2(Q(4),Q(-18));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0501():
    a=Vec2(Q(9),Q(9));b=Vec2(Q(28),Q(14))
    c=a+Vec2(Q(5),Q(-19));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0502():
    a=Vec2(Q(10),Q(10));b=Vec2(Q(30),Q(16))
    c=a+Vec2(Q(6),Q(-20));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0503():
    a=Vec2(Q(11),Q(11));b=Vec2(Q(32),Q(18))
    c=a+Vec2(Q(7),Q(-21));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0504():
    a=Vec2(Q(12),Q(12));b=Vec2(Q(34),Q(13))
    c=a+Vec2(Q(1),Q(-22));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0505():
    a=Vec2(Q(13),Q(13));b=Vec2(Q(36),Q(15))
    c=a+Vec2(Q(2),Q(-23));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0506():
    a=Vec2(Q(14),Q(14));b=Vec2(Q(15),Q(17))
    c=a+Vec2(Q(3),Q(-1));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0507():
    a=Vec2(Q(15),Q(2));b=Vec2(Q(17),Q(6))
    c=a+Vec2(Q(4),Q(-2));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0508():
    a=Vec2(Q(16),Q(3));b=Vec2(Q(19),Q(8))
    c=a+Vec2(Q(5),Q(-3));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0509():
    a=Vec2(Q(17),Q(4));b=Vec2(Q(21),Q(10))
    c=a+Vec2(Q(6),Q(-4));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0510():
    a=Vec2(Q(1),Q(5));b=Vec2(Q(6),Q(12))
    c=a+Vec2(Q(7),Q(-5));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0511():
    a=Vec2(Q(2),Q(6));b=Vec2(Q(8),Q(7))
    c=a+Vec2(Q(1),Q(-6));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0512():
    a=Vec2(Q(3),Q(7));b=Vec2(Q(10),Q(9))
    c=a+Vec2(Q(2),Q(-7));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0513():
    a=Vec2(Q(4),Q(8));b=Vec2(Q(12),Q(11))
    c=a+Vec2(Q(3),Q(-8));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0514():
    a=Vec2(Q(5),Q(9));b=Vec2(Q(14),Q(13))
    c=a+Vec2(Q(4),Q(-9));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0515():
    a=Vec2(Q(6),Q(10));b=Vec2(Q(16),Q(15))
    c=a+Vec2(Q(5),Q(-10));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0516():
    a=Vec2(Q(7),Q(11));b=Vec2(Q(18),Q(17))
    c=a+Vec2(Q(6),Q(-11));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0517():
    a=Vec2(Q(8),Q(12));b=Vec2(Q(20),Q(19))
    c=a+Vec2(Q(7),Q(-12));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0518():
    a=Vec2(Q(9),Q(13));b=Vec2(Q(22),Q(14))
    c=a+Vec2(Q(1),Q(-13));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0519():
    a=Vec2(Q(10),Q(14));b=Vec2(Q(24),Q(16))
    c=a+Vec2(Q(2),Q(-14));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0520():
    a=Vec2(Q(11),Q(2));b=Vec2(Q(26),Q(5))
    c=a+Vec2(Q(3),Q(-15));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0521():
    a=Vec2(Q(12),Q(3));b=Vec2(Q(28),Q(7))
    c=a+Vec2(Q(4),Q(-16));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0522():
    a=Vec2(Q(13),Q(4));b=Vec2(Q(30),Q(9))
    c=a+Vec2(Q(5),Q(-17));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0523():
    a=Vec2(Q(14),Q(5));b=Vec2(Q(32),Q(11))
    c=a+Vec2(Q(6),Q(-18));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0524():
    a=Vec2(Q(15),Q(6));b=Vec2(Q(34),Q(13))
    c=a+Vec2(Q(7),Q(-19));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0525():
    a=Vec2(Q(16),Q(7));b=Vec2(Q(36),Q(8))
    c=a+Vec2(Q(1),Q(-20));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0526():
    a=Vec2(Q(17),Q(8));b=Vec2(Q(38),Q(10))
    c=a+Vec2(Q(2),Q(-21));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0527():
    a=Vec2(Q(1),Q(9));b=Vec2(Q(23),Q(12))
    c=a+Vec2(Q(3),Q(-22));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0528():
    a=Vec2(Q(2),Q(10));b=Vec2(Q(25),Q(14))
    c=a+Vec2(Q(4),Q(-23));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0529():
    a=Vec2(Q(3),Q(11));b=Vec2(Q(4),Q(16))
    c=a+Vec2(Q(5),Q(-1));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0530():
    a=Vec2(Q(4),Q(12));b=Vec2(Q(6),Q(18))
    c=a+Vec2(Q(6),Q(-2));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0531():
    a=Vec2(Q(5),Q(13));b=Vec2(Q(8),Q(20))
    c=a+Vec2(Q(7),Q(-3));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0532():
    a=Vec2(Q(6),Q(14));b=Vec2(Q(10),Q(15))
    c=a+Vec2(Q(1),Q(-4));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0533():
    a=Vec2(Q(7),Q(2));b=Vec2(Q(12),Q(4))
    c=a+Vec2(Q(2),Q(-5));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0534():
    a=Vec2(Q(8),Q(3));b=Vec2(Q(14),Q(6))
    c=a+Vec2(Q(3),Q(-6));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0535():
    a=Vec2(Q(9),Q(4));b=Vec2(Q(16),Q(8))
    c=a+Vec2(Q(4),Q(-7));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0536():
    a=Vec2(Q(10),Q(5));b=Vec2(Q(18),Q(10))
    c=a+Vec2(Q(5),Q(-8));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0537():
    a=Vec2(Q(11),Q(6));b=Vec2(Q(20),Q(12))
    c=a+Vec2(Q(6),Q(-9));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0538():
    a=Vec2(Q(12),Q(7));b=Vec2(Q(22),Q(14))
    c=a+Vec2(Q(7),Q(-10));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0539():
    a=Vec2(Q(13),Q(8));b=Vec2(Q(24),Q(9))
    c=a+Vec2(Q(1),Q(-11));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0540():
    a=Vec2(Q(14),Q(9));b=Vec2(Q(26),Q(11))
    c=a+Vec2(Q(2),Q(-12));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0541():
    a=Vec2(Q(15),Q(10));b=Vec2(Q(28),Q(13))
    c=a+Vec2(Q(3),Q(-13));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0542():
    a=Vec2(Q(16),Q(11));b=Vec2(Q(30),Q(15))
    c=a+Vec2(Q(4),Q(-14));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0543():
    a=Vec2(Q(17),Q(12));b=Vec2(Q(32),Q(17))
    c=a+Vec2(Q(5),Q(-15));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0544():
    a=Vec2(Q(1),Q(13));b=Vec2(Q(17),Q(19))
    c=a+Vec2(Q(6),Q(-16));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0545():
    a=Vec2(Q(2),Q(14));b=Vec2(Q(19),Q(21))
    c=a+Vec2(Q(7),Q(-17));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0546():
    a=Vec2(Q(3),Q(2));b=Vec2(Q(21),Q(3))
    c=a+Vec2(Q(1),Q(-18));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0547():
    a=Vec2(Q(4),Q(3));b=Vec2(Q(23),Q(5))
    c=a+Vec2(Q(2),Q(-19));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0548():
    a=Vec2(Q(5),Q(4));b=Vec2(Q(25),Q(7))
    c=a+Vec2(Q(3),Q(-20));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0549():
    a=Vec2(Q(6),Q(5));b=Vec2(Q(27),Q(9))
    c=a+Vec2(Q(4),Q(-21));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0550():
    a=Vec2(Q(7),Q(6));b=Vec2(Q(29),Q(11))
    c=a+Vec2(Q(5),Q(-22));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0551():
    a=Vec2(Q(8),Q(7));b=Vec2(Q(31),Q(13))
    c=a+Vec2(Q(6),Q(-23));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0552():
    a=Vec2(Q(9),Q(8));b=Vec2(Q(10),Q(15))
    c=a+Vec2(Q(7),Q(-1));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0553():
    a=Vec2(Q(10),Q(9));b=Vec2(Q(12),Q(10))
    c=a+Vec2(Q(1),Q(-2));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0554():
    a=Vec2(Q(11),Q(10));b=Vec2(Q(14),Q(12))
    c=a+Vec2(Q(2),Q(-3));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0555():
    a=Vec2(Q(12),Q(11));b=Vec2(Q(16),Q(14))
    c=a+Vec2(Q(3),Q(-4));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0556():
    a=Vec2(Q(13),Q(12));b=Vec2(Q(18),Q(16))
    c=a+Vec2(Q(4),Q(-5));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0557():
    a=Vec2(Q(14),Q(13));b=Vec2(Q(20),Q(18))
    c=a+Vec2(Q(5),Q(-6));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0558():
    a=Vec2(Q(15),Q(14));b=Vec2(Q(22),Q(20))
    c=a+Vec2(Q(6),Q(-7));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0559():
    a=Vec2(Q(16),Q(2));b=Vec2(Q(24),Q(9))
    c=a+Vec2(Q(7),Q(-8));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0560():
    a=Vec2(Q(17),Q(3));b=Vec2(Q(26),Q(4))
    c=a+Vec2(Q(1),Q(-9));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0561():
    a=Vec2(Q(1),Q(4));b=Vec2(Q(11),Q(6))
    c=a+Vec2(Q(2),Q(-10));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0562():
    a=Vec2(Q(2),Q(5));b=Vec2(Q(13),Q(8))
    c=a+Vec2(Q(3),Q(-11));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0563():
    a=Vec2(Q(3),Q(6));b=Vec2(Q(15),Q(10))
    c=a+Vec2(Q(4),Q(-12));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0564():
    a=Vec2(Q(4),Q(7));b=Vec2(Q(17),Q(12))
    c=a+Vec2(Q(5),Q(-13));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0565():
    a=Vec2(Q(5),Q(8));b=Vec2(Q(19),Q(14))
    c=a+Vec2(Q(6),Q(-14));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0566():
    a=Vec2(Q(6),Q(9));b=Vec2(Q(21),Q(16))
    c=a+Vec2(Q(7),Q(-15));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0567():
    a=Vec2(Q(7),Q(10));b=Vec2(Q(23),Q(11))
    c=a+Vec2(Q(1),Q(-16));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0568():
    a=Vec2(Q(8),Q(11));b=Vec2(Q(25),Q(13))
    c=a+Vec2(Q(2),Q(-17));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0569():
    a=Vec2(Q(9),Q(12));b=Vec2(Q(27),Q(15))
    c=a+Vec2(Q(3),Q(-18));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0570():
    a=Vec2(Q(10),Q(13));b=Vec2(Q(29),Q(17))
    c=a+Vec2(Q(4),Q(-19));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0571():
    a=Vec2(Q(11),Q(14));b=Vec2(Q(31),Q(19))
    c=a+Vec2(Q(5),Q(-20));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0572():
    a=Vec2(Q(12),Q(2));b=Vec2(Q(33),Q(8))
    c=a+Vec2(Q(6),Q(-21));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0573():
    a=Vec2(Q(13),Q(3));b=Vec2(Q(35),Q(10))
    c=a+Vec2(Q(7),Q(-22));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0574():
    a=Vec2(Q(14),Q(4));b=Vec2(Q(37),Q(5))
    c=a+Vec2(Q(1),Q(-23));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0575():
    a=Vec2(Q(15),Q(5));b=Vec2(Q(16),Q(7))
    c=a+Vec2(Q(2),Q(-1));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0576():
    a=Vec2(Q(16),Q(6));b=Vec2(Q(18),Q(9))
    c=a+Vec2(Q(3),Q(-2));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0577():
    a=Vec2(Q(17),Q(7));b=Vec2(Q(20),Q(11))
    c=a+Vec2(Q(4),Q(-3));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0578():
    a=Vec2(Q(1),Q(8));b=Vec2(Q(5),Q(13))
    c=a+Vec2(Q(5),Q(-4));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0579():
    a=Vec2(Q(2),Q(9));b=Vec2(Q(7),Q(15))
    c=a+Vec2(Q(6),Q(-5));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0580():
    a=Vec2(Q(3),Q(10));b=Vec2(Q(9),Q(17))
    c=a+Vec2(Q(7),Q(-6));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0581():
    a=Vec2(Q(4),Q(11));b=Vec2(Q(11),Q(12))
    c=a+Vec2(Q(1),Q(-7));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0582():
    a=Vec2(Q(5),Q(12));b=Vec2(Q(13),Q(14))
    c=a+Vec2(Q(2),Q(-8));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0583():
    a=Vec2(Q(6),Q(13));b=Vec2(Q(15),Q(16))
    c=a+Vec2(Q(3),Q(-9));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0584():
    a=Vec2(Q(7),Q(14));b=Vec2(Q(17),Q(18))
    c=a+Vec2(Q(4),Q(-10));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0585():
    a=Vec2(Q(8),Q(2));b=Vec2(Q(19),Q(7))
    c=a+Vec2(Q(5),Q(-11));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0586():
    a=Vec2(Q(9),Q(3));b=Vec2(Q(21),Q(9))
    c=a+Vec2(Q(6),Q(-12));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0587():
    a=Vec2(Q(10),Q(4));b=Vec2(Q(23),Q(11))
    c=a+Vec2(Q(7),Q(-13));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0588():
    a=Vec2(Q(11),Q(5));b=Vec2(Q(25),Q(6))
    c=a+Vec2(Q(1),Q(-14));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0589():
    a=Vec2(Q(12),Q(6));b=Vec2(Q(27),Q(8))
    c=a+Vec2(Q(2),Q(-15));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0590():
    a=Vec2(Q(13),Q(7));b=Vec2(Q(29),Q(10))
    c=a+Vec2(Q(3),Q(-16));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0591():
    a=Vec2(Q(14),Q(8));b=Vec2(Q(31),Q(12))
    c=a+Vec2(Q(4),Q(-17));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0592():
    a=Vec2(Q(15),Q(9));b=Vec2(Q(33),Q(14))
    c=a+Vec2(Q(5),Q(-18));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0593():
    a=Vec2(Q(16),Q(10));b=Vec2(Q(35),Q(16))
    c=a+Vec2(Q(6),Q(-19));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0594():
    a=Vec2(Q(17),Q(11));b=Vec2(Q(37),Q(18))
    c=a+Vec2(Q(7),Q(-20));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0595():
    a=Vec2(Q(1),Q(12));b=Vec2(Q(22),Q(13))
    c=a+Vec2(Q(1),Q(-21));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0596():
    a=Vec2(Q(2),Q(13));b=Vec2(Q(24),Q(15))
    c=a+Vec2(Q(2),Q(-22));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0597():
    a=Vec2(Q(3),Q(14));b=Vec2(Q(26),Q(17))
    c=a+Vec2(Q(3),Q(-23));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0598():
    a=Vec2(Q(4),Q(2));b=Vec2(Q(5),Q(6))
    c=a+Vec2(Q(4),Q(-1));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

def test_equal_lengths_0599():
    a=Vec2(Q(5),Q(3));b=Vec2(Q(7),Q(8))
    c=a+Vec2(Q(5),Q(-2));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()

