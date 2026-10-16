"""Training-free, bounded auxiliary search using the genuine public AG2 DDAR.

Only exact rational midpoint/intersection/foot constructions are proposed. The
underlying DDAR deduces consequences; failed search does not refute the goal.
This is not the original neural/SKEST AlphaGeometry 2 search.
"""
from __future__ import annotations
from dataclasses import dataclass,asdict
from fractions import Fraction
from itertools import combinations
import argparse,json,re,time
from pathlib import Path
from geoforge_prover.ddar2_reference import prove_with_reference

_POINT_RE=re.compile(r'([A-Za-z][A-Za-z0-9]*)@([-+0-9.eE]+)_([-+0-9.eE]+)')

@dataclass(frozen=True)
class Auxiliary:
    name:str
    kind:str
    x:Fraction
    y:Fraction
    predicates:tuple[str,...]
    def statement(self):
        return f'{self.name}@{float(self.x):.17g}_{float(self.y):.17g} = '+', '.join(self.predicates)

@dataclass(frozen=True)
class SearchOutcome:
    status:str
    attempts:int
    auxiliary:tuple[str,...]=()
    tested:tuple[tuple[str,str],...]=()

def extract_coordinates(problem):
    if '?' not in problem:raise ValueError('AG2 problem requires ? goal')
    before,_=problem.split('?',1)
    pts={}
    for m in _POINT_RE.finditer(before):
        name=m.group(1)
        if name in pts:raise ValueError('duplicate point definition: '+name)
        pts[name]=(Fraction(m.group(2)),Fraction(m.group(3)))
    if len(pts)<3:raise ValueError('three coordinate points required')
    return pts

def _sub(a,b):
    return a[0]-b[0],a[1]-b[1]

def _det(a,b):
    return a[0]*b[1]-a[1]*b[0]

def candidate_auxiliaries(points,*,limit=100,kinds=('midpoint','intersection','foot')):
    if limit<0:raise ValueError('negative limit')
    if not limit:return
    names=sorted(points)
    pts={name:tuple(map(Fraction,points[name])) for name in names}
    existing=set(pts.values())
    used=set(names)
    dedup=set()
    i=0
    emitted=0
    def offer(kind,xy,preds):
        nonlocal i,emitted
        if xy in existing or max(abs(xy[0]),abs(xy[1]))>10000000:return None
        sig=(xy,preds)
        if sig in dedup:return None
        dedup.add(sig)
        while 'aux'+str(i) in used:i+=1
        name='aux'+str(i);i+=1;used.add(name)
        emitted+=1
        return Auxiliary(name,kind,*xy,tuple(p.replace('OUT',name) for p in preds))
    if 'midpoint' in kinds:
        for a,b in combinations(names,2):
            xy=((pts[a][0]+pts[b][0])/2,(pts[a][1]+pts[b][1])/2)
            item=offer('midpoint',xy,(f'midp OUT {a} {b}',))
            if item:yield item
            if emitted>=limit:return
    if 'intersection' in kinds:
        for (a,b),(c,d) in combinations(combinations(names,2),2):
            if len({a,b,c,d})<4:continue
            p,q,r,s=pts[a],pts[b],pts[c],pts[d]
            u,v=_sub(q,p),_sub(s,r)
            den=_det(u,v)
            if not den:continue
            t=_det(_sub(r,p),v)/den
            xy=(p[0]+t*u[0],p[1]+t*u[1])
            item=offer('intersection',xy,(f'coll OUT {a} {b}',f'coll OUT {c} {d}'))
            if item:yield item
            if emitted>=limit:return
    if 'foot' in kinds:
        for a,b in combinations(names,2):
            p,q=pts[a],pts[b]
            v=_sub(q,p);norm=v[0]**2+v[1]**2
            if not norm:continue
            for c in names:
                if c in (a,b):continue
                w=_sub(pts[c],p)
                t=(w[0]*v[0]+w[1]*v[1])/norm
                xy=(p[0]+t*v[0],p[1]+t*v[1])
                if xy==pts[c]:continue
                item=offer('foot',xy,(f'coll OUT {a} {b}',f'perp {c} OUT {a} {b}'))
                if item:yield item
                if emitted>=limit:return

def append_auxiliary(problem,aux):
    before,goal=problem.rsplit('?',1)
    if not goal.strip():raise ValueError('missing goal')
    return before.rstrip(' ;')+' ; '+aux.statement()+' ? '+goal.strip()

def search(problem,*,max_candidates=60,seconds=60.,per_candidate=8.,
           kinds=('midpoint','intersection','foot')):
    if seconds<=0 or per_candidate<=0:raise ValueError('positive time limits required')
    if max_candidates<0:raise ValueError('negative candidate limit')
    coords=extract_coordinates(problem)
    deadline=time.monotonic()+seconds
    first=prove_with_reference(problem,timeout=min(per_candidate,seconds))
    if first.result=='deduced':return SearchOutcome('deduced_without_aux',0)
    if first.result not in ('unknown','timeout'):
        return SearchOutcome('reference_'+first.result,0)
    tested=[]
    for candidate in candidate_auxiliaries(coords,limit=max_candidates,kinds=kinds):
        remaining=deadline-time.monotonic()
        if remaining<=0:return SearchOutcome('timeout',len(tested),tested=tuple(tested))
        result=prove_with_reference(append_auxiliary(problem,candidate),
                                    timeout=min(per_candidate,remaining))
        tested.append((candidate.kind,result.result))
        if result.result=='deduced':
            return SearchOutcome('deduced_with_aux',len(tested),
                                 auxiliary=(candidate.statement(),),tested=tuple(tested))
    return SearchOutcome('unknown',len(tested),tested=tuple(tested))

def main(argv=None):
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--file',required=True)
    ap.add_argument('--max-candidates',type=int,default=60)
    ap.add_argument('--seconds',type=float,default=60.)
    ap.add_argument('--per-candidate',type=float,default=8.)
    ns=ap.parse_args(argv)
    result=search(Path(ns.file).read_text(encoding='utf8'),max_candidates=ns.max_candidates,
                  seconds=ns.seconds,per_candidate=ns.per_candidate)
    print(json.dumps(asdict(result),indent=2))
    return 0 if result.status.startswith('deduced') else 2

if __name__=='__main__':
    raise SystemExit(main())
