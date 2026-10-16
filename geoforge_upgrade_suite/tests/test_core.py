from pathlib import Path
import sys
import json
import tempfile
from fractions import Fraction as Q
import pytest

sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from geometry_exact import (Vec2,Line,Circle,Inversion,radical_center,
  Polynomial,groebner_basis,prove_polynomial_membership,
  HPoint,Mat3,DomainError,cross_ratio,midpoint,convex_hull,
  point_inside_convex_polygon)
from symbolic_coordinates import (CoordinatePredicateCompiler,
  AlgebraicCoordinateProver,NumericalEquationValidator,SystemSolvabilityGuard)
from formal_language import (NaturalLanguageGeometryParser,LaTeXGeometryParser,
    NLToDSLTranslator,FormalizationConsistencyChecker)
from neural_baseline import GeometryTokenizer,ConstructionGrammar
from dataset_engineering import deterministic_seed,FamilySplit,DatasetConfig
from reasoning_search import load_engine,CertifiedSearchEnsemble,Budget

ROOT=Path(__file__).resolve().parents[2]
ENGINE=str(ROOT/'geoforge.py')


def test_vectors_lines_exact():
    a=Vec2(0,0);b=Vec2(4,0);c=Vec2(2,3)
    assert Line.through(a,b).intersect(Line.through(c,Vec2(2,4)))==Vec2(2,0)
    assert Line.through(a,b).reflect(c)==Vec2(2,-3)
    assert midpoint(a,b)==Vec2(2,0)


def test_circumcircle_radical_axis():
    a=Circle(Vec2(0,0),25);b=Circle(Vec2(6,0),25)
    assert a.radical_axis(b).contains(Vec2(3,4))
    assert b.radical_axis(a).contains(Vec2(3,4))
    c=Circle(Vec2(0,8),25)
    p=radical_center(a,b,c)
    assert a.power(p)==b.power(p)==c.power(p)


def test_inversion_circle_and_line():
    inv=Inversion(Vec2(0,0),9)
    assert inv.is_involution(Vec2(3,4))
    line=Line.through(Vec2(2,1),Vec2(2,3))
    img=inv.line(line)
    assert isinstance(img,Circle)
    assert img.contains(inv.point(Vec2(2,1)))
    assert img.contains(Vec2(0,0))
    circ=Circle(Vec2(2,0),4)
    linear=inv.circle(circ)
    assert isinstance(linear,Line)
    assert linear.contains(inv.point(Vec2(4,0)))


def test_homogeneous_projection():
    p=HPoint(3,4,1)
    t=Mat3(((1,0,5),(0,1,-3),(0,0,1)))
    assert t.invert().point(t.point(p))==p
    assert p.cross(HPoint(4,6,1)).contains(p)


def test_polynomial_ideal_exact():
    x=Polynomial.variable(2,0);y=Polynomial.variable(2,1)
    f=x*x-y*y
    q,r=f.divided_remainder([x-y])
    assert not r and q[0]==x+y
    assert (f.derivative(0)).eval((3,1))==6
    yes,gb,_=prove_polynomial_membership(x*x-y*y,[x-y])
    assert yes and not gb.exhausted


def test_coordinate_compilation():
    assert NumericalEquationValidator.check('midp',('m','a','b'),
         {'a':(0,0),'b':(4,0),'m':(2,0)})
    assert NumericalEquationValidator.check('perp',('a','b','c','d'),
         {'a':(0,0),'b':(1,0),'c':(3,4),'d':(3,5)})
    assert NumericalEquationValidator.check('cyclic',('a','b','c','d'),
         {'a':(1,0),'b':(0,1),'c':(-1,0),'d':(0,-1)})


def test_coordinate_prover_simple():
    p=AlgebraicCoordinateProver(max_pairs=40)
    r=p.prove(('midp m a b',),'coll a m b')
    # May be conditional due to explicit distinctness; must not claim it is
    # universally valid without discharging that condition.
    assert r.status in ('conditional_polynomial_identity','polynomial_identity_proven')


def test_natural_language_explicit_goals():
    p=NaturalLanguageGeometryParser().parse('D e o ponto medio de AB; Demonstre que DE e paralelo a BC.')
    assert 'midp D A B' in p.hypotheses
    assert p.goal=='para D E B C'
    assert p.is_complete()
    assert LaTeXGeometryParser().parse(r'\overline{AB} \parallel \overline{CD}')=='para A B C D'


def test_tokenizer_and_grammar():
    tokenizer=GeometryTokenizer.fit(('midp d a b','para e f b c'))
    ids=tokenizer.encode('midp d a b')
    assert tokenizer.decode(ids)=='midp d a b'
    assert ConstructionGrammar().parse('x = midpoint a b',('a','b'))==('x','midpoint',('a','b'))


def test_proof_search_safe():
    core=load_engine(ENGINE)
    cert=CertifiedSearchEnsemble(core,Budget(seconds=3,max_nodes=6))
    result=cert.solve(('midp d a b','midp e a c','ncoll a b c'),
                      'para d e b c')
    assert result.status=='certified'
    assert result.certificate is not None


def test_seed_reproducibility():
    assert deterministic_seed(1,2)==deterministic_seed(1,2)
    assert deterministic_seed(1,2)!=deterministic_seed(2,1)
    sp=FamilySplit(DatasetConfig(seed=11))
    assert sp.split('midline')==sp.split('midline')
