"""Deterministic exact geometry auxiliary tests, independent of model weights."""
from fractions import Fraction as F
import pytest
from geoforge_search import reference_auxiliary as aux
from geoforge_prover.ddar2_reference import ReferenceResult

PROBLEM='a@0_0 = ; b@4_0 = ; c@0_4 = ? para a b a c'

def test_extract_coordinates_and_midpoint():
    pts=aux.extract_coordinates(PROBLEM)
    assert pts['c']==(F(0),F(4))
    choices=list(aux.candidate_auxiliaries(pts,kinds=('midpoint',),limit=20))
    assert any(x.x==2 and x.y==0 and x.predicates==('midp aux0 a b',) for x in choices)

def test_foot_constructed_perpendicular():
    pts={'a':(F(0),F(0)),'b':(F(4),F(0)),'c':(F(1),F(3)),
         'd':(F(2),F(-2))}
    feet=list(aux.candidate_auxiliaries(pts,kinds=('foot',),limit=50))
    assert any(x.kind=='foot' and x.x==1 and x.y==0 for x in feet)
    assert all('perp' in x.predicates[-1] for x in feet)

def test_goal_preserved():
    p=aux.extract_coordinates(PROBLEM)
    c=next(aux.candidate_auxiliaries(p,kinds=('midpoint',)))
    result=aux.append_auxiliary(PROBLEM,c)
    assert result.rsplit('?',1)[1].strip()=='para a b a c'

def test_finds_aux_under_mock_reference(monkeypatch):
    calls=[]
    def stub(problem,timeout=0):
        calls.append(problem)
        return ReferenceResult('deduced' if 'midp' in problem else 'unknown')
    monkeypatch.setattr(aux,'prove_with_reference',stub)
    result=aux.search(PROBLEM,max_candidates=4,seconds=2.)
    assert result.status=='deduced_with_aux' and result.attempts==1
    assert len(calls)==2

def test_unproved_not_refuted(monkeypatch):
    monkeypatch.setattr(aux,'prove_with_reference',
                        lambda *args,**kwargs:ReferenceResult('unknown'))
    result=aux.search(PROBLEM,max_candidates=3,seconds=2.)
    assert result.status=='unknown' and result.attempts<=3

def test_invalid_inputs():
    with pytest.raises(ValueError):aux.extract_coordinates('no goal')
    with pytest.raises(ValueError):aux.search(PROBLEM,seconds=0)
