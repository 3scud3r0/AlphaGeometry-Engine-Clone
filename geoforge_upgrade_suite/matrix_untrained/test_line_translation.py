# GENERATED, DETERMINISTIC, NO TRAINED MODEL USED.
# Source generator: geoforge_upgrade_suite/generate_untrained_matrix.py
from fractions import Fraction as Q
from geoforge_upgrade_suite.geometry_exact import Vec2,Polynomial,Line
from geoforge_upgrade_suite.exact_constructions import SPoint,foot,line_intersection
from geoforge_upgrade_suite.deterministic_ideal import ExactIdealEngine,certificate_to_json,verify_certificate_json
from geoforge_upgrade_suite.deterministic_solver import ExactFactEvaluator,GuardLedger

def test_line_translation_0000():
    a=Vec2(Q(1),Q(2));b=a+Vec2(Q(1),Q(1))
    shift=Vec2(Q(1),Q(-1))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0001():
    a=Vec2(Q(2),Q(3));b=a+Vec2(Q(2),Q(2))
    shift=Vec2(Q(2),Q(-2))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0002():
    a=Vec2(Q(3),Q(4));b=a+Vec2(Q(3),Q(3))
    shift=Vec2(Q(3),Q(-3))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0003():
    a=Vec2(Q(4),Q(5));b=a+Vec2(Q(4),Q(4))
    shift=Vec2(Q(4),Q(-4))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0004():
    a=Vec2(Q(5),Q(6));b=a+Vec2(Q(5),Q(5))
    shift=Vec2(Q(5),Q(-5))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0005():
    a=Vec2(Q(6),Q(7));b=a+Vec2(Q(6),Q(6))
    shift=Vec2(Q(6),Q(-6))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0006():
    a=Vec2(Q(7),Q(8));b=a+Vec2(Q(7),Q(7))
    shift=Vec2(Q(7),Q(-7))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0007():
    a=Vec2(Q(8),Q(9));b=a+Vec2(Q(8),Q(1))
    shift=Vec2(Q(1),Q(-8))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0008():
    a=Vec2(Q(9),Q(10));b=a+Vec2(Q(9),Q(2))
    shift=Vec2(Q(2),Q(-9))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0009():
    a=Vec2(Q(10),Q(11));b=a+Vec2(Q(10),Q(3))
    shift=Vec2(Q(3),Q(-10))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0010():
    a=Vec2(Q(11),Q(12));b=a+Vec2(Q(11),Q(4))
    shift=Vec2(Q(4),Q(-11))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0011():
    a=Vec2(Q(12),Q(13));b=a+Vec2(Q(12),Q(5))
    shift=Vec2(Q(5),Q(-12))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0012():
    a=Vec2(Q(13),Q(14));b=a+Vec2(Q(13),Q(6))
    shift=Vec2(Q(6),Q(-13))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0013():
    a=Vec2(Q(14),Q(2));b=a+Vec2(Q(14),Q(7))
    shift=Vec2(Q(7),Q(-14))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0014():
    a=Vec2(Q(15),Q(3));b=a+Vec2(Q(15),Q(1))
    shift=Vec2(Q(1),Q(-15))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0015():
    a=Vec2(Q(16),Q(4));b=a+Vec2(Q(16),Q(2))
    shift=Vec2(Q(2),Q(-16))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0016():
    a=Vec2(Q(17),Q(5));b=a+Vec2(Q(17),Q(3))
    shift=Vec2(Q(3),Q(-17))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0017():
    a=Vec2(Q(1),Q(6));b=a+Vec2(Q(18),Q(4))
    shift=Vec2(Q(4),Q(-18))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0018():
    a=Vec2(Q(2),Q(7));b=a+Vec2(Q(19),Q(5))
    shift=Vec2(Q(5),Q(-19))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0019():
    a=Vec2(Q(3),Q(8));b=a+Vec2(Q(20),Q(6))
    shift=Vec2(Q(6),Q(-20))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0020():
    a=Vec2(Q(4),Q(9));b=a+Vec2(Q(21),Q(7))
    shift=Vec2(Q(7),Q(-21))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0021():
    a=Vec2(Q(5),Q(10));b=a+Vec2(Q(22),Q(1))
    shift=Vec2(Q(1),Q(-22))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0022():
    a=Vec2(Q(6),Q(11));b=a+Vec2(Q(23),Q(2))
    shift=Vec2(Q(2),Q(-23))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0023():
    a=Vec2(Q(7),Q(12));b=a+Vec2(Q(1),Q(3))
    shift=Vec2(Q(3),Q(-1))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0024():
    a=Vec2(Q(8),Q(13));b=a+Vec2(Q(2),Q(4))
    shift=Vec2(Q(4),Q(-2))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0025():
    a=Vec2(Q(9),Q(14));b=a+Vec2(Q(3),Q(5))
    shift=Vec2(Q(5),Q(-3))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0026():
    a=Vec2(Q(10),Q(2));b=a+Vec2(Q(4),Q(6))
    shift=Vec2(Q(6),Q(-4))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0027():
    a=Vec2(Q(11),Q(3));b=a+Vec2(Q(5),Q(7))
    shift=Vec2(Q(7),Q(-5))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0028():
    a=Vec2(Q(12),Q(4));b=a+Vec2(Q(6),Q(1))
    shift=Vec2(Q(1),Q(-6))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0029():
    a=Vec2(Q(13),Q(5));b=a+Vec2(Q(7),Q(2))
    shift=Vec2(Q(2),Q(-7))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0030():
    a=Vec2(Q(14),Q(6));b=a+Vec2(Q(8),Q(3))
    shift=Vec2(Q(3),Q(-8))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0031():
    a=Vec2(Q(15),Q(7));b=a+Vec2(Q(9),Q(4))
    shift=Vec2(Q(4),Q(-9))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0032():
    a=Vec2(Q(16),Q(8));b=a+Vec2(Q(10),Q(5))
    shift=Vec2(Q(5),Q(-10))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0033():
    a=Vec2(Q(17),Q(9));b=a+Vec2(Q(11),Q(6))
    shift=Vec2(Q(6),Q(-11))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0034():
    a=Vec2(Q(1),Q(10));b=a+Vec2(Q(12),Q(7))
    shift=Vec2(Q(7),Q(-12))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0035():
    a=Vec2(Q(2),Q(11));b=a+Vec2(Q(13),Q(1))
    shift=Vec2(Q(1),Q(-13))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0036():
    a=Vec2(Q(3),Q(12));b=a+Vec2(Q(14),Q(2))
    shift=Vec2(Q(2),Q(-14))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0037():
    a=Vec2(Q(4),Q(13));b=a+Vec2(Q(15),Q(3))
    shift=Vec2(Q(3),Q(-15))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0038():
    a=Vec2(Q(5),Q(14));b=a+Vec2(Q(16),Q(4))
    shift=Vec2(Q(4),Q(-16))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0039():
    a=Vec2(Q(6),Q(2));b=a+Vec2(Q(17),Q(5))
    shift=Vec2(Q(5),Q(-17))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0040():
    a=Vec2(Q(7),Q(3));b=a+Vec2(Q(18),Q(6))
    shift=Vec2(Q(6),Q(-18))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0041():
    a=Vec2(Q(8),Q(4));b=a+Vec2(Q(19),Q(7))
    shift=Vec2(Q(7),Q(-19))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0042():
    a=Vec2(Q(9),Q(5));b=a+Vec2(Q(20),Q(1))
    shift=Vec2(Q(1),Q(-20))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0043():
    a=Vec2(Q(10),Q(6));b=a+Vec2(Q(21),Q(2))
    shift=Vec2(Q(2),Q(-21))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0044():
    a=Vec2(Q(11),Q(7));b=a+Vec2(Q(22),Q(3))
    shift=Vec2(Q(3),Q(-22))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0045():
    a=Vec2(Q(12),Q(8));b=a+Vec2(Q(23),Q(4))
    shift=Vec2(Q(4),Q(-23))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0046():
    a=Vec2(Q(13),Q(9));b=a+Vec2(Q(1),Q(5))
    shift=Vec2(Q(5),Q(-1))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0047():
    a=Vec2(Q(14),Q(10));b=a+Vec2(Q(2),Q(6))
    shift=Vec2(Q(6),Q(-2))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0048():
    a=Vec2(Q(15),Q(11));b=a+Vec2(Q(3),Q(7))
    shift=Vec2(Q(7),Q(-3))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0049():
    a=Vec2(Q(16),Q(12));b=a+Vec2(Q(4),Q(1))
    shift=Vec2(Q(1),Q(-4))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0050():
    a=Vec2(Q(17),Q(13));b=a+Vec2(Q(5),Q(2))
    shift=Vec2(Q(2),Q(-5))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0051():
    a=Vec2(Q(1),Q(14));b=a+Vec2(Q(6),Q(3))
    shift=Vec2(Q(3),Q(-6))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0052():
    a=Vec2(Q(2),Q(2));b=a+Vec2(Q(7),Q(4))
    shift=Vec2(Q(4),Q(-7))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0053():
    a=Vec2(Q(3),Q(3));b=a+Vec2(Q(8),Q(5))
    shift=Vec2(Q(5),Q(-8))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0054():
    a=Vec2(Q(4),Q(4));b=a+Vec2(Q(9),Q(6))
    shift=Vec2(Q(6),Q(-9))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0055():
    a=Vec2(Q(5),Q(5));b=a+Vec2(Q(10),Q(7))
    shift=Vec2(Q(7),Q(-10))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0056():
    a=Vec2(Q(6),Q(6));b=a+Vec2(Q(11),Q(1))
    shift=Vec2(Q(1),Q(-11))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0057():
    a=Vec2(Q(7),Q(7));b=a+Vec2(Q(12),Q(2))
    shift=Vec2(Q(2),Q(-12))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0058():
    a=Vec2(Q(8),Q(8));b=a+Vec2(Q(13),Q(3))
    shift=Vec2(Q(3),Q(-13))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0059():
    a=Vec2(Q(9),Q(9));b=a+Vec2(Q(14),Q(4))
    shift=Vec2(Q(4),Q(-14))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0060():
    a=Vec2(Q(10),Q(10));b=a+Vec2(Q(15),Q(5))
    shift=Vec2(Q(5),Q(-15))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0061():
    a=Vec2(Q(11),Q(11));b=a+Vec2(Q(16),Q(6))
    shift=Vec2(Q(6),Q(-16))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0062():
    a=Vec2(Q(12),Q(12));b=a+Vec2(Q(17),Q(7))
    shift=Vec2(Q(7),Q(-17))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0063():
    a=Vec2(Q(13),Q(13));b=a+Vec2(Q(18),Q(1))
    shift=Vec2(Q(1),Q(-18))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0064():
    a=Vec2(Q(14),Q(14));b=a+Vec2(Q(19),Q(2))
    shift=Vec2(Q(2),Q(-19))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0065():
    a=Vec2(Q(15),Q(2));b=a+Vec2(Q(20),Q(3))
    shift=Vec2(Q(3),Q(-20))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0066():
    a=Vec2(Q(16),Q(3));b=a+Vec2(Q(21),Q(4))
    shift=Vec2(Q(4),Q(-21))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0067():
    a=Vec2(Q(17),Q(4));b=a+Vec2(Q(22),Q(5))
    shift=Vec2(Q(5),Q(-22))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0068():
    a=Vec2(Q(1),Q(5));b=a+Vec2(Q(23),Q(6))
    shift=Vec2(Q(6),Q(-23))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0069():
    a=Vec2(Q(2),Q(6));b=a+Vec2(Q(1),Q(7))
    shift=Vec2(Q(7),Q(-1))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0070():
    a=Vec2(Q(3),Q(7));b=a+Vec2(Q(2),Q(1))
    shift=Vec2(Q(1),Q(-2))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0071():
    a=Vec2(Q(4),Q(8));b=a+Vec2(Q(3),Q(2))
    shift=Vec2(Q(2),Q(-3))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0072():
    a=Vec2(Q(5),Q(9));b=a+Vec2(Q(4),Q(3))
    shift=Vec2(Q(3),Q(-4))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0073():
    a=Vec2(Q(6),Q(10));b=a+Vec2(Q(5),Q(4))
    shift=Vec2(Q(4),Q(-5))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0074():
    a=Vec2(Q(7),Q(11));b=a+Vec2(Q(6),Q(5))
    shift=Vec2(Q(5),Q(-6))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0075():
    a=Vec2(Q(8),Q(12));b=a+Vec2(Q(7),Q(6))
    shift=Vec2(Q(6),Q(-7))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0076():
    a=Vec2(Q(9),Q(13));b=a+Vec2(Q(8),Q(7))
    shift=Vec2(Q(7),Q(-8))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0077():
    a=Vec2(Q(10),Q(14));b=a+Vec2(Q(9),Q(1))
    shift=Vec2(Q(1),Q(-9))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0078():
    a=Vec2(Q(11),Q(2));b=a+Vec2(Q(10),Q(2))
    shift=Vec2(Q(2),Q(-10))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0079():
    a=Vec2(Q(12),Q(3));b=a+Vec2(Q(11),Q(3))
    shift=Vec2(Q(3),Q(-11))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0080():
    a=Vec2(Q(13),Q(4));b=a+Vec2(Q(12),Q(4))
    shift=Vec2(Q(4),Q(-12))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0081():
    a=Vec2(Q(14),Q(5));b=a+Vec2(Q(13),Q(5))
    shift=Vec2(Q(5),Q(-13))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0082():
    a=Vec2(Q(15),Q(6));b=a+Vec2(Q(14),Q(6))
    shift=Vec2(Q(6),Q(-14))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0083():
    a=Vec2(Q(16),Q(7));b=a+Vec2(Q(15),Q(7))
    shift=Vec2(Q(7),Q(-15))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0084():
    a=Vec2(Q(17),Q(8));b=a+Vec2(Q(16),Q(1))
    shift=Vec2(Q(1),Q(-16))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0085():
    a=Vec2(Q(1),Q(9));b=a+Vec2(Q(17),Q(2))
    shift=Vec2(Q(2),Q(-17))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0086():
    a=Vec2(Q(2),Q(10));b=a+Vec2(Q(18),Q(3))
    shift=Vec2(Q(3),Q(-18))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0087():
    a=Vec2(Q(3),Q(11));b=a+Vec2(Q(19),Q(4))
    shift=Vec2(Q(4),Q(-19))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0088():
    a=Vec2(Q(4),Q(12));b=a+Vec2(Q(20),Q(5))
    shift=Vec2(Q(5),Q(-20))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0089():
    a=Vec2(Q(5),Q(13));b=a+Vec2(Q(21),Q(6))
    shift=Vec2(Q(6),Q(-21))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0090():
    a=Vec2(Q(6),Q(14));b=a+Vec2(Q(22),Q(7))
    shift=Vec2(Q(7),Q(-22))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0091():
    a=Vec2(Q(7),Q(2));b=a+Vec2(Q(23),Q(1))
    shift=Vec2(Q(1),Q(-23))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0092():
    a=Vec2(Q(8),Q(3));b=a+Vec2(Q(1),Q(2))
    shift=Vec2(Q(2),Q(-1))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0093():
    a=Vec2(Q(9),Q(4));b=a+Vec2(Q(2),Q(3))
    shift=Vec2(Q(3),Q(-2))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0094():
    a=Vec2(Q(10),Q(5));b=a+Vec2(Q(3),Q(4))
    shift=Vec2(Q(4),Q(-3))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0095():
    a=Vec2(Q(11),Q(6));b=a+Vec2(Q(4),Q(5))
    shift=Vec2(Q(5),Q(-4))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0096():
    a=Vec2(Q(12),Q(7));b=a+Vec2(Q(5),Q(6))
    shift=Vec2(Q(6),Q(-5))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0097():
    a=Vec2(Q(13),Q(8));b=a+Vec2(Q(6),Q(7))
    shift=Vec2(Q(7),Q(-6))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0098():
    a=Vec2(Q(14),Q(9));b=a+Vec2(Q(7),Q(1))
    shift=Vec2(Q(1),Q(-7))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0099():
    a=Vec2(Q(15),Q(10));b=a+Vec2(Q(8),Q(2))
    shift=Vec2(Q(2),Q(-8))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0100():
    a=Vec2(Q(16),Q(11));b=a+Vec2(Q(9),Q(3))
    shift=Vec2(Q(3),Q(-9))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0101():
    a=Vec2(Q(17),Q(12));b=a+Vec2(Q(10),Q(4))
    shift=Vec2(Q(4),Q(-10))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0102():
    a=Vec2(Q(1),Q(13));b=a+Vec2(Q(11),Q(5))
    shift=Vec2(Q(5),Q(-11))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0103():
    a=Vec2(Q(2),Q(14));b=a+Vec2(Q(12),Q(6))
    shift=Vec2(Q(6),Q(-12))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0104():
    a=Vec2(Q(3),Q(2));b=a+Vec2(Q(13),Q(7))
    shift=Vec2(Q(7),Q(-13))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0105():
    a=Vec2(Q(4),Q(3));b=a+Vec2(Q(14),Q(1))
    shift=Vec2(Q(1),Q(-14))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0106():
    a=Vec2(Q(5),Q(4));b=a+Vec2(Q(15),Q(2))
    shift=Vec2(Q(2),Q(-15))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0107():
    a=Vec2(Q(6),Q(5));b=a+Vec2(Q(16),Q(3))
    shift=Vec2(Q(3),Q(-16))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0108():
    a=Vec2(Q(7),Q(6));b=a+Vec2(Q(17),Q(4))
    shift=Vec2(Q(4),Q(-17))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0109():
    a=Vec2(Q(8),Q(7));b=a+Vec2(Q(18),Q(5))
    shift=Vec2(Q(5),Q(-18))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0110():
    a=Vec2(Q(9),Q(8));b=a+Vec2(Q(19),Q(6))
    shift=Vec2(Q(6),Q(-19))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0111():
    a=Vec2(Q(10),Q(9));b=a+Vec2(Q(20),Q(7))
    shift=Vec2(Q(7),Q(-20))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0112():
    a=Vec2(Q(11),Q(10));b=a+Vec2(Q(21),Q(1))
    shift=Vec2(Q(1),Q(-21))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0113():
    a=Vec2(Q(12),Q(11));b=a+Vec2(Q(22),Q(2))
    shift=Vec2(Q(2),Q(-22))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0114():
    a=Vec2(Q(13),Q(12));b=a+Vec2(Q(23),Q(3))
    shift=Vec2(Q(3),Q(-23))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0115():
    a=Vec2(Q(14),Q(13));b=a+Vec2(Q(1),Q(4))
    shift=Vec2(Q(4),Q(-1))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0116():
    a=Vec2(Q(15),Q(14));b=a+Vec2(Q(2),Q(5))
    shift=Vec2(Q(5),Q(-2))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0117():
    a=Vec2(Q(16),Q(2));b=a+Vec2(Q(3),Q(6))
    shift=Vec2(Q(6),Q(-3))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0118():
    a=Vec2(Q(17),Q(3));b=a+Vec2(Q(4),Q(7))
    shift=Vec2(Q(7),Q(-4))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0119():
    a=Vec2(Q(1),Q(4));b=a+Vec2(Q(5),Q(1))
    shift=Vec2(Q(1),Q(-5))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0120():
    a=Vec2(Q(2),Q(5));b=a+Vec2(Q(6),Q(2))
    shift=Vec2(Q(2),Q(-6))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0121():
    a=Vec2(Q(3),Q(6));b=a+Vec2(Q(7),Q(3))
    shift=Vec2(Q(3),Q(-7))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0122():
    a=Vec2(Q(4),Q(7));b=a+Vec2(Q(8),Q(4))
    shift=Vec2(Q(4),Q(-8))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0123():
    a=Vec2(Q(5),Q(8));b=a+Vec2(Q(9),Q(5))
    shift=Vec2(Q(5),Q(-9))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0124():
    a=Vec2(Q(6),Q(9));b=a+Vec2(Q(10),Q(6))
    shift=Vec2(Q(6),Q(-10))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0125():
    a=Vec2(Q(7),Q(10));b=a+Vec2(Q(11),Q(7))
    shift=Vec2(Q(7),Q(-11))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0126():
    a=Vec2(Q(8),Q(11));b=a+Vec2(Q(12),Q(1))
    shift=Vec2(Q(1),Q(-12))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0127():
    a=Vec2(Q(9),Q(12));b=a+Vec2(Q(13),Q(2))
    shift=Vec2(Q(2),Q(-13))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0128():
    a=Vec2(Q(10),Q(13));b=a+Vec2(Q(14),Q(3))
    shift=Vec2(Q(3),Q(-14))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0129():
    a=Vec2(Q(11),Q(14));b=a+Vec2(Q(15),Q(4))
    shift=Vec2(Q(4),Q(-15))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0130():
    a=Vec2(Q(12),Q(2));b=a+Vec2(Q(16),Q(5))
    shift=Vec2(Q(5),Q(-16))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0131():
    a=Vec2(Q(13),Q(3));b=a+Vec2(Q(17),Q(6))
    shift=Vec2(Q(6),Q(-17))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0132():
    a=Vec2(Q(14),Q(4));b=a+Vec2(Q(18),Q(7))
    shift=Vec2(Q(7),Q(-18))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0133():
    a=Vec2(Q(15),Q(5));b=a+Vec2(Q(19),Q(1))
    shift=Vec2(Q(1),Q(-19))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0134():
    a=Vec2(Q(16),Q(6));b=a+Vec2(Q(20),Q(2))
    shift=Vec2(Q(2),Q(-20))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0135():
    a=Vec2(Q(17),Q(7));b=a+Vec2(Q(21),Q(3))
    shift=Vec2(Q(3),Q(-21))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0136():
    a=Vec2(Q(1),Q(8));b=a+Vec2(Q(22),Q(4))
    shift=Vec2(Q(4),Q(-22))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0137():
    a=Vec2(Q(2),Q(9));b=a+Vec2(Q(23),Q(5))
    shift=Vec2(Q(5),Q(-23))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0138():
    a=Vec2(Q(3),Q(10));b=a+Vec2(Q(1),Q(6))
    shift=Vec2(Q(6),Q(-1))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0139():
    a=Vec2(Q(4),Q(11));b=a+Vec2(Q(2),Q(7))
    shift=Vec2(Q(7),Q(-2))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0140():
    a=Vec2(Q(5),Q(12));b=a+Vec2(Q(3),Q(1))
    shift=Vec2(Q(1),Q(-3))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0141():
    a=Vec2(Q(6),Q(13));b=a+Vec2(Q(4),Q(2))
    shift=Vec2(Q(2),Q(-4))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0142():
    a=Vec2(Q(7),Q(14));b=a+Vec2(Q(5),Q(3))
    shift=Vec2(Q(3),Q(-5))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0143():
    a=Vec2(Q(8),Q(2));b=a+Vec2(Q(6),Q(4))
    shift=Vec2(Q(4),Q(-6))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0144():
    a=Vec2(Q(9),Q(3));b=a+Vec2(Q(7),Q(5))
    shift=Vec2(Q(5),Q(-7))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0145():
    a=Vec2(Q(10),Q(4));b=a+Vec2(Q(8),Q(6))
    shift=Vec2(Q(6),Q(-8))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0146():
    a=Vec2(Q(11),Q(5));b=a+Vec2(Q(9),Q(7))
    shift=Vec2(Q(7),Q(-9))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0147():
    a=Vec2(Q(12),Q(6));b=a+Vec2(Q(10),Q(1))
    shift=Vec2(Q(1),Q(-10))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0148():
    a=Vec2(Q(13),Q(7));b=a+Vec2(Q(11),Q(2))
    shift=Vec2(Q(2),Q(-11))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0149():
    a=Vec2(Q(14),Q(8));b=a+Vec2(Q(12),Q(3))
    shift=Vec2(Q(3),Q(-12))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0150():
    a=Vec2(Q(15),Q(9));b=a+Vec2(Q(13),Q(4))
    shift=Vec2(Q(4),Q(-13))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0151():
    a=Vec2(Q(16),Q(10));b=a+Vec2(Q(14),Q(5))
    shift=Vec2(Q(5),Q(-14))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0152():
    a=Vec2(Q(17),Q(11));b=a+Vec2(Q(15),Q(6))
    shift=Vec2(Q(6),Q(-15))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0153():
    a=Vec2(Q(1),Q(12));b=a+Vec2(Q(16),Q(7))
    shift=Vec2(Q(7),Q(-16))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0154():
    a=Vec2(Q(2),Q(13));b=a+Vec2(Q(17),Q(1))
    shift=Vec2(Q(1),Q(-17))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0155():
    a=Vec2(Q(3),Q(14));b=a+Vec2(Q(18),Q(2))
    shift=Vec2(Q(2),Q(-18))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0156():
    a=Vec2(Q(4),Q(2));b=a+Vec2(Q(19),Q(3))
    shift=Vec2(Q(3),Q(-19))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0157():
    a=Vec2(Q(5),Q(3));b=a+Vec2(Q(20),Q(4))
    shift=Vec2(Q(4),Q(-20))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0158():
    a=Vec2(Q(6),Q(4));b=a+Vec2(Q(21),Q(5))
    shift=Vec2(Q(5),Q(-21))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0159():
    a=Vec2(Q(7),Q(5));b=a+Vec2(Q(22),Q(6))
    shift=Vec2(Q(6),Q(-22))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0160():
    a=Vec2(Q(8),Q(6));b=a+Vec2(Q(23),Q(7))
    shift=Vec2(Q(7),Q(-23))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0161():
    a=Vec2(Q(9),Q(7));b=a+Vec2(Q(1),Q(1))
    shift=Vec2(Q(1),Q(-1))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0162():
    a=Vec2(Q(10),Q(8));b=a+Vec2(Q(2),Q(2))
    shift=Vec2(Q(2),Q(-2))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0163():
    a=Vec2(Q(11),Q(9));b=a+Vec2(Q(3),Q(3))
    shift=Vec2(Q(3),Q(-3))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0164():
    a=Vec2(Q(12),Q(10));b=a+Vec2(Q(4),Q(4))
    shift=Vec2(Q(4),Q(-4))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0165():
    a=Vec2(Q(13),Q(11));b=a+Vec2(Q(5),Q(5))
    shift=Vec2(Q(5),Q(-5))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0166():
    a=Vec2(Q(14),Q(12));b=a+Vec2(Q(6),Q(6))
    shift=Vec2(Q(6),Q(-6))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0167():
    a=Vec2(Q(15),Q(13));b=a+Vec2(Q(7),Q(7))
    shift=Vec2(Q(7),Q(-7))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0168():
    a=Vec2(Q(16),Q(14));b=a+Vec2(Q(8),Q(1))
    shift=Vec2(Q(1),Q(-8))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0169():
    a=Vec2(Q(17),Q(2));b=a+Vec2(Q(9),Q(2))
    shift=Vec2(Q(2),Q(-9))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0170():
    a=Vec2(Q(1),Q(3));b=a+Vec2(Q(10),Q(3))
    shift=Vec2(Q(3),Q(-10))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0171():
    a=Vec2(Q(2),Q(4));b=a+Vec2(Q(11),Q(4))
    shift=Vec2(Q(4),Q(-11))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0172():
    a=Vec2(Q(3),Q(5));b=a+Vec2(Q(12),Q(5))
    shift=Vec2(Q(5),Q(-12))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0173():
    a=Vec2(Q(4),Q(6));b=a+Vec2(Q(13),Q(6))
    shift=Vec2(Q(6),Q(-13))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0174():
    a=Vec2(Q(5),Q(7));b=a+Vec2(Q(14),Q(7))
    shift=Vec2(Q(7),Q(-14))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0175():
    a=Vec2(Q(6),Q(8));b=a+Vec2(Q(15),Q(1))
    shift=Vec2(Q(1),Q(-15))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0176():
    a=Vec2(Q(7),Q(9));b=a+Vec2(Q(16),Q(2))
    shift=Vec2(Q(2),Q(-16))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0177():
    a=Vec2(Q(8),Q(10));b=a+Vec2(Q(17),Q(3))
    shift=Vec2(Q(3),Q(-17))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0178():
    a=Vec2(Q(9),Q(11));b=a+Vec2(Q(18),Q(4))
    shift=Vec2(Q(4),Q(-18))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0179():
    a=Vec2(Q(10),Q(12));b=a+Vec2(Q(19),Q(5))
    shift=Vec2(Q(5),Q(-19))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0180():
    a=Vec2(Q(11),Q(13));b=a+Vec2(Q(20),Q(6))
    shift=Vec2(Q(6),Q(-20))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0181():
    a=Vec2(Q(12),Q(14));b=a+Vec2(Q(21),Q(7))
    shift=Vec2(Q(7),Q(-21))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0182():
    a=Vec2(Q(13),Q(2));b=a+Vec2(Q(22),Q(1))
    shift=Vec2(Q(1),Q(-22))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0183():
    a=Vec2(Q(14),Q(3));b=a+Vec2(Q(23),Q(2))
    shift=Vec2(Q(2),Q(-23))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0184():
    a=Vec2(Q(15),Q(4));b=a+Vec2(Q(1),Q(3))
    shift=Vec2(Q(3),Q(-1))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0185():
    a=Vec2(Q(16),Q(5));b=a+Vec2(Q(2),Q(4))
    shift=Vec2(Q(4),Q(-2))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0186():
    a=Vec2(Q(17),Q(6));b=a+Vec2(Q(3),Q(5))
    shift=Vec2(Q(5),Q(-3))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0187():
    a=Vec2(Q(1),Q(7));b=a+Vec2(Q(4),Q(6))
    shift=Vec2(Q(6),Q(-4))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0188():
    a=Vec2(Q(2),Q(8));b=a+Vec2(Q(5),Q(7))
    shift=Vec2(Q(7),Q(-5))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0189():
    a=Vec2(Q(3),Q(9));b=a+Vec2(Q(6),Q(1))
    shift=Vec2(Q(1),Q(-6))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0190():
    a=Vec2(Q(4),Q(10));b=a+Vec2(Q(7),Q(2))
    shift=Vec2(Q(2),Q(-7))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0191():
    a=Vec2(Q(5),Q(11));b=a+Vec2(Q(8),Q(3))
    shift=Vec2(Q(3),Q(-8))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0192():
    a=Vec2(Q(6),Q(12));b=a+Vec2(Q(9),Q(4))
    shift=Vec2(Q(4),Q(-9))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0193():
    a=Vec2(Q(7),Q(13));b=a+Vec2(Q(10),Q(5))
    shift=Vec2(Q(5),Q(-10))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0194():
    a=Vec2(Q(8),Q(14));b=a+Vec2(Q(11),Q(6))
    shift=Vec2(Q(6),Q(-11))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0195():
    a=Vec2(Q(9),Q(2));b=a+Vec2(Q(12),Q(7))
    shift=Vec2(Q(7),Q(-12))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0196():
    a=Vec2(Q(10),Q(3));b=a+Vec2(Q(13),Q(1))
    shift=Vec2(Q(1),Q(-13))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0197():
    a=Vec2(Q(11),Q(4));b=a+Vec2(Q(14),Q(2))
    shift=Vec2(Q(2),Q(-14))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0198():
    a=Vec2(Q(12),Q(5));b=a+Vec2(Q(15),Q(3))
    shift=Vec2(Q(3),Q(-15))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0199():
    a=Vec2(Q(13),Q(6));b=a+Vec2(Q(16),Q(4))
    shift=Vec2(Q(4),Q(-16))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0200():
    a=Vec2(Q(14),Q(7));b=a+Vec2(Q(17),Q(5))
    shift=Vec2(Q(5),Q(-17))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0201():
    a=Vec2(Q(15),Q(8));b=a+Vec2(Q(18),Q(6))
    shift=Vec2(Q(6),Q(-18))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0202():
    a=Vec2(Q(16),Q(9));b=a+Vec2(Q(19),Q(7))
    shift=Vec2(Q(7),Q(-19))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0203():
    a=Vec2(Q(17),Q(10));b=a+Vec2(Q(20),Q(1))
    shift=Vec2(Q(1),Q(-20))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0204():
    a=Vec2(Q(1),Q(11));b=a+Vec2(Q(21),Q(2))
    shift=Vec2(Q(2),Q(-21))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0205():
    a=Vec2(Q(2),Q(12));b=a+Vec2(Q(22),Q(3))
    shift=Vec2(Q(3),Q(-22))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0206():
    a=Vec2(Q(3),Q(13));b=a+Vec2(Q(23),Q(4))
    shift=Vec2(Q(4),Q(-23))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0207():
    a=Vec2(Q(4),Q(14));b=a+Vec2(Q(1),Q(5))
    shift=Vec2(Q(5),Q(-1))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0208():
    a=Vec2(Q(5),Q(2));b=a+Vec2(Q(2),Q(6))
    shift=Vec2(Q(6),Q(-2))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0209():
    a=Vec2(Q(6),Q(3));b=a+Vec2(Q(3),Q(7))
    shift=Vec2(Q(7),Q(-3))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0210():
    a=Vec2(Q(7),Q(4));b=a+Vec2(Q(4),Q(1))
    shift=Vec2(Q(1),Q(-4))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0211():
    a=Vec2(Q(8),Q(5));b=a+Vec2(Q(5),Q(2))
    shift=Vec2(Q(2),Q(-5))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0212():
    a=Vec2(Q(9),Q(6));b=a+Vec2(Q(6),Q(3))
    shift=Vec2(Q(3),Q(-6))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0213():
    a=Vec2(Q(10),Q(7));b=a+Vec2(Q(7),Q(4))
    shift=Vec2(Q(4),Q(-7))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0214():
    a=Vec2(Q(11),Q(8));b=a+Vec2(Q(8),Q(5))
    shift=Vec2(Q(5),Q(-8))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0215():
    a=Vec2(Q(12),Q(9));b=a+Vec2(Q(9),Q(6))
    shift=Vec2(Q(6),Q(-9))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0216():
    a=Vec2(Q(13),Q(10));b=a+Vec2(Q(10),Q(7))
    shift=Vec2(Q(7),Q(-10))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0217():
    a=Vec2(Q(14),Q(11));b=a+Vec2(Q(11),Q(1))
    shift=Vec2(Q(1),Q(-11))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0218():
    a=Vec2(Q(15),Q(12));b=a+Vec2(Q(12),Q(2))
    shift=Vec2(Q(2),Q(-12))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0219():
    a=Vec2(Q(16),Q(13));b=a+Vec2(Q(13),Q(3))
    shift=Vec2(Q(3),Q(-13))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0220():
    a=Vec2(Q(17),Q(14));b=a+Vec2(Q(14),Q(4))
    shift=Vec2(Q(4),Q(-14))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0221():
    a=Vec2(Q(1),Q(2));b=a+Vec2(Q(15),Q(5))
    shift=Vec2(Q(5),Q(-15))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0222():
    a=Vec2(Q(2),Q(3));b=a+Vec2(Q(16),Q(6))
    shift=Vec2(Q(6),Q(-16))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0223():
    a=Vec2(Q(3),Q(4));b=a+Vec2(Q(17),Q(7))
    shift=Vec2(Q(7),Q(-17))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0224():
    a=Vec2(Q(4),Q(5));b=a+Vec2(Q(18),Q(1))
    shift=Vec2(Q(1),Q(-18))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0225():
    a=Vec2(Q(5),Q(6));b=a+Vec2(Q(19),Q(2))
    shift=Vec2(Q(2),Q(-19))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0226():
    a=Vec2(Q(6),Q(7));b=a+Vec2(Q(20),Q(3))
    shift=Vec2(Q(3),Q(-20))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0227():
    a=Vec2(Q(7),Q(8));b=a+Vec2(Q(21),Q(4))
    shift=Vec2(Q(4),Q(-21))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0228():
    a=Vec2(Q(8),Q(9));b=a+Vec2(Q(22),Q(5))
    shift=Vec2(Q(5),Q(-22))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0229():
    a=Vec2(Q(9),Q(10));b=a+Vec2(Q(23),Q(6))
    shift=Vec2(Q(6),Q(-23))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0230():
    a=Vec2(Q(10),Q(11));b=a+Vec2(Q(1),Q(7))
    shift=Vec2(Q(7),Q(-1))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0231():
    a=Vec2(Q(11),Q(12));b=a+Vec2(Q(2),Q(1))
    shift=Vec2(Q(1),Q(-2))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0232():
    a=Vec2(Q(12),Q(13));b=a+Vec2(Q(3),Q(2))
    shift=Vec2(Q(2),Q(-3))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0233():
    a=Vec2(Q(13),Q(14));b=a+Vec2(Q(4),Q(3))
    shift=Vec2(Q(3),Q(-4))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0234():
    a=Vec2(Q(14),Q(2));b=a+Vec2(Q(5),Q(4))
    shift=Vec2(Q(4),Q(-5))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0235():
    a=Vec2(Q(15),Q(3));b=a+Vec2(Q(6),Q(5))
    shift=Vec2(Q(5),Q(-6))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0236():
    a=Vec2(Q(16),Q(4));b=a+Vec2(Q(7),Q(6))
    shift=Vec2(Q(6),Q(-7))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0237():
    a=Vec2(Q(17),Q(5));b=a+Vec2(Q(8),Q(7))
    shift=Vec2(Q(7),Q(-8))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0238():
    a=Vec2(Q(1),Q(6));b=a+Vec2(Q(9),Q(1))
    shift=Vec2(Q(1),Q(-9))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0239():
    a=Vec2(Q(2),Q(7));b=a+Vec2(Q(10),Q(2))
    shift=Vec2(Q(2),Q(-10))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0240():
    a=Vec2(Q(3),Q(8));b=a+Vec2(Q(11),Q(3))
    shift=Vec2(Q(3),Q(-11))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0241():
    a=Vec2(Q(4),Q(9));b=a+Vec2(Q(12),Q(4))
    shift=Vec2(Q(4),Q(-12))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0242():
    a=Vec2(Q(5),Q(10));b=a+Vec2(Q(13),Q(5))
    shift=Vec2(Q(5),Q(-13))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0243():
    a=Vec2(Q(6),Q(11));b=a+Vec2(Q(14),Q(6))
    shift=Vec2(Q(6),Q(-14))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0244():
    a=Vec2(Q(7),Q(12));b=a+Vec2(Q(15),Q(7))
    shift=Vec2(Q(7),Q(-15))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0245():
    a=Vec2(Q(8),Q(13));b=a+Vec2(Q(16),Q(1))
    shift=Vec2(Q(1),Q(-16))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0246():
    a=Vec2(Q(9),Q(14));b=a+Vec2(Q(17),Q(2))
    shift=Vec2(Q(2),Q(-17))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0247():
    a=Vec2(Q(10),Q(2));b=a+Vec2(Q(18),Q(3))
    shift=Vec2(Q(3),Q(-18))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0248():
    a=Vec2(Q(11),Q(3));b=a+Vec2(Q(19),Q(4))
    shift=Vec2(Q(4),Q(-19))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0249():
    a=Vec2(Q(12),Q(4));b=a+Vec2(Q(20),Q(5))
    shift=Vec2(Q(5),Q(-20))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0250():
    a=Vec2(Q(13),Q(5));b=a+Vec2(Q(21),Q(6))
    shift=Vec2(Q(6),Q(-21))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0251():
    a=Vec2(Q(14),Q(6));b=a+Vec2(Q(22),Q(7))
    shift=Vec2(Q(7),Q(-22))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0252():
    a=Vec2(Q(15),Q(7));b=a+Vec2(Q(23),Q(1))
    shift=Vec2(Q(1),Q(-23))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0253():
    a=Vec2(Q(16),Q(8));b=a+Vec2(Q(1),Q(2))
    shift=Vec2(Q(2),Q(-1))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0254():
    a=Vec2(Q(17),Q(9));b=a+Vec2(Q(2),Q(3))
    shift=Vec2(Q(3),Q(-2))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0255():
    a=Vec2(Q(1),Q(10));b=a+Vec2(Q(3),Q(4))
    shift=Vec2(Q(4),Q(-3))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0256():
    a=Vec2(Q(2),Q(11));b=a+Vec2(Q(4),Q(5))
    shift=Vec2(Q(5),Q(-4))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0257():
    a=Vec2(Q(3),Q(12));b=a+Vec2(Q(5),Q(6))
    shift=Vec2(Q(6),Q(-5))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0258():
    a=Vec2(Q(4),Q(13));b=a+Vec2(Q(6),Q(7))
    shift=Vec2(Q(7),Q(-6))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0259():
    a=Vec2(Q(5),Q(14));b=a+Vec2(Q(7),Q(1))
    shift=Vec2(Q(1),Q(-7))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0260():
    a=Vec2(Q(6),Q(2));b=a+Vec2(Q(8),Q(2))
    shift=Vec2(Q(2),Q(-8))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0261():
    a=Vec2(Q(7),Q(3));b=a+Vec2(Q(9),Q(3))
    shift=Vec2(Q(3),Q(-9))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0262():
    a=Vec2(Q(8),Q(4));b=a+Vec2(Q(10),Q(4))
    shift=Vec2(Q(4),Q(-10))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0263():
    a=Vec2(Q(9),Q(5));b=a+Vec2(Q(11),Q(5))
    shift=Vec2(Q(5),Q(-11))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0264():
    a=Vec2(Q(10),Q(6));b=a+Vec2(Q(12),Q(6))
    shift=Vec2(Q(6),Q(-12))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0265():
    a=Vec2(Q(11),Q(7));b=a+Vec2(Q(13),Q(7))
    shift=Vec2(Q(7),Q(-13))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0266():
    a=Vec2(Q(12),Q(8));b=a+Vec2(Q(14),Q(1))
    shift=Vec2(Q(1),Q(-14))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0267():
    a=Vec2(Q(13),Q(9));b=a+Vec2(Q(15),Q(2))
    shift=Vec2(Q(2),Q(-15))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0268():
    a=Vec2(Q(14),Q(10));b=a+Vec2(Q(16),Q(3))
    shift=Vec2(Q(3),Q(-16))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0269():
    a=Vec2(Q(15),Q(11));b=a+Vec2(Q(17),Q(4))
    shift=Vec2(Q(4),Q(-17))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0270():
    a=Vec2(Q(16),Q(12));b=a+Vec2(Q(18),Q(5))
    shift=Vec2(Q(5),Q(-18))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0271():
    a=Vec2(Q(17),Q(13));b=a+Vec2(Q(19),Q(6))
    shift=Vec2(Q(6),Q(-19))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0272():
    a=Vec2(Q(1),Q(14));b=a+Vec2(Q(20),Q(7))
    shift=Vec2(Q(7),Q(-20))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0273():
    a=Vec2(Q(2),Q(2));b=a+Vec2(Q(21),Q(1))
    shift=Vec2(Q(1),Q(-21))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0274():
    a=Vec2(Q(3),Q(3));b=a+Vec2(Q(22),Q(2))
    shift=Vec2(Q(2),Q(-22))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0275():
    a=Vec2(Q(4),Q(4));b=a+Vec2(Q(23),Q(3))
    shift=Vec2(Q(3),Q(-23))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0276():
    a=Vec2(Q(5),Q(5));b=a+Vec2(Q(1),Q(4))
    shift=Vec2(Q(4),Q(-1))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0277():
    a=Vec2(Q(6),Q(6));b=a+Vec2(Q(2),Q(5))
    shift=Vec2(Q(5),Q(-2))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0278():
    a=Vec2(Q(7),Q(7));b=a+Vec2(Q(3),Q(6))
    shift=Vec2(Q(6),Q(-3))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0279():
    a=Vec2(Q(8),Q(8));b=a+Vec2(Q(4),Q(7))
    shift=Vec2(Q(7),Q(-4))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0280():
    a=Vec2(Q(9),Q(9));b=a+Vec2(Q(5),Q(1))
    shift=Vec2(Q(1),Q(-5))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0281():
    a=Vec2(Q(10),Q(10));b=a+Vec2(Q(6),Q(2))
    shift=Vec2(Q(2),Q(-6))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0282():
    a=Vec2(Q(11),Q(11));b=a+Vec2(Q(7),Q(3))
    shift=Vec2(Q(3),Q(-7))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0283():
    a=Vec2(Q(12),Q(12));b=a+Vec2(Q(8),Q(4))
    shift=Vec2(Q(4),Q(-8))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0284():
    a=Vec2(Q(13),Q(13));b=a+Vec2(Q(9),Q(5))
    shift=Vec2(Q(5),Q(-9))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0285():
    a=Vec2(Q(14),Q(14));b=a+Vec2(Q(10),Q(6))
    shift=Vec2(Q(6),Q(-10))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0286():
    a=Vec2(Q(15),Q(2));b=a+Vec2(Q(11),Q(7))
    shift=Vec2(Q(7),Q(-11))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0287():
    a=Vec2(Q(16),Q(3));b=a+Vec2(Q(12),Q(1))
    shift=Vec2(Q(1),Q(-12))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0288():
    a=Vec2(Q(17),Q(4));b=a+Vec2(Q(13),Q(2))
    shift=Vec2(Q(2),Q(-13))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0289():
    a=Vec2(Q(1),Q(5));b=a+Vec2(Q(14),Q(3))
    shift=Vec2(Q(3),Q(-14))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0290():
    a=Vec2(Q(2),Q(6));b=a+Vec2(Q(15),Q(4))
    shift=Vec2(Q(4),Q(-15))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0291():
    a=Vec2(Q(3),Q(7));b=a+Vec2(Q(16),Q(5))
    shift=Vec2(Q(5),Q(-16))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0292():
    a=Vec2(Q(4),Q(8));b=a+Vec2(Q(17),Q(6))
    shift=Vec2(Q(6),Q(-17))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0293():
    a=Vec2(Q(5),Q(9));b=a+Vec2(Q(18),Q(7))
    shift=Vec2(Q(7),Q(-18))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0294():
    a=Vec2(Q(6),Q(10));b=a+Vec2(Q(19),Q(1))
    shift=Vec2(Q(1),Q(-19))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0295():
    a=Vec2(Q(7),Q(11));b=a+Vec2(Q(20),Q(2))
    shift=Vec2(Q(2),Q(-20))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0296():
    a=Vec2(Q(8),Q(12));b=a+Vec2(Q(21),Q(3))
    shift=Vec2(Q(3),Q(-21))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0297():
    a=Vec2(Q(9),Q(13));b=a+Vec2(Q(22),Q(4))
    shift=Vec2(Q(4),Q(-22))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0298():
    a=Vec2(Q(10),Q(14));b=a+Vec2(Q(23),Q(5))
    shift=Vec2(Q(5),Q(-23))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0299():
    a=Vec2(Q(11),Q(2));b=a+Vec2(Q(1),Q(6))
    shift=Vec2(Q(6),Q(-1))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0300():
    a=Vec2(Q(12),Q(3));b=a+Vec2(Q(2),Q(7))
    shift=Vec2(Q(7),Q(-2))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0301():
    a=Vec2(Q(13),Q(4));b=a+Vec2(Q(3),Q(1))
    shift=Vec2(Q(1),Q(-3))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0302():
    a=Vec2(Q(14),Q(5));b=a+Vec2(Q(4),Q(2))
    shift=Vec2(Q(2),Q(-4))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0303():
    a=Vec2(Q(15),Q(6));b=a+Vec2(Q(5),Q(3))
    shift=Vec2(Q(3),Q(-5))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0304():
    a=Vec2(Q(16),Q(7));b=a+Vec2(Q(6),Q(4))
    shift=Vec2(Q(4),Q(-6))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0305():
    a=Vec2(Q(17),Q(8));b=a+Vec2(Q(7),Q(5))
    shift=Vec2(Q(5),Q(-7))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0306():
    a=Vec2(Q(1),Q(9));b=a+Vec2(Q(8),Q(6))
    shift=Vec2(Q(6),Q(-8))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0307():
    a=Vec2(Q(2),Q(10));b=a+Vec2(Q(9),Q(7))
    shift=Vec2(Q(7),Q(-9))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0308():
    a=Vec2(Q(3),Q(11));b=a+Vec2(Q(10),Q(1))
    shift=Vec2(Q(1),Q(-10))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0309():
    a=Vec2(Q(4),Q(12));b=a+Vec2(Q(11),Q(2))
    shift=Vec2(Q(2),Q(-11))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0310():
    a=Vec2(Q(5),Q(13));b=a+Vec2(Q(12),Q(3))
    shift=Vec2(Q(3),Q(-12))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0311():
    a=Vec2(Q(6),Q(14));b=a+Vec2(Q(13),Q(4))
    shift=Vec2(Q(4),Q(-13))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0312():
    a=Vec2(Q(7),Q(2));b=a+Vec2(Q(14),Q(5))
    shift=Vec2(Q(5),Q(-14))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0313():
    a=Vec2(Q(8),Q(3));b=a+Vec2(Q(15),Q(6))
    shift=Vec2(Q(6),Q(-15))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0314():
    a=Vec2(Q(9),Q(4));b=a+Vec2(Q(16),Q(7))
    shift=Vec2(Q(7),Q(-16))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0315():
    a=Vec2(Q(10),Q(5));b=a+Vec2(Q(17),Q(1))
    shift=Vec2(Q(1),Q(-17))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0316():
    a=Vec2(Q(11),Q(6));b=a+Vec2(Q(18),Q(2))
    shift=Vec2(Q(2),Q(-18))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0317():
    a=Vec2(Q(12),Q(7));b=a+Vec2(Q(19),Q(3))
    shift=Vec2(Q(3),Q(-19))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0318():
    a=Vec2(Q(13),Q(8));b=a+Vec2(Q(20),Q(4))
    shift=Vec2(Q(4),Q(-20))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0319():
    a=Vec2(Q(14),Q(9));b=a+Vec2(Q(21),Q(5))
    shift=Vec2(Q(5),Q(-21))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0320():
    a=Vec2(Q(15),Q(10));b=a+Vec2(Q(22),Q(6))
    shift=Vec2(Q(6),Q(-22))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0321():
    a=Vec2(Q(16),Q(11));b=a+Vec2(Q(23),Q(7))
    shift=Vec2(Q(7),Q(-23))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0322():
    a=Vec2(Q(17),Q(12));b=a+Vec2(Q(1),Q(1))
    shift=Vec2(Q(1),Q(-1))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0323():
    a=Vec2(Q(1),Q(13));b=a+Vec2(Q(2),Q(2))
    shift=Vec2(Q(2),Q(-2))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0324():
    a=Vec2(Q(2),Q(14));b=a+Vec2(Q(3),Q(3))
    shift=Vec2(Q(3),Q(-3))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0325():
    a=Vec2(Q(3),Q(2));b=a+Vec2(Q(4),Q(4))
    shift=Vec2(Q(4),Q(-4))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0326():
    a=Vec2(Q(4),Q(3));b=a+Vec2(Q(5),Q(5))
    shift=Vec2(Q(5),Q(-5))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0327():
    a=Vec2(Q(5),Q(4));b=a+Vec2(Q(6),Q(6))
    shift=Vec2(Q(6),Q(-6))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0328():
    a=Vec2(Q(6),Q(5));b=a+Vec2(Q(7),Q(7))
    shift=Vec2(Q(7),Q(-7))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0329():
    a=Vec2(Q(7),Q(6));b=a+Vec2(Q(8),Q(1))
    shift=Vec2(Q(1),Q(-8))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0330():
    a=Vec2(Q(8),Q(7));b=a+Vec2(Q(9),Q(2))
    shift=Vec2(Q(2),Q(-9))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0331():
    a=Vec2(Q(9),Q(8));b=a+Vec2(Q(10),Q(3))
    shift=Vec2(Q(3),Q(-10))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0332():
    a=Vec2(Q(10),Q(9));b=a+Vec2(Q(11),Q(4))
    shift=Vec2(Q(4),Q(-11))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0333():
    a=Vec2(Q(11),Q(10));b=a+Vec2(Q(12),Q(5))
    shift=Vec2(Q(5),Q(-12))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0334():
    a=Vec2(Q(12),Q(11));b=a+Vec2(Q(13),Q(6))
    shift=Vec2(Q(6),Q(-13))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0335():
    a=Vec2(Q(13),Q(12));b=a+Vec2(Q(14),Q(7))
    shift=Vec2(Q(7),Q(-14))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0336():
    a=Vec2(Q(14),Q(13));b=a+Vec2(Q(15),Q(1))
    shift=Vec2(Q(1),Q(-15))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0337():
    a=Vec2(Q(15),Q(14));b=a+Vec2(Q(16),Q(2))
    shift=Vec2(Q(2),Q(-16))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0338():
    a=Vec2(Q(16),Q(2));b=a+Vec2(Q(17),Q(3))
    shift=Vec2(Q(3),Q(-17))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0339():
    a=Vec2(Q(17),Q(3));b=a+Vec2(Q(18),Q(4))
    shift=Vec2(Q(4),Q(-18))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0340():
    a=Vec2(Q(1),Q(4));b=a+Vec2(Q(19),Q(5))
    shift=Vec2(Q(5),Q(-19))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0341():
    a=Vec2(Q(2),Q(5));b=a+Vec2(Q(20),Q(6))
    shift=Vec2(Q(6),Q(-20))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0342():
    a=Vec2(Q(3),Q(6));b=a+Vec2(Q(21),Q(7))
    shift=Vec2(Q(7),Q(-21))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0343():
    a=Vec2(Q(4),Q(7));b=a+Vec2(Q(22),Q(1))
    shift=Vec2(Q(1),Q(-22))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0344():
    a=Vec2(Q(5),Q(8));b=a+Vec2(Q(23),Q(2))
    shift=Vec2(Q(2),Q(-23))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0345():
    a=Vec2(Q(6),Q(9));b=a+Vec2(Q(1),Q(3))
    shift=Vec2(Q(3),Q(-1))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0346():
    a=Vec2(Q(7),Q(10));b=a+Vec2(Q(2),Q(4))
    shift=Vec2(Q(4),Q(-2))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0347():
    a=Vec2(Q(8),Q(11));b=a+Vec2(Q(3),Q(5))
    shift=Vec2(Q(5),Q(-3))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0348():
    a=Vec2(Q(9),Q(12));b=a+Vec2(Q(4),Q(6))
    shift=Vec2(Q(6),Q(-4))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0349():
    a=Vec2(Q(10),Q(13));b=a+Vec2(Q(5),Q(7))
    shift=Vec2(Q(7),Q(-5))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0350():
    a=Vec2(Q(11),Q(14));b=a+Vec2(Q(6),Q(1))
    shift=Vec2(Q(1),Q(-6))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0351():
    a=Vec2(Q(12),Q(2));b=a+Vec2(Q(7),Q(2))
    shift=Vec2(Q(2),Q(-7))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0352():
    a=Vec2(Q(13),Q(3));b=a+Vec2(Q(8),Q(3))
    shift=Vec2(Q(3),Q(-8))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0353():
    a=Vec2(Q(14),Q(4));b=a+Vec2(Q(9),Q(4))
    shift=Vec2(Q(4),Q(-9))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0354():
    a=Vec2(Q(15),Q(5));b=a+Vec2(Q(10),Q(5))
    shift=Vec2(Q(5),Q(-10))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0355():
    a=Vec2(Q(16),Q(6));b=a+Vec2(Q(11),Q(6))
    shift=Vec2(Q(6),Q(-11))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0356():
    a=Vec2(Q(17),Q(7));b=a+Vec2(Q(12),Q(7))
    shift=Vec2(Q(7),Q(-12))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0357():
    a=Vec2(Q(1),Q(8));b=a+Vec2(Q(13),Q(1))
    shift=Vec2(Q(1),Q(-13))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0358():
    a=Vec2(Q(2),Q(9));b=a+Vec2(Q(14),Q(2))
    shift=Vec2(Q(2),Q(-14))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0359():
    a=Vec2(Q(3),Q(10));b=a+Vec2(Q(15),Q(3))
    shift=Vec2(Q(3),Q(-15))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0360():
    a=Vec2(Q(4),Q(11));b=a+Vec2(Q(16),Q(4))
    shift=Vec2(Q(4),Q(-16))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0361():
    a=Vec2(Q(5),Q(12));b=a+Vec2(Q(17),Q(5))
    shift=Vec2(Q(5),Q(-17))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0362():
    a=Vec2(Q(6),Q(13));b=a+Vec2(Q(18),Q(6))
    shift=Vec2(Q(6),Q(-18))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0363():
    a=Vec2(Q(7),Q(14));b=a+Vec2(Q(19),Q(7))
    shift=Vec2(Q(7),Q(-19))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0364():
    a=Vec2(Q(8),Q(2));b=a+Vec2(Q(20),Q(1))
    shift=Vec2(Q(1),Q(-20))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0365():
    a=Vec2(Q(9),Q(3));b=a+Vec2(Q(21),Q(2))
    shift=Vec2(Q(2),Q(-21))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0366():
    a=Vec2(Q(10),Q(4));b=a+Vec2(Q(22),Q(3))
    shift=Vec2(Q(3),Q(-22))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0367():
    a=Vec2(Q(11),Q(5));b=a+Vec2(Q(23),Q(4))
    shift=Vec2(Q(4),Q(-23))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0368():
    a=Vec2(Q(12),Q(6));b=a+Vec2(Q(1),Q(5))
    shift=Vec2(Q(5),Q(-1))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0369():
    a=Vec2(Q(13),Q(7));b=a+Vec2(Q(2),Q(6))
    shift=Vec2(Q(6),Q(-2))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0370():
    a=Vec2(Q(14),Q(8));b=a+Vec2(Q(3),Q(7))
    shift=Vec2(Q(7),Q(-3))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0371():
    a=Vec2(Q(15),Q(9));b=a+Vec2(Q(4),Q(1))
    shift=Vec2(Q(1),Q(-4))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0372():
    a=Vec2(Q(16),Q(10));b=a+Vec2(Q(5),Q(2))
    shift=Vec2(Q(2),Q(-5))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0373():
    a=Vec2(Q(17),Q(11));b=a+Vec2(Q(6),Q(3))
    shift=Vec2(Q(3),Q(-6))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0374():
    a=Vec2(Q(1),Q(12));b=a+Vec2(Q(7),Q(4))
    shift=Vec2(Q(4),Q(-7))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0375():
    a=Vec2(Q(2),Q(13));b=a+Vec2(Q(8),Q(5))
    shift=Vec2(Q(5),Q(-8))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0376():
    a=Vec2(Q(3),Q(14));b=a+Vec2(Q(9),Q(6))
    shift=Vec2(Q(6),Q(-9))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0377():
    a=Vec2(Q(4),Q(2));b=a+Vec2(Q(10),Q(7))
    shift=Vec2(Q(7),Q(-10))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0378():
    a=Vec2(Q(5),Q(3));b=a+Vec2(Q(11),Q(1))
    shift=Vec2(Q(1),Q(-11))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0379():
    a=Vec2(Q(6),Q(4));b=a+Vec2(Q(12),Q(2))
    shift=Vec2(Q(2),Q(-12))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0380():
    a=Vec2(Q(7),Q(5));b=a+Vec2(Q(13),Q(3))
    shift=Vec2(Q(3),Q(-13))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0381():
    a=Vec2(Q(8),Q(6));b=a+Vec2(Q(14),Q(4))
    shift=Vec2(Q(4),Q(-14))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0382():
    a=Vec2(Q(9),Q(7));b=a+Vec2(Q(15),Q(5))
    shift=Vec2(Q(5),Q(-15))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0383():
    a=Vec2(Q(10),Q(8));b=a+Vec2(Q(16),Q(6))
    shift=Vec2(Q(6),Q(-16))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0384():
    a=Vec2(Q(11),Q(9));b=a+Vec2(Q(17),Q(7))
    shift=Vec2(Q(7),Q(-17))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0385():
    a=Vec2(Q(12),Q(10));b=a+Vec2(Q(18),Q(1))
    shift=Vec2(Q(1),Q(-18))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0386():
    a=Vec2(Q(13),Q(11));b=a+Vec2(Q(19),Q(2))
    shift=Vec2(Q(2),Q(-19))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0387():
    a=Vec2(Q(14),Q(12));b=a+Vec2(Q(20),Q(3))
    shift=Vec2(Q(3),Q(-20))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0388():
    a=Vec2(Q(15),Q(13));b=a+Vec2(Q(21),Q(4))
    shift=Vec2(Q(4),Q(-21))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0389():
    a=Vec2(Q(16),Q(14));b=a+Vec2(Q(22),Q(5))
    shift=Vec2(Q(5),Q(-22))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0390():
    a=Vec2(Q(17),Q(2));b=a+Vec2(Q(23),Q(6))
    shift=Vec2(Q(6),Q(-23))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0391():
    a=Vec2(Q(1),Q(3));b=a+Vec2(Q(1),Q(7))
    shift=Vec2(Q(7),Q(-1))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0392():
    a=Vec2(Q(2),Q(4));b=a+Vec2(Q(2),Q(1))
    shift=Vec2(Q(1),Q(-2))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0393():
    a=Vec2(Q(3),Q(5));b=a+Vec2(Q(3),Q(2))
    shift=Vec2(Q(2),Q(-3))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0394():
    a=Vec2(Q(4),Q(6));b=a+Vec2(Q(4),Q(3))
    shift=Vec2(Q(3),Q(-4))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0395():
    a=Vec2(Q(5),Q(7));b=a+Vec2(Q(5),Q(4))
    shift=Vec2(Q(4),Q(-5))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0396():
    a=Vec2(Q(6),Q(8));b=a+Vec2(Q(6),Q(5))
    shift=Vec2(Q(5),Q(-6))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0397():
    a=Vec2(Q(7),Q(9));b=a+Vec2(Q(7),Q(6))
    shift=Vec2(Q(6),Q(-7))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0398():
    a=Vec2(Q(8),Q(10));b=a+Vec2(Q(8),Q(7))
    shift=Vec2(Q(7),Q(-8))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0399():
    a=Vec2(Q(9),Q(11));b=a+Vec2(Q(9),Q(1))
    shift=Vec2(Q(1),Q(-9))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0400():
    a=Vec2(Q(10),Q(12));b=a+Vec2(Q(10),Q(2))
    shift=Vec2(Q(2),Q(-10))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0401():
    a=Vec2(Q(11),Q(13));b=a+Vec2(Q(11),Q(3))
    shift=Vec2(Q(3),Q(-11))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0402():
    a=Vec2(Q(12),Q(14));b=a+Vec2(Q(12),Q(4))
    shift=Vec2(Q(4),Q(-12))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0403():
    a=Vec2(Q(13),Q(2));b=a+Vec2(Q(13),Q(5))
    shift=Vec2(Q(5),Q(-13))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0404():
    a=Vec2(Q(14),Q(3));b=a+Vec2(Q(14),Q(6))
    shift=Vec2(Q(6),Q(-14))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0405():
    a=Vec2(Q(15),Q(4));b=a+Vec2(Q(15),Q(7))
    shift=Vec2(Q(7),Q(-15))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0406():
    a=Vec2(Q(16),Q(5));b=a+Vec2(Q(16),Q(1))
    shift=Vec2(Q(1),Q(-16))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0407():
    a=Vec2(Q(17),Q(6));b=a+Vec2(Q(17),Q(2))
    shift=Vec2(Q(2),Q(-17))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0408():
    a=Vec2(Q(1),Q(7));b=a+Vec2(Q(18),Q(3))
    shift=Vec2(Q(3),Q(-18))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0409():
    a=Vec2(Q(2),Q(8));b=a+Vec2(Q(19),Q(4))
    shift=Vec2(Q(4),Q(-19))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0410():
    a=Vec2(Q(3),Q(9));b=a+Vec2(Q(20),Q(5))
    shift=Vec2(Q(5),Q(-20))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0411():
    a=Vec2(Q(4),Q(10));b=a+Vec2(Q(21),Q(6))
    shift=Vec2(Q(6),Q(-21))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0412():
    a=Vec2(Q(5),Q(11));b=a+Vec2(Q(22),Q(7))
    shift=Vec2(Q(7),Q(-22))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0413():
    a=Vec2(Q(6),Q(12));b=a+Vec2(Q(23),Q(1))
    shift=Vec2(Q(1),Q(-23))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0414():
    a=Vec2(Q(7),Q(13));b=a+Vec2(Q(1),Q(2))
    shift=Vec2(Q(2),Q(-1))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0415():
    a=Vec2(Q(8),Q(14));b=a+Vec2(Q(2),Q(3))
    shift=Vec2(Q(3),Q(-2))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0416():
    a=Vec2(Q(9),Q(2));b=a+Vec2(Q(3),Q(4))
    shift=Vec2(Q(4),Q(-3))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0417():
    a=Vec2(Q(10),Q(3));b=a+Vec2(Q(4),Q(5))
    shift=Vec2(Q(5),Q(-4))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0418():
    a=Vec2(Q(11),Q(4));b=a+Vec2(Q(5),Q(6))
    shift=Vec2(Q(6),Q(-5))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0419():
    a=Vec2(Q(12),Q(5));b=a+Vec2(Q(6),Q(7))
    shift=Vec2(Q(7),Q(-6))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0420():
    a=Vec2(Q(13),Q(6));b=a+Vec2(Q(7),Q(1))
    shift=Vec2(Q(1),Q(-7))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0421():
    a=Vec2(Q(14),Q(7));b=a+Vec2(Q(8),Q(2))
    shift=Vec2(Q(2),Q(-8))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0422():
    a=Vec2(Q(15),Q(8));b=a+Vec2(Q(9),Q(3))
    shift=Vec2(Q(3),Q(-9))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0423():
    a=Vec2(Q(16),Q(9));b=a+Vec2(Q(10),Q(4))
    shift=Vec2(Q(4),Q(-10))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0424():
    a=Vec2(Q(17),Q(10));b=a+Vec2(Q(11),Q(5))
    shift=Vec2(Q(5),Q(-11))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0425():
    a=Vec2(Q(1),Q(11));b=a+Vec2(Q(12),Q(6))
    shift=Vec2(Q(6),Q(-12))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0426():
    a=Vec2(Q(2),Q(12));b=a+Vec2(Q(13),Q(7))
    shift=Vec2(Q(7),Q(-13))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0427():
    a=Vec2(Q(3),Q(13));b=a+Vec2(Q(14),Q(1))
    shift=Vec2(Q(1),Q(-14))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0428():
    a=Vec2(Q(4),Q(14));b=a+Vec2(Q(15),Q(2))
    shift=Vec2(Q(2),Q(-15))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0429():
    a=Vec2(Q(5),Q(2));b=a+Vec2(Q(16),Q(3))
    shift=Vec2(Q(3),Q(-16))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0430():
    a=Vec2(Q(6),Q(3));b=a+Vec2(Q(17),Q(4))
    shift=Vec2(Q(4),Q(-17))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0431():
    a=Vec2(Q(7),Q(4));b=a+Vec2(Q(18),Q(5))
    shift=Vec2(Q(5),Q(-18))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0432():
    a=Vec2(Q(8),Q(5));b=a+Vec2(Q(19),Q(6))
    shift=Vec2(Q(6),Q(-19))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0433():
    a=Vec2(Q(9),Q(6));b=a+Vec2(Q(20),Q(7))
    shift=Vec2(Q(7),Q(-20))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0434():
    a=Vec2(Q(10),Q(7));b=a+Vec2(Q(21),Q(1))
    shift=Vec2(Q(1),Q(-21))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0435():
    a=Vec2(Q(11),Q(8));b=a+Vec2(Q(22),Q(2))
    shift=Vec2(Q(2),Q(-22))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0436():
    a=Vec2(Q(12),Q(9));b=a+Vec2(Q(23),Q(3))
    shift=Vec2(Q(3),Q(-23))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0437():
    a=Vec2(Q(13),Q(10));b=a+Vec2(Q(1),Q(4))
    shift=Vec2(Q(4),Q(-1))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0438():
    a=Vec2(Q(14),Q(11));b=a+Vec2(Q(2),Q(5))
    shift=Vec2(Q(5),Q(-2))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0439():
    a=Vec2(Q(15),Q(12));b=a+Vec2(Q(3),Q(6))
    shift=Vec2(Q(6),Q(-3))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0440():
    a=Vec2(Q(16),Q(13));b=a+Vec2(Q(4),Q(7))
    shift=Vec2(Q(7),Q(-4))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0441():
    a=Vec2(Q(17),Q(14));b=a+Vec2(Q(5),Q(1))
    shift=Vec2(Q(1),Q(-5))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0442():
    a=Vec2(Q(1),Q(2));b=a+Vec2(Q(6),Q(2))
    shift=Vec2(Q(2),Q(-6))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0443():
    a=Vec2(Q(2),Q(3));b=a+Vec2(Q(7),Q(3))
    shift=Vec2(Q(3),Q(-7))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0444():
    a=Vec2(Q(3),Q(4));b=a+Vec2(Q(8),Q(4))
    shift=Vec2(Q(4),Q(-8))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0445():
    a=Vec2(Q(4),Q(5));b=a+Vec2(Q(9),Q(5))
    shift=Vec2(Q(5),Q(-9))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0446():
    a=Vec2(Q(5),Q(6));b=a+Vec2(Q(10),Q(6))
    shift=Vec2(Q(6),Q(-10))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0447():
    a=Vec2(Q(6),Q(7));b=a+Vec2(Q(11),Q(7))
    shift=Vec2(Q(7),Q(-11))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0448():
    a=Vec2(Q(7),Q(8));b=a+Vec2(Q(12),Q(1))
    shift=Vec2(Q(1),Q(-12))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0449():
    a=Vec2(Q(8),Q(9));b=a+Vec2(Q(13),Q(2))
    shift=Vec2(Q(2),Q(-13))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0450():
    a=Vec2(Q(9),Q(10));b=a+Vec2(Q(14),Q(3))
    shift=Vec2(Q(3),Q(-14))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0451():
    a=Vec2(Q(10),Q(11));b=a+Vec2(Q(15),Q(4))
    shift=Vec2(Q(4),Q(-15))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0452():
    a=Vec2(Q(11),Q(12));b=a+Vec2(Q(16),Q(5))
    shift=Vec2(Q(5),Q(-16))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0453():
    a=Vec2(Q(12),Q(13));b=a+Vec2(Q(17),Q(6))
    shift=Vec2(Q(6),Q(-17))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0454():
    a=Vec2(Q(13),Q(14));b=a+Vec2(Q(18),Q(7))
    shift=Vec2(Q(7),Q(-18))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0455():
    a=Vec2(Q(14),Q(2));b=a+Vec2(Q(19),Q(1))
    shift=Vec2(Q(1),Q(-19))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0456():
    a=Vec2(Q(15),Q(3));b=a+Vec2(Q(20),Q(2))
    shift=Vec2(Q(2),Q(-20))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0457():
    a=Vec2(Q(16),Q(4));b=a+Vec2(Q(21),Q(3))
    shift=Vec2(Q(3),Q(-21))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0458():
    a=Vec2(Q(17),Q(5));b=a+Vec2(Q(22),Q(4))
    shift=Vec2(Q(4),Q(-22))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0459():
    a=Vec2(Q(1),Q(6));b=a+Vec2(Q(23),Q(5))
    shift=Vec2(Q(5),Q(-23))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0460():
    a=Vec2(Q(2),Q(7));b=a+Vec2(Q(1),Q(6))
    shift=Vec2(Q(6),Q(-1))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0461():
    a=Vec2(Q(3),Q(8));b=a+Vec2(Q(2),Q(7))
    shift=Vec2(Q(7),Q(-2))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0462():
    a=Vec2(Q(4),Q(9));b=a+Vec2(Q(3),Q(1))
    shift=Vec2(Q(1),Q(-3))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0463():
    a=Vec2(Q(5),Q(10));b=a+Vec2(Q(4),Q(2))
    shift=Vec2(Q(2),Q(-4))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0464():
    a=Vec2(Q(6),Q(11));b=a+Vec2(Q(5),Q(3))
    shift=Vec2(Q(3),Q(-5))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0465():
    a=Vec2(Q(7),Q(12));b=a+Vec2(Q(6),Q(4))
    shift=Vec2(Q(4),Q(-6))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0466():
    a=Vec2(Q(8),Q(13));b=a+Vec2(Q(7),Q(5))
    shift=Vec2(Q(5),Q(-7))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0467():
    a=Vec2(Q(9),Q(14));b=a+Vec2(Q(8),Q(6))
    shift=Vec2(Q(6),Q(-8))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0468():
    a=Vec2(Q(10),Q(2));b=a+Vec2(Q(9),Q(7))
    shift=Vec2(Q(7),Q(-9))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0469():
    a=Vec2(Q(11),Q(3));b=a+Vec2(Q(10),Q(1))
    shift=Vec2(Q(1),Q(-10))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0470():
    a=Vec2(Q(12),Q(4));b=a+Vec2(Q(11),Q(2))
    shift=Vec2(Q(2),Q(-11))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0471():
    a=Vec2(Q(13),Q(5));b=a+Vec2(Q(12),Q(3))
    shift=Vec2(Q(3),Q(-12))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0472():
    a=Vec2(Q(14),Q(6));b=a+Vec2(Q(13),Q(4))
    shift=Vec2(Q(4),Q(-13))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0473():
    a=Vec2(Q(15),Q(7));b=a+Vec2(Q(14),Q(5))
    shift=Vec2(Q(5),Q(-14))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0474():
    a=Vec2(Q(16),Q(8));b=a+Vec2(Q(15),Q(6))
    shift=Vec2(Q(6),Q(-15))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0475():
    a=Vec2(Q(17),Q(9));b=a+Vec2(Q(16),Q(7))
    shift=Vec2(Q(7),Q(-16))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0476():
    a=Vec2(Q(1),Q(10));b=a+Vec2(Q(17),Q(1))
    shift=Vec2(Q(1),Q(-17))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0477():
    a=Vec2(Q(2),Q(11));b=a+Vec2(Q(18),Q(2))
    shift=Vec2(Q(2),Q(-18))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0478():
    a=Vec2(Q(3),Q(12));b=a+Vec2(Q(19),Q(3))
    shift=Vec2(Q(3),Q(-19))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0479():
    a=Vec2(Q(4),Q(13));b=a+Vec2(Q(20),Q(4))
    shift=Vec2(Q(4),Q(-20))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0480():
    a=Vec2(Q(5),Q(14));b=a+Vec2(Q(21),Q(5))
    shift=Vec2(Q(5),Q(-21))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0481():
    a=Vec2(Q(6),Q(2));b=a+Vec2(Q(22),Q(6))
    shift=Vec2(Q(6),Q(-22))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0482():
    a=Vec2(Q(7),Q(3));b=a+Vec2(Q(23),Q(7))
    shift=Vec2(Q(7),Q(-23))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0483():
    a=Vec2(Q(8),Q(4));b=a+Vec2(Q(1),Q(1))
    shift=Vec2(Q(1),Q(-1))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0484():
    a=Vec2(Q(9),Q(5));b=a+Vec2(Q(2),Q(2))
    shift=Vec2(Q(2),Q(-2))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0485():
    a=Vec2(Q(10),Q(6));b=a+Vec2(Q(3),Q(3))
    shift=Vec2(Q(3),Q(-3))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0486():
    a=Vec2(Q(11),Q(7));b=a+Vec2(Q(4),Q(4))
    shift=Vec2(Q(4),Q(-4))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0487():
    a=Vec2(Q(12),Q(8));b=a+Vec2(Q(5),Q(5))
    shift=Vec2(Q(5),Q(-5))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0488():
    a=Vec2(Q(13),Q(9));b=a+Vec2(Q(6),Q(6))
    shift=Vec2(Q(6),Q(-6))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0489():
    a=Vec2(Q(14),Q(10));b=a+Vec2(Q(7),Q(7))
    shift=Vec2(Q(7),Q(-7))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0490():
    a=Vec2(Q(15),Q(11));b=a+Vec2(Q(8),Q(1))
    shift=Vec2(Q(1),Q(-8))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0491():
    a=Vec2(Q(16),Q(12));b=a+Vec2(Q(9),Q(2))
    shift=Vec2(Q(2),Q(-9))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0492():
    a=Vec2(Q(17),Q(13));b=a+Vec2(Q(10),Q(3))
    shift=Vec2(Q(3),Q(-10))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0493():
    a=Vec2(Q(1),Q(14));b=a+Vec2(Q(11),Q(4))
    shift=Vec2(Q(4),Q(-11))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0494():
    a=Vec2(Q(2),Q(2));b=a+Vec2(Q(12),Q(5))
    shift=Vec2(Q(5),Q(-12))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0495():
    a=Vec2(Q(3),Q(3));b=a+Vec2(Q(13),Q(6))
    shift=Vec2(Q(6),Q(-13))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0496():
    a=Vec2(Q(4),Q(4));b=a+Vec2(Q(14),Q(7))
    shift=Vec2(Q(7),Q(-14))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0497():
    a=Vec2(Q(5),Q(5));b=a+Vec2(Q(15),Q(1))
    shift=Vec2(Q(1),Q(-15))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0498():
    a=Vec2(Q(6),Q(6));b=a+Vec2(Q(16),Q(2))
    shift=Vec2(Q(2),Q(-16))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0499():
    a=Vec2(Q(7),Q(7));b=a+Vec2(Q(17),Q(3))
    shift=Vec2(Q(3),Q(-17))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0500():
    a=Vec2(Q(8),Q(8));b=a+Vec2(Q(18),Q(4))
    shift=Vec2(Q(4),Q(-18))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0501():
    a=Vec2(Q(9),Q(9));b=a+Vec2(Q(19),Q(5))
    shift=Vec2(Q(5),Q(-19))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0502():
    a=Vec2(Q(10),Q(10));b=a+Vec2(Q(20),Q(6))
    shift=Vec2(Q(6),Q(-20))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0503():
    a=Vec2(Q(11),Q(11));b=a+Vec2(Q(21),Q(7))
    shift=Vec2(Q(7),Q(-21))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0504():
    a=Vec2(Q(12),Q(12));b=a+Vec2(Q(22),Q(1))
    shift=Vec2(Q(1),Q(-22))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0505():
    a=Vec2(Q(13),Q(13));b=a+Vec2(Q(23),Q(2))
    shift=Vec2(Q(2),Q(-23))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0506():
    a=Vec2(Q(14),Q(14));b=a+Vec2(Q(1),Q(3))
    shift=Vec2(Q(3),Q(-1))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0507():
    a=Vec2(Q(15),Q(2));b=a+Vec2(Q(2),Q(4))
    shift=Vec2(Q(4),Q(-2))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0508():
    a=Vec2(Q(16),Q(3));b=a+Vec2(Q(3),Q(5))
    shift=Vec2(Q(5),Q(-3))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0509():
    a=Vec2(Q(17),Q(4));b=a+Vec2(Q(4),Q(6))
    shift=Vec2(Q(6),Q(-4))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0510():
    a=Vec2(Q(1),Q(5));b=a+Vec2(Q(5),Q(7))
    shift=Vec2(Q(7),Q(-5))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0511():
    a=Vec2(Q(2),Q(6));b=a+Vec2(Q(6),Q(1))
    shift=Vec2(Q(1),Q(-6))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0512():
    a=Vec2(Q(3),Q(7));b=a+Vec2(Q(7),Q(2))
    shift=Vec2(Q(2),Q(-7))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0513():
    a=Vec2(Q(4),Q(8));b=a+Vec2(Q(8),Q(3))
    shift=Vec2(Q(3),Q(-8))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0514():
    a=Vec2(Q(5),Q(9));b=a+Vec2(Q(9),Q(4))
    shift=Vec2(Q(4),Q(-9))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0515():
    a=Vec2(Q(6),Q(10));b=a+Vec2(Q(10),Q(5))
    shift=Vec2(Q(5),Q(-10))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0516():
    a=Vec2(Q(7),Q(11));b=a+Vec2(Q(11),Q(6))
    shift=Vec2(Q(6),Q(-11))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0517():
    a=Vec2(Q(8),Q(12));b=a+Vec2(Q(12),Q(7))
    shift=Vec2(Q(7),Q(-12))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0518():
    a=Vec2(Q(9),Q(13));b=a+Vec2(Q(13),Q(1))
    shift=Vec2(Q(1),Q(-13))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0519():
    a=Vec2(Q(10),Q(14));b=a+Vec2(Q(14),Q(2))
    shift=Vec2(Q(2),Q(-14))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0520():
    a=Vec2(Q(11),Q(2));b=a+Vec2(Q(15),Q(3))
    shift=Vec2(Q(3),Q(-15))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0521():
    a=Vec2(Q(12),Q(3));b=a+Vec2(Q(16),Q(4))
    shift=Vec2(Q(4),Q(-16))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0522():
    a=Vec2(Q(13),Q(4));b=a+Vec2(Q(17),Q(5))
    shift=Vec2(Q(5),Q(-17))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0523():
    a=Vec2(Q(14),Q(5));b=a+Vec2(Q(18),Q(6))
    shift=Vec2(Q(6),Q(-18))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0524():
    a=Vec2(Q(15),Q(6));b=a+Vec2(Q(19),Q(7))
    shift=Vec2(Q(7),Q(-19))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0525():
    a=Vec2(Q(16),Q(7));b=a+Vec2(Q(20),Q(1))
    shift=Vec2(Q(1),Q(-20))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0526():
    a=Vec2(Q(17),Q(8));b=a+Vec2(Q(21),Q(2))
    shift=Vec2(Q(2),Q(-21))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0527():
    a=Vec2(Q(1),Q(9));b=a+Vec2(Q(22),Q(3))
    shift=Vec2(Q(3),Q(-22))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0528():
    a=Vec2(Q(2),Q(10));b=a+Vec2(Q(23),Q(4))
    shift=Vec2(Q(4),Q(-23))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0529():
    a=Vec2(Q(3),Q(11));b=a+Vec2(Q(1),Q(5))
    shift=Vec2(Q(5),Q(-1))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0530():
    a=Vec2(Q(4),Q(12));b=a+Vec2(Q(2),Q(6))
    shift=Vec2(Q(6),Q(-2))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0531():
    a=Vec2(Q(5),Q(13));b=a+Vec2(Q(3),Q(7))
    shift=Vec2(Q(7),Q(-3))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0532():
    a=Vec2(Q(6),Q(14));b=a+Vec2(Q(4),Q(1))
    shift=Vec2(Q(1),Q(-4))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0533():
    a=Vec2(Q(7),Q(2));b=a+Vec2(Q(5),Q(2))
    shift=Vec2(Q(2),Q(-5))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0534():
    a=Vec2(Q(8),Q(3));b=a+Vec2(Q(6),Q(3))
    shift=Vec2(Q(3),Q(-6))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0535():
    a=Vec2(Q(9),Q(4));b=a+Vec2(Q(7),Q(4))
    shift=Vec2(Q(4),Q(-7))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0536():
    a=Vec2(Q(10),Q(5));b=a+Vec2(Q(8),Q(5))
    shift=Vec2(Q(5),Q(-8))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0537():
    a=Vec2(Q(11),Q(6));b=a+Vec2(Q(9),Q(6))
    shift=Vec2(Q(6),Q(-9))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0538():
    a=Vec2(Q(12),Q(7));b=a+Vec2(Q(10),Q(7))
    shift=Vec2(Q(7),Q(-10))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0539():
    a=Vec2(Q(13),Q(8));b=a+Vec2(Q(11),Q(1))
    shift=Vec2(Q(1),Q(-11))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0540():
    a=Vec2(Q(14),Q(9));b=a+Vec2(Q(12),Q(2))
    shift=Vec2(Q(2),Q(-12))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0541():
    a=Vec2(Q(15),Q(10));b=a+Vec2(Q(13),Q(3))
    shift=Vec2(Q(3),Q(-13))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0542():
    a=Vec2(Q(16),Q(11));b=a+Vec2(Q(14),Q(4))
    shift=Vec2(Q(4),Q(-14))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0543():
    a=Vec2(Q(17),Q(12));b=a+Vec2(Q(15),Q(5))
    shift=Vec2(Q(5),Q(-15))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0544():
    a=Vec2(Q(1),Q(13));b=a+Vec2(Q(16),Q(6))
    shift=Vec2(Q(6),Q(-16))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0545():
    a=Vec2(Q(2),Q(14));b=a+Vec2(Q(17),Q(7))
    shift=Vec2(Q(7),Q(-17))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0546():
    a=Vec2(Q(3),Q(2));b=a+Vec2(Q(18),Q(1))
    shift=Vec2(Q(1),Q(-18))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0547():
    a=Vec2(Q(4),Q(3));b=a+Vec2(Q(19),Q(2))
    shift=Vec2(Q(2),Q(-19))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0548():
    a=Vec2(Q(5),Q(4));b=a+Vec2(Q(20),Q(3))
    shift=Vec2(Q(3),Q(-20))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0549():
    a=Vec2(Q(6),Q(5));b=a+Vec2(Q(21),Q(4))
    shift=Vec2(Q(4),Q(-21))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0550():
    a=Vec2(Q(7),Q(6));b=a+Vec2(Q(22),Q(5))
    shift=Vec2(Q(5),Q(-22))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0551():
    a=Vec2(Q(8),Q(7));b=a+Vec2(Q(23),Q(6))
    shift=Vec2(Q(6),Q(-23))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0552():
    a=Vec2(Q(9),Q(8));b=a+Vec2(Q(1),Q(7))
    shift=Vec2(Q(7),Q(-1))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0553():
    a=Vec2(Q(10),Q(9));b=a+Vec2(Q(2),Q(1))
    shift=Vec2(Q(1),Q(-2))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0554():
    a=Vec2(Q(11),Q(10));b=a+Vec2(Q(3),Q(2))
    shift=Vec2(Q(2),Q(-3))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0555():
    a=Vec2(Q(12),Q(11));b=a+Vec2(Q(4),Q(3))
    shift=Vec2(Q(3),Q(-4))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0556():
    a=Vec2(Q(13),Q(12));b=a+Vec2(Q(5),Q(4))
    shift=Vec2(Q(4),Q(-5))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0557():
    a=Vec2(Q(14),Q(13));b=a+Vec2(Q(6),Q(5))
    shift=Vec2(Q(5),Q(-6))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0558():
    a=Vec2(Q(15),Q(14));b=a+Vec2(Q(7),Q(6))
    shift=Vec2(Q(6),Q(-7))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0559():
    a=Vec2(Q(16),Q(2));b=a+Vec2(Q(8),Q(7))
    shift=Vec2(Q(7),Q(-8))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0560():
    a=Vec2(Q(17),Q(3));b=a+Vec2(Q(9),Q(1))
    shift=Vec2(Q(1),Q(-9))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0561():
    a=Vec2(Q(1),Q(4));b=a+Vec2(Q(10),Q(2))
    shift=Vec2(Q(2),Q(-10))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0562():
    a=Vec2(Q(2),Q(5));b=a+Vec2(Q(11),Q(3))
    shift=Vec2(Q(3),Q(-11))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0563():
    a=Vec2(Q(3),Q(6));b=a+Vec2(Q(12),Q(4))
    shift=Vec2(Q(4),Q(-12))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0564():
    a=Vec2(Q(4),Q(7));b=a+Vec2(Q(13),Q(5))
    shift=Vec2(Q(5),Q(-13))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0565():
    a=Vec2(Q(5),Q(8));b=a+Vec2(Q(14),Q(6))
    shift=Vec2(Q(6),Q(-14))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0566():
    a=Vec2(Q(6),Q(9));b=a+Vec2(Q(15),Q(7))
    shift=Vec2(Q(7),Q(-15))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0567():
    a=Vec2(Q(7),Q(10));b=a+Vec2(Q(16),Q(1))
    shift=Vec2(Q(1),Q(-16))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0568():
    a=Vec2(Q(8),Q(11));b=a+Vec2(Q(17),Q(2))
    shift=Vec2(Q(2),Q(-17))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0569():
    a=Vec2(Q(9),Q(12));b=a+Vec2(Q(18),Q(3))
    shift=Vec2(Q(3),Q(-18))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0570():
    a=Vec2(Q(10),Q(13));b=a+Vec2(Q(19),Q(4))
    shift=Vec2(Q(4),Q(-19))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0571():
    a=Vec2(Q(11),Q(14));b=a+Vec2(Q(20),Q(5))
    shift=Vec2(Q(5),Q(-20))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0572():
    a=Vec2(Q(12),Q(2));b=a+Vec2(Q(21),Q(6))
    shift=Vec2(Q(6),Q(-21))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0573():
    a=Vec2(Q(13),Q(3));b=a+Vec2(Q(22),Q(7))
    shift=Vec2(Q(7),Q(-22))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0574():
    a=Vec2(Q(14),Q(4));b=a+Vec2(Q(23),Q(1))
    shift=Vec2(Q(1),Q(-23))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0575():
    a=Vec2(Q(15),Q(5));b=a+Vec2(Q(1),Q(2))
    shift=Vec2(Q(2),Q(-1))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0576():
    a=Vec2(Q(16),Q(6));b=a+Vec2(Q(2),Q(3))
    shift=Vec2(Q(3),Q(-2))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0577():
    a=Vec2(Q(17),Q(7));b=a+Vec2(Q(3),Q(4))
    shift=Vec2(Q(4),Q(-3))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0578():
    a=Vec2(Q(1),Q(8));b=a+Vec2(Q(4),Q(5))
    shift=Vec2(Q(5),Q(-4))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0579():
    a=Vec2(Q(2),Q(9));b=a+Vec2(Q(5),Q(6))
    shift=Vec2(Q(6),Q(-5))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0580():
    a=Vec2(Q(3),Q(10));b=a+Vec2(Q(6),Q(7))
    shift=Vec2(Q(7),Q(-6))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0581():
    a=Vec2(Q(4),Q(11));b=a+Vec2(Q(7),Q(1))
    shift=Vec2(Q(1),Q(-7))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0582():
    a=Vec2(Q(5),Q(12));b=a+Vec2(Q(8),Q(2))
    shift=Vec2(Q(2),Q(-8))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0583():
    a=Vec2(Q(6),Q(13));b=a+Vec2(Q(9),Q(3))
    shift=Vec2(Q(3),Q(-9))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0584():
    a=Vec2(Q(7),Q(14));b=a+Vec2(Q(10),Q(4))
    shift=Vec2(Q(4),Q(-10))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0585():
    a=Vec2(Q(8),Q(2));b=a+Vec2(Q(11),Q(5))
    shift=Vec2(Q(5),Q(-11))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0586():
    a=Vec2(Q(9),Q(3));b=a+Vec2(Q(12),Q(6))
    shift=Vec2(Q(6),Q(-12))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0587():
    a=Vec2(Q(10),Q(4));b=a+Vec2(Q(13),Q(7))
    shift=Vec2(Q(7),Q(-13))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0588():
    a=Vec2(Q(11),Q(5));b=a+Vec2(Q(14),Q(1))
    shift=Vec2(Q(1),Q(-14))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0589():
    a=Vec2(Q(12),Q(6));b=a+Vec2(Q(15),Q(2))
    shift=Vec2(Q(2),Q(-15))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0590():
    a=Vec2(Q(13),Q(7));b=a+Vec2(Q(16),Q(3))
    shift=Vec2(Q(3),Q(-16))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0591():
    a=Vec2(Q(14),Q(8));b=a+Vec2(Q(17),Q(4))
    shift=Vec2(Q(4),Q(-17))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0592():
    a=Vec2(Q(15),Q(9));b=a+Vec2(Q(18),Q(5))
    shift=Vec2(Q(5),Q(-18))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0593():
    a=Vec2(Q(16),Q(10));b=a+Vec2(Q(19),Q(6))
    shift=Vec2(Q(6),Q(-19))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0594():
    a=Vec2(Q(17),Q(11));b=a+Vec2(Q(20),Q(7))
    shift=Vec2(Q(7),Q(-20))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0595():
    a=Vec2(Q(1),Q(12));b=a+Vec2(Q(21),Q(1))
    shift=Vec2(Q(1),Q(-21))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0596():
    a=Vec2(Q(2),Q(13));b=a+Vec2(Q(22),Q(2))
    shift=Vec2(Q(2),Q(-22))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0597():
    a=Vec2(Q(3),Q(14));b=a+Vec2(Q(23),Q(3))
    shift=Vec2(Q(3),Q(-23))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0598():
    a=Vec2(Q(4),Q(2));b=a+Vec2(Q(1),Q(4))
    shift=Vec2(Q(4),Q(-1))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

def test_line_translation_0599():
    a=Vec2(Q(5),Q(3));b=a+Vec2(Q(2),Q(5))
    shift=Vec2(Q(5),Q(-2))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0

