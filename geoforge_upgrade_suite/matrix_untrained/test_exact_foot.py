# GENERATED, DETERMINISTIC, NO TRAINED MODEL USED.
# Source generator: geoforge_upgrade_suite/generate_untrained_matrix.py
from fractions import Fraction as Q
from geoforge_upgrade_suite.geometry_exact import Vec2,Polynomial,Line
from geoforge_upgrade_suite.exact_constructions import SPoint,foot,line_intersection
from geoforge_upgrade_suite.deterministic_ideal import ExactIdealEngine,certificate_to_json,verify_certificate_json
from geoforge_upgrade_suite.deterministic_solver import ExactFactEvaluator,GuardLedger

def test_exact_foot_0000():
    a=SPoint(1,2);b=SPoint(0,0);c=SPoint(1,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0001():
    a=SPoint(2,3);b=SPoint(0,0);c=SPoint(2,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0002():
    a=SPoint(3,4);b=SPoint(0,0);c=SPoint(3,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0003():
    a=SPoint(4,5);b=SPoint(0,0);c=SPoint(4,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0004():
    a=SPoint(5,6);b=SPoint(0,0);c=SPoint(5,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0005():
    a=SPoint(6,7);b=SPoint(0,0);c=SPoint(6,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0006():
    a=SPoint(7,8);b=SPoint(0,0);c=SPoint(7,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0007():
    a=SPoint(8,9);b=SPoint(0,0);c=SPoint(8,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0008():
    a=SPoint(9,10);b=SPoint(0,0);c=SPoint(9,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0009():
    a=SPoint(10,11);b=SPoint(0,0);c=SPoint(10,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0010():
    a=SPoint(11,12);b=SPoint(0,0);c=SPoint(11,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0011():
    a=SPoint(12,13);b=SPoint(0,0);c=SPoint(12,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0012():
    a=SPoint(13,14);b=SPoint(0,0);c=SPoint(13,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0013():
    a=SPoint(14,2);b=SPoint(0,0);c=SPoint(14,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0014():
    a=SPoint(15,3);b=SPoint(0,0);c=SPoint(15,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0015():
    a=SPoint(16,4);b=SPoint(0,0);c=SPoint(16,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0016():
    a=SPoint(17,5);b=SPoint(0,0);c=SPoint(17,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0017():
    a=SPoint(1,6);b=SPoint(0,0);c=SPoint(18,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0018():
    a=SPoint(2,7);b=SPoint(0,0);c=SPoint(19,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0019():
    a=SPoint(3,8);b=SPoint(0,0);c=SPoint(20,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0020():
    a=SPoint(4,9);b=SPoint(0,0);c=SPoint(21,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0021():
    a=SPoint(5,10);b=SPoint(0,0);c=SPoint(22,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0022():
    a=SPoint(6,11);b=SPoint(0,0);c=SPoint(23,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0023():
    a=SPoint(7,12);b=SPoint(0,0);c=SPoint(1,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0024():
    a=SPoint(8,13);b=SPoint(0,0);c=SPoint(2,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0025():
    a=SPoint(9,14);b=SPoint(0,0);c=SPoint(3,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0026():
    a=SPoint(10,2);b=SPoint(0,0);c=SPoint(4,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0027():
    a=SPoint(11,3);b=SPoint(0,0);c=SPoint(5,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0028():
    a=SPoint(12,4);b=SPoint(0,0);c=SPoint(6,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0029():
    a=SPoint(13,5);b=SPoint(0,0);c=SPoint(7,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0030():
    a=SPoint(14,6);b=SPoint(0,0);c=SPoint(8,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0031():
    a=SPoint(15,7);b=SPoint(0,0);c=SPoint(9,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0032():
    a=SPoint(16,8);b=SPoint(0,0);c=SPoint(10,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0033():
    a=SPoint(17,9);b=SPoint(0,0);c=SPoint(11,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0034():
    a=SPoint(1,10);b=SPoint(0,0);c=SPoint(12,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0035():
    a=SPoint(2,11);b=SPoint(0,0);c=SPoint(13,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0036():
    a=SPoint(3,12);b=SPoint(0,0);c=SPoint(14,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0037():
    a=SPoint(4,13);b=SPoint(0,0);c=SPoint(15,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0038():
    a=SPoint(5,14);b=SPoint(0,0);c=SPoint(16,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0039():
    a=SPoint(6,2);b=SPoint(0,0);c=SPoint(17,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0040():
    a=SPoint(7,3);b=SPoint(0,0);c=SPoint(18,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0041():
    a=SPoint(8,4);b=SPoint(0,0);c=SPoint(19,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0042():
    a=SPoint(9,5);b=SPoint(0,0);c=SPoint(20,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0043():
    a=SPoint(10,6);b=SPoint(0,0);c=SPoint(21,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0044():
    a=SPoint(11,7);b=SPoint(0,0);c=SPoint(22,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0045():
    a=SPoint(12,8);b=SPoint(0,0);c=SPoint(23,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0046():
    a=SPoint(13,9);b=SPoint(0,0);c=SPoint(1,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0047():
    a=SPoint(14,10);b=SPoint(0,0);c=SPoint(2,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0048():
    a=SPoint(15,11);b=SPoint(0,0);c=SPoint(3,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0049():
    a=SPoint(16,12);b=SPoint(0,0);c=SPoint(4,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0050():
    a=SPoint(17,13);b=SPoint(0,0);c=SPoint(5,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0051():
    a=SPoint(1,14);b=SPoint(0,0);c=SPoint(6,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0052():
    a=SPoint(2,2);b=SPoint(0,0);c=SPoint(7,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0053():
    a=SPoint(3,3);b=SPoint(0,0);c=SPoint(8,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0054():
    a=SPoint(4,4);b=SPoint(0,0);c=SPoint(9,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0055():
    a=SPoint(5,5);b=SPoint(0,0);c=SPoint(10,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0056():
    a=SPoint(6,6);b=SPoint(0,0);c=SPoint(11,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0057():
    a=SPoint(7,7);b=SPoint(0,0);c=SPoint(12,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0058():
    a=SPoint(8,8);b=SPoint(0,0);c=SPoint(13,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0059():
    a=SPoint(9,9);b=SPoint(0,0);c=SPoint(14,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0060():
    a=SPoint(10,10);b=SPoint(0,0);c=SPoint(15,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0061():
    a=SPoint(11,11);b=SPoint(0,0);c=SPoint(16,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0062():
    a=SPoint(12,12);b=SPoint(0,0);c=SPoint(17,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0063():
    a=SPoint(13,13);b=SPoint(0,0);c=SPoint(18,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0064():
    a=SPoint(14,14);b=SPoint(0,0);c=SPoint(19,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0065():
    a=SPoint(15,2);b=SPoint(0,0);c=SPoint(20,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0066():
    a=SPoint(16,3);b=SPoint(0,0);c=SPoint(21,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0067():
    a=SPoint(17,4);b=SPoint(0,0);c=SPoint(22,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0068():
    a=SPoint(1,5);b=SPoint(0,0);c=SPoint(23,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0069():
    a=SPoint(2,6);b=SPoint(0,0);c=SPoint(1,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0070():
    a=SPoint(3,7);b=SPoint(0,0);c=SPoint(2,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0071():
    a=SPoint(4,8);b=SPoint(0,0);c=SPoint(3,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0072():
    a=SPoint(5,9);b=SPoint(0,0);c=SPoint(4,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0073():
    a=SPoint(6,10);b=SPoint(0,0);c=SPoint(5,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0074():
    a=SPoint(7,11);b=SPoint(0,0);c=SPoint(6,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0075():
    a=SPoint(8,12);b=SPoint(0,0);c=SPoint(7,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0076():
    a=SPoint(9,13);b=SPoint(0,0);c=SPoint(8,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0077():
    a=SPoint(10,14);b=SPoint(0,0);c=SPoint(9,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0078():
    a=SPoint(11,2);b=SPoint(0,0);c=SPoint(10,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0079():
    a=SPoint(12,3);b=SPoint(0,0);c=SPoint(11,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0080():
    a=SPoint(13,4);b=SPoint(0,0);c=SPoint(12,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0081():
    a=SPoint(14,5);b=SPoint(0,0);c=SPoint(13,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0082():
    a=SPoint(15,6);b=SPoint(0,0);c=SPoint(14,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0083():
    a=SPoint(16,7);b=SPoint(0,0);c=SPoint(15,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0084():
    a=SPoint(17,8);b=SPoint(0,0);c=SPoint(16,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0085():
    a=SPoint(1,9);b=SPoint(0,0);c=SPoint(17,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0086():
    a=SPoint(2,10);b=SPoint(0,0);c=SPoint(18,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0087():
    a=SPoint(3,11);b=SPoint(0,0);c=SPoint(19,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0088():
    a=SPoint(4,12);b=SPoint(0,0);c=SPoint(20,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0089():
    a=SPoint(5,13);b=SPoint(0,0);c=SPoint(21,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0090():
    a=SPoint(6,14);b=SPoint(0,0);c=SPoint(22,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0091():
    a=SPoint(7,2);b=SPoint(0,0);c=SPoint(23,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0092():
    a=SPoint(8,3);b=SPoint(0,0);c=SPoint(1,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0093():
    a=SPoint(9,4);b=SPoint(0,0);c=SPoint(2,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0094():
    a=SPoint(10,5);b=SPoint(0,0);c=SPoint(3,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0095():
    a=SPoint(11,6);b=SPoint(0,0);c=SPoint(4,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0096():
    a=SPoint(12,7);b=SPoint(0,0);c=SPoint(5,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0097():
    a=SPoint(13,8);b=SPoint(0,0);c=SPoint(6,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0098():
    a=SPoint(14,9);b=SPoint(0,0);c=SPoint(7,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0099():
    a=SPoint(15,10);b=SPoint(0,0);c=SPoint(8,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0100():
    a=SPoint(16,11);b=SPoint(0,0);c=SPoint(9,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0101():
    a=SPoint(17,12);b=SPoint(0,0);c=SPoint(10,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0102():
    a=SPoint(1,13);b=SPoint(0,0);c=SPoint(11,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0103():
    a=SPoint(2,14);b=SPoint(0,0);c=SPoint(12,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0104():
    a=SPoint(3,2);b=SPoint(0,0);c=SPoint(13,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0105():
    a=SPoint(4,3);b=SPoint(0,0);c=SPoint(14,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0106():
    a=SPoint(5,4);b=SPoint(0,0);c=SPoint(15,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0107():
    a=SPoint(6,5);b=SPoint(0,0);c=SPoint(16,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0108():
    a=SPoint(7,6);b=SPoint(0,0);c=SPoint(17,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0109():
    a=SPoint(8,7);b=SPoint(0,0);c=SPoint(18,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0110():
    a=SPoint(9,8);b=SPoint(0,0);c=SPoint(19,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0111():
    a=SPoint(10,9);b=SPoint(0,0);c=SPoint(20,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0112():
    a=SPoint(11,10);b=SPoint(0,0);c=SPoint(21,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0113():
    a=SPoint(12,11);b=SPoint(0,0);c=SPoint(22,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0114():
    a=SPoint(13,12);b=SPoint(0,0);c=SPoint(23,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0115():
    a=SPoint(14,13);b=SPoint(0,0);c=SPoint(1,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0116():
    a=SPoint(15,14);b=SPoint(0,0);c=SPoint(2,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0117():
    a=SPoint(16,2);b=SPoint(0,0);c=SPoint(3,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0118():
    a=SPoint(17,3);b=SPoint(0,0);c=SPoint(4,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0119():
    a=SPoint(1,4);b=SPoint(0,0);c=SPoint(5,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0120():
    a=SPoint(2,5);b=SPoint(0,0);c=SPoint(6,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0121():
    a=SPoint(3,6);b=SPoint(0,0);c=SPoint(7,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0122():
    a=SPoint(4,7);b=SPoint(0,0);c=SPoint(8,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0123():
    a=SPoint(5,8);b=SPoint(0,0);c=SPoint(9,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0124():
    a=SPoint(6,9);b=SPoint(0,0);c=SPoint(10,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0125():
    a=SPoint(7,10);b=SPoint(0,0);c=SPoint(11,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0126():
    a=SPoint(8,11);b=SPoint(0,0);c=SPoint(12,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0127():
    a=SPoint(9,12);b=SPoint(0,0);c=SPoint(13,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0128():
    a=SPoint(10,13);b=SPoint(0,0);c=SPoint(14,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0129():
    a=SPoint(11,14);b=SPoint(0,0);c=SPoint(15,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0130():
    a=SPoint(12,2);b=SPoint(0,0);c=SPoint(16,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0131():
    a=SPoint(13,3);b=SPoint(0,0);c=SPoint(17,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0132():
    a=SPoint(14,4);b=SPoint(0,0);c=SPoint(18,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0133():
    a=SPoint(15,5);b=SPoint(0,0);c=SPoint(19,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0134():
    a=SPoint(16,6);b=SPoint(0,0);c=SPoint(20,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0135():
    a=SPoint(17,7);b=SPoint(0,0);c=SPoint(21,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0136():
    a=SPoint(1,8);b=SPoint(0,0);c=SPoint(22,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0137():
    a=SPoint(2,9);b=SPoint(0,0);c=SPoint(23,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0138():
    a=SPoint(3,10);b=SPoint(0,0);c=SPoint(1,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0139():
    a=SPoint(4,11);b=SPoint(0,0);c=SPoint(2,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0140():
    a=SPoint(5,12);b=SPoint(0,0);c=SPoint(3,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0141():
    a=SPoint(6,13);b=SPoint(0,0);c=SPoint(4,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0142():
    a=SPoint(7,14);b=SPoint(0,0);c=SPoint(5,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0143():
    a=SPoint(8,2);b=SPoint(0,0);c=SPoint(6,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0144():
    a=SPoint(9,3);b=SPoint(0,0);c=SPoint(7,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0145():
    a=SPoint(10,4);b=SPoint(0,0);c=SPoint(8,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0146():
    a=SPoint(11,5);b=SPoint(0,0);c=SPoint(9,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0147():
    a=SPoint(12,6);b=SPoint(0,0);c=SPoint(10,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0148():
    a=SPoint(13,7);b=SPoint(0,0);c=SPoint(11,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0149():
    a=SPoint(14,8);b=SPoint(0,0);c=SPoint(12,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0150():
    a=SPoint(15,9);b=SPoint(0,0);c=SPoint(13,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0151():
    a=SPoint(16,10);b=SPoint(0,0);c=SPoint(14,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0152():
    a=SPoint(17,11);b=SPoint(0,0);c=SPoint(15,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0153():
    a=SPoint(1,12);b=SPoint(0,0);c=SPoint(16,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0154():
    a=SPoint(2,13);b=SPoint(0,0);c=SPoint(17,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0155():
    a=SPoint(3,14);b=SPoint(0,0);c=SPoint(18,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0156():
    a=SPoint(4,2);b=SPoint(0,0);c=SPoint(19,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0157():
    a=SPoint(5,3);b=SPoint(0,0);c=SPoint(20,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0158():
    a=SPoint(6,4);b=SPoint(0,0);c=SPoint(21,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0159():
    a=SPoint(7,5);b=SPoint(0,0);c=SPoint(22,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0160():
    a=SPoint(8,6);b=SPoint(0,0);c=SPoint(23,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0161():
    a=SPoint(9,7);b=SPoint(0,0);c=SPoint(1,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0162():
    a=SPoint(10,8);b=SPoint(0,0);c=SPoint(2,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0163():
    a=SPoint(11,9);b=SPoint(0,0);c=SPoint(3,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0164():
    a=SPoint(12,10);b=SPoint(0,0);c=SPoint(4,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0165():
    a=SPoint(13,11);b=SPoint(0,0);c=SPoint(5,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0166():
    a=SPoint(14,12);b=SPoint(0,0);c=SPoint(6,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0167():
    a=SPoint(15,13);b=SPoint(0,0);c=SPoint(7,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0168():
    a=SPoint(16,14);b=SPoint(0,0);c=SPoint(8,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0169():
    a=SPoint(17,2);b=SPoint(0,0);c=SPoint(9,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0170():
    a=SPoint(1,3);b=SPoint(0,0);c=SPoint(10,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0171():
    a=SPoint(2,4);b=SPoint(0,0);c=SPoint(11,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0172():
    a=SPoint(3,5);b=SPoint(0,0);c=SPoint(12,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0173():
    a=SPoint(4,6);b=SPoint(0,0);c=SPoint(13,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0174():
    a=SPoint(5,7);b=SPoint(0,0);c=SPoint(14,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0175():
    a=SPoint(6,8);b=SPoint(0,0);c=SPoint(15,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0176():
    a=SPoint(7,9);b=SPoint(0,0);c=SPoint(16,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0177():
    a=SPoint(8,10);b=SPoint(0,0);c=SPoint(17,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0178():
    a=SPoint(9,11);b=SPoint(0,0);c=SPoint(18,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0179():
    a=SPoint(10,12);b=SPoint(0,0);c=SPoint(19,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0180():
    a=SPoint(11,13);b=SPoint(0,0);c=SPoint(20,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0181():
    a=SPoint(12,14);b=SPoint(0,0);c=SPoint(21,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0182():
    a=SPoint(13,2);b=SPoint(0,0);c=SPoint(22,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0183():
    a=SPoint(14,3);b=SPoint(0,0);c=SPoint(23,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0184():
    a=SPoint(15,4);b=SPoint(0,0);c=SPoint(1,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0185():
    a=SPoint(16,5);b=SPoint(0,0);c=SPoint(2,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0186():
    a=SPoint(17,6);b=SPoint(0,0);c=SPoint(3,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0187():
    a=SPoint(1,7);b=SPoint(0,0);c=SPoint(4,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0188():
    a=SPoint(2,8);b=SPoint(0,0);c=SPoint(5,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0189():
    a=SPoint(3,9);b=SPoint(0,0);c=SPoint(6,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0190():
    a=SPoint(4,10);b=SPoint(0,0);c=SPoint(7,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0191():
    a=SPoint(5,11);b=SPoint(0,0);c=SPoint(8,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0192():
    a=SPoint(6,12);b=SPoint(0,0);c=SPoint(9,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0193():
    a=SPoint(7,13);b=SPoint(0,0);c=SPoint(10,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0194():
    a=SPoint(8,14);b=SPoint(0,0);c=SPoint(11,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0195():
    a=SPoint(9,2);b=SPoint(0,0);c=SPoint(12,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0196():
    a=SPoint(10,3);b=SPoint(0,0);c=SPoint(13,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0197():
    a=SPoint(11,4);b=SPoint(0,0);c=SPoint(14,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0198():
    a=SPoint(12,5);b=SPoint(0,0);c=SPoint(15,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0199():
    a=SPoint(13,6);b=SPoint(0,0);c=SPoint(16,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0200():
    a=SPoint(14,7);b=SPoint(0,0);c=SPoint(17,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0201():
    a=SPoint(15,8);b=SPoint(0,0);c=SPoint(18,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0202():
    a=SPoint(16,9);b=SPoint(0,0);c=SPoint(19,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0203():
    a=SPoint(17,10);b=SPoint(0,0);c=SPoint(20,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0204():
    a=SPoint(1,11);b=SPoint(0,0);c=SPoint(21,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0205():
    a=SPoint(2,12);b=SPoint(0,0);c=SPoint(22,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0206():
    a=SPoint(3,13);b=SPoint(0,0);c=SPoint(23,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0207():
    a=SPoint(4,14);b=SPoint(0,0);c=SPoint(1,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0208():
    a=SPoint(5,2);b=SPoint(0,0);c=SPoint(2,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0209():
    a=SPoint(6,3);b=SPoint(0,0);c=SPoint(3,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0210():
    a=SPoint(7,4);b=SPoint(0,0);c=SPoint(4,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0211():
    a=SPoint(8,5);b=SPoint(0,0);c=SPoint(5,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0212():
    a=SPoint(9,6);b=SPoint(0,0);c=SPoint(6,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0213():
    a=SPoint(10,7);b=SPoint(0,0);c=SPoint(7,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0214():
    a=SPoint(11,8);b=SPoint(0,0);c=SPoint(8,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0215():
    a=SPoint(12,9);b=SPoint(0,0);c=SPoint(9,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0216():
    a=SPoint(13,10);b=SPoint(0,0);c=SPoint(10,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0217():
    a=SPoint(14,11);b=SPoint(0,0);c=SPoint(11,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0218():
    a=SPoint(15,12);b=SPoint(0,0);c=SPoint(12,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0219():
    a=SPoint(16,13);b=SPoint(0,0);c=SPoint(13,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0220():
    a=SPoint(17,14);b=SPoint(0,0);c=SPoint(14,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0221():
    a=SPoint(1,2);b=SPoint(0,0);c=SPoint(15,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0222():
    a=SPoint(2,3);b=SPoint(0,0);c=SPoint(16,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0223():
    a=SPoint(3,4);b=SPoint(0,0);c=SPoint(17,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0224():
    a=SPoint(4,5);b=SPoint(0,0);c=SPoint(18,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0225():
    a=SPoint(5,6);b=SPoint(0,0);c=SPoint(19,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0226():
    a=SPoint(6,7);b=SPoint(0,0);c=SPoint(20,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0227():
    a=SPoint(7,8);b=SPoint(0,0);c=SPoint(21,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0228():
    a=SPoint(8,9);b=SPoint(0,0);c=SPoint(22,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0229():
    a=SPoint(9,10);b=SPoint(0,0);c=SPoint(23,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0230():
    a=SPoint(10,11);b=SPoint(0,0);c=SPoint(1,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0231():
    a=SPoint(11,12);b=SPoint(0,0);c=SPoint(2,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0232():
    a=SPoint(12,13);b=SPoint(0,0);c=SPoint(3,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0233():
    a=SPoint(13,14);b=SPoint(0,0);c=SPoint(4,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0234():
    a=SPoint(14,2);b=SPoint(0,0);c=SPoint(5,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0235():
    a=SPoint(15,3);b=SPoint(0,0);c=SPoint(6,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0236():
    a=SPoint(16,4);b=SPoint(0,0);c=SPoint(7,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0237():
    a=SPoint(17,5);b=SPoint(0,0);c=SPoint(8,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0238():
    a=SPoint(1,6);b=SPoint(0,0);c=SPoint(9,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0239():
    a=SPoint(2,7);b=SPoint(0,0);c=SPoint(10,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0240():
    a=SPoint(3,8);b=SPoint(0,0);c=SPoint(11,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0241():
    a=SPoint(4,9);b=SPoint(0,0);c=SPoint(12,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0242():
    a=SPoint(5,10);b=SPoint(0,0);c=SPoint(13,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0243():
    a=SPoint(6,11);b=SPoint(0,0);c=SPoint(14,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0244():
    a=SPoint(7,12);b=SPoint(0,0);c=SPoint(15,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0245():
    a=SPoint(8,13);b=SPoint(0,0);c=SPoint(16,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0246():
    a=SPoint(9,14);b=SPoint(0,0);c=SPoint(17,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0247():
    a=SPoint(10,2);b=SPoint(0,0);c=SPoint(18,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0248():
    a=SPoint(11,3);b=SPoint(0,0);c=SPoint(19,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0249():
    a=SPoint(12,4);b=SPoint(0,0);c=SPoint(20,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0250():
    a=SPoint(13,5);b=SPoint(0,0);c=SPoint(21,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0251():
    a=SPoint(14,6);b=SPoint(0,0);c=SPoint(22,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0252():
    a=SPoint(15,7);b=SPoint(0,0);c=SPoint(23,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0253():
    a=SPoint(16,8);b=SPoint(0,0);c=SPoint(1,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0254():
    a=SPoint(17,9);b=SPoint(0,0);c=SPoint(2,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0255():
    a=SPoint(1,10);b=SPoint(0,0);c=SPoint(3,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0256():
    a=SPoint(2,11);b=SPoint(0,0);c=SPoint(4,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0257():
    a=SPoint(3,12);b=SPoint(0,0);c=SPoint(5,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0258():
    a=SPoint(4,13);b=SPoint(0,0);c=SPoint(6,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0259():
    a=SPoint(5,14);b=SPoint(0,0);c=SPoint(7,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0260():
    a=SPoint(6,2);b=SPoint(0,0);c=SPoint(8,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0261():
    a=SPoint(7,3);b=SPoint(0,0);c=SPoint(9,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0262():
    a=SPoint(8,4);b=SPoint(0,0);c=SPoint(10,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0263():
    a=SPoint(9,5);b=SPoint(0,0);c=SPoint(11,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0264():
    a=SPoint(10,6);b=SPoint(0,0);c=SPoint(12,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0265():
    a=SPoint(11,7);b=SPoint(0,0);c=SPoint(13,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0266():
    a=SPoint(12,8);b=SPoint(0,0);c=SPoint(14,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0267():
    a=SPoint(13,9);b=SPoint(0,0);c=SPoint(15,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0268():
    a=SPoint(14,10);b=SPoint(0,0);c=SPoint(16,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0269():
    a=SPoint(15,11);b=SPoint(0,0);c=SPoint(17,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0270():
    a=SPoint(16,12);b=SPoint(0,0);c=SPoint(18,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0271():
    a=SPoint(17,13);b=SPoint(0,0);c=SPoint(19,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0272():
    a=SPoint(1,14);b=SPoint(0,0);c=SPoint(20,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0273():
    a=SPoint(2,2);b=SPoint(0,0);c=SPoint(21,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0274():
    a=SPoint(3,3);b=SPoint(0,0);c=SPoint(22,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0275():
    a=SPoint(4,4);b=SPoint(0,0);c=SPoint(23,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0276():
    a=SPoint(5,5);b=SPoint(0,0);c=SPoint(1,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0277():
    a=SPoint(6,6);b=SPoint(0,0);c=SPoint(2,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0278():
    a=SPoint(7,7);b=SPoint(0,0);c=SPoint(3,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0279():
    a=SPoint(8,8);b=SPoint(0,0);c=SPoint(4,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0280():
    a=SPoint(9,9);b=SPoint(0,0);c=SPoint(5,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0281():
    a=SPoint(10,10);b=SPoint(0,0);c=SPoint(6,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0282():
    a=SPoint(11,11);b=SPoint(0,0);c=SPoint(7,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0283():
    a=SPoint(12,12);b=SPoint(0,0);c=SPoint(8,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0284():
    a=SPoint(13,13);b=SPoint(0,0);c=SPoint(9,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0285():
    a=SPoint(14,14);b=SPoint(0,0);c=SPoint(10,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0286():
    a=SPoint(15,2);b=SPoint(0,0);c=SPoint(11,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0287():
    a=SPoint(16,3);b=SPoint(0,0);c=SPoint(12,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0288():
    a=SPoint(17,4);b=SPoint(0,0);c=SPoint(13,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0289():
    a=SPoint(1,5);b=SPoint(0,0);c=SPoint(14,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0290():
    a=SPoint(2,6);b=SPoint(0,0);c=SPoint(15,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0291():
    a=SPoint(3,7);b=SPoint(0,0);c=SPoint(16,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0292():
    a=SPoint(4,8);b=SPoint(0,0);c=SPoint(17,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0293():
    a=SPoint(5,9);b=SPoint(0,0);c=SPoint(18,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0294():
    a=SPoint(6,10);b=SPoint(0,0);c=SPoint(19,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0295():
    a=SPoint(7,11);b=SPoint(0,0);c=SPoint(20,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0296():
    a=SPoint(8,12);b=SPoint(0,0);c=SPoint(21,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0297():
    a=SPoint(9,13);b=SPoint(0,0);c=SPoint(22,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0298():
    a=SPoint(10,14);b=SPoint(0,0);c=SPoint(23,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0299():
    a=SPoint(11,2);b=SPoint(0,0);c=SPoint(1,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0300():
    a=SPoint(12,3);b=SPoint(0,0);c=SPoint(2,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0301():
    a=SPoint(13,4);b=SPoint(0,0);c=SPoint(3,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0302():
    a=SPoint(14,5);b=SPoint(0,0);c=SPoint(4,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0303():
    a=SPoint(15,6);b=SPoint(0,0);c=SPoint(5,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0304():
    a=SPoint(16,7);b=SPoint(0,0);c=SPoint(6,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0305():
    a=SPoint(17,8);b=SPoint(0,0);c=SPoint(7,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0306():
    a=SPoint(1,9);b=SPoint(0,0);c=SPoint(8,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0307():
    a=SPoint(2,10);b=SPoint(0,0);c=SPoint(9,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0308():
    a=SPoint(3,11);b=SPoint(0,0);c=SPoint(10,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0309():
    a=SPoint(4,12);b=SPoint(0,0);c=SPoint(11,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0310():
    a=SPoint(5,13);b=SPoint(0,0);c=SPoint(12,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0311():
    a=SPoint(6,14);b=SPoint(0,0);c=SPoint(13,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0312():
    a=SPoint(7,2);b=SPoint(0,0);c=SPoint(14,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0313():
    a=SPoint(8,3);b=SPoint(0,0);c=SPoint(15,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0314():
    a=SPoint(9,4);b=SPoint(0,0);c=SPoint(16,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0315():
    a=SPoint(10,5);b=SPoint(0,0);c=SPoint(17,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0316():
    a=SPoint(11,6);b=SPoint(0,0);c=SPoint(18,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0317():
    a=SPoint(12,7);b=SPoint(0,0);c=SPoint(19,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0318():
    a=SPoint(13,8);b=SPoint(0,0);c=SPoint(20,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0319():
    a=SPoint(14,9);b=SPoint(0,0);c=SPoint(21,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0320():
    a=SPoint(15,10);b=SPoint(0,0);c=SPoint(22,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0321():
    a=SPoint(16,11);b=SPoint(0,0);c=SPoint(23,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0322():
    a=SPoint(17,12);b=SPoint(0,0);c=SPoint(1,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0323():
    a=SPoint(1,13);b=SPoint(0,0);c=SPoint(2,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0324():
    a=SPoint(2,14);b=SPoint(0,0);c=SPoint(3,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0325():
    a=SPoint(3,2);b=SPoint(0,0);c=SPoint(4,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0326():
    a=SPoint(4,3);b=SPoint(0,0);c=SPoint(5,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0327():
    a=SPoint(5,4);b=SPoint(0,0);c=SPoint(6,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0328():
    a=SPoint(6,5);b=SPoint(0,0);c=SPoint(7,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0329():
    a=SPoint(7,6);b=SPoint(0,0);c=SPoint(8,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0330():
    a=SPoint(8,7);b=SPoint(0,0);c=SPoint(9,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0331():
    a=SPoint(9,8);b=SPoint(0,0);c=SPoint(10,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0332():
    a=SPoint(10,9);b=SPoint(0,0);c=SPoint(11,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0333():
    a=SPoint(11,10);b=SPoint(0,0);c=SPoint(12,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0334():
    a=SPoint(12,11);b=SPoint(0,0);c=SPoint(13,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0335():
    a=SPoint(13,12);b=SPoint(0,0);c=SPoint(14,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0336():
    a=SPoint(14,13);b=SPoint(0,0);c=SPoint(15,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0337():
    a=SPoint(15,14);b=SPoint(0,0);c=SPoint(16,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0338():
    a=SPoint(16,2);b=SPoint(0,0);c=SPoint(17,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0339():
    a=SPoint(17,3);b=SPoint(0,0);c=SPoint(18,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0340():
    a=SPoint(1,4);b=SPoint(0,0);c=SPoint(19,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0341():
    a=SPoint(2,5);b=SPoint(0,0);c=SPoint(20,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0342():
    a=SPoint(3,6);b=SPoint(0,0);c=SPoint(21,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0343():
    a=SPoint(4,7);b=SPoint(0,0);c=SPoint(22,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0344():
    a=SPoint(5,8);b=SPoint(0,0);c=SPoint(23,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0345():
    a=SPoint(6,9);b=SPoint(0,0);c=SPoint(1,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0346():
    a=SPoint(7,10);b=SPoint(0,0);c=SPoint(2,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0347():
    a=SPoint(8,11);b=SPoint(0,0);c=SPoint(3,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0348():
    a=SPoint(9,12);b=SPoint(0,0);c=SPoint(4,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0349():
    a=SPoint(10,13);b=SPoint(0,0);c=SPoint(5,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0350():
    a=SPoint(11,14);b=SPoint(0,0);c=SPoint(6,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0351():
    a=SPoint(12,2);b=SPoint(0,0);c=SPoint(7,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0352():
    a=SPoint(13,3);b=SPoint(0,0);c=SPoint(8,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0353():
    a=SPoint(14,4);b=SPoint(0,0);c=SPoint(9,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0354():
    a=SPoint(15,5);b=SPoint(0,0);c=SPoint(10,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0355():
    a=SPoint(16,6);b=SPoint(0,0);c=SPoint(11,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0356():
    a=SPoint(17,7);b=SPoint(0,0);c=SPoint(12,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0357():
    a=SPoint(1,8);b=SPoint(0,0);c=SPoint(13,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0358():
    a=SPoint(2,9);b=SPoint(0,0);c=SPoint(14,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0359():
    a=SPoint(3,10);b=SPoint(0,0);c=SPoint(15,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0360():
    a=SPoint(4,11);b=SPoint(0,0);c=SPoint(16,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0361():
    a=SPoint(5,12);b=SPoint(0,0);c=SPoint(17,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0362():
    a=SPoint(6,13);b=SPoint(0,0);c=SPoint(18,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0363():
    a=SPoint(7,14);b=SPoint(0,0);c=SPoint(19,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0364():
    a=SPoint(8,2);b=SPoint(0,0);c=SPoint(20,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0365():
    a=SPoint(9,3);b=SPoint(0,0);c=SPoint(21,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0366():
    a=SPoint(10,4);b=SPoint(0,0);c=SPoint(22,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0367():
    a=SPoint(11,5);b=SPoint(0,0);c=SPoint(23,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0368():
    a=SPoint(12,6);b=SPoint(0,0);c=SPoint(1,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0369():
    a=SPoint(13,7);b=SPoint(0,0);c=SPoint(2,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0370():
    a=SPoint(14,8);b=SPoint(0,0);c=SPoint(3,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0371():
    a=SPoint(15,9);b=SPoint(0,0);c=SPoint(4,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0372():
    a=SPoint(16,10);b=SPoint(0,0);c=SPoint(5,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0373():
    a=SPoint(17,11);b=SPoint(0,0);c=SPoint(6,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0374():
    a=SPoint(1,12);b=SPoint(0,0);c=SPoint(7,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0375():
    a=SPoint(2,13);b=SPoint(0,0);c=SPoint(8,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0376():
    a=SPoint(3,14);b=SPoint(0,0);c=SPoint(9,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0377():
    a=SPoint(4,2);b=SPoint(0,0);c=SPoint(10,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0378():
    a=SPoint(5,3);b=SPoint(0,0);c=SPoint(11,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0379():
    a=SPoint(6,4);b=SPoint(0,0);c=SPoint(12,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0380():
    a=SPoint(7,5);b=SPoint(0,0);c=SPoint(13,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0381():
    a=SPoint(8,6);b=SPoint(0,0);c=SPoint(14,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0382():
    a=SPoint(9,7);b=SPoint(0,0);c=SPoint(15,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0383():
    a=SPoint(10,8);b=SPoint(0,0);c=SPoint(16,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0384():
    a=SPoint(11,9);b=SPoint(0,0);c=SPoint(17,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0385():
    a=SPoint(12,10);b=SPoint(0,0);c=SPoint(18,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0386():
    a=SPoint(13,11);b=SPoint(0,0);c=SPoint(19,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0387():
    a=SPoint(14,12);b=SPoint(0,0);c=SPoint(20,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0388():
    a=SPoint(15,13);b=SPoint(0,0);c=SPoint(21,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0389():
    a=SPoint(16,14);b=SPoint(0,0);c=SPoint(22,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0390():
    a=SPoint(17,2);b=SPoint(0,0);c=SPoint(23,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0391():
    a=SPoint(1,3);b=SPoint(0,0);c=SPoint(1,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0392():
    a=SPoint(2,4);b=SPoint(0,0);c=SPoint(2,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0393():
    a=SPoint(3,5);b=SPoint(0,0);c=SPoint(3,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0394():
    a=SPoint(4,6);b=SPoint(0,0);c=SPoint(4,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0395():
    a=SPoint(5,7);b=SPoint(0,0);c=SPoint(5,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0396():
    a=SPoint(6,8);b=SPoint(0,0);c=SPoint(6,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0397():
    a=SPoint(7,9);b=SPoint(0,0);c=SPoint(7,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0398():
    a=SPoint(8,10);b=SPoint(0,0);c=SPoint(8,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0399():
    a=SPoint(9,11);b=SPoint(0,0);c=SPoint(9,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0400():
    a=SPoint(10,12);b=SPoint(0,0);c=SPoint(10,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0401():
    a=SPoint(11,13);b=SPoint(0,0);c=SPoint(11,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0402():
    a=SPoint(12,14);b=SPoint(0,0);c=SPoint(12,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0403():
    a=SPoint(13,2);b=SPoint(0,0);c=SPoint(13,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0404():
    a=SPoint(14,3);b=SPoint(0,0);c=SPoint(14,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0405():
    a=SPoint(15,4);b=SPoint(0,0);c=SPoint(15,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0406():
    a=SPoint(16,5);b=SPoint(0,0);c=SPoint(16,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0407():
    a=SPoint(17,6);b=SPoint(0,0);c=SPoint(17,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0408():
    a=SPoint(1,7);b=SPoint(0,0);c=SPoint(18,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0409():
    a=SPoint(2,8);b=SPoint(0,0);c=SPoint(19,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0410():
    a=SPoint(3,9);b=SPoint(0,0);c=SPoint(20,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0411():
    a=SPoint(4,10);b=SPoint(0,0);c=SPoint(21,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0412():
    a=SPoint(5,11);b=SPoint(0,0);c=SPoint(22,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0413():
    a=SPoint(6,12);b=SPoint(0,0);c=SPoint(23,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0414():
    a=SPoint(7,13);b=SPoint(0,0);c=SPoint(1,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0415():
    a=SPoint(8,14);b=SPoint(0,0);c=SPoint(2,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0416():
    a=SPoint(9,2);b=SPoint(0,0);c=SPoint(3,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0417():
    a=SPoint(10,3);b=SPoint(0,0);c=SPoint(4,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0418():
    a=SPoint(11,4);b=SPoint(0,0);c=SPoint(5,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0419():
    a=SPoint(12,5);b=SPoint(0,0);c=SPoint(6,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0420():
    a=SPoint(13,6);b=SPoint(0,0);c=SPoint(7,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0421():
    a=SPoint(14,7);b=SPoint(0,0);c=SPoint(8,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0422():
    a=SPoint(15,8);b=SPoint(0,0);c=SPoint(9,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0423():
    a=SPoint(16,9);b=SPoint(0,0);c=SPoint(10,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0424():
    a=SPoint(17,10);b=SPoint(0,0);c=SPoint(11,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0425():
    a=SPoint(1,11);b=SPoint(0,0);c=SPoint(12,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0426():
    a=SPoint(2,12);b=SPoint(0,0);c=SPoint(13,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0427():
    a=SPoint(3,13);b=SPoint(0,0);c=SPoint(14,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0428():
    a=SPoint(4,14);b=SPoint(0,0);c=SPoint(15,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0429():
    a=SPoint(5,2);b=SPoint(0,0);c=SPoint(16,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0430():
    a=SPoint(6,3);b=SPoint(0,0);c=SPoint(17,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0431():
    a=SPoint(7,4);b=SPoint(0,0);c=SPoint(18,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0432():
    a=SPoint(8,5);b=SPoint(0,0);c=SPoint(19,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0433():
    a=SPoint(9,6);b=SPoint(0,0);c=SPoint(20,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0434():
    a=SPoint(10,7);b=SPoint(0,0);c=SPoint(21,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0435():
    a=SPoint(11,8);b=SPoint(0,0);c=SPoint(22,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0436():
    a=SPoint(12,9);b=SPoint(0,0);c=SPoint(23,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0437():
    a=SPoint(13,10);b=SPoint(0,0);c=SPoint(1,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0438():
    a=SPoint(14,11);b=SPoint(0,0);c=SPoint(2,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0439():
    a=SPoint(15,12);b=SPoint(0,0);c=SPoint(3,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0440():
    a=SPoint(16,13);b=SPoint(0,0);c=SPoint(4,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0441():
    a=SPoint(17,14);b=SPoint(0,0);c=SPoint(5,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0442():
    a=SPoint(1,2);b=SPoint(0,0);c=SPoint(6,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0443():
    a=SPoint(2,3);b=SPoint(0,0);c=SPoint(7,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0444():
    a=SPoint(3,4);b=SPoint(0,0);c=SPoint(8,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0445():
    a=SPoint(4,5);b=SPoint(0,0);c=SPoint(9,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0446():
    a=SPoint(5,6);b=SPoint(0,0);c=SPoint(10,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0447():
    a=SPoint(6,7);b=SPoint(0,0);c=SPoint(11,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0448():
    a=SPoint(7,8);b=SPoint(0,0);c=SPoint(12,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0449():
    a=SPoint(8,9);b=SPoint(0,0);c=SPoint(13,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0450():
    a=SPoint(9,10);b=SPoint(0,0);c=SPoint(14,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0451():
    a=SPoint(10,11);b=SPoint(0,0);c=SPoint(15,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0452():
    a=SPoint(11,12);b=SPoint(0,0);c=SPoint(16,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0453():
    a=SPoint(12,13);b=SPoint(0,0);c=SPoint(17,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0454():
    a=SPoint(13,14);b=SPoint(0,0);c=SPoint(18,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0455():
    a=SPoint(14,2);b=SPoint(0,0);c=SPoint(19,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0456():
    a=SPoint(15,3);b=SPoint(0,0);c=SPoint(20,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0457():
    a=SPoint(16,4);b=SPoint(0,0);c=SPoint(21,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0458():
    a=SPoint(17,5);b=SPoint(0,0);c=SPoint(22,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0459():
    a=SPoint(1,6);b=SPoint(0,0);c=SPoint(23,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0460():
    a=SPoint(2,7);b=SPoint(0,0);c=SPoint(1,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0461():
    a=SPoint(3,8);b=SPoint(0,0);c=SPoint(2,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0462():
    a=SPoint(4,9);b=SPoint(0,0);c=SPoint(3,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0463():
    a=SPoint(5,10);b=SPoint(0,0);c=SPoint(4,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0464():
    a=SPoint(6,11);b=SPoint(0,0);c=SPoint(5,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0465():
    a=SPoint(7,12);b=SPoint(0,0);c=SPoint(6,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0466():
    a=SPoint(8,13);b=SPoint(0,0);c=SPoint(7,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0467():
    a=SPoint(9,14);b=SPoint(0,0);c=SPoint(8,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0468():
    a=SPoint(10,2);b=SPoint(0,0);c=SPoint(9,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0469():
    a=SPoint(11,3);b=SPoint(0,0);c=SPoint(10,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0470():
    a=SPoint(12,4);b=SPoint(0,0);c=SPoint(11,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0471():
    a=SPoint(13,5);b=SPoint(0,0);c=SPoint(12,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0472():
    a=SPoint(14,6);b=SPoint(0,0);c=SPoint(13,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0473():
    a=SPoint(15,7);b=SPoint(0,0);c=SPoint(14,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0474():
    a=SPoint(16,8);b=SPoint(0,0);c=SPoint(15,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0475():
    a=SPoint(17,9);b=SPoint(0,0);c=SPoint(16,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0476():
    a=SPoint(1,10);b=SPoint(0,0);c=SPoint(17,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0477():
    a=SPoint(2,11);b=SPoint(0,0);c=SPoint(18,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0478():
    a=SPoint(3,12);b=SPoint(0,0);c=SPoint(19,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0479():
    a=SPoint(4,13);b=SPoint(0,0);c=SPoint(20,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0480():
    a=SPoint(5,14);b=SPoint(0,0);c=SPoint(21,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0481():
    a=SPoint(6,2);b=SPoint(0,0);c=SPoint(22,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0482():
    a=SPoint(7,3);b=SPoint(0,0);c=SPoint(23,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0483():
    a=SPoint(8,4);b=SPoint(0,0);c=SPoint(1,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0484():
    a=SPoint(9,5);b=SPoint(0,0);c=SPoint(2,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0485():
    a=SPoint(10,6);b=SPoint(0,0);c=SPoint(3,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0486():
    a=SPoint(11,7);b=SPoint(0,0);c=SPoint(4,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0487():
    a=SPoint(12,8);b=SPoint(0,0);c=SPoint(5,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0488():
    a=SPoint(13,9);b=SPoint(0,0);c=SPoint(6,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0489():
    a=SPoint(14,10);b=SPoint(0,0);c=SPoint(7,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0490():
    a=SPoint(15,11);b=SPoint(0,0);c=SPoint(8,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0491():
    a=SPoint(16,12);b=SPoint(0,0);c=SPoint(9,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0492():
    a=SPoint(17,13);b=SPoint(0,0);c=SPoint(10,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0493():
    a=SPoint(1,14);b=SPoint(0,0);c=SPoint(11,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0494():
    a=SPoint(2,2);b=SPoint(0,0);c=SPoint(12,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0495():
    a=SPoint(3,3);b=SPoint(0,0);c=SPoint(13,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0496():
    a=SPoint(4,4);b=SPoint(0,0);c=SPoint(14,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0497():
    a=SPoint(5,5);b=SPoint(0,0);c=SPoint(15,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0498():
    a=SPoint(6,6);b=SPoint(0,0);c=SPoint(16,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0499():
    a=SPoint(7,7);b=SPoint(0,0);c=SPoint(17,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0500():
    a=SPoint(8,8);b=SPoint(0,0);c=SPoint(18,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0501():
    a=SPoint(9,9);b=SPoint(0,0);c=SPoint(19,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0502():
    a=SPoint(10,10);b=SPoint(0,0);c=SPoint(20,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0503():
    a=SPoint(11,11);b=SPoint(0,0);c=SPoint(21,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0504():
    a=SPoint(12,12);b=SPoint(0,0);c=SPoint(22,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0505():
    a=SPoint(13,13);b=SPoint(0,0);c=SPoint(23,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0506():
    a=SPoint(14,14);b=SPoint(0,0);c=SPoint(1,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0507():
    a=SPoint(15,2);b=SPoint(0,0);c=SPoint(2,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0508():
    a=SPoint(16,3);b=SPoint(0,0);c=SPoint(3,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0509():
    a=SPoint(17,4);b=SPoint(0,0);c=SPoint(4,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0510():
    a=SPoint(1,5);b=SPoint(0,0);c=SPoint(5,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0511():
    a=SPoint(2,6);b=SPoint(0,0);c=SPoint(6,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0512():
    a=SPoint(3,7);b=SPoint(0,0);c=SPoint(7,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0513():
    a=SPoint(4,8);b=SPoint(0,0);c=SPoint(8,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0514():
    a=SPoint(5,9);b=SPoint(0,0);c=SPoint(9,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0515():
    a=SPoint(6,10);b=SPoint(0,0);c=SPoint(10,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0516():
    a=SPoint(7,11);b=SPoint(0,0);c=SPoint(11,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0517():
    a=SPoint(8,12);b=SPoint(0,0);c=SPoint(12,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0518():
    a=SPoint(9,13);b=SPoint(0,0);c=SPoint(13,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0519():
    a=SPoint(10,14);b=SPoint(0,0);c=SPoint(14,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0520():
    a=SPoint(11,2);b=SPoint(0,0);c=SPoint(15,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0521():
    a=SPoint(12,3);b=SPoint(0,0);c=SPoint(16,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0522():
    a=SPoint(13,4);b=SPoint(0,0);c=SPoint(17,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0523():
    a=SPoint(14,5);b=SPoint(0,0);c=SPoint(18,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0524():
    a=SPoint(15,6);b=SPoint(0,0);c=SPoint(19,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0525():
    a=SPoint(16,7);b=SPoint(0,0);c=SPoint(20,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0526():
    a=SPoint(17,8);b=SPoint(0,0);c=SPoint(21,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0527():
    a=SPoint(1,9);b=SPoint(0,0);c=SPoint(22,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0528():
    a=SPoint(2,10);b=SPoint(0,0);c=SPoint(23,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0529():
    a=SPoint(3,11);b=SPoint(0,0);c=SPoint(1,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0530():
    a=SPoint(4,12);b=SPoint(0,0);c=SPoint(2,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0531():
    a=SPoint(5,13);b=SPoint(0,0);c=SPoint(3,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0532():
    a=SPoint(6,14);b=SPoint(0,0);c=SPoint(4,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0533():
    a=SPoint(7,2);b=SPoint(0,0);c=SPoint(5,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0534():
    a=SPoint(8,3);b=SPoint(0,0);c=SPoint(6,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0535():
    a=SPoint(9,4);b=SPoint(0,0);c=SPoint(7,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0536():
    a=SPoint(10,5);b=SPoint(0,0);c=SPoint(8,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0537():
    a=SPoint(11,6);b=SPoint(0,0);c=SPoint(9,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0538():
    a=SPoint(12,7);b=SPoint(0,0);c=SPoint(10,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0539():
    a=SPoint(13,8);b=SPoint(0,0);c=SPoint(11,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0540():
    a=SPoint(14,9);b=SPoint(0,0);c=SPoint(12,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0541():
    a=SPoint(15,10);b=SPoint(0,0);c=SPoint(13,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0542():
    a=SPoint(16,11);b=SPoint(0,0);c=SPoint(14,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0543():
    a=SPoint(17,12);b=SPoint(0,0);c=SPoint(15,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0544():
    a=SPoint(1,13);b=SPoint(0,0);c=SPoint(16,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0545():
    a=SPoint(2,14);b=SPoint(0,0);c=SPoint(17,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0546():
    a=SPoint(3,2);b=SPoint(0,0);c=SPoint(18,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0547():
    a=SPoint(4,3);b=SPoint(0,0);c=SPoint(19,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0548():
    a=SPoint(5,4);b=SPoint(0,0);c=SPoint(20,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0549():
    a=SPoint(6,5);b=SPoint(0,0);c=SPoint(21,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0550():
    a=SPoint(7,6);b=SPoint(0,0);c=SPoint(22,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0551():
    a=SPoint(8,7);b=SPoint(0,0);c=SPoint(23,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0552():
    a=SPoint(9,8);b=SPoint(0,0);c=SPoint(1,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0553():
    a=SPoint(10,9);b=SPoint(0,0);c=SPoint(2,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0554():
    a=SPoint(11,10);b=SPoint(0,0);c=SPoint(3,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0555():
    a=SPoint(12,11);b=SPoint(0,0);c=SPoint(4,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0556():
    a=SPoint(13,12);b=SPoint(0,0);c=SPoint(5,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0557():
    a=SPoint(14,13);b=SPoint(0,0);c=SPoint(6,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0558():
    a=SPoint(15,14);b=SPoint(0,0);c=SPoint(7,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0559():
    a=SPoint(16,2);b=SPoint(0,0);c=SPoint(8,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0560():
    a=SPoint(17,3);b=SPoint(0,0);c=SPoint(9,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0561():
    a=SPoint(1,4);b=SPoint(0,0);c=SPoint(10,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0562():
    a=SPoint(2,5);b=SPoint(0,0);c=SPoint(11,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0563():
    a=SPoint(3,6);b=SPoint(0,0);c=SPoint(12,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0564():
    a=SPoint(4,7);b=SPoint(0,0);c=SPoint(13,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0565():
    a=SPoint(5,8);b=SPoint(0,0);c=SPoint(14,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0566():
    a=SPoint(6,9);b=SPoint(0,0);c=SPoint(15,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0567():
    a=SPoint(7,10);b=SPoint(0,0);c=SPoint(16,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0568():
    a=SPoint(8,11);b=SPoint(0,0);c=SPoint(17,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0569():
    a=SPoint(9,12);b=SPoint(0,0);c=SPoint(18,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0570():
    a=SPoint(10,13);b=SPoint(0,0);c=SPoint(19,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0571():
    a=SPoint(11,14);b=SPoint(0,0);c=SPoint(20,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0572():
    a=SPoint(12,2);b=SPoint(0,0);c=SPoint(21,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0573():
    a=SPoint(13,3);b=SPoint(0,0);c=SPoint(22,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0574():
    a=SPoint(14,4);b=SPoint(0,0);c=SPoint(23,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0575():
    a=SPoint(15,5);b=SPoint(0,0);c=SPoint(1,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0576():
    a=SPoint(16,6);b=SPoint(0,0);c=SPoint(2,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0577():
    a=SPoint(17,7);b=SPoint(0,0);c=SPoint(3,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0578():
    a=SPoint(1,8);b=SPoint(0,0);c=SPoint(4,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0579():
    a=SPoint(2,9);b=SPoint(0,0);c=SPoint(5,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0580():
    a=SPoint(3,10);b=SPoint(0,0);c=SPoint(6,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0581():
    a=SPoint(4,11);b=SPoint(0,0);c=SPoint(7,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0582():
    a=SPoint(5,12);b=SPoint(0,0);c=SPoint(8,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0583():
    a=SPoint(6,13);b=SPoint(0,0);c=SPoint(9,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0584():
    a=SPoint(7,14);b=SPoint(0,0);c=SPoint(10,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0585():
    a=SPoint(8,2);b=SPoint(0,0);c=SPoint(11,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0586():
    a=SPoint(9,3);b=SPoint(0,0);c=SPoint(12,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0587():
    a=SPoint(10,4);b=SPoint(0,0);c=SPoint(13,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0588():
    a=SPoint(11,5);b=SPoint(0,0);c=SPoint(14,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0589():
    a=SPoint(12,6);b=SPoint(0,0);c=SPoint(15,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0590():
    a=SPoint(13,7);b=SPoint(0,0);c=SPoint(16,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0591():
    a=SPoint(14,8);b=SPoint(0,0);c=SPoint(17,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0592():
    a=SPoint(15,9);b=SPoint(0,0);c=SPoint(18,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0593():
    a=SPoint(16,10);b=SPoint(0,0);c=SPoint(19,-6)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0594():
    a=SPoint(17,11);b=SPoint(0,0);c=SPoint(20,-7)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0595():
    a=SPoint(1,12);b=SPoint(0,0);c=SPoint(21,-1)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0596():
    a=SPoint(2,13);b=SPoint(0,0);c=SPoint(22,-2)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0597():
    a=SPoint(3,14);b=SPoint(0,0);c=SPoint(23,-3)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0598():
    a=SPoint(4,2);b=SPoint(0,0);c=SPoint(1,-4)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

def test_exact_foot_0599():
    a=SPoint(5,3);b=SPoint(0,0);c=SPoint(2,-5)
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True

