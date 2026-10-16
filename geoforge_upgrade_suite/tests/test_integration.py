from pathlib import Path
import sys
import json
import tempfile
import pytest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from reasoning_search import (load_engine,CertifiedSearchEnsemble,Budget,
     SharedKnowledgeWorkspace,ProvedFact,Auxiliary,AuxiliaryBuilder,
     SearchStateCanonicalizer,ProofGapAnalyzer,BranchSelector)
from dataset_engineering import (DatasetConfig,ProofRecordValidator,
     AtomicDatasetWriter,DatasetAuditor,StreamingDatasetReader,DatasetStatistics,
     DatasetCurriculum,LeakageAuditor,DatasetIntegrityError)
from symbolic_coordinates import AlgebraicCoordinateProver
from formal_language import NaturalLanguageGeometryParser,FormalizationConsistencyChecker
from technical_benchmark import (SourceInventory,CapabilityEvidenceRegistry,
     ExternalBenchmarkGuard)
from neural_baseline import (GeometryTokenizer,TransformerConfig,GeometryTransformer,
     NeuralTrainer,TrainingConfig,ProofTextDataset,torch)

ENG=load_engine(str(ROOT.parent/'geoforge.py'))


def valid_record():
    factory=ENG.GeometryTemplateFactory(11)
    family,coords,assumptions,goal=factory.build('midline')
    engine=ENG.CertifiedDDAR2Engine(assumptions,maxfacts=300).close()
    cert=engine.certificate(goal)
    assert cert is not None
    return {'schema':'geoforge-synthetic-v2','family':family,
       'problem':{'hypotheses':[str(f) for f in cert.assumptions],
                  'goal':str(cert.goal),'points':sorted(coords)},
       'proof':cert.to_dict(),'auxiliaries':[],
       'metadata':{'source':'certified_integration_test'}}


def independent_checker(raw):
    cert=ENG.ProofCertificate.from_dict(raw)
    return ENG.ProofCheckerV2().verify(cert)


def test_dataset_real_certificates_and_tamper():
    record=valid_record();validator=ProofRecordValidator(independent_checker)
    assert validator.validate(record)[0]
    with tempfile.TemporaryDirectory() as td:
        ds=AtomicDatasetWriter(td,DatasetConfig(seed=11,shard_size=2),validator)
        manifest=ds.write([record])
        assert manifest.accepted_records==1
        report=DatasetAuditor(validator).verify(td)
        assert report['passed'] and report['records']==1
        samples=list(StreamingDatasetReader(td))
        assert len(samples)==1
        file=Path(td)/manifest.files[0]['name']
        file.write_bytes(file.read_bytes()+b'x')
        assert not DatasetAuditor(validator).verify(td)['passed']


def test_tampered_proof_refused():
    rec=valid_record();validator=ProofRecordValidator(independent_checker)
    rec['proof']['steps'][-1]['conclusion']='perp a b c d'
    assert not validator.validate(rec)[0]


def test_shared_knowledge_requires_base_hypotheses():
    rec=valid_record();base=tuple(rec['problem']['hypotheses'])
    ws=SharedKnowledgeWorkspace(ENG,base)
    item=ProvedFact(rec['proof']['goal'],json.dumps(rec['proof']),base,0)
    assert ws.add(item)
    assert not ws.add(item)
    wrong=ProvedFact(rec['proof']['goal'],json.dumps(rec['proof']),base+('distinct z y',),0)
    assert not ws.add(wrong)


def test_search_auxiliary_never_claims_unconditional():
    search=CertifiedSearchEnsemble(ENG,Budget(seconds=2,max_nodes=5,
          beam_width=3,max_auxiliary_points=1))
    rec=valid_record()
    result=search.solve(rec['problem']['hypotheses'],rec['problem']['goal'])
    assert result.status=='certified'
    assert result.auxiliary_constructions==()


def test_search_unknown_goal_finite():
    search=CertifiedSearchEnsemble(ENG,Budget(seconds=2,max_nodes=5,
          beam_width=2,max_auxiliary_points=1))
    result=search.solve(('distinct a b','distinct b c'),
          'cyclic a b c d',coordinates={'a':(0,0),'b':(5,0),'c':(2,4),'d':(0,5)})
    assert result.status in ('not_proven','conditional_auxiliary_derivation')
    assert result.status!='certified'


def test_polynomial_subgoal_degree_and_guards():
    result=AlgebraicCoordinateProver(max_pairs=80).prove(
        ('midp m a b',),'coll a m b')
    assert result.status=='conditional_polynomial_identity'
    assert 'distinct a m' in result.assumptions_needed


def test_formal_language_unknown_is_not_hallucinated():
    p=NaturalLanguageGeometryParser().parse('A esfera astral é azul; Mostre que AB é um hipercubo.')
    assert p.goal is None and p.unsupported and not p.is_complete()
    result=FormalizationConsistencyChecker().check(p)
    assert result['errors']==['goal not specified']


def test_capability_evidence_requires_test():
    reg=CapabilityEvidenceRegistry()
    with pytest.raises(ValueError):reg.record(296,'verified_subset',[],'')
    reg.record(296,'verified_subset',['test_inversion_circle_and_line'],
               'exact inversion subset only')
    assert reg.export()['requirements'][0]['status']=='verified_subset'
    assert ExternalBenchmarkGuard(None).inspect()['imo_ag_30.txt']['status']=='BLOCKED_DATASET_MISSING'


@pytest.mark.skipif(torch is None,reason='optional torch not installed')
def test_neural_tiny_train_and_checkpoint():
    texts=['given midp d a b prove cong d a d b',
           'given midp e a c prove coll a e c']
    tok=GeometryTokenizer.fit(texts)
    cfg=TransformerConfig(vocab_size=len(tok.vocab),context=24,dim=16,
                          heads=2,layers=1)
    model=GeometryTransformer(cfg)
    training=NeuralTrainer(model,TrainingConfig(steps=3,batch=2,seed=5))
    scores=training.train(ProofTextDataset(texts,tok,24))
    assert scores['steps']==3 and scores['last_loss']>0
    with tempfile.TemporaryDirectory() as td:
        path=Path(td)/'model.pt'
        training.save_checkpoint(path,tok)
        loaded,tokenizer,meta=NeuralTrainer.load_checkpoint(path)
        assert tokenizer.vocab==tok.vocab
        assert loaded.config==cfg


@pytest.mark.skipif(torch is None,reason='optional torch not installed')
def test_neural_moe_backward():
    cfg=TransformerConfig(vocab_size=20,context=12,dim=16,
                          heads=2,layers=1,experts=3,top_k=2)
    model=GeometryTransformer(cfg)
    inputs=torch.randint(1,20,(2,8))
    out,loss=model(inputs,inputs)
    loss.backward()
    assert out.shape==(2,8,20)
    assert torch.isfinite(loss)
    assert any(p.grad is not None for p in model.parameters())
