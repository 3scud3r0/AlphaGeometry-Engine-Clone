# GENERATED, DETERMINISTIC, NO TRAINED MODEL USED.
# Source generator: geoforge_upgrade_suite/generate_untrained_matrix.py
from fractions import Fraction as Q
from geoforge_upgrade_suite.geometry_exact import Vec2,Polynomial,Line
from geoforge_upgrade_suite.exact_constructions import SPoint,foot,line_intersection
from geoforge_upgrade_suite.deterministic_ideal import ExactIdealEngine,certificate_to_json,verify_certificate_json
from geoforge_upgrade_suite.deterministic_solver import ExactFactEvaluator,GuardLedger

def test_line_intersection_0000():
    a=SPoint(0,0);b=SPoint(1,1)
    c=SPoint(0,2);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0001():
    a=SPoint(0,0);b=SPoint(2,1)
    c=SPoint(0,3);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0002():
    a=SPoint(0,0);b=SPoint(3,1)
    c=SPoint(0,4);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0003():
    a=SPoint(0,0);b=SPoint(4,1)
    c=SPoint(0,5);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0004():
    a=SPoint(0,0);b=SPoint(5,1)
    c=SPoint(0,6);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0005():
    a=SPoint(0,0);b=SPoint(6,1)
    c=SPoint(0,7);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0006():
    a=SPoint(0,0);b=SPoint(7,1)
    c=SPoint(0,8);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0007():
    a=SPoint(0,0);b=SPoint(8,1)
    c=SPoint(0,9);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0008():
    a=SPoint(0,0);b=SPoint(9,1)
    c=SPoint(0,10);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0009():
    a=SPoint(0,0);b=SPoint(10,1)
    c=SPoint(0,11);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0010():
    a=SPoint(0,0);b=SPoint(11,1)
    c=SPoint(0,12);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0011():
    a=SPoint(0,0);b=SPoint(12,1)
    c=SPoint(0,13);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0012():
    a=SPoint(0,0);b=SPoint(13,1)
    c=SPoint(0,14);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0013():
    a=SPoint(0,0);b=SPoint(14,1)
    c=SPoint(0,2);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0014():
    a=SPoint(0,0);b=SPoint(15,1)
    c=SPoint(0,3);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0015():
    a=SPoint(0,0);b=SPoint(16,1)
    c=SPoint(0,4);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0016():
    a=SPoint(0,0);b=SPoint(17,1)
    c=SPoint(0,5);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0017():
    a=SPoint(0,0);b=SPoint(1,1)
    c=SPoint(0,6);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0018():
    a=SPoint(0,0);b=SPoint(2,1)
    c=SPoint(0,7);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0019():
    a=SPoint(0,0);b=SPoint(3,1)
    c=SPoint(0,8);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0020():
    a=SPoint(0,0);b=SPoint(4,1)
    c=SPoint(0,9);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0021():
    a=SPoint(0,0);b=SPoint(5,1)
    c=SPoint(0,10);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0022():
    a=SPoint(0,0);b=SPoint(6,1)
    c=SPoint(0,11);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0023():
    a=SPoint(0,0);b=SPoint(7,1)
    c=SPoint(0,12);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0024():
    a=SPoint(0,0);b=SPoint(8,1)
    c=SPoint(0,13);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0025():
    a=SPoint(0,0);b=SPoint(9,1)
    c=SPoint(0,14);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0026():
    a=SPoint(0,0);b=SPoint(10,1)
    c=SPoint(0,2);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0027():
    a=SPoint(0,0);b=SPoint(11,1)
    c=SPoint(0,3);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0028():
    a=SPoint(0,0);b=SPoint(12,1)
    c=SPoint(0,4);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0029():
    a=SPoint(0,0);b=SPoint(13,1)
    c=SPoint(0,5);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0030():
    a=SPoint(0,0);b=SPoint(14,1)
    c=SPoint(0,6);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0031():
    a=SPoint(0,0);b=SPoint(15,1)
    c=SPoint(0,7);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0032():
    a=SPoint(0,0);b=SPoint(16,1)
    c=SPoint(0,8);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0033():
    a=SPoint(0,0);b=SPoint(17,1)
    c=SPoint(0,9);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0034():
    a=SPoint(0,0);b=SPoint(1,1)
    c=SPoint(0,10);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0035():
    a=SPoint(0,0);b=SPoint(2,1)
    c=SPoint(0,11);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0036():
    a=SPoint(0,0);b=SPoint(3,1)
    c=SPoint(0,12);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0037():
    a=SPoint(0,0);b=SPoint(4,1)
    c=SPoint(0,13);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0038():
    a=SPoint(0,0);b=SPoint(5,1)
    c=SPoint(0,14);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0039():
    a=SPoint(0,0);b=SPoint(6,1)
    c=SPoint(0,2);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0040():
    a=SPoint(0,0);b=SPoint(7,1)
    c=SPoint(0,3);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0041():
    a=SPoint(0,0);b=SPoint(8,1)
    c=SPoint(0,4);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0042():
    a=SPoint(0,0);b=SPoint(9,1)
    c=SPoint(0,5);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0043():
    a=SPoint(0,0);b=SPoint(10,1)
    c=SPoint(0,6);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0044():
    a=SPoint(0,0);b=SPoint(11,1)
    c=SPoint(0,7);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0045():
    a=SPoint(0,0);b=SPoint(12,1)
    c=SPoint(0,8);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0046():
    a=SPoint(0,0);b=SPoint(13,1)
    c=SPoint(0,9);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0047():
    a=SPoint(0,0);b=SPoint(14,1)
    c=SPoint(0,10);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0048():
    a=SPoint(0,0);b=SPoint(15,1)
    c=SPoint(0,11);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0049():
    a=SPoint(0,0);b=SPoint(16,1)
    c=SPoint(0,12);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0050():
    a=SPoint(0,0);b=SPoint(17,1)
    c=SPoint(0,13);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0051():
    a=SPoint(0,0);b=SPoint(1,1)
    c=SPoint(0,14);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0052():
    a=SPoint(0,0);b=SPoint(2,1)
    c=SPoint(0,2);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0053():
    a=SPoint(0,0);b=SPoint(3,1)
    c=SPoint(0,3);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0054():
    a=SPoint(0,0);b=SPoint(4,1)
    c=SPoint(0,4);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0055():
    a=SPoint(0,0);b=SPoint(5,1)
    c=SPoint(0,5);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0056():
    a=SPoint(0,0);b=SPoint(6,1)
    c=SPoint(0,6);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0057():
    a=SPoint(0,0);b=SPoint(7,1)
    c=SPoint(0,7);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0058():
    a=SPoint(0,0);b=SPoint(8,1)
    c=SPoint(0,8);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0059():
    a=SPoint(0,0);b=SPoint(9,1)
    c=SPoint(0,9);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0060():
    a=SPoint(0,0);b=SPoint(10,1)
    c=SPoint(0,10);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0061():
    a=SPoint(0,0);b=SPoint(11,1)
    c=SPoint(0,11);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0062():
    a=SPoint(0,0);b=SPoint(12,1)
    c=SPoint(0,12);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0063():
    a=SPoint(0,0);b=SPoint(13,1)
    c=SPoint(0,13);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0064():
    a=SPoint(0,0);b=SPoint(14,1)
    c=SPoint(0,14);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0065():
    a=SPoint(0,0);b=SPoint(15,1)
    c=SPoint(0,2);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0066():
    a=SPoint(0,0);b=SPoint(16,1)
    c=SPoint(0,3);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0067():
    a=SPoint(0,0);b=SPoint(17,1)
    c=SPoint(0,4);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0068():
    a=SPoint(0,0);b=SPoint(1,1)
    c=SPoint(0,5);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0069():
    a=SPoint(0,0);b=SPoint(2,1)
    c=SPoint(0,6);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0070():
    a=SPoint(0,0);b=SPoint(3,1)
    c=SPoint(0,7);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0071():
    a=SPoint(0,0);b=SPoint(4,1)
    c=SPoint(0,8);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0072():
    a=SPoint(0,0);b=SPoint(5,1)
    c=SPoint(0,9);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0073():
    a=SPoint(0,0);b=SPoint(6,1)
    c=SPoint(0,10);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0074():
    a=SPoint(0,0);b=SPoint(7,1)
    c=SPoint(0,11);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0075():
    a=SPoint(0,0);b=SPoint(8,1)
    c=SPoint(0,12);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0076():
    a=SPoint(0,0);b=SPoint(9,1)
    c=SPoint(0,13);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0077():
    a=SPoint(0,0);b=SPoint(10,1)
    c=SPoint(0,14);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0078():
    a=SPoint(0,0);b=SPoint(11,1)
    c=SPoint(0,2);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0079():
    a=SPoint(0,0);b=SPoint(12,1)
    c=SPoint(0,3);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0080():
    a=SPoint(0,0);b=SPoint(13,1)
    c=SPoint(0,4);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0081():
    a=SPoint(0,0);b=SPoint(14,1)
    c=SPoint(0,5);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0082():
    a=SPoint(0,0);b=SPoint(15,1)
    c=SPoint(0,6);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0083():
    a=SPoint(0,0);b=SPoint(16,1)
    c=SPoint(0,7);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0084():
    a=SPoint(0,0);b=SPoint(17,1)
    c=SPoint(0,8);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0085():
    a=SPoint(0,0);b=SPoint(1,1)
    c=SPoint(0,9);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0086():
    a=SPoint(0,0);b=SPoint(2,1)
    c=SPoint(0,10);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0087():
    a=SPoint(0,0);b=SPoint(3,1)
    c=SPoint(0,11);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0088():
    a=SPoint(0,0);b=SPoint(4,1)
    c=SPoint(0,12);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0089():
    a=SPoint(0,0);b=SPoint(5,1)
    c=SPoint(0,13);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0090():
    a=SPoint(0,0);b=SPoint(6,1)
    c=SPoint(0,14);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0091():
    a=SPoint(0,0);b=SPoint(7,1)
    c=SPoint(0,2);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0092():
    a=SPoint(0,0);b=SPoint(8,1)
    c=SPoint(0,3);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0093():
    a=SPoint(0,0);b=SPoint(9,1)
    c=SPoint(0,4);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0094():
    a=SPoint(0,0);b=SPoint(10,1)
    c=SPoint(0,5);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0095():
    a=SPoint(0,0);b=SPoint(11,1)
    c=SPoint(0,6);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0096():
    a=SPoint(0,0);b=SPoint(12,1)
    c=SPoint(0,7);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0097():
    a=SPoint(0,0);b=SPoint(13,1)
    c=SPoint(0,8);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0098():
    a=SPoint(0,0);b=SPoint(14,1)
    c=SPoint(0,9);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0099():
    a=SPoint(0,0);b=SPoint(15,1)
    c=SPoint(0,10);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0100():
    a=SPoint(0,0);b=SPoint(16,1)
    c=SPoint(0,11);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0101():
    a=SPoint(0,0);b=SPoint(17,1)
    c=SPoint(0,12);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0102():
    a=SPoint(0,0);b=SPoint(1,1)
    c=SPoint(0,13);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0103():
    a=SPoint(0,0);b=SPoint(2,1)
    c=SPoint(0,14);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0104():
    a=SPoint(0,0);b=SPoint(3,1)
    c=SPoint(0,2);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0105():
    a=SPoint(0,0);b=SPoint(4,1)
    c=SPoint(0,3);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0106():
    a=SPoint(0,0);b=SPoint(5,1)
    c=SPoint(0,4);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0107():
    a=SPoint(0,0);b=SPoint(6,1)
    c=SPoint(0,5);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0108():
    a=SPoint(0,0);b=SPoint(7,1)
    c=SPoint(0,6);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0109():
    a=SPoint(0,0);b=SPoint(8,1)
    c=SPoint(0,7);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0110():
    a=SPoint(0,0);b=SPoint(9,1)
    c=SPoint(0,8);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0111():
    a=SPoint(0,0);b=SPoint(10,1)
    c=SPoint(0,9);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0112():
    a=SPoint(0,0);b=SPoint(11,1)
    c=SPoint(0,10);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0113():
    a=SPoint(0,0);b=SPoint(12,1)
    c=SPoint(0,11);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0114():
    a=SPoint(0,0);b=SPoint(13,1)
    c=SPoint(0,12);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0115():
    a=SPoint(0,0);b=SPoint(14,1)
    c=SPoint(0,13);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0116():
    a=SPoint(0,0);b=SPoint(15,1)
    c=SPoint(0,14);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0117():
    a=SPoint(0,0);b=SPoint(16,1)
    c=SPoint(0,2);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0118():
    a=SPoint(0,0);b=SPoint(17,1)
    c=SPoint(0,3);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0119():
    a=SPoint(0,0);b=SPoint(1,1)
    c=SPoint(0,4);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0120():
    a=SPoint(0,0);b=SPoint(2,1)
    c=SPoint(0,5);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0121():
    a=SPoint(0,0);b=SPoint(3,1)
    c=SPoint(0,6);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0122():
    a=SPoint(0,0);b=SPoint(4,1)
    c=SPoint(0,7);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0123():
    a=SPoint(0,0);b=SPoint(5,1)
    c=SPoint(0,8);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0124():
    a=SPoint(0,0);b=SPoint(6,1)
    c=SPoint(0,9);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0125():
    a=SPoint(0,0);b=SPoint(7,1)
    c=SPoint(0,10);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0126():
    a=SPoint(0,0);b=SPoint(8,1)
    c=SPoint(0,11);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0127():
    a=SPoint(0,0);b=SPoint(9,1)
    c=SPoint(0,12);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0128():
    a=SPoint(0,0);b=SPoint(10,1)
    c=SPoint(0,13);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0129():
    a=SPoint(0,0);b=SPoint(11,1)
    c=SPoint(0,14);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0130():
    a=SPoint(0,0);b=SPoint(12,1)
    c=SPoint(0,2);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0131():
    a=SPoint(0,0);b=SPoint(13,1)
    c=SPoint(0,3);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0132():
    a=SPoint(0,0);b=SPoint(14,1)
    c=SPoint(0,4);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0133():
    a=SPoint(0,0);b=SPoint(15,1)
    c=SPoint(0,5);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0134():
    a=SPoint(0,0);b=SPoint(16,1)
    c=SPoint(0,6);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0135():
    a=SPoint(0,0);b=SPoint(17,1)
    c=SPoint(0,7);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0136():
    a=SPoint(0,0);b=SPoint(1,1)
    c=SPoint(0,8);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0137():
    a=SPoint(0,0);b=SPoint(2,1)
    c=SPoint(0,9);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0138():
    a=SPoint(0,0);b=SPoint(3,1)
    c=SPoint(0,10);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0139():
    a=SPoint(0,0);b=SPoint(4,1)
    c=SPoint(0,11);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0140():
    a=SPoint(0,0);b=SPoint(5,1)
    c=SPoint(0,12);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0141():
    a=SPoint(0,0);b=SPoint(6,1)
    c=SPoint(0,13);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0142():
    a=SPoint(0,0);b=SPoint(7,1)
    c=SPoint(0,14);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0143():
    a=SPoint(0,0);b=SPoint(8,1)
    c=SPoint(0,2);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0144():
    a=SPoint(0,0);b=SPoint(9,1)
    c=SPoint(0,3);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0145():
    a=SPoint(0,0);b=SPoint(10,1)
    c=SPoint(0,4);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0146():
    a=SPoint(0,0);b=SPoint(11,1)
    c=SPoint(0,5);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0147():
    a=SPoint(0,0);b=SPoint(12,1)
    c=SPoint(0,6);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0148():
    a=SPoint(0,0);b=SPoint(13,1)
    c=SPoint(0,7);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0149():
    a=SPoint(0,0);b=SPoint(14,1)
    c=SPoint(0,8);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0150():
    a=SPoint(0,0);b=SPoint(15,1)
    c=SPoint(0,9);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0151():
    a=SPoint(0,0);b=SPoint(16,1)
    c=SPoint(0,10);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0152():
    a=SPoint(0,0);b=SPoint(17,1)
    c=SPoint(0,11);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0153():
    a=SPoint(0,0);b=SPoint(1,1)
    c=SPoint(0,12);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0154():
    a=SPoint(0,0);b=SPoint(2,1)
    c=SPoint(0,13);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0155():
    a=SPoint(0,0);b=SPoint(3,1)
    c=SPoint(0,14);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0156():
    a=SPoint(0,0);b=SPoint(4,1)
    c=SPoint(0,2);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0157():
    a=SPoint(0,0);b=SPoint(5,1)
    c=SPoint(0,3);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0158():
    a=SPoint(0,0);b=SPoint(6,1)
    c=SPoint(0,4);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0159():
    a=SPoint(0,0);b=SPoint(7,1)
    c=SPoint(0,5);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0160():
    a=SPoint(0,0);b=SPoint(8,1)
    c=SPoint(0,6);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0161():
    a=SPoint(0,0);b=SPoint(9,1)
    c=SPoint(0,7);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0162():
    a=SPoint(0,0);b=SPoint(10,1)
    c=SPoint(0,8);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0163():
    a=SPoint(0,0);b=SPoint(11,1)
    c=SPoint(0,9);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0164():
    a=SPoint(0,0);b=SPoint(12,1)
    c=SPoint(0,10);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0165():
    a=SPoint(0,0);b=SPoint(13,1)
    c=SPoint(0,11);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0166():
    a=SPoint(0,0);b=SPoint(14,1)
    c=SPoint(0,12);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0167():
    a=SPoint(0,0);b=SPoint(15,1)
    c=SPoint(0,13);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0168():
    a=SPoint(0,0);b=SPoint(16,1)
    c=SPoint(0,14);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0169():
    a=SPoint(0,0);b=SPoint(17,1)
    c=SPoint(0,2);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0170():
    a=SPoint(0,0);b=SPoint(1,1)
    c=SPoint(0,3);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0171():
    a=SPoint(0,0);b=SPoint(2,1)
    c=SPoint(0,4);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0172():
    a=SPoint(0,0);b=SPoint(3,1)
    c=SPoint(0,5);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0173():
    a=SPoint(0,0);b=SPoint(4,1)
    c=SPoint(0,6);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0174():
    a=SPoint(0,0);b=SPoint(5,1)
    c=SPoint(0,7);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0175():
    a=SPoint(0,0);b=SPoint(6,1)
    c=SPoint(0,8);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0176():
    a=SPoint(0,0);b=SPoint(7,1)
    c=SPoint(0,9);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0177():
    a=SPoint(0,0);b=SPoint(8,1)
    c=SPoint(0,10);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0178():
    a=SPoint(0,0);b=SPoint(9,1)
    c=SPoint(0,11);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0179():
    a=SPoint(0,0);b=SPoint(10,1)
    c=SPoint(0,12);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0180():
    a=SPoint(0,0);b=SPoint(11,1)
    c=SPoint(0,13);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0181():
    a=SPoint(0,0);b=SPoint(12,1)
    c=SPoint(0,14);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0182():
    a=SPoint(0,0);b=SPoint(13,1)
    c=SPoint(0,2);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0183():
    a=SPoint(0,0);b=SPoint(14,1)
    c=SPoint(0,3);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0184():
    a=SPoint(0,0);b=SPoint(15,1)
    c=SPoint(0,4);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0185():
    a=SPoint(0,0);b=SPoint(16,1)
    c=SPoint(0,5);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0186():
    a=SPoint(0,0);b=SPoint(17,1)
    c=SPoint(0,6);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0187():
    a=SPoint(0,0);b=SPoint(1,1)
    c=SPoint(0,7);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0188():
    a=SPoint(0,0);b=SPoint(2,1)
    c=SPoint(0,8);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0189():
    a=SPoint(0,0);b=SPoint(3,1)
    c=SPoint(0,9);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0190():
    a=SPoint(0,0);b=SPoint(4,1)
    c=SPoint(0,10);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0191():
    a=SPoint(0,0);b=SPoint(5,1)
    c=SPoint(0,11);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0192():
    a=SPoint(0,0);b=SPoint(6,1)
    c=SPoint(0,12);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0193():
    a=SPoint(0,0);b=SPoint(7,1)
    c=SPoint(0,13);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0194():
    a=SPoint(0,0);b=SPoint(8,1)
    c=SPoint(0,14);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0195():
    a=SPoint(0,0);b=SPoint(9,1)
    c=SPoint(0,2);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0196():
    a=SPoint(0,0);b=SPoint(10,1)
    c=SPoint(0,3);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0197():
    a=SPoint(0,0);b=SPoint(11,1)
    c=SPoint(0,4);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0198():
    a=SPoint(0,0);b=SPoint(12,1)
    c=SPoint(0,5);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0199():
    a=SPoint(0,0);b=SPoint(13,1)
    c=SPoint(0,6);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0200():
    a=SPoint(0,0);b=SPoint(14,1)
    c=SPoint(0,7);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0201():
    a=SPoint(0,0);b=SPoint(15,1)
    c=SPoint(0,8);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0202():
    a=SPoint(0,0);b=SPoint(16,1)
    c=SPoint(0,9);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0203():
    a=SPoint(0,0);b=SPoint(17,1)
    c=SPoint(0,10);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0204():
    a=SPoint(0,0);b=SPoint(1,1)
    c=SPoint(0,11);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0205():
    a=SPoint(0,0);b=SPoint(2,1)
    c=SPoint(0,12);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0206():
    a=SPoint(0,0);b=SPoint(3,1)
    c=SPoint(0,13);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0207():
    a=SPoint(0,0);b=SPoint(4,1)
    c=SPoint(0,14);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0208():
    a=SPoint(0,0);b=SPoint(5,1)
    c=SPoint(0,2);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0209():
    a=SPoint(0,0);b=SPoint(6,1)
    c=SPoint(0,3);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0210():
    a=SPoint(0,0);b=SPoint(7,1)
    c=SPoint(0,4);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0211():
    a=SPoint(0,0);b=SPoint(8,1)
    c=SPoint(0,5);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0212():
    a=SPoint(0,0);b=SPoint(9,1)
    c=SPoint(0,6);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0213():
    a=SPoint(0,0);b=SPoint(10,1)
    c=SPoint(0,7);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0214():
    a=SPoint(0,0);b=SPoint(11,1)
    c=SPoint(0,8);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0215():
    a=SPoint(0,0);b=SPoint(12,1)
    c=SPoint(0,9);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0216():
    a=SPoint(0,0);b=SPoint(13,1)
    c=SPoint(0,10);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0217():
    a=SPoint(0,0);b=SPoint(14,1)
    c=SPoint(0,11);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0218():
    a=SPoint(0,0);b=SPoint(15,1)
    c=SPoint(0,12);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0219():
    a=SPoint(0,0);b=SPoint(16,1)
    c=SPoint(0,13);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0220():
    a=SPoint(0,0);b=SPoint(17,1)
    c=SPoint(0,14);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0221():
    a=SPoint(0,0);b=SPoint(1,1)
    c=SPoint(0,2);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0222():
    a=SPoint(0,0);b=SPoint(2,1)
    c=SPoint(0,3);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0223():
    a=SPoint(0,0);b=SPoint(3,1)
    c=SPoint(0,4);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0224():
    a=SPoint(0,0);b=SPoint(4,1)
    c=SPoint(0,5);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0225():
    a=SPoint(0,0);b=SPoint(5,1)
    c=SPoint(0,6);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0226():
    a=SPoint(0,0);b=SPoint(6,1)
    c=SPoint(0,7);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0227():
    a=SPoint(0,0);b=SPoint(7,1)
    c=SPoint(0,8);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0228():
    a=SPoint(0,0);b=SPoint(8,1)
    c=SPoint(0,9);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0229():
    a=SPoint(0,0);b=SPoint(9,1)
    c=SPoint(0,10);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0230():
    a=SPoint(0,0);b=SPoint(10,1)
    c=SPoint(0,11);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0231():
    a=SPoint(0,0);b=SPoint(11,1)
    c=SPoint(0,12);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0232():
    a=SPoint(0,0);b=SPoint(12,1)
    c=SPoint(0,13);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0233():
    a=SPoint(0,0);b=SPoint(13,1)
    c=SPoint(0,14);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0234():
    a=SPoint(0,0);b=SPoint(14,1)
    c=SPoint(0,2);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0235():
    a=SPoint(0,0);b=SPoint(15,1)
    c=SPoint(0,3);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0236():
    a=SPoint(0,0);b=SPoint(16,1)
    c=SPoint(0,4);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0237():
    a=SPoint(0,0);b=SPoint(17,1)
    c=SPoint(0,5);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0238():
    a=SPoint(0,0);b=SPoint(1,1)
    c=SPoint(0,6);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0239():
    a=SPoint(0,0);b=SPoint(2,1)
    c=SPoint(0,7);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0240():
    a=SPoint(0,0);b=SPoint(3,1)
    c=SPoint(0,8);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0241():
    a=SPoint(0,0);b=SPoint(4,1)
    c=SPoint(0,9);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0242():
    a=SPoint(0,0);b=SPoint(5,1)
    c=SPoint(0,10);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0243():
    a=SPoint(0,0);b=SPoint(6,1)
    c=SPoint(0,11);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0244():
    a=SPoint(0,0);b=SPoint(7,1)
    c=SPoint(0,12);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0245():
    a=SPoint(0,0);b=SPoint(8,1)
    c=SPoint(0,13);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0246():
    a=SPoint(0,0);b=SPoint(9,1)
    c=SPoint(0,14);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0247():
    a=SPoint(0,0);b=SPoint(10,1)
    c=SPoint(0,2);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0248():
    a=SPoint(0,0);b=SPoint(11,1)
    c=SPoint(0,3);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0249():
    a=SPoint(0,0);b=SPoint(12,1)
    c=SPoint(0,4);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0250():
    a=SPoint(0,0);b=SPoint(13,1)
    c=SPoint(0,5);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0251():
    a=SPoint(0,0);b=SPoint(14,1)
    c=SPoint(0,6);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0252():
    a=SPoint(0,0);b=SPoint(15,1)
    c=SPoint(0,7);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0253():
    a=SPoint(0,0);b=SPoint(16,1)
    c=SPoint(0,8);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0254():
    a=SPoint(0,0);b=SPoint(17,1)
    c=SPoint(0,9);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0255():
    a=SPoint(0,0);b=SPoint(1,1)
    c=SPoint(0,10);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0256():
    a=SPoint(0,0);b=SPoint(2,1)
    c=SPoint(0,11);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0257():
    a=SPoint(0,0);b=SPoint(3,1)
    c=SPoint(0,12);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0258():
    a=SPoint(0,0);b=SPoint(4,1)
    c=SPoint(0,13);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0259():
    a=SPoint(0,0);b=SPoint(5,1)
    c=SPoint(0,14);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0260():
    a=SPoint(0,0);b=SPoint(6,1)
    c=SPoint(0,2);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0261():
    a=SPoint(0,0);b=SPoint(7,1)
    c=SPoint(0,3);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0262():
    a=SPoint(0,0);b=SPoint(8,1)
    c=SPoint(0,4);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0263():
    a=SPoint(0,0);b=SPoint(9,1)
    c=SPoint(0,5);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0264():
    a=SPoint(0,0);b=SPoint(10,1)
    c=SPoint(0,6);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0265():
    a=SPoint(0,0);b=SPoint(11,1)
    c=SPoint(0,7);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0266():
    a=SPoint(0,0);b=SPoint(12,1)
    c=SPoint(0,8);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0267():
    a=SPoint(0,0);b=SPoint(13,1)
    c=SPoint(0,9);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0268():
    a=SPoint(0,0);b=SPoint(14,1)
    c=SPoint(0,10);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0269():
    a=SPoint(0,0);b=SPoint(15,1)
    c=SPoint(0,11);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0270():
    a=SPoint(0,0);b=SPoint(16,1)
    c=SPoint(0,12);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0271():
    a=SPoint(0,0);b=SPoint(17,1)
    c=SPoint(0,13);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0272():
    a=SPoint(0,0);b=SPoint(1,1)
    c=SPoint(0,14);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0273():
    a=SPoint(0,0);b=SPoint(2,1)
    c=SPoint(0,2);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0274():
    a=SPoint(0,0);b=SPoint(3,1)
    c=SPoint(0,3);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0275():
    a=SPoint(0,0);b=SPoint(4,1)
    c=SPoint(0,4);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0276():
    a=SPoint(0,0);b=SPoint(5,1)
    c=SPoint(0,5);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0277():
    a=SPoint(0,0);b=SPoint(6,1)
    c=SPoint(0,6);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0278():
    a=SPoint(0,0);b=SPoint(7,1)
    c=SPoint(0,7);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0279():
    a=SPoint(0,0);b=SPoint(8,1)
    c=SPoint(0,8);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0280():
    a=SPoint(0,0);b=SPoint(9,1)
    c=SPoint(0,9);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0281():
    a=SPoint(0,0);b=SPoint(10,1)
    c=SPoint(0,10);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0282():
    a=SPoint(0,0);b=SPoint(11,1)
    c=SPoint(0,11);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0283():
    a=SPoint(0,0);b=SPoint(12,1)
    c=SPoint(0,12);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0284():
    a=SPoint(0,0);b=SPoint(13,1)
    c=SPoint(0,13);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0285():
    a=SPoint(0,0);b=SPoint(14,1)
    c=SPoint(0,14);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0286():
    a=SPoint(0,0);b=SPoint(15,1)
    c=SPoint(0,2);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0287():
    a=SPoint(0,0);b=SPoint(16,1)
    c=SPoint(0,3);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0288():
    a=SPoint(0,0);b=SPoint(17,1)
    c=SPoint(0,4);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0289():
    a=SPoint(0,0);b=SPoint(1,1)
    c=SPoint(0,5);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0290():
    a=SPoint(0,0);b=SPoint(2,1)
    c=SPoint(0,6);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0291():
    a=SPoint(0,0);b=SPoint(3,1)
    c=SPoint(0,7);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0292():
    a=SPoint(0,0);b=SPoint(4,1)
    c=SPoint(0,8);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0293():
    a=SPoint(0,0);b=SPoint(5,1)
    c=SPoint(0,9);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0294():
    a=SPoint(0,0);b=SPoint(6,1)
    c=SPoint(0,10);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0295():
    a=SPoint(0,0);b=SPoint(7,1)
    c=SPoint(0,11);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0296():
    a=SPoint(0,0);b=SPoint(8,1)
    c=SPoint(0,12);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0297():
    a=SPoint(0,0);b=SPoint(9,1)
    c=SPoint(0,13);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0298():
    a=SPoint(0,0);b=SPoint(10,1)
    c=SPoint(0,14);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0299():
    a=SPoint(0,0);b=SPoint(11,1)
    c=SPoint(0,2);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0300():
    a=SPoint(0,0);b=SPoint(12,1)
    c=SPoint(0,3);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0301():
    a=SPoint(0,0);b=SPoint(13,1)
    c=SPoint(0,4);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0302():
    a=SPoint(0,0);b=SPoint(14,1)
    c=SPoint(0,5);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0303():
    a=SPoint(0,0);b=SPoint(15,1)
    c=SPoint(0,6);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0304():
    a=SPoint(0,0);b=SPoint(16,1)
    c=SPoint(0,7);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0305():
    a=SPoint(0,0);b=SPoint(17,1)
    c=SPoint(0,8);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0306():
    a=SPoint(0,0);b=SPoint(1,1)
    c=SPoint(0,9);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0307():
    a=SPoint(0,0);b=SPoint(2,1)
    c=SPoint(0,10);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0308():
    a=SPoint(0,0);b=SPoint(3,1)
    c=SPoint(0,11);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0309():
    a=SPoint(0,0);b=SPoint(4,1)
    c=SPoint(0,12);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0310():
    a=SPoint(0,0);b=SPoint(5,1)
    c=SPoint(0,13);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0311():
    a=SPoint(0,0);b=SPoint(6,1)
    c=SPoint(0,14);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0312():
    a=SPoint(0,0);b=SPoint(7,1)
    c=SPoint(0,2);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0313():
    a=SPoint(0,0);b=SPoint(8,1)
    c=SPoint(0,3);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0314():
    a=SPoint(0,0);b=SPoint(9,1)
    c=SPoint(0,4);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0315():
    a=SPoint(0,0);b=SPoint(10,1)
    c=SPoint(0,5);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0316():
    a=SPoint(0,0);b=SPoint(11,1)
    c=SPoint(0,6);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0317():
    a=SPoint(0,0);b=SPoint(12,1)
    c=SPoint(0,7);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0318():
    a=SPoint(0,0);b=SPoint(13,1)
    c=SPoint(0,8);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0319():
    a=SPoint(0,0);b=SPoint(14,1)
    c=SPoint(0,9);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0320():
    a=SPoint(0,0);b=SPoint(15,1)
    c=SPoint(0,10);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0321():
    a=SPoint(0,0);b=SPoint(16,1)
    c=SPoint(0,11);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0322():
    a=SPoint(0,0);b=SPoint(17,1)
    c=SPoint(0,12);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0323():
    a=SPoint(0,0);b=SPoint(1,1)
    c=SPoint(0,13);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0324():
    a=SPoint(0,0);b=SPoint(2,1)
    c=SPoint(0,14);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0325():
    a=SPoint(0,0);b=SPoint(3,1)
    c=SPoint(0,2);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0326():
    a=SPoint(0,0);b=SPoint(4,1)
    c=SPoint(0,3);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0327():
    a=SPoint(0,0);b=SPoint(5,1)
    c=SPoint(0,4);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0328():
    a=SPoint(0,0);b=SPoint(6,1)
    c=SPoint(0,5);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0329():
    a=SPoint(0,0);b=SPoint(7,1)
    c=SPoint(0,6);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0330():
    a=SPoint(0,0);b=SPoint(8,1)
    c=SPoint(0,7);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0331():
    a=SPoint(0,0);b=SPoint(9,1)
    c=SPoint(0,8);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0332():
    a=SPoint(0,0);b=SPoint(10,1)
    c=SPoint(0,9);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0333():
    a=SPoint(0,0);b=SPoint(11,1)
    c=SPoint(0,10);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0334():
    a=SPoint(0,0);b=SPoint(12,1)
    c=SPoint(0,11);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0335():
    a=SPoint(0,0);b=SPoint(13,1)
    c=SPoint(0,12);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0336():
    a=SPoint(0,0);b=SPoint(14,1)
    c=SPoint(0,13);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0337():
    a=SPoint(0,0);b=SPoint(15,1)
    c=SPoint(0,14);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0338():
    a=SPoint(0,0);b=SPoint(16,1)
    c=SPoint(0,2);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0339():
    a=SPoint(0,0);b=SPoint(17,1)
    c=SPoint(0,3);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0340():
    a=SPoint(0,0);b=SPoint(1,1)
    c=SPoint(0,4);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0341():
    a=SPoint(0,0);b=SPoint(2,1)
    c=SPoint(0,5);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0342():
    a=SPoint(0,0);b=SPoint(3,1)
    c=SPoint(0,6);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0343():
    a=SPoint(0,0);b=SPoint(4,1)
    c=SPoint(0,7);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0344():
    a=SPoint(0,0);b=SPoint(5,1)
    c=SPoint(0,8);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0345():
    a=SPoint(0,0);b=SPoint(6,1)
    c=SPoint(0,9);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0346():
    a=SPoint(0,0);b=SPoint(7,1)
    c=SPoint(0,10);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0347():
    a=SPoint(0,0);b=SPoint(8,1)
    c=SPoint(0,11);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0348():
    a=SPoint(0,0);b=SPoint(9,1)
    c=SPoint(0,12);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0349():
    a=SPoint(0,0);b=SPoint(10,1)
    c=SPoint(0,13);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0350():
    a=SPoint(0,0);b=SPoint(11,1)
    c=SPoint(0,14);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0351():
    a=SPoint(0,0);b=SPoint(12,1)
    c=SPoint(0,2);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0352():
    a=SPoint(0,0);b=SPoint(13,1)
    c=SPoint(0,3);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0353():
    a=SPoint(0,0);b=SPoint(14,1)
    c=SPoint(0,4);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0354():
    a=SPoint(0,0);b=SPoint(15,1)
    c=SPoint(0,5);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0355():
    a=SPoint(0,0);b=SPoint(16,1)
    c=SPoint(0,6);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0356():
    a=SPoint(0,0);b=SPoint(17,1)
    c=SPoint(0,7);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0357():
    a=SPoint(0,0);b=SPoint(1,1)
    c=SPoint(0,8);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0358():
    a=SPoint(0,0);b=SPoint(2,1)
    c=SPoint(0,9);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0359():
    a=SPoint(0,0);b=SPoint(3,1)
    c=SPoint(0,10);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0360():
    a=SPoint(0,0);b=SPoint(4,1)
    c=SPoint(0,11);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0361():
    a=SPoint(0,0);b=SPoint(5,1)
    c=SPoint(0,12);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0362():
    a=SPoint(0,0);b=SPoint(6,1)
    c=SPoint(0,13);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0363():
    a=SPoint(0,0);b=SPoint(7,1)
    c=SPoint(0,14);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0364():
    a=SPoint(0,0);b=SPoint(8,1)
    c=SPoint(0,2);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0365():
    a=SPoint(0,0);b=SPoint(9,1)
    c=SPoint(0,3);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0366():
    a=SPoint(0,0);b=SPoint(10,1)
    c=SPoint(0,4);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0367():
    a=SPoint(0,0);b=SPoint(11,1)
    c=SPoint(0,5);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0368():
    a=SPoint(0,0);b=SPoint(12,1)
    c=SPoint(0,6);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0369():
    a=SPoint(0,0);b=SPoint(13,1)
    c=SPoint(0,7);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0370():
    a=SPoint(0,0);b=SPoint(14,1)
    c=SPoint(0,8);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0371():
    a=SPoint(0,0);b=SPoint(15,1)
    c=SPoint(0,9);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0372():
    a=SPoint(0,0);b=SPoint(16,1)
    c=SPoint(0,10);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0373():
    a=SPoint(0,0);b=SPoint(17,1)
    c=SPoint(0,11);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0374():
    a=SPoint(0,0);b=SPoint(1,1)
    c=SPoint(0,12);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0375():
    a=SPoint(0,0);b=SPoint(2,1)
    c=SPoint(0,13);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0376():
    a=SPoint(0,0);b=SPoint(3,1)
    c=SPoint(0,14);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0377():
    a=SPoint(0,0);b=SPoint(4,1)
    c=SPoint(0,2);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0378():
    a=SPoint(0,0);b=SPoint(5,1)
    c=SPoint(0,3);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0379():
    a=SPoint(0,0);b=SPoint(6,1)
    c=SPoint(0,4);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0380():
    a=SPoint(0,0);b=SPoint(7,1)
    c=SPoint(0,5);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0381():
    a=SPoint(0,0);b=SPoint(8,1)
    c=SPoint(0,6);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0382():
    a=SPoint(0,0);b=SPoint(9,1)
    c=SPoint(0,7);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0383():
    a=SPoint(0,0);b=SPoint(10,1)
    c=SPoint(0,8);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0384():
    a=SPoint(0,0);b=SPoint(11,1)
    c=SPoint(0,9);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0385():
    a=SPoint(0,0);b=SPoint(12,1)
    c=SPoint(0,10);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0386():
    a=SPoint(0,0);b=SPoint(13,1)
    c=SPoint(0,11);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0387():
    a=SPoint(0,0);b=SPoint(14,1)
    c=SPoint(0,12);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0388():
    a=SPoint(0,0);b=SPoint(15,1)
    c=SPoint(0,13);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0389():
    a=SPoint(0,0);b=SPoint(16,1)
    c=SPoint(0,14);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0390():
    a=SPoint(0,0);b=SPoint(17,1)
    c=SPoint(0,2);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0391():
    a=SPoint(0,0);b=SPoint(1,1)
    c=SPoint(0,3);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0392():
    a=SPoint(0,0);b=SPoint(2,1)
    c=SPoint(0,4);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0393():
    a=SPoint(0,0);b=SPoint(3,1)
    c=SPoint(0,5);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0394():
    a=SPoint(0,0);b=SPoint(4,1)
    c=SPoint(0,6);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0395():
    a=SPoint(0,0);b=SPoint(5,1)
    c=SPoint(0,7);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0396():
    a=SPoint(0,0);b=SPoint(6,1)
    c=SPoint(0,8);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0397():
    a=SPoint(0,0);b=SPoint(7,1)
    c=SPoint(0,9);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0398():
    a=SPoint(0,0);b=SPoint(8,1)
    c=SPoint(0,10);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0399():
    a=SPoint(0,0);b=SPoint(9,1)
    c=SPoint(0,11);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0400():
    a=SPoint(0,0);b=SPoint(10,1)
    c=SPoint(0,12);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0401():
    a=SPoint(0,0);b=SPoint(11,1)
    c=SPoint(0,13);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0402():
    a=SPoint(0,0);b=SPoint(12,1)
    c=SPoint(0,14);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0403():
    a=SPoint(0,0);b=SPoint(13,1)
    c=SPoint(0,2);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0404():
    a=SPoint(0,0);b=SPoint(14,1)
    c=SPoint(0,3);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0405():
    a=SPoint(0,0);b=SPoint(15,1)
    c=SPoint(0,4);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0406():
    a=SPoint(0,0);b=SPoint(16,1)
    c=SPoint(0,5);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0407():
    a=SPoint(0,0);b=SPoint(17,1)
    c=SPoint(0,6);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0408():
    a=SPoint(0,0);b=SPoint(1,1)
    c=SPoint(0,7);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0409():
    a=SPoint(0,0);b=SPoint(2,1)
    c=SPoint(0,8);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0410():
    a=SPoint(0,0);b=SPoint(3,1)
    c=SPoint(0,9);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0411():
    a=SPoint(0,0);b=SPoint(4,1)
    c=SPoint(0,10);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0412():
    a=SPoint(0,0);b=SPoint(5,1)
    c=SPoint(0,11);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0413():
    a=SPoint(0,0);b=SPoint(6,1)
    c=SPoint(0,12);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0414():
    a=SPoint(0,0);b=SPoint(7,1)
    c=SPoint(0,13);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0415():
    a=SPoint(0,0);b=SPoint(8,1)
    c=SPoint(0,14);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0416():
    a=SPoint(0,0);b=SPoint(9,1)
    c=SPoint(0,2);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0417():
    a=SPoint(0,0);b=SPoint(10,1)
    c=SPoint(0,3);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0418():
    a=SPoint(0,0);b=SPoint(11,1)
    c=SPoint(0,4);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0419():
    a=SPoint(0,0);b=SPoint(12,1)
    c=SPoint(0,5);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0420():
    a=SPoint(0,0);b=SPoint(13,1)
    c=SPoint(0,6);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0421():
    a=SPoint(0,0);b=SPoint(14,1)
    c=SPoint(0,7);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0422():
    a=SPoint(0,0);b=SPoint(15,1)
    c=SPoint(0,8);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0423():
    a=SPoint(0,0);b=SPoint(16,1)
    c=SPoint(0,9);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0424():
    a=SPoint(0,0);b=SPoint(17,1)
    c=SPoint(0,10);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0425():
    a=SPoint(0,0);b=SPoint(1,1)
    c=SPoint(0,11);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0426():
    a=SPoint(0,0);b=SPoint(2,1)
    c=SPoint(0,12);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0427():
    a=SPoint(0,0);b=SPoint(3,1)
    c=SPoint(0,13);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0428():
    a=SPoint(0,0);b=SPoint(4,1)
    c=SPoint(0,14);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0429():
    a=SPoint(0,0);b=SPoint(5,1)
    c=SPoint(0,2);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0430():
    a=SPoint(0,0);b=SPoint(6,1)
    c=SPoint(0,3);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0431():
    a=SPoint(0,0);b=SPoint(7,1)
    c=SPoint(0,4);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0432():
    a=SPoint(0,0);b=SPoint(8,1)
    c=SPoint(0,5);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0433():
    a=SPoint(0,0);b=SPoint(9,1)
    c=SPoint(0,6);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0434():
    a=SPoint(0,0);b=SPoint(10,1)
    c=SPoint(0,7);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0435():
    a=SPoint(0,0);b=SPoint(11,1)
    c=SPoint(0,8);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0436():
    a=SPoint(0,0);b=SPoint(12,1)
    c=SPoint(0,9);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0437():
    a=SPoint(0,0);b=SPoint(13,1)
    c=SPoint(0,10);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0438():
    a=SPoint(0,0);b=SPoint(14,1)
    c=SPoint(0,11);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0439():
    a=SPoint(0,0);b=SPoint(15,1)
    c=SPoint(0,12);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0440():
    a=SPoint(0,0);b=SPoint(16,1)
    c=SPoint(0,13);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0441():
    a=SPoint(0,0);b=SPoint(17,1)
    c=SPoint(0,14);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0442():
    a=SPoint(0,0);b=SPoint(1,1)
    c=SPoint(0,2);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0443():
    a=SPoint(0,0);b=SPoint(2,1)
    c=SPoint(0,3);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0444():
    a=SPoint(0,0);b=SPoint(3,1)
    c=SPoint(0,4);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0445():
    a=SPoint(0,0);b=SPoint(4,1)
    c=SPoint(0,5);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0446():
    a=SPoint(0,0);b=SPoint(5,1)
    c=SPoint(0,6);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0447():
    a=SPoint(0,0);b=SPoint(6,1)
    c=SPoint(0,7);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0448():
    a=SPoint(0,0);b=SPoint(7,1)
    c=SPoint(0,8);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0449():
    a=SPoint(0,0);b=SPoint(8,1)
    c=SPoint(0,9);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0450():
    a=SPoint(0,0);b=SPoint(9,1)
    c=SPoint(0,10);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0451():
    a=SPoint(0,0);b=SPoint(10,1)
    c=SPoint(0,11);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0452():
    a=SPoint(0,0);b=SPoint(11,1)
    c=SPoint(0,12);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0453():
    a=SPoint(0,0);b=SPoint(12,1)
    c=SPoint(0,13);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0454():
    a=SPoint(0,0);b=SPoint(13,1)
    c=SPoint(0,14);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0455():
    a=SPoint(0,0);b=SPoint(14,1)
    c=SPoint(0,2);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0456():
    a=SPoint(0,0);b=SPoint(15,1)
    c=SPoint(0,3);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0457():
    a=SPoint(0,0);b=SPoint(16,1)
    c=SPoint(0,4);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0458():
    a=SPoint(0,0);b=SPoint(17,1)
    c=SPoint(0,5);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0459():
    a=SPoint(0,0);b=SPoint(1,1)
    c=SPoint(0,6);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0460():
    a=SPoint(0,0);b=SPoint(2,1)
    c=SPoint(0,7);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0461():
    a=SPoint(0,0);b=SPoint(3,1)
    c=SPoint(0,8);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0462():
    a=SPoint(0,0);b=SPoint(4,1)
    c=SPoint(0,9);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0463():
    a=SPoint(0,0);b=SPoint(5,1)
    c=SPoint(0,10);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0464():
    a=SPoint(0,0);b=SPoint(6,1)
    c=SPoint(0,11);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0465():
    a=SPoint(0,0);b=SPoint(7,1)
    c=SPoint(0,12);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0466():
    a=SPoint(0,0);b=SPoint(8,1)
    c=SPoint(0,13);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0467():
    a=SPoint(0,0);b=SPoint(9,1)
    c=SPoint(0,14);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0468():
    a=SPoint(0,0);b=SPoint(10,1)
    c=SPoint(0,2);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0469():
    a=SPoint(0,0);b=SPoint(11,1)
    c=SPoint(0,3);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0470():
    a=SPoint(0,0);b=SPoint(12,1)
    c=SPoint(0,4);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0471():
    a=SPoint(0,0);b=SPoint(13,1)
    c=SPoint(0,5);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0472():
    a=SPoint(0,0);b=SPoint(14,1)
    c=SPoint(0,6);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0473():
    a=SPoint(0,0);b=SPoint(15,1)
    c=SPoint(0,7);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0474():
    a=SPoint(0,0);b=SPoint(16,1)
    c=SPoint(0,8);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0475():
    a=SPoint(0,0);b=SPoint(17,1)
    c=SPoint(0,9);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0476():
    a=SPoint(0,0);b=SPoint(1,1)
    c=SPoint(0,10);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0477():
    a=SPoint(0,0);b=SPoint(2,1)
    c=SPoint(0,11);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0478():
    a=SPoint(0,0);b=SPoint(3,1)
    c=SPoint(0,12);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0479():
    a=SPoint(0,0);b=SPoint(4,1)
    c=SPoint(0,13);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0480():
    a=SPoint(0,0);b=SPoint(5,1)
    c=SPoint(0,14);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0481():
    a=SPoint(0,0);b=SPoint(6,1)
    c=SPoint(0,2);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0482():
    a=SPoint(0,0);b=SPoint(7,1)
    c=SPoint(0,3);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0483():
    a=SPoint(0,0);b=SPoint(8,1)
    c=SPoint(0,4);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0484():
    a=SPoint(0,0);b=SPoint(9,1)
    c=SPoint(0,5);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0485():
    a=SPoint(0,0);b=SPoint(10,1)
    c=SPoint(0,6);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0486():
    a=SPoint(0,0);b=SPoint(11,1)
    c=SPoint(0,7);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0487():
    a=SPoint(0,0);b=SPoint(12,1)
    c=SPoint(0,8);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0488():
    a=SPoint(0,0);b=SPoint(13,1)
    c=SPoint(0,9);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0489():
    a=SPoint(0,0);b=SPoint(14,1)
    c=SPoint(0,10);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0490():
    a=SPoint(0,0);b=SPoint(15,1)
    c=SPoint(0,11);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0491():
    a=SPoint(0,0);b=SPoint(16,1)
    c=SPoint(0,12);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0492():
    a=SPoint(0,0);b=SPoint(17,1)
    c=SPoint(0,13);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0493():
    a=SPoint(0,0);b=SPoint(1,1)
    c=SPoint(0,14);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0494():
    a=SPoint(0,0);b=SPoint(2,1)
    c=SPoint(0,2);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0495():
    a=SPoint(0,0);b=SPoint(3,1)
    c=SPoint(0,3);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0496():
    a=SPoint(0,0);b=SPoint(4,1)
    c=SPoint(0,4);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0497():
    a=SPoint(0,0);b=SPoint(5,1)
    c=SPoint(0,5);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0498():
    a=SPoint(0,0);b=SPoint(6,1)
    c=SPoint(0,6);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0499():
    a=SPoint(0,0);b=SPoint(7,1)
    c=SPoint(0,7);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0500():
    a=SPoint(0,0);b=SPoint(8,1)
    c=SPoint(0,8);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0501():
    a=SPoint(0,0);b=SPoint(9,1)
    c=SPoint(0,9);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0502():
    a=SPoint(0,0);b=SPoint(10,1)
    c=SPoint(0,10);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0503():
    a=SPoint(0,0);b=SPoint(11,1)
    c=SPoint(0,11);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0504():
    a=SPoint(0,0);b=SPoint(12,1)
    c=SPoint(0,12);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0505():
    a=SPoint(0,0);b=SPoint(13,1)
    c=SPoint(0,13);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0506():
    a=SPoint(0,0);b=SPoint(14,1)
    c=SPoint(0,14);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0507():
    a=SPoint(0,0);b=SPoint(15,1)
    c=SPoint(0,2);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0508():
    a=SPoint(0,0);b=SPoint(16,1)
    c=SPoint(0,3);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0509():
    a=SPoint(0,0);b=SPoint(17,1)
    c=SPoint(0,4);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0510():
    a=SPoint(0,0);b=SPoint(1,1)
    c=SPoint(0,5);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0511():
    a=SPoint(0,0);b=SPoint(2,1)
    c=SPoint(0,6);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0512():
    a=SPoint(0,0);b=SPoint(3,1)
    c=SPoint(0,7);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0513():
    a=SPoint(0,0);b=SPoint(4,1)
    c=SPoint(0,8);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0514():
    a=SPoint(0,0);b=SPoint(5,1)
    c=SPoint(0,9);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0515():
    a=SPoint(0,0);b=SPoint(6,1)
    c=SPoint(0,10);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0516():
    a=SPoint(0,0);b=SPoint(7,1)
    c=SPoint(0,11);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0517():
    a=SPoint(0,0);b=SPoint(8,1)
    c=SPoint(0,12);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0518():
    a=SPoint(0,0);b=SPoint(9,1)
    c=SPoint(0,13);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0519():
    a=SPoint(0,0);b=SPoint(10,1)
    c=SPoint(0,14);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0520():
    a=SPoint(0,0);b=SPoint(11,1)
    c=SPoint(0,2);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0521():
    a=SPoint(0,0);b=SPoint(12,1)
    c=SPoint(0,3);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0522():
    a=SPoint(0,0);b=SPoint(13,1)
    c=SPoint(0,4);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0523():
    a=SPoint(0,0);b=SPoint(14,1)
    c=SPoint(0,5);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0524():
    a=SPoint(0,0);b=SPoint(15,1)
    c=SPoint(0,6);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0525():
    a=SPoint(0,0);b=SPoint(16,1)
    c=SPoint(0,7);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0526():
    a=SPoint(0,0);b=SPoint(17,1)
    c=SPoint(0,8);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0527():
    a=SPoint(0,0);b=SPoint(1,1)
    c=SPoint(0,9);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0528():
    a=SPoint(0,0);b=SPoint(2,1)
    c=SPoint(0,10);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0529():
    a=SPoint(0,0);b=SPoint(3,1)
    c=SPoint(0,11);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0530():
    a=SPoint(0,0);b=SPoint(4,1)
    c=SPoint(0,12);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0531():
    a=SPoint(0,0);b=SPoint(5,1)
    c=SPoint(0,13);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0532():
    a=SPoint(0,0);b=SPoint(6,1)
    c=SPoint(0,14);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0533():
    a=SPoint(0,0);b=SPoint(7,1)
    c=SPoint(0,2);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0534():
    a=SPoint(0,0);b=SPoint(8,1)
    c=SPoint(0,3);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0535():
    a=SPoint(0,0);b=SPoint(9,1)
    c=SPoint(0,4);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0536():
    a=SPoint(0,0);b=SPoint(10,1)
    c=SPoint(0,5);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0537():
    a=SPoint(0,0);b=SPoint(11,1)
    c=SPoint(0,6);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0538():
    a=SPoint(0,0);b=SPoint(12,1)
    c=SPoint(0,7);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0539():
    a=SPoint(0,0);b=SPoint(13,1)
    c=SPoint(0,8);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0540():
    a=SPoint(0,0);b=SPoint(14,1)
    c=SPoint(0,9);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0541():
    a=SPoint(0,0);b=SPoint(15,1)
    c=SPoint(0,10);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0542():
    a=SPoint(0,0);b=SPoint(16,1)
    c=SPoint(0,11);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0543():
    a=SPoint(0,0);b=SPoint(17,1)
    c=SPoint(0,12);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0544():
    a=SPoint(0,0);b=SPoint(1,1)
    c=SPoint(0,13);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0545():
    a=SPoint(0,0);b=SPoint(2,1)
    c=SPoint(0,14);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0546():
    a=SPoint(0,0);b=SPoint(3,1)
    c=SPoint(0,2);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0547():
    a=SPoint(0,0);b=SPoint(4,1)
    c=SPoint(0,3);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0548():
    a=SPoint(0,0);b=SPoint(5,1)
    c=SPoint(0,4);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0549():
    a=SPoint(0,0);b=SPoint(6,1)
    c=SPoint(0,5);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0550():
    a=SPoint(0,0);b=SPoint(7,1)
    c=SPoint(0,6);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0551():
    a=SPoint(0,0);b=SPoint(8,1)
    c=SPoint(0,7);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0552():
    a=SPoint(0,0);b=SPoint(9,1)
    c=SPoint(0,8);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0553():
    a=SPoint(0,0);b=SPoint(10,1)
    c=SPoint(0,9);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0554():
    a=SPoint(0,0);b=SPoint(11,1)
    c=SPoint(0,10);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0555():
    a=SPoint(0,0);b=SPoint(12,1)
    c=SPoint(0,11);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0556():
    a=SPoint(0,0);b=SPoint(13,1)
    c=SPoint(0,12);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0557():
    a=SPoint(0,0);b=SPoint(14,1)
    c=SPoint(0,13);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0558():
    a=SPoint(0,0);b=SPoint(15,1)
    c=SPoint(0,14);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0559():
    a=SPoint(0,0);b=SPoint(16,1)
    c=SPoint(0,2);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0560():
    a=SPoint(0,0);b=SPoint(17,1)
    c=SPoint(0,3);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0561():
    a=SPoint(0,0);b=SPoint(1,1)
    c=SPoint(0,4);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0562():
    a=SPoint(0,0);b=SPoint(2,1)
    c=SPoint(0,5);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0563():
    a=SPoint(0,0);b=SPoint(3,1)
    c=SPoint(0,6);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0564():
    a=SPoint(0,0);b=SPoint(4,1)
    c=SPoint(0,7);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0565():
    a=SPoint(0,0);b=SPoint(5,1)
    c=SPoint(0,8);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0566():
    a=SPoint(0,0);b=SPoint(6,1)
    c=SPoint(0,9);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0567():
    a=SPoint(0,0);b=SPoint(7,1)
    c=SPoint(0,10);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0568():
    a=SPoint(0,0);b=SPoint(8,1)
    c=SPoint(0,11);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0569():
    a=SPoint(0,0);b=SPoint(9,1)
    c=SPoint(0,12);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0570():
    a=SPoint(0,0);b=SPoint(10,1)
    c=SPoint(0,13);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0571():
    a=SPoint(0,0);b=SPoint(11,1)
    c=SPoint(0,14);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0572():
    a=SPoint(0,0);b=SPoint(12,1)
    c=SPoint(0,2);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0573():
    a=SPoint(0,0);b=SPoint(13,1)
    c=SPoint(0,3);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0574():
    a=SPoint(0,0);b=SPoint(14,1)
    c=SPoint(0,4);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0575():
    a=SPoint(0,0);b=SPoint(15,1)
    c=SPoint(0,5);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0576():
    a=SPoint(0,0);b=SPoint(16,1)
    c=SPoint(0,6);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0577():
    a=SPoint(0,0);b=SPoint(17,1)
    c=SPoint(0,7);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0578():
    a=SPoint(0,0);b=SPoint(1,1)
    c=SPoint(0,8);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0579():
    a=SPoint(0,0);b=SPoint(2,1)
    c=SPoint(0,9);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0580():
    a=SPoint(0,0);b=SPoint(3,1)
    c=SPoint(0,10);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0581():
    a=SPoint(0,0);b=SPoint(4,1)
    c=SPoint(0,11);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0582():
    a=SPoint(0,0);b=SPoint(5,1)
    c=SPoint(0,12);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0583():
    a=SPoint(0,0);b=SPoint(6,1)
    c=SPoint(0,13);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0584():
    a=SPoint(0,0);b=SPoint(7,1)
    c=SPoint(0,14);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0585():
    a=SPoint(0,0);b=SPoint(8,1)
    c=SPoint(0,2);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0586():
    a=SPoint(0,0);b=SPoint(9,1)
    c=SPoint(0,3);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0587():
    a=SPoint(0,0);b=SPoint(10,1)
    c=SPoint(0,4);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0588():
    a=SPoint(0,0);b=SPoint(11,1)
    c=SPoint(0,5);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0589():
    a=SPoint(0,0);b=SPoint(12,1)
    c=SPoint(0,6);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0590():
    a=SPoint(0,0);b=SPoint(13,1)
    c=SPoint(0,7);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0591():
    a=SPoint(0,0);b=SPoint(14,1)
    c=SPoint(0,8);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0592():
    a=SPoint(0,0);b=SPoint(15,1)
    c=SPoint(0,9);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0593():
    a=SPoint(0,0);b=SPoint(16,1)
    c=SPoint(0,10);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0594():
    a=SPoint(0,0);b=SPoint(17,1)
    c=SPoint(0,11);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0595():
    a=SPoint(0,0);b=SPoint(1,1)
    c=SPoint(0,12);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0596():
    a=SPoint(0,0);b=SPoint(2,1)
    c=SPoint(0,13);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0597():
    a=SPoint(0,0);b=SPoint(3,1)
    c=SPoint(0,14);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0598():
    a=SPoint(0,0);b=SPoint(4,1)
    c=SPoint(0,2);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

def test_line_intersection_0599():
    a=SPoint(0,0);b=SPoint(5,1)
    c=SPoint(0,3);d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True

