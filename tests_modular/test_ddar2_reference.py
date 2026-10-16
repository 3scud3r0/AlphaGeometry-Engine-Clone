"""Isolated reference subprocess tests. Do not confuse with official parity."""
import pytest
from geoforge_prover import ddar2_reference as ag2

def _fake_vendor(folder):
    folder.mkdir(parents=True,exist_ok=True)
    for name in ("numericals.py","elimination.py"):
        (folder/name).write_text("\n")
    (folder/"parse.py").write_text("""
class AGProblem:
    @classmethod
    def parse(cls,text):
        if 'THROW' in text: raise ValueError('bad problem')
        return type('P',(),{'points':['a','b'],'preds':['p'],
                            'goal': 'g' if '?' in text else None})()
""")
    (folder/"ddar.py").write_text("""
class DDAR:
    def __init__(self,points): self.points=points
    def force_pred(self,pred): pass
    def deduction_closure(self): print('progress...',end='')
    def check_pred(self,goal): return goal=='g'
""")
    (folder/"test.py").write_text(
        "problems_without_aux={'sample':'a@0_0 = ? goal'}\n"
        "problems_with_aux={'sample2':'a@0_0 = ? goal'}\n")

def test_fails_closed_when_vendor_missing(tmp_path,monkeypatch):
    monkeypatch.setattr(ag2,"_VENDOR",tmp_path)
    assert ag2.prove_with_reference("a@0_0 = ? goal").result=="unavailable"

def test_subprocess_output(tmp_path,monkeypatch):
    _fake_vendor(tmp_path);monkeypatch.setattr(ag2,"_VENDOR",tmp_path)
    result=ag2.prove_with_reference("a@0_0 = ? goal",timeout=4)
    assert result.result=="deduced" and result.num_points==2

def test_exception_not_promoted_to_proof(tmp_path,monkeypatch):
    _fake_vendor(tmp_path);monkeypatch.setattr(ag2,"_VENDOR",tmp_path)
    result=ag2.prove_with_reference("THROW ? goal")
    assert result.result=="error" and result.exception=="ValueError"

def test_example_runner_mock(tmp_path,monkeypatch):
    _fake_vendor(tmp_path);monkeypatch.setattr(ag2,"_VENDOR",tmp_path)
    assert ag2.official_examples()["without_aux"][0][0]=="sample"
    audit=ag2.evaluate_examples(limit=1)
    assert audit["deduced"]==audit["tested"]==1

def test_invalid_input_rejected():
    with pytest.raises(ValueError):ag2.prove_with_reference("no target")
    with pytest.raises(ValueError):ag2._invoke("print(1)",timeout=0)
    with pytest.raises(ValueError):ag2.evaluate_examples(limit=0)

def test_one_actual_upstream_example():
    # This is a public *example*, not a holdout benchmark or proof certificate.
    result=ag2.evaluate_examples(limit=1,timeout=90)
    assert result["tested"]==result["deduced"]==1
