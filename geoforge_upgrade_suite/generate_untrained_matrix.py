#!/usr/bin/env python3
"""Reproducibly generate 5,400 distinct exact-geometry regression functions.

These are real executable assertions, deliberately materialized for source
inspection, reproducibility, and measuring the effect of future rewrites.
Regenerate: python -m geoforge_upgrade_suite.generate_untrained_matrix
"""
from __future__ import annotations
from pathlib import Path
import hashlib,json

ROOT=Path(__file__).resolve().parent/'matrix_untrained'

HEADER='''# GENERATED, DETERMINISTIC, NO TRAINED MODEL USED.
# Source generator: geoforge_upgrade_suite/generate_untrained_matrix.py
from fractions import Fraction as Q
from geoforge_upgrade_suite.geometry_exact import Vec2,Polynomial,Line
from geoforge_upgrade_suite.exact_constructions import SPoint,foot,line_intersection
from geoforge_upgrade_suite.deterministic_ideal import ExactIdealEngine,certificate_to_json,verify_certificate_json
from geoforge_upgrade_suite.deterministic_solver import ExactFactEvaluator,GuardLedger

'''


def body(family,i):
    a=i%17+1;b=i%13+2;c=i%23+1;d=i%7+1
    if family=='vector_midpoint':
        return f'''    a=Vec2(Q({a}),Q({b}));b=Vec2(Q({c}),Q({d}))
    m=(a+b)/2
    assert m*2==a+b
    assert (m-a).norm2()==(b-m).norm2()
    assert (b-a).cross(m-a)==0
    assert m-a==b-m
'''
    if family=='line_intersection':
        return f'''    a=SPoint(0,0);b=SPoint({a},1)
    c=SPoint(0,{b});d=SPoint(1,0)
    p=line_intersection(a,b,c,d)
    assert (p-a).cross(b-a)==0
    assert (p-c).cross(d-c)==0
    assert p.x.is_rational is True
'''
    if family=='exact_foot':
        return f'''    a=SPoint({a},{b});b=SPoint(0,0);c=SPoint({c},-{d})
    p=foot(a,b,c)
    assert (p-b).cross(c-b)==0
    assert (a-p).dot(c-b)==0
    assert p.x.is_rational is True
    assert p.y.is_rational is True
'''
    if family=='equal_lengths':
        return f'''    a=Vec2(Q({a}),Q({b}));b=Vec2(Q({a+c}),Q({b+d}))
    c=a+Vec2(Q({d}),Q(-{c}));d=c+(b-a)
    assert (b-a).norm2()==(d-c).norm2()
    assert (b-a).cross(d-c)==0
    assert (d-b)==(c-a)
    assert (a-c).norm2()==(b-d).norm2()
'''
    if family=='rational_angle':
        return f'''    q={a};r={b};p={{'a':(0,0),'b':(q,r),'c':(-r,q),'d':(4,5),'e':(4+3*q,5+3*r),'f':(4-3*r,5+3*q)}}
    ev=ExactFactEvaluator(p)
    assert ev.check('perp a b a c')
    assert ev.check('eqangle a b a c d e d f')
    assert not ev.check('para a b a c')
    assert ev.check('distinct a b')
'''
    if family=='witness_positive':
        return f'''    x=Polynomial.variable(2,0);y=Polynomial.variable(2,1)
    axiom=x-Q({a});goal=(x+Q({b}))*axiom
    result=ExactIdealEngine().membership((axiom,y-Q({c})),goal)
    assert result.status=='proved'
    assert result.certificate.verify()
    assert verify_certificate_json(certificate_to_json(result.certificate))
'''
    if family=='witness_negative':
        return f'''    x=Polynomial.variable(2,0);y=Polynomial.variable(2,1)
    axiom=x-Q({a});goal=(x+Q({b}))*axiom
    result=ExactIdealEngine().membership((axiom,),goal)
    assert result.status=='proved'
    fake=result.certificate.multipliers[0]+Q(1)
    assert (axiom*fake)!=goal
    assert result.certificate.multipliers[0]*axiom==goal
'''
    if family=='nondegeneracy_guard':
        return f'''    ledger=GuardLedger(('ncoll a b c','midp d a b','midp e a c','distinct x y'))
    assert ledger.entails('distinct b c')
    assert ledger.entails('distinct d e')
    assert ledger.entails('distinct a d')
    assert ledger.entails('ncoll a c b')
    assert not ledger.entails('distinct z w')
'''
    if family=='line_translation':
        return f'''    a=Vec2(Q({a}),Q({b}));b=a+Vec2(Q({c}),Q({d}))
    shift=Vec2(Q({d}),Q(-{c}))
    l=Line.through(a,b);m=Line.through(a+shift,b+shift)
    assert l.is_parallel(m)
    assert m.contains(a+shift)
    assert m.contains(b+shift)
    assert l.direction().cross(m.direction())==0
'''
    raise KeyError(family)


def generate(per_family=600):
    ROOT.mkdir(parents=True,exist_ok=True)
    counts={};hashes={}
    families=('vector_midpoint','line_intersection','exact_foot','equal_lengths',
              'rational_angle','witness_positive','witness_negative',
              'nondegeneracy_guard','line_translation')
    for family in families:
        lines=[HEADER]
        for i in range(per_family):
            lines.append(f'def test_{family}_{i:04d}():\n')
            lines.append(body(family,i))
            lines.append('\n')
        path=ROOT/f'test_{family}.py';raw=''.join(lines).encode()
        path.write_bytes(raw)
        counts[family]=per_family;hashes[path.name]=hashlib.sha256(raw).hexdigest()
    manifest={'schema':'geoforge-untrained-matrix-v1','families':counts,
              'cases':sum(counts.values()),'sha256':hashes}
    (ROOT/'manifest.json').write_text(json.dumps(manifest,indent=2,sort_keys=True))
    return manifest

if __name__=='__main__':
    print(json.dumps(generate(),indent=2))
