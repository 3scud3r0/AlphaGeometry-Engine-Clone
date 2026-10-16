#!/usr/bin/env python3
"""∇ GEOFORGE — gerador/filtro/treino estilo AlphaGeometry em UM arquivo (stdlib + NumPy).

Destino sugerido no Nabla: src/nablamath/geometry/geoforge.py  (ou tools/geoforge.py)
Pipeline:  gen  -> dedupe -> tokenize -> train -> eval          (cada fase é um subcomando)
  gen       constrói diagramas aleatórios (construções com coordenadas reais), fecha dedutivamente
            (DD: regras + AR: álgebra linear exata em GF(p)), escolhe metas derivadas, rastreia a
            prova, separa o que é ENUNCIADO (ancestrais da meta) do que é CONSTRUÇÃO AUXILIAR
            (pontos usados na prova fora dos ancestrais = "dependency difference" do paper).
  dedupe    particiona por hash (buckets) -> dedupe exato por bucket -> quotas de equilíbrio.
  tokenize  vocabulário fechado (~150 tokens) -> shards uint16 (compatível com memmap/nanoGPT).
  train     transformer decoder-only em NumPy com backprop manual (gradiente verificado).
  eval      solve@K: DD+AR puro vs aux aleatória vs aux proposta pelo LM (busca em feixe restrita).
  selftest  teoremas conhecidos, solidez numérica, gradcheck, dedupe, e2e minúsculo.
  bench     mede vazão real e projeta o custo de 100M/300M problemas (sem prometer o que não mede).

RÉGUA EXTERNA (medida, `agbench`, 1 núcleo, ≤20s/problema, 25 diagramas aleatórios por problema):
  IMO-AG-30   : 4/30 resolvidos (18 expressáveis; 12 usam construções não suportadas)   | DDAR do paper: 14/30 | AlphaGeometry: 25/30
  JGEX-AG-231 : 103/231 resolvidos (164 expressáveis; 67 não suportados)                 | DDAR do paper: 198/231
  Solidez: 0 fatos derivados falsos em ~15 mil fatos nos diagramas do benchmark. Estamos ABAIXO do DDAR original: faltam regras/construções.
HONESTIDADE: Python puro não gera "centenas de milhões" num laptop. O arquivo é escalável por
construção (shards determinísticos, retomável, buckets por hash), mas a vazão é MEDIDA, não presumida.
O paper usou ~100k CPUs. O motor é um subconjunto do DDAR (≈18 regras + AR de ângulos/razões),
NÃO reproduz os 43 teoremas do original; toda meta é verificada numericamente no diagrama.
"""
from __future__ import annotations
import argparse, gzip, hashlib, io, itertools, json, math, os, random, re, struct, sys, time
from fractions import Fraction
from pathlib import Path

# ═══════════════════════════ neon ═══════════════════════════
_COL = sys.stdout.isatty() and not os.environ.get("NO_COLOR")
def _c(rgb, s, b=False): return f"\x1b[{'1;' if b else ''}38;2;{rgb[0]};{rgb[1]};{rgb[2]}m{s}\x1b[0m" if _COL else str(s)
CY, MG, AM, LM = (0, 255, 255), (255, 0, 255), (255, 191, 0), (57, 255, 20)
def log(tag, msg, col=CY): print(_c(col, f"[{tag}]", True), msg, flush=True)

# ═══════════════════════════ estatísticas canônicas ═══════════════════════════
LET = "abcdefghijklmnopqrstuvwxyz"
def L2(a, b): return (a, b) if a <= b else (b, a)
def _orbit_min(t):  # (x1,x2,x3,x4) ~ x1-x2 = x3-x4 ; grupo de ordem 8
    seen, st = {t}, [t]
    while st:
        a, b, c, d = st.pop()
        for u in ((c, d, a, b), (a, c, b, d), (b, a, d, c)):
            if u not in seen: seen.add(u); st.append(u)
    return min(seen)
def mk_coll(a, b, c): return ("coll",) + tuple(sorted((a, b, c)))
def mk_para(a, b, c, d): x, y = sorted((L2(a, b), L2(c, d))); return ("para", *x, *y)
def mk_perp(a, b, c, d): x, y = sorted((L2(a, b), L2(c, d))); return ("perp", *x, *y)
def mk_cong(a, b, c, d): x, y = sorted((L2(a, b), L2(c, d))); return ("cong", *x, *y)
def mk_cyc(a, b, c, d): return ("cyclic",) + tuple(sorted((a, b, c, d)))
def mk_midp(m, a, b): return ("midp", m) + L2(a, b)
def mk_eqang(a, b, c, d, e, f, g, h):
    t = _orbit_min((L2(a, b), L2(c, d), L2(e, f), L2(g, h))); return ("eqangle",) + tuple(p for l in t for p in l)
def mk_eqrat(a, b, c, d, e, f, g, h):
    t = _orbit_min((L2(a, b), L2(c, d), L2(e, f), L2(g, h))); return ("eqratio",) + tuple(p for l in t for p in l)
def mk_simtri(a, b, c, p, q, r):
    pr = sorted([(a, p), (b, q), (c, r)]); u = tuple(x for x, _ in pr), tuple(y for _, y in pr)
    v = tuple(sorted([(p, a), (q, b), (r, c)])); v = (tuple(x for x, _ in v), tuple(y for _, y in v))
    s = min(u, v); return ("simtri",) + s[0] + s[1]
ARITY = {"coll": 3, "para": 4, "perp": 4, "cong": 4, "cyclic": 4, "midp": 3, "eqangle": 8, "eqratio": 8, "simtri": 6}
MK = {"coll": mk_coll, "para": mk_para, "perp": mk_perp, "cong": mk_cong, "cyclic": mk_cyc, "midp": mk_midp, "eqangle": mk_eqang, "eqratio": mk_eqrat, "simtri": mk_simtri}
def canon(s): return MK[s[0]](*s[1:])
def spts(s): return set(s[1:])
def stxt(s): return " ".join(s)

# ═══════════════════════════ geometria numérica ═══════════════════════════
def sub(p, q): return (p[0] - q[0], p[1] - q[1])
def dist(p, q): return math.hypot(p[0] - q[0], p[1] - q[1])
def cross(u, v): return u[0] * v[1] - u[1] * v[0]
def dot(u, v): return u[0] * v[0] + u[1] * v[1]
def area2(a, b, c): return cross(sub(b, a), sub(c, a))
def lerp(a, b, t): return (a[0] + t * (b[0] - a[0]), a[1] + t * (b[1] - a[1]))
def _foot(a, b, c):
    d = sub(c, b); n = dot(d, d)
    return None if n < 1e-12 else lerp(b, c, dot(sub(a, b), d) / n)
def _inter(a, b, c, d):
    u, v = sub(b, a), sub(d, c); den = cross(u, v)
    if abs(den) < 1e-9 * (dist(a, b) * dist(c, d) + 1e-12): return None
    t = cross(sub(c, a), v) / den; return (a[0] + t * u[0], a[1] + t * u[1])
def _circum(a, b, c):
    d = 2 * area2(a, b, c)
    if abs(d) < 1e-9: return None
    ax, ay, bx, by, cx, cy = *a, *b, *c; a2, b2, c2 = ax * ax + ay * ay, bx * bx + by * by, cx * cx + cy * cy
    return ((a2 * (by - cy) + b2 * (cy - ay) + c2 * (ay - by)) / d, (a2 * (cx - bx) + b2 * (ax - cx) + c2 * (bx - ax)) / d)
def _orth(a, b, c):
    x = _foot(a, b, c); y = _foot(b, a, c)
    return None if x is None or y is None else _inter(a, x, b, y)
def _perp(v): return (-v[1], v[0])
def _rt(rng, lo, hi):
    t = rng.uniform(lo, hi); return t if rng.random() < .5 else -t

# nome: (nargs, realize(coords, rng)->pt|None, facts(x,args)->[stmts], simétrico: grupos de args ordenáveis)
def _r_midp(P, r): return lerp(P[0], P[1], .5)
def _r_foot(P, r): return _foot(P[0], P[1], P[2])
def _r_onl(P, r): return lerp(P[0], P[1], r.choice((-1, 1)) * r.uniform(.2, 1.6) + (0 if r.random() < .5 else 1))
def _r_pline(P, r): d = sub(P[2], P[1]); t = _rt(r, .3, 1.8); return (P[0][0] + t * d[0], P[0][1] + t * d[1])
def _r_tline(P, r): d = _perp(sub(P[2], P[1])); t = _rt(r, .3, 1.8); return (P[0][0] + t * d[0], P[0][1] + t * d[1])
def _r_circ(P, r): return _circum(*P)
def _r_onc(P, r): R = dist(P[0], P[1]); th = r.uniform(0, 2 * math.pi); return (P[0][0] + R * math.cos(th), P[0][1] + R * math.sin(th))
def _r_bis(P, r): m = lerp(P[0], P[1], .5); d = _perp(sub(P[1], P[0])); t = _rt(r, .2, 1.5); return (m[0] + t * d[0], m[1] + t * d[1])
def _r_inter(P, r): return _inter(*P)
def _r_refl(P, r): return (2 * P[1][0] - P[0][0], 2 * P[1][1] - P[0][1])
def _r_par(P, r): return (P[0][0] + P[2][0] - P[1][0], P[0][1] + P[2][1] - P[1][1])
def _r_orth(P, r): return _orth(*P)
CONS = {
    "midp": (2, _r_midp, lambda x, a: [mk_midp(x, a[0], a[1])], ((0, 1),)),
    "foot": (3, _r_foot, lambda x, a: [mk_coll(x, a[1], a[2]), mk_perp(a[0], x, a[1], a[2])], ((1, 2),)),
    "onl": (2, _r_onl, lambda x, a: [mk_coll(x, a[0], a[1])], ((0, 1),)),
    "pline": (3, _r_pline, lambda x, a: [mk_para(a[0], x, a[1], a[2])], ((1, 2),)),
    "tline": (3, _r_tline, lambda x, a: [mk_perp(a[0], x, a[1], a[2])], ((1, 2),)),
    "circ": (3, _r_circ, lambda x, a: [mk_cong(x, a[0], x, a[1]), mk_cong(x, a[1], x, a[2])], ((0, 1, 2),)),
    "onc": (2, _r_onc, lambda x, a: [mk_cong(a[0], x, a[0], a[1])], ()),
    "bis": (2, _r_bis, lambda x, a: [mk_cong(x, a[0], x, a[1])], ((0, 1),)),
    "inter": (4, _r_inter, lambda x, a: [mk_coll(x, a[0], a[1]), mk_coll(x, a[2], a[3])], ()),
    "refl": (2, _r_refl, lambda x, a: [mk_midp(a[1], a[0], x)], ()),
    "parall": (3, _r_par, lambda x, a: [mk_para(a[0], a[1], a[2], x), mk_para(a[1], a[2], x, a[0])], ()),
    "orth": (3, _r_orth, lambda x, a: [mk_perp(a[0], x, a[1], a[2]), mk_perp(a[1], x, a[0], a[2])], ((0, 1, 2),)),
}
CONS_W = {"midp": 5, "foot": 4, "onl": 2, "pline": 3, "tline": 3, "circ": 3, "onc": 3, "bis": 2, "inter": 3, "refl": 2, "parall": 2, "orth": 2}
def norm_args(name, args):  # canonicaliza argumentos simétricos (dedupe e determinismo)
    a = list(args)
    for g in CONS[name][3]:
        s = sorted(a[i] for i in g)
        for i, v in zip(g, s): a[i] = v
    if name == "inter":
        l1, l2 = sorted((L2(a[0], a[1]), L2(a[2], a[3]))); a = [*l1, *l2]
    return a

def num_check(s, C, eps=1e-6):
    """A afirmação vale no diagrama numérico? (guarda de solidez de todo passo de prova)"""
    t, p = s[0], s[1:]; P = [C[x] for x in p]
    sc = max(1.0, max(abs(v) for q in P for v in q))
    def ang(u, v): return math.atan2(cross(u, v), dot(u, v))
    def dirs(i): return sub(P[i + 1], P[i])
    if t == "coll": return abs(area2(*P)) < eps * sc * sc
    if t == "para": return abs(cross(dirs(0), dirs(2))) < eps * sc * sc
    if t == "perp": return abs(dot(dirs(0), dirs(2))) < eps * sc * sc
    if t == "cong": return abs(dist(P[0], P[1]) - dist(P[2], P[3])) < eps * sc
    if t == "midp": return dist(lerp(P[1], P[2], .5), P[0]) < eps * sc
    if t == "cyclic":
        o = _circum(P[0], P[1], P[2]); return o is not None and abs(dist(o, P[3]) - dist(o, P[0])) < eps * sc * 10
    if t == "eqangle":
        d = lambda i: sub(P[2 * i + 1], P[2 * i]); a1, a2 = ang(d(0), d(1)), ang(d(2), d(3)); x = (a1 - a2) % math.pi
        return min(x, math.pi - x) < eps * 10
    if t == "eqratio":
        n = lambda i: dist(P[2 * i], P[2 * i + 1]); return abs(n(0) * n(3) - n(1) * n(2)) < eps * sc * sc * 10
    if t == "simtri":
        a, b, c, q, r, s2 = P; k = [dist(a, b) / max(dist(q, r), 1e-12), dist(a, c) / max(dist(q, s2), 1e-12), dist(b, c) / max(dist(r, s2), 1e-12)]
        return max(k) - min(k) < eps * 10 * max(k)
    return False

# ═══════════════════════════ álgebra linear exata em GF(p) com proveniência ═══════════════════════════
PR = 2147483647
class LinSys:
    """Forma escalonada reduzida esparsa; cada linha carrega uma máscara de fatos-fonte (bitset em int)."""
    def __init__(s, unit=False): s.rows = {}; s.unit = unit   # unit: só pivôs ±1 => combinações INTEIRAS (válido mod π)
    def reduce(s, vec, mask=0):
        v = dict(vec)
        for p in [k for k in v if k in s.rows]:
            c = v.get(p)
            if not c: continue
            r, m = s.rows[p]; mask |= m
            for k, x in r.items():
                nv = (v.get(k, 0) - c * x) % PR
                if nv: v[k] = nv
                else: v.pop(k, None)
        return v, mask
    def add(s, vec, mask, free=()):
        v, m = s.reduce(vec, mask); cand = [k for k in v if k not in free and (not s.unit or v[k] in (1, PR - 1))]
        if not cand: return False
        p = min(cand); ci = pow(v[p], PR - 2, PR); v = {k: x * ci % PR for k, x in v.items()}
        for q, (r, mm) in list(s.rows.items()):
            f = r.get(p)
            if f:
                nr = dict(r)
                for k, x in v.items():
                    nv = (nr.get(k, 0) - f * x) % PR
                    if nv: nr[k] = nv
                    else: nr.pop(k, None)
                s.rows[q] = (nr, mm | m)
        s.rows[p] = (v, m); return True

def _sg(x): return x if x < PR // 2 else x - PR
class VarIdx:
    def __init__(s): s.d = {}
    def __call__(s, a, b):
        k = L2(a, b)
        if k not in s.d: s.d[k] = len(s.d) + 1
        return s.d[k]

def stmt_rows(s, vi):
    """Linhas lineares de um fato. ('a', {var:coef}) ângulos (var 0 = K = π/2) | ('l', ...) log-comprimentos."""
    t, p = s[0], s[1:]; out = []
    D = lambda a, b: vi(a, b)
    if t == "coll":
        a, b, c = p; out += [("a", {D(a, b): 1, D(a, c): PR - 1}), ("a", {D(a, b): 1, D(b, c): PR - 1})]
    elif t == "para": out.append(("a", {D(p[0], p[1]): 1, D(p[2], p[3]): PR - 1}))
    elif t == "perp": out.append(("a", {D(p[0], p[1]): 1, D(p[2], p[3]): PR - 1, 0: PR - 1}))
    elif t == "cong": out.append(("l", {D(p[0], p[1]): 1, D(p[2], p[3]): PR - 1}))
    elif t == "midp": out.append(("l", {D(p[0], p[1]): 1, D(p[0], p[2]): PR - 1}))
    elif t == "eqangle": out.append(("a", _comb4([D(p[0], p[1]), D(p[2], p[3]), D(p[4], p[5]), D(p[6], p[7])])))
    elif t == "eqratio": out.append(("l", _comb4([D(p[0], p[1]), D(p[2], p[3]), D(p[4], p[5]), D(p[6], p[7])])))
    elif t == "cyclic":
        a, b, c, d = p
        for x, y, u, v in ((a, b, c, d), (a, c, b, d), (a, d, b, c)):  # corda xy: ∠(u x,u y)=∠(v x,v y)
            out.append(("a", _comb4([D(u, x), D(u, y), D(v, x), D(v, y)])))
    elif t == "simtri":
        a, b, c, q, r, w = p
        out.append(("l", _comb4([D(a, b), D(q, r), D(a, c), D(q, w)]))); out.append(("l", _comb4([D(a, b), D(q, r), D(b, c), D(r, w)])))
    return out
def _comb4(v):
    d = {}
    for i, sg in zip(v, (1, -1, -1, 1)): d[i] = (d.get(i, 0) + sg) % PR
    return {k: x for k, x in d.items() if x}

# ═══════════════════════════ motor dedutivo: DD (regras) + AR (álgebra) ═══════════════════════════
def _kp(v):  # (chave sem K, paridade|None) a partir do vetor reduzido de ângulos
    v = dict(v); k = _sg(v.pop(0, 0)); return tuple(sorted(v.items())), (k % 2 if abs(k) < 10000 else None)
def _prove(st, A, Ln, vi):
    """(ok, mask) se o sistema linear A/Ln implica st (ângulos: resíduo ∈ {c·K, c par}; razões: resíduo nulo)."""
    rows = stmt_rows(st, vi)
    if not rows or st[0] in ("coll", "cyclic", "simtri", "midp"): return False, 0
    mask = 0
    for kind, r in rows:
        v, m = (A if kind == "a" else Ln).reduce(r); mask |= m
        if kind == "a":
            if any(k != 0 for k in v) or (v.get(0, 0) and (abs(_sg(v[0])) >= 10000 or _sg(v[0]) % 2)): return False, 0
        elif v: return False, 0
    return True, mask

class Closure:
    def __init__(s, coords, givens, maxfacts=700, deadline=None):
        s.C = coords; s.pts = sorted(coords); s.maxf = maxfacts; s.deadline = deadline
        s.facts, s.fl, s.fi = {}, [], {}; s.vi = VarIdx(); s.A, s.Ln = LinSys(unit=True), LinSys()
        s.graph = GeometryGraph()  # índice simbólico paralelo, sem usar coordenadas como axiomas
        s.lines, s.circles, s.given, s._sta = [], [], set(), set(); s.pairs = list(itertools.combinations(s.pts, 2)); s.dk, s.lk = {}, {}
        for g in givens: s.add(g, "given", ())
    # ── estrutura ──
    def add(s, st, rule, par):
        if st in s.facts or len(s.facts) >= s.maxf: return False
        # Filtro de integridade numérica (NÃO é certificado formal).
        # Rejeita fatos derivados inválidos ou degenerados no diagrama.
        if not num_check(st, s.C): return False
        i = len(s.fl); s.facts[st] = (rule, tuple(par)); s.fl.append(st); s.fi[st] = i
        s.graph.add_fact(GeoFact.from_tuple(st),tuple(GeoFact.from_tuple(x) for x in par))
        if rule == "given": s.given.add(st)
        m = 1 << i
        for kind, r in stmt_rows(st, s.vi): (s.A if kind == "a" else s.Ln).add(r, m, free=(0,))
        t = st[0]
        if t == "coll" and rule != "coll_merge": s._merge(st, s.lines, 2, "coll_merge", lambda p: mk_coll(*p), 3)
        elif t == "cyclic" and rule != "cyclic_merge": s._merge(st, s.circles, 3, "cyclic_merge", lambda p: mk_cyc(*p), 4, cap=7)
        elif t == "midp": s.add(mk_coll(st[1], st[2], st[3]), "midp_coll", (st,))
        return True
    def _merge(s, st, store, share, rule, mk, k, cap=9):
        S = set(st[1:]); src = {st}
        while True:
            hit = [e for e in store if len(e[0] & S) >= share]
            if not hit: break
            for e in hit: S |= e[0]; src |= e[1]; store.remove(e)
        store.append((S, src))
        if len(S) <= cap:
            ps = tuple(sorted(src, key=lambda x: s.fi[x]))
            for sub_ in itertools.combinations(sorted(S), k):
                s.add(mk(sub_), rule, ps)
    def parents(s, mask): return tuple(s.fl[i] for i in range(mask.bit_length()) if mask >> i & 1)
    def ensure(s, st, rule=None):
        if st in s.facts: return True
        if st[0] not in ("para", "perp", "cong", "eqangle", "eqratio"): return False
        ok, m = _prove(st, s.A, s.Ln, s.vi)
        if not ok: return False
        return s.add(st, rule or ("ar_len" if st[0] in ("cong", "eqratio") else "ar_ang"), s.parents(m)) or st in s.facts
    def refresh(s):
        s.dv = {}; s.lv = {}
        for p in s.pairs:
            i = s.vi(*p); v, _ = s.A.reduce({i: 1}); s.dv[p] = v; s.dk[p] = _kp(v); v, _ = s.Ln.reduce({i: 1}); s.lv[p] = v; s.lk[p] = tuple(sorted(v.items()))
    def lsig(s, p, q):
        v = dict(s.lv[p])
        for k, x in s.lv[q].items():
            nv = (v.get(k, 0) - x) % PR
            if nv: v[k] = nv
            else: v.pop(k, None)
        return tuple(sorted(v.items()))
    def comb(s, ps, sg=(1, -1, -1, 1)):
        v = {}
        for p, g in zip(ps, sg):
            for k, x in s.dv[p].items():
                nv = (v.get(k, 0) + g * x) % PR
                if nv: v[k] = nv
                else: v.pop(k, None)
        return v
    def dsig(s, p, q): return _kp(s.comb((p, q), (1, -1)))
    def angeq0(s, ps):  # a combinação 1,-1,-1,1 dos pares é nula (mod π)?
        v = s.comb(ps); k = v.pop(0, 0)
        return not v and abs(_sg(k)) < 10000 and _sg(k) % 2 == 0
    def rel(s, a, b, c, d):
        x, y = s.dk[L2(a, b)], s.dk[L2(c, d)]
        if x[1] is None or y[1] is None or x[0] != y[0]: return None
        return "para" if x[1] == y[1] else "perp"
    def col(s, a, b, c): return mk_coll(a, b, c) in s.facts
    def ndeg(s, a, b, c): return abs(area2(s.C[a], s.C[b], s.C[c])) > 1e-6
    def eqd(s, m, a, b): return s.lk[L2(m, a)] == s.lk[L2(m, b)]
    # ── regras ──
    def r_ar_dir(s):
        n = 0; g = {}
        for p in s.pairs:
            k, par = s.dk[p]
            if par is not None and k: g.setdefault(k, []).append((p, par))
        for k, mem in g.items():
            ln = {}
            for p, par in mem:
                lid = next((frozenset(S) for S, _ in s.lines if p[0] in S and p[1] in S), frozenset(p))
                ln.setdefault(lid, (p, par))
            reps = list(ln.values())[:12]
            for (p1, a1), (p2, a2) in itertools.combinations(reps, 2):
                sh = set(p1) & set(p2)
                if len(sh) == 1 and a1 == a2:
                    x = (set(p1) | set(p2)); st = mk_coll(*x)
                    if st not in s.facts:
                        pa = mk_para(*p1, *p2)
                        if s.ensure(pa, "ar_ang") and s.add(st, "para_shared_coll", (pa,)): n += 1
                    continue
                if sh: continue
                st = mk_para(*p1, *p2) if a1 == a2 else mk_perp(*p1, *p2)
                n += s.ensure(st) and st not in s.given
        return n
    def r_ar_len(s):
        n = 0; g = {}
        for p in s.pairs: g.setdefault(s.lk[p], []).append(p)
        for k, mem in g.items():
            if not k or len(mem) < 2: continue
            for p1, p2 in itertools.combinations(mem[:8], 2):
                st = mk_cong(*p1, *p2)
                if st not in s.facts: n += s.ensure(st)
        return n
    def r_midp(s):
        n = 0
        for S, _ in list(s.lines):
            if len(S) < 3: continue
            for m in sorted(S):
                for a, b in itertools.combinations(sorted(S - {m}), 2):
                    if s.eqd(m, a, b):
                        st = mk_midp(m, a, b)
                        if st not in s.facts:
                            cg = mk_cong(m, a, m, b)
                            if s.ensure(cg): n += s.add(st, "coll_cong_midp", (mk_coll(m, a, b), cg))
        return n
    def _mids(s): return [x for x in s.fl if x[0] == "midp"]
    def r_midline(s):
        n = 0; M = s._mids()
        for u, v in itertools.combinations(M, 2):
            e1, e2 = set(u[2:]), set(v[2:]); sh = e1 & e2
            if len(sh) != 1 or u[1] == v[1]: continue
            a = next(iter(sh)); b = next(iter(e1 - sh)); c = next(iter(e2 - sh))
            if s.ndeg(a, b, c): n += s.add(mk_para(u[1], v[1], b, c), "midline", (u, v))
        return n
    def r_para(s):
        n = 0; M = s._mids()
        for u, v in itertools.combinations(M, 2):
            if u[1] != v[1] or set(u[2:]) & set(v[2:]): continue
            a, c = u[2:]; b, d = v[2:]
            if not s.ndeg(a, b, c): continue
            for st in (mk_para(a, b, c, d), mk_para(b, c, d, a), mk_cong(a, b, c, d), mk_cong(b, c, d, a)): n += s.add(st, "parallelogram", (u, v))
        return n
    def r_perpbis(s):
        n = 0; E = {}
        for a, b in s.pairs: E[(a, b)] = [m for m in s.pts if m != a and m != b and s.eqd(m, a, b)]
        for (a, b), ms in E.items():
            for m, k in itertools.combinations(ms, 2):
                st = mk_perp(a, b, m, k)
                if st not in s.facts and s.ensure(mk_cong(m, a, m, b)) and s.ensure(mk_cong(k, a, k, b)): n += s.add(st, "perp_bisector", (mk_cong(m, a, m, b), mk_cong(k, a, k, b)))
            for m in ms:
                for k in s.pts:
                    if k in (a, b, m) or k in ms or s.rel(a, b, m, k) != "perp": continue
                    st = mk_cong(k, a, k, b); pp = mk_perp(a, b, m, k)
                    if st not in s.facts and s.ensure(pp) and s.ensure(mk_cong(m, a, m, b)): n += s.add(st, "perp_bisector_conv", (pp, mk_cong(m, a, m, b)))
        return n
    def r_circle(s):
        n = 0
        for m in s.pts:
            g = {}
            for x in s.pts:
                if x != m: g.setdefault(s.lk[L2(m, x)], []).append(x)
            for k, mem in g.items():
                if len(mem) < 4: continue
                for q in itertools.combinations(mem[:7], 4):
                    st = mk_cyc(*q)
                    if st in s.facts: continue
                    ps = tuple(mk_cong(m, q[0], m, y) for y in q[1:])
                    if all(s.ensure(p) for p in ps): n += s.add(st, "circle_center", ps)
        return n
    def r_cycang(s):
        n = 0
        for a, b in s.pairs:
            g = {}
            for c in s.pts:
                if c in (a, b) or s.col(a, b, c) or not s.ndeg(a, b, c): continue
                k, par = s.dsig(L2(c, a), L2(c, b))
                if par is not None: g.setdefault((k, par), []).append(c)
            for mem in g.values():
                for c, d in itertools.combinations(mem[:6], 2):
                    st = mk_cyc(a, b, c, d)
                    if st in s.facts: continue
                    ea = mk_eqang(c, a, c, b, d, a, d, b)
                    if s.ensure(ea): n += s.add(st, "eqangle_cyclic", (ea,))
        return n
    def r_iso(s):
        n = 0
        for a in s.pts:
            g = {}
            for x in s.pts:
                if x != a: g.setdefault(s.lk[L2(a, x)], []).append(x)
            for mem in g.values():
                for b, c in itertools.combinations(mem[:6], 2):
                    if s.col(a, b, c): continue
                    ea = mk_eqang(b, a, b, c, c, b, c, a); cg = mk_cong(a, b, a, c)
                    if ea not in s.facts and cg in s.facts: n += s.add(ea, "iso_base", (cg,))
        for a in s.pts:
            for b, c in itertools.combinations([x for x in s.pts if x != a], 2):
                cg = mk_cong(a, b, a, c)
                if cg in s.facts or s.col(a, b, c) or not s.ndeg(a, b, c): continue
                if not s.angeq0((L2(b, a), L2(b, c), L2(c, b), L2(c, a))): continue
                ea = mk_eqang(b, a, b, c, c, b, c, a)
                if s.ensure(ea): n += s.add(cg, "iso_conv", (ea,))
        return n
    def r_thales(s):
        n = 0
        for u in s._mids():
            o, a, c = u[1:]
            for b in s.pts:
                if b in (o, a, c): continue
                pp = mk_perp(a, b, b, c); cg = mk_cong(o, b, o, a)
                if cg not in s.facts and s.rel(a, b, b, c) == "perp" and s.ndeg(a, b, c) and s.ensure(pp): n += s.add(cg, "thales", (u, pp))
                if pp not in s.facts and s.eqd(o, b, a) and s.ndeg(a, b, c) and s.ensure(cg): n += s.add(pp, "thales_conv", (u, cg))
        return n
    def r_simtri(s, cap=30):
        n = 0; key = {}; tri = [t for q in itertools.combinations(s.pts, 3) if s.ndeg(*q) for t in itertools.permutations(q)]
        def sg(a, b, c): return s.dsig(L2(a, b), L2(a, c))
        for t in tri:
            a, b, c = t; x, y = sg(a, b, c), sg(b, a, c)
            if x and y and x[1] is not None and y[1] is not None: key.setdefault((x, y), []).append(t)
        neg = lambda z: (tuple((i, (-w) % PR) for i, w in z[0]), None if z[1] is None else (-z[1]) % 2)
        for t in tri:
            if not (t[0] < t[1] < t[2]): continue
            x, y = sg(t[0], t[1], t[2]), sg(t[1], t[0], t[2])
            if not (x and y and x[1] is not None and y[1] is not None): continue
            for mir, kk in ((0, (x, y)), (1, (neg(x), neg(y)))):
                for u in key.get(kk, ()):
                    if set(u) == set(t): continue
                    a, b, c = t; p, q, r = u
                    e1 = mk_eqang(a, b, a, c, *( (p, q, p, r) if not mir else (p, r, p, q)))
                    e2 = mk_eqang(b, a, b, c, *( (q, p, q, r) if not mir else (q, r, q, p)))
                    st = mk_simtri(a, b, c, p, q, r)
                    if st in s.facts: continue
                    if s.ensure(e1) and s.ensure(e2): n += s.add(st, "aa_simtri", (e1, e2))
                    if n >= cap: return n
        return n
    def r_simtri_ss(s, cap=30):
        """Semelhança SSS via razões no sistema de comprimentos. (SAS NÃO: ângulo dirigido mod π não fixa o raio => falso positivo, achado pela auditoria.)"""
        n = 0; trip = [t for q in itertools.combinations(s.pts, 3) if s.ndeg(*q) for t in itertools.permutations(q)]; K1, K2 = {}, {}
        ang = lambda a, b, c: s.dsig(L2(a, b), L2(a, c))
        for a, b, c in trip:
            K1.setdefault((s.lsig(L2(a, b), L2(a, c)), s.lsig(L2(a, b), L2(b, c))), []).append((a, b, c))
        neg = lambda z: (tuple((i, (-w) % PR) for i, w in z[0]), None if z[1] is None else (-z[1]) % 2)
        for a, b, c in trip:
            if not (a < b < c): continue
            cands = [(u, "sss", None) for u in K1.get((s.lsig(L2(a, b), L2(a, c)), s.lsig(L2(a, b), L2(b, c))), ())]
            for u, kind, mir in cands:
                if set(u) == {a, b, c}: continue
                p, q, r = u; st = mk_simtri(a, b, c, p, q, r)
                if st in s.facts: continue
                e1, e2 = mk_eqrat(a, b, a, c, p, q, p, r), mk_eqrat(a, b, b, c, p, q, q, r)
                if s.ensure(e1) and s.ensure(e2): n += s.add(st, "sss_simtri", (e1, e2))
                if n >= cap: return n
        return n
    def r_simtri_ang(s):
        n = 0
        for st in [x for x in s.fl if x[0] == "simtri"]:
            if st in s._sta: continue
            s._sta.add(st); a, b, c, p, q, r = st[1:]
            if abs(area2(*(s.C[x] for x in (a, b, c)))) < 1e-6 or abs(area2(*(s.C[x] for x in (p, q, r)))) < 1e-6: continue
            mir = area2(*(s.C[x] for x in (a, b, c))) * area2(*(s.C[x] for x in (p, q, r))) < 0
            for (u, v, w), (x, y, z) in (((a, b, c), (p, q, r)), ((b, a, c), (q, p, r)), ((c, a, b), (r, p, q))):
                # Semelhança sem orientação NÃO implica igualdade de ângulos
                # dirigidos: somente materialize se o AR já a implicar.
                e = mk_eqang(u, v, u, w, *((x, y, x, z) if not mir else (x, z, x, y)))
                if e not in s.facts: n += int(s.ensure(e, "ar_ang"))
        return n
    def r_tangent(s):
        n = 0
        for o in s.pts:
            g = {}
            for x in s.pts:
                if x != o: g.setdefault(s.lk[L2(o, x)], []).append(x)
            for mem in g.values():
                if len(mem) < 3: continue
                for a in mem[:6]:
                    for x in s.pts:
                        if x in (a, o) or x in mem or s.rel(o, a, a, x) != "perp": continue
                        pp = mk_perp(o, a, a, x)
                        if not s.ensure(pp): continue
                        for b, c in itertools.combinations([y for y in mem[:6] if y != a], 2):
                            ea = mk_eqang(a, x, a, b, c, a, c, b)
                            if ea not in s.facts and s.ndeg(a, b, c):
                                ps = (pp, mk_cong(o, a, o, b), mk_cong(o, a, o, c))
                                if all(s.ensure(q) for q in ps): n += s.add(ea, "tangent_chord", ps)
        return n
    def r_bisect(s):
        n = 0
        for S, _ in list(s.lines):
            for b, c in itertools.combinations(sorted(S), 2):
                for d in S - {b, c}:
                    for a in s.pts:
                        if a in S or not s.ndeg(a, b, c): continue
                        er = mk_eqrat(d, b, d, c, a, b, a, c); ea = mk_eqang(a, b, a, d, a, d, a, c); co = mk_coll(d, b, c)
                        if s.angeq0((L2(a, b), L2(a, d), L2(a, d), L2(a, c))):
                            if er not in s.facts and s.ensure(ea): n += s.add(er, "bisector_thm", (ea, co))
                        elif s.lsig(L2(d, b), L2(d, c)) == s.lsig(L2(a, b), L2(a, c)):
                            if ea not in s.facts and s.ensure(er): n += s.add(ea, "bisector_conv", (er, co))
        return n
    def r_chord(s):
        """Mesma circunferência: ângulos inscritos iguais <=> cordas iguais (rules.txt: cyclic+eqangle => cong)."""
        n = 0
        for S, _ in list(s.circles):
            if len(S) < 5: continue
            pts = sorted(S)[:8]; g = {}
            for a, b in itertools.combinations(pts, 2):
                c = next(x for x in pts if x not in (a, b)); k, par = s.dsig(L2(c, a), L2(c, b))
                if par is not None: g.setdefault((k, par), []).append((a, b, c))
            for mem in g.values():
                for (a, b, c), (p, q, r) in itertools.combinations(mem, 2):
                    cg = mk_cong(a, b, p, q)
                    if cg in s.facts or len({a, b, p, q}) < 3: continue
                    ea = mk_eqang(c, a, c, b, r, p, r, q)
                    if s.ensure(ea):
                        cy = next((x for x in s.fl if x[0] == "cyclic" and {a, b, c} <= set(x[1:]) and set(x[1:]) <= S), None)
                        n += s.add(cg, "chord_angle", (ea,) + ((cy,) if cy else ()))
        return n
    def r_center_angle(s):
        n = 0
        for u in s._mids():
            m, b, c = u[1:]
            for o in s.pts:
                if o in (m, b, c) or not s.eqd(o, b, c): continue
                for a in s.pts:
                    if a in (m, b, c, o) or not s.eqd(o, a, b) or not s.ndeg(a, b, c): continue
                    ea = mk_eqang(a, b, a, c, o, b, o, m)
                    if ea in s.facts: continue
                    ps = tuple(x for x in (u, mk_cong(o, a, o, b), mk_cong(o, b, o, c)) if x == u or s.ensure(x))
                    if len(ps) == 3: n += s.add(ea, "center_angle", ps)
        for S, _ in list(s.lines):
            for b, c in itertools.combinations(sorted(S), 2):
                for m in S - {b, c}:
                    if mk_midp(m, b, c) in s.facts: continue
                    for o in s.pts:
                        if o in S or not s.eqd(o, b, c): continue
                        for a in s.pts:
                            if a in S or a == o or not s.eqd(o, a, b) or not s.ndeg(a, b, c): continue
                            if s.angeq0((L2(a, b), L2(a, c), L2(o, b), L2(o, m))):
                                ea = mk_eqang(a, b, a, c, o, b, o, m); ps = (ea, mk_coll(m, b, c), mk_cong(o, a, o, b), mk_cong(o, b, o, c))
                                if all(x in s.facts or s.ensure(x) for x in ps): n += s.add(mk_midp(m, b, c), "center_angle_conv", ps)
        return n
    RULES = ("r_ar_dir", "r_ar_len", "r_midp", "r_midline", "r_para", "r_perpbis", "r_circle", "r_cycang", "r_iso", "r_thales", "r_simtri", "r_simtri_ss", "r_simtri_ang", "r_tangent", "r_bisect", "r_chord", "r_center_angle")
    def close(s, rounds=5):
        for _ in range(rounds):
            s.refresh(); n = 0
            for r in s.RULES:
                n += getattr(s, r)()
                if len(s.facts) >= s.maxf or (s.deadline and time.time() > s.deadline): return s
            if not n: break
        return s
    def proves(s, g): return g in s.facts or s.ensure(g)
    def export_certificate(s, goal):
        """Exporta prova candidata; use ProofChecker.verify() para certificá-la."""
        return ProofCertificate.from_closure(s,goal)
    def prune(s, st, par):
        cur = list(par)
        def ent(sub_):
            A, Ln = LinSys(unit=True), LinSys()
            for q in sub_:
                for kind, r in stmt_rows(q, s.vi): (A if kind == "a" else Ln).add(r, 0, free=(0,))
            return _prove(st, A, Ln, s.vi)[0]
        for q in list(cur):
            t = [x for x in cur if x != q]
            if ent(t): cur = t
        return tuple(cur)
    def explain(s, goal):
        memo, order = {}, []
        def need(st):
            if st in memo: return
            rule, par = s.facts[st]
            if rule.startswith("ar_"): par = s.prune(st, par)
            memo[st] = (rule, par)
            for q in par: need(q)
            order.append(st)
        need(goal); return [(memo[x][0], memo[x][1], x) for x in order]

# ═══════════════════════════ gerador de problemas ═══════════════════════════
class Cfg:
    min_pts, max_pts, min_steps, max_steps, goals_per_diagram = 6, 11, 3, 14, 3
    require_aux = False; keep_noaux = 0.25; screen = 14; verify = True; maxfacts = 500; budget_s = 1.5; max_tok = 360
GOALT = {"para": 1.5, "perp": 1.5, "cong": 1.5, "cyclic": 3.0, "eqangle": 1.5, "eqratio": 0.6, "midp": 2.0, "coll": 2.0, "simtri": 0.5}
STRUCT = {"coll_merge", "cyclic_merge", "midp_coll"}

def build_diagram(rng, cfg):
    """-> defs [(nome, kind, args)], coords, givens [(stmt, ponto-que-introduziu)] ; None se degenerar."""
    for _ in range(50):
        P = [(rng.uniform(-5, 5), rng.uniform(-5, 5)) for _ in range(3)]
        if abs(area2(*P)) > 6 and min(dist(P[0], P[1]), dist(P[1], P[2]), dist(P[0], P[2])) > 1.8: break
    else: return None
    C = {"a": P[0], "b": P[1], "c": P[2]}; defs = [("a", "triangle", ()), ("b", "triangle", ()), ("c", "triangle", ())]; giv = []
    names = list(CONS); wts = [CONS_W[n] for n in names]; target = rng.randint(cfg.min_pts, cfg.max_pts); tries = 0
    while len(C) < target and tries < 80:
        tries += 1; kind = rng.choices(names, wts)[0]; k = CONS[kind][0]
        if len(C) < k: continue
        args = norm_args(kind, rng.sample(sorted(C), k)); P = [C[x] for x in args]
        if kind in ("circ", "orth") and abs(area2(*P)) < 1e-2: continue
        if kind == "inter" and len(set(args)) < 4: continue
        x = CONS[kind][1](P, rng)
        if x is None or abs(x[0]) > 30 or abs(x[1]) > 30 or any(dist(x, q) < 5e-3 for q in C.values()): continue
        nm = LET[len(C)]; C[nm] = x; defs.append((nm, kind, tuple(args))); giv += [(f, nm) for f in CONS[kind][2](nm, args)]
    return (defs, C, giv) if len(C) >= cfg.min_pts else None

def _ancestors(defs, pts):
    dep = {n: set(a) for n, k, a in defs}; out, st = set(), list(pts)
    while st:
        p = st.pop()
        if p in out: continue
        out.add(p); st += list(dep.get(p, ()))
    return out

def _relabel_txt(defs, order, mp, aux_set):
    def one(n):
        k, a = next((k, a) for nn, k, a in defs if nn == n)
        return f"{mp[n]} = {k} " + " ".join(mp[x] for x in a)
    return one

def make_records(rng, cfg, stats):
    """Um diagrama -> até goals_per_diagram registros (problema, meta, aux, prova). stats: contadores do funil."""
    stats["diagrams"] = stats.get("diagrams", 0) + 1
    d = build_diagram(rng, cfg)
    if d is None: stats["degenerate"] = stats.get("degenerate", 0) + 1; return []
    defs, C, giv = d; tag = {}
    for f, p in giv: tag.setdefault(f, p)
    cl = Closure(C, [f for f, _ in giv], cfg.maxfacts, time.time() + cfg.budget_s).close()
    for st in [x for x in cl.fl if x[0] == "simtri"][:16]:
        a, b, c, p, q, r = st[1:]; cl.add(mk_eqrat(a, b, p, q, a, c, p, r), "simtri_ratio", (st,))
    pool = []
    for st in cl.fl:
        rule = cl.facts[st][0]
        if rule == "given" or rule in STRUCT or st[0] not in GOALT: continue
        if st[0] == "para" and set(st[1:3]) & set(st[3:5]): continue
        if st[0] == "eqangle" and False: continue
        pool.append(st)
    stats["closure_facts"] = stats.get("closure_facts", 0) + len(cl.fl)
    if not pool: stats["no_goal"] = stats.get("no_goal", 0) + 1; return []
    # triagem barata: explica K metas candidatas e prioriza as que EXIGEM construção auxiliar (como no paper)
    byt = {}
    for g in pool: byt.setdefault(g[0], []).append(g)
    for v in byt.values(): rng.shuffle(v)
    pick = []
    while len(pick) < cfg.screen and byt:
        t = rng.choices(list(byt), [GOALT[x] for x in byt])[0]; pick.append(byt[t].pop())
        if not byt[t]: del byt[t]
    scr = []
    for g in pick:
        stp = cl.explain(g); U = {tag[x] for r, _, x in stp if r == "given" and x in tag}
        A = _ancestors(defs, spts(g)) | ({"a", "b", "c"} if _ancestors(defs, spts(g)) & {"a", "b", "c"} else set())
        scr.append((any(p not in A for p in U), g, stp))
    scr.sort(key=lambda x: (not x[0], rng.random())); out, tried = [], 0
    for hasaux, g, stp in scr:
        if len(out) >= cfg.goals_per_diagram or tried >= cfg.goals_per_diagram + 2: break
        if not hasaux and rng.random() > cfg.keep_noaux: continue
        tried += 1; rec = _one_goal(cfg, defs, C, giv, tag, cl, g, stats, stp)
        if rec: out.append(rec)
    return out

def _one_goal(cfg, defs, C, giv, tag, cl, g, stats, steps=None):
    steps = steps or cl.explain(g); nontriv = [x for x in steps if x[0] != "given" and x[0] not in STRUCT]
    if len(nontriv) < cfg.min_steps: stats["too_easy"] = stats.get("too_easy", 0) + 1; return None
    if len(nontriv) > cfg.max_steps: stats["too_long"] = stats.get("too_long", 0) + 1; return None
    if not all(num_check(x, C) for _, _, x in steps): stats["unsound"] = stats.get("unsound", 0) + 1; return None
    used = {x for r, _, x in steps if r == "given"}; U = {tag[x] for x in used if x in tag}
    A = _ancestors(defs, spts(g)); dmap = {n: (k, a) for n, k, a in defs}
    if A & {"a", "b", "c"}: A |= {"a", "b", "c"}
    aux = set()
    for p in U:
        if p not in A: aux |= _ancestors(defs, [p]) - A
    needs = False
    if aux:
        sub = [f for f, p in giv if p in A]; c2 = Closure(C, sub, cfg.maxfacts, time.time() + cfg.budget_s).close()
        if c2.proves(g):  # a prova original usou aux sem precisar: reexplica sem aux
            steps = c2.explain(g); nontriv = [x for x in steps if x[0] != "given" and x[0] not in STRUCT]
            if len(nontriv) < cfg.min_steps or not all(num_check(x, C) for _, _, x in steps): stats["too_easy"] = stats.get("too_easy", 0) + 1; return None
            aux = set()
        else:
            needs = True
            if cfg.verify:
                c3 = Closure(C, [f for f, p in giv if p in A | aux], cfg.maxfacts, time.time() + cfg.budget_s).close()
                if not c3.proves(g): stats["aux_insufficient"] = stats.get("aux_insufficient", 0) + 1; return None
    if cfg.require_aux and not needs: stats["no_aux"] = stats.get("no_aux", 0) + 1; return None
    order_ = [n for n, _, _ in defs]; base = [n for n in order_ if n in A]; ax = [n for n in order_ if n in aux]
    mp = {n: LET[i] for i, n in enumerate(base + ax)}
    if len(mp) > 26: return None
    rn = lambda st: tuple([st[0]] + [mp.get(x, x) for x in st[1:]])
    prob = " ; ".join(["a b c = triangle"] + [f"{mp[n]} = {dmap[n][0]} " + " ".join(mp[x] for x in dmap[n][1]) for n in base if n not in "abc"])
    auxt = " ; ".join(f"{mp[n]} = {dmap[n][0]} " + " ".join(mp[x] for x in dmap[n][1]) for n in ax)
    goal = stxt(rn(g)); prf = " ".join(f"{r} " + " , ".join(stxt(rn(q)) for q in par) + f" => {stxt(rn(x))} ." for r, par, x in steps if r != "given" and r not in STRUCT)
    # steps cujos pais são só 'given' ficam; estruturais já foram filtrados como pais? mantém-nos como pais textuais
    meta = f"t={g[0]};n={len(mp)};aux={len(ax)};st={len(nontriv)};need={int(needs)}"
    return (prob, goal, auxt, prf, meta)

def rec_hash(prob, goal): return int.from_bytes(hashlib.blake2b((prob + "\x1f" + goal).encode(), digest_size=8).digest(), "big")

# ═══════════════════════════ pipeline em escala: gen / dedupe / tokenize ═══════════════════════════
def _cfg_from(d):
    c = Cfg()
    for k, v in d.items(): setattr(c, k, v)
    return c
NB = 64
def _chunk_job(job):
    out, cid, seed, cd, n_diag, nb = job; out = Path(out); mark = out / "done" / f"{cid}.json"
    if mark.exists(): return json.loads(mark.read_text())
    rng = random.Random(f"{seed}:{cid}"); cfg = _cfg_from(cd); st = {}; buf = {}; t0 = time.time(); nrec = 0
    for _ in range(n_diag):
        for r in make_records(rng, cfg, st):
            line = "\t".join(r); buf.setdefault(rec_hash(r[0], r[1]) % nb, []).append(line); nrec += 1
    for bk, lines in buf.items():
        d = out / "raw" / f"b{bk:03d}"; d.mkdir(parents=True, exist_ok=True)
        with gzip.open(d / f"p{os.getpid()}.tsv.gz", "ab", 3) as f: f.write(("\n".join(lines) + "\n").encode())
    st.update(records=nrec, secs=time.time() - t0, diag_target=n_diag); mark.parent.mkdir(exist_ok=True); mark.write_text(json.dumps(st)); return st

def cmd_gen(a):
    import multiprocessing as mp
    out = Path(a.out); (out / "done").mkdir(parents=True, exist_ok=True)
    cd = dict(min_pts=a.min_pts, max_pts=a.max_pts, min_steps=a.min_steps, max_steps=a.max_steps, require_aux=a.require_aux, goals_per_diagram=a.goals, keep_noaux=a.keep_noaux)
    n_chunks = math.ceil(a.n / a.chunk); ids = [i for i in range(n_chunks) if i % a.shards == a.shard]
    jobs = [(str(out), i, a.seed, cd, a.chunk, NB) for i in ids]; tot = {}; t0 = time.time(); doneN = 0
    log("gen", f"{a.n:,} diagramas -> {len(jobs)} chunks (shard {a.shard}/{a.shards}) × {a.workers} workers  seed={a.seed}", MG)
    it = (map(_chunk_job, jobs) if a.workers <= 1 else mp.Pool(a.workers).imap_unordered(_chunk_job, jobs))
    for st in it:
        doneN += 1
        for k, v in st.items():
            if isinstance(v, (int, float)) and k != "secs": tot[k] = tot.get(k, 0) + v
        el = time.time() - t0; rate = tot.get("records", 0) / max(el, 1e-9)
        nr = int(tot.get("records", 0)); print(f"\r{_c(CY, 'chunk')} {doneN}/{len(jobs)}  {_c(LM, f'{nr:,}')} registros  {_c(AM, f'{rate:,.0f}/s')}  ETA {(len(jobs) - doneN) * el / doneN:,.0f}s ", end="", flush=True)
    print(); (out / f"gen_stats_shard{a.shard}.json").write_text(json.dumps(tot, indent=1)); log("gen", f"funil: {tot}", CY); return tot

def _dedupe_bucket(job):
    src, dst, frac, only_aux = job; seen = {}; cnt = {}
    for f in sorted(Path(src).glob("*.tsv.gz")):
        with gzip.open(f, "rt", encoding="utf-8") as fh:
            for ln in fh:
                p = ln.rstrip("\n").split("\t")
                if len(p) != 5: continue
                if only_aux and "need=1" not in p[4]: continue
                h = rec_hash(p[0], p[1])
                if h not in seen: seen[h] = p
    tot = len(seen); typ = {}
    for h, p in seen.items(): typ.setdefault(p[4].split(";")[0], []).append(h)
    cap = max(1, int(math.ceil(frac * tot))); keep = []
    for t, hs in typ.items(): keep += sorted(hs)[:cap]
    with gzip.open(dst, "wt", encoding="utf-8") as fo:
        for h in sorted(keep): fo.write("\t".join(seen[h]) + "\n")
    return dict(bucket=Path(src).name, unique=tot, kept=len(keep), types={t: len(h) for t, h in typ.items()})

def cmd_dedupe(a):
    import multiprocessing as mp
    out = Path(a.out); (out / "clean").mkdir(exist_ok=True); bks = sorted((out / "raw").glob("b*")); raw_n = 0
    jobs = [(str(b), str(out / "clean" / f"{b.name}.tsv.gz"), a.max_type_frac, a.only_aux) for b in bks]
    res = list(mp.Pool(a.workers).imap_unordered(_dedupe_bucket, jobs)) if a.workers > 1 else [_dedupe_bucket(j) for j in jobs]
    uniq = sum(r["unique"] for r in res); kept = sum(r["kept"] for r in res); types = {}
    for r in res:
        for t, n in r["types"].items(): types[t] = types.get(t, 0) + n
    st = dict(buckets=len(res), unique=uniq, kept=kept, by_type=types); (out / "dedupe_stats.json").write_text(json.dumps(st, indent=1))
    log("dedupe", f"{uniq:,} únicos -> {kept:,} após quota por tipo (≤{a.max_type_frac:.0%}/tipo/bucket)  tipos={types}", LM); return st

# ── vocabulário fechado (DSL finita) ──
RULES = ["bisector_thm", "bisector_conv", "chord_angle", "center_angle", "center_angle_conv", "sss_simtri", "simtri_ang", "tangent_chord", "ar_ang", "ar_len", "para_shared_coll", "aa_simtri", "coll_cong_midp", "midline", "parallelogram", "perp_bisector", "perp_bisector_conv",
         "circle_center", "eqangle_cyclic", "iso_base", "iso_conv", "thales", "thales_conv", "simtri_ratio", "midp_coll", "coll_merge", "cyclic_merge", "given"]
VOCAB = ["<pad>", "<bos>", "<eos>", "AUX", "PROOF", "?", ";", ",", "=>", ".", "="] + list(LET) + ["triangle"] + list(CONS) + list(ARITY) + RULES
VOCAB = list(dict.fromkeys(VOCAB))
TOK = {t: i for i, t in enumerate(VOCAB)}; PAD, BOS, EOS, AUXT = 0, 1, 2, 3
def encode(prob, goal, aux, proof):
    ids = [BOS] + [TOK[t] for t in prob.split()] + [TOK["?"]] + [TOK[t] for t in goal.split()] + [AUXT] + [TOK[t] for t in aux.split()] + [TOK["PROOF"]] + [TOK[t] for t in proof.split()] + [EOS]
    return ids
def decode(ids): return " ".join(VOCAB[i] for i in ids if i != PAD)

def cmd_tokenize(a):
    import numpy as np
    out = Path(a.out); T = a.maxlen; rows = {"train": [], "val": []}; skipped = 0
    for f in sorted((out / "clean").glob("*.tsv.gz")):
        with gzip.open(f, "rt", encoding="utf-8") as fh:
            for ln in fh:
                p = ln.rstrip("\n").split("\t")
                ids = encode(p[0], p[1], p[2], p[3] if a.target == "full" else "")
                if len(ids) > T: skipped += 1; continue
                rows["val" if rec_hash(p[0], p[1]) % 100 < a.val_pct else "train"].append(ids + [PAD] * (T - len(ids)))
    (out / "tok").mkdir(exist_ok=True)
    for k, v in rows.items(): np.array(v, dtype=np.uint8).tofile(out / "tok" / f"{k}.u8")
    meta = dict(T=T, V=len(VOCAB), vocab=VOCAB, train=len(rows["train"]), val=len(rows["val"]), skipped_too_long=skipped, target=a.target); (out / "tok" / "meta.json").write_text(json.dumps(meta))
    log("tokenize", f"train={meta['train']:,} val={meta['val']:,} T={T} V={meta['V']} (uint8, memmap-ável; {skipped} longos descartados)", LM); return meta

# ═══════════════════════════ transformer decoder-only em NumPy (backprop manual) ═══════════════════════════
try:
    import numpy as np
except ImportError:  # geração/dedupe funcionam sem NumPy; treino/avaliação com LM exigem
    np = None
PRESETS = {"tiny": dict(d=64, L=2, H=4), "small": dict(d=128, L=4, H=4), "base": dict(d=256, L=6, H=8), "ag151m": dict(d=1024, L=12, H=8)}  # ag151m = arquitetura do paper (≈151M; só p/ export)
def _gelu(u): return 0.5 * u * (1 + np.tanh(0.7978845608028654 * (u + 0.044715 * u ** 3)))
def _dgelu(u):
    t = np.tanh(0.7978845608028654 * (u + 0.044715 * u ** 3)); return 0.5 * (1 + t) + 0.5 * u * (1 - t * t) * 0.7978845608028654 * (1 + 3 * 0.044715 * u * u)
def _ln(x, g, b, eps=1e-5):
    mu = x.mean(-1, keepdims=True); xc = x - mu; rs = 1.0 / np.sqrt((xc * xc).mean(-1, keepdims=True) + eps); xh = xc * rs; return xh * g + b, (xh, rs, g)
def _ln_back(dy, c):
    xh, rs, g = c; dxh = dy * g; dx = rs * (dxh - dxh.mean(-1, keepdims=True) - xh * (dxh * xh).mean(-1, keepdims=True))
    return dx, (dy * xh).reshape(-1, xh.shape[-1]).sum(0), dy.reshape(-1, xh.shape[-1]).sum(0)

class Model:
    def __init__(s, V, T, d, L, H, seed=0, dtype=None):
        dtype = dtype or np.float32; s.V, s.T, s.d, s.L, s.H, s.dt = V, T, d, L, H, dtype; r = np.random.default_rng(seed); P = {}
        n = lambda *sh, sc=0.02: (r.standard_normal(sh) * sc).astype(dtype)
        P["tok"], P["pos"] = n(V, d), n(T, d)
        for l in range(L):
            P[f"g1_{l}"], P[f"b1_{l}"] = np.ones(d, dtype), np.zeros(d, dtype); P[f"Wqkv_{l}"], P[f"bqkv_{l}"] = n(d, 3 * d), np.zeros(3 * d, dtype)
            P[f"Wo_{l}"], P[f"bo_{l}"] = n(d, d, sc=0.02 / math.sqrt(2 * L)), np.zeros(d, dtype); P[f"g2_{l}"], P[f"b2_{l}"] = np.ones(d, dtype), np.zeros(d, dtype)
            P[f"W1_{l}"], P[f"c1_{l}"] = n(d, 4 * d), np.zeros(4 * d, dtype); P[f"W2_{l}"], P[f"c2_{l}"] = n(4 * d, d, sc=0.02 / math.sqrt(2 * L)), np.zeros(d, dtype)
        P["gf"], P["bf"], P["Wout"], P["bout"] = np.ones(d, dtype), np.zeros(d, dtype), n(d, V), np.zeros(V, dtype); s.P = P
    def nparams(s): return sum(v.size for v in s.P.values())
    def forward(s, ids, keep=True):
        P, B, T, d, H = s.P, ids.shape[0], ids.shape[1], s.d, s.H; hd = d // H; x = P["tok"][ids] + P["pos"][:T]; C = []
        mask = np.triu(np.full((T, T), -1e9, s.dt), 1)
        for l in range(s.L):
            h1, c1 = _ln(x, P[f"g1_{l}"], P[f"b1_{l}"]); qkv = h1 @ P[f"Wqkv_{l}"] + P[f"bqkv_{l}"]
            q, k, v = (qkv[..., i * d:(i + 1) * d].reshape(B, T, H, hd).transpose(0, 2, 1, 3) for i in range(3))
            sc = q @ k.transpose(0, 1, 3, 2) / math.sqrt(hd) + mask; sc -= sc.max(-1, keepdims=True); p = np.exp(sc); p /= p.sum(-1, keepdims=True)
            o = (p @ v).transpose(0, 2, 1, 3).reshape(B, T, d); x1 = x + o @ P[f"Wo_{l}"] + P[f"bo_{l}"]
            h2, c2 = _ln(x1, P[f"g2_{l}"], P[f"b2_{l}"]); u = h2 @ P[f"W1_{l}"] + P[f"c1_{l}"]; a = _gelu(u); x = x1 + a @ P[f"W2_{l}"] + P[f"c2_{l}"]
            if keep: C.append((h1, c1, q, k, v, p, o, h2, c2, u, a))
        hf, cf = _ln(x, P["gf"], P["bf"]); return hf @ P["Wout"] + P["bout"], (ids, C, hf, cf)
    def loss_grad(s, ids, tgt, w):
        """CE médio ponderado por w (B,T) sobre previsão de tgt (B,T). Retorna loss e gradientes."""
        P, d, H = s.P, s.d, s.H; hd = d // H; lg, (ids_, C, hf, cf) = s.forward(ids); B, T = ids.shape
        lg = lg.astype(np.float64); lg -= lg.max(-1, keepdims=True); e = np.exp(lg); pr = e / e.sum(-1, keepdims=True)
        n = max(w.sum(), 1.0); lp = -np.log(np.take_along_axis(pr, tgt[..., None], -1)[..., 0] + 1e-30); loss = float((lp * w).sum() / n)
        dl = pr; np.put_along_axis(dl, tgt[..., None], np.take_along_axis(dl, tgt[..., None], -1) - 1, -1); dl = (dl * (w / n)[..., None]).astype(s.dt)
        G = {k: np.zeros_like(v) for k, v in P.items()}; f2 = lambda t: t.reshape(-1, t.shape[-1])
        G["Wout"] = f2(hf).T @ f2(dl); G["bout"] = dl.sum((0, 1)); dx, G["gf"], G["bf"] = _ln_back(dl @ P["Wout"].T, cf)
        for l in reversed(range(s.L)):
            h1, c1, q, k, v, p, o, h2, c2, u, a = C[l]; G[f"W2_{l}"] = f2(a).T @ f2(dx); G[f"c2_{l}"] = dx.sum((0, 1)); du = (dx @ P[f"W2_{l}"].T) * _dgelu(u)
            G[f"W1_{l}"] = f2(h2).T @ f2(du); G[f"c1_{l}"] = du.sum((0, 1)); dh, G[f"g2_{l}"], G[f"b2_{l}"] = _ln_back(du @ P[f"W1_{l}"].T, c2); dx = dx + dh
            G[f"Wo_{l}"] = f2(o).T @ f2(dx); G[f"bo_{l}"] = dx.sum((0, 1)); do = (dx @ P[f"Wo_{l}"].T).reshape(B, T, H, hd).transpose(0, 2, 1, 3)
            dp = do @ v.transpose(0, 1, 3, 2); dv = p.transpose(0, 1, 3, 2) @ do; ds = p * (dp - (dp * p).sum(-1, keepdims=True)) / math.sqrt(hd)
            dq = ds @ k; dk = ds.transpose(0, 1, 3, 2) @ q; dqkv = np.concatenate([t.transpose(0, 2, 1, 3).reshape(B, T, d) for t in (dq, dk, dv)], -1)
            G[f"Wqkv_{l}"] = f2(h1).T @ f2(dqkv); G[f"bqkv_{l}"] = dqkv.sum((0, 1)); dh, G[f"g1_{l}"], G[f"b1_{l}"] = _ln_back(dqkv @ P[f"Wqkv_{l}"].T, c1); dx = dx + dh
        np.add.at(G["tok"], ids, dx); G["pos"][:T] = dx.sum(0); return loss, G
    def save(s, path): np.savez(path, **s.P, _cfg=np.array(json.dumps(dict(V=s.V, T=s.T, d=s.d, L=s.L, H=s.H))))
    @staticmethod
    def load(path):
        z = np.load(path); c = json.loads(str(z["_cfg"])); m = Model(**c)
        for k in m.P: m.P[k] = z[k].astype(m.dt)
        return m

class AdamW:
    def __init__(s, P, lr=3e-4, wd=0.01, b1=0.9, b2=0.95): s.m = {k: np.zeros_like(v) for k, v in P.items()}; s.v = {k: np.zeros_like(v) for k, v in P.items()}; s.t = 0; s.lr, s.wd, s.b1, s.b2 = lr, wd, b1, b2
    def step(s, P, G, lr):
        s.t += 1; gn = math.sqrt(sum(float((g.astype(np.float64) ** 2).sum()) for g in G.values())); sc = min(1.0, 1.0 / (gn + 1e-9))
        for k in P:
            g = G[k] * sc; s.m[k] = s.b1 * s.m[k] + (1 - s.b1) * g; s.v[k] = s.b2 * s.v[k] + (1 - s.b2) * g * g
            mh = s.m[k] / (1 - s.b1 ** s.t); vh = s.v[k] / (1 - s.b2 ** s.t); wd = s.wd if P[k].ndim > 1 and k not in ("tok", "pos") else 0
            P[k] -= (lr * (mh / (np.sqrt(vh) + 1e-8) + wd * P[k])).astype(P[k].dtype)
        return gn

def _load_tok(out, split):
    m = json.loads((Path(out) / "tok" / "meta.json").read_text()); T = m["T"]; f = Path(out) / "tok" / f"{split}.u8"
    return np.fromfile(f, dtype=np.uint8).reshape(-1, T), m
def _batch(arr, rng, B, loss_on):
    ix = rng.integers(0, len(arr), B); x = arr[ix].astype(np.int64); L = int((x != PAD).sum(1).max()); x = x[:, :L]
    tgt = np.roll(x, -1, 1); tgt[:, -1] = PAD; w = ((tgt != PAD)).astype(np.float32)
    if loss_on == "target":  # perda só em aux+prova: posições após o token AUX
        pos = (x == AUXT).argmax(1); w *= (np.arange(L)[None, :] >= pos[:, None])
    return x, tgt, w

def cmd_train(a):
    arr, m = _load_tok(a.out, "train"); val, _ = _load_tok(a.out, "val"); cfg = PRESETS[a.preset]
    mod = Model(m["V"], m["T"], cfg["d"], cfg["L"], cfg["H"], a.seed); opt = AdamW(mod.P, wd=a.wd); rng = np.random.default_rng(a.seed); t0 = time.time()
    log("train", f"{mod.nparams():,} parâmetros  d={cfg['d']} L={cfg['L']} H={cfg['H']}  dados={len(arr):,}  batch={a.batch}", MG); hist = []
    for it in range(1, a.steps + 1):
        lr = a.lr * min(1, it / max(1, a.warmup)) * (0.1 + 0.9 * 0.5 * (1 + math.cos(math.pi * min(1, it / a.steps))))
        x, t, w = _batch(arr, rng, a.batch, a.loss_on); loss, G = mod.loss_grad(x, t, w); gn = opt.step(mod.P, G, lr); hist.append(loss)
        if it % a.log_every == 0 or it == a.steps:
            vl = 0.0
            if len(val): vx, vt, vw = _batch(val, rng, min(a.batch, len(val)), a.loss_on); vl = float(mod.loss_grad(vx, vt, vw)[0])
            print(f"\r{_c(CY, f'it {it}/{a.steps}')} loss {_c(LM, f'{np.mean(hist[-a.log_every:]):.3f}')} val {_c(AM, f'{vl:.3f}')} |g| {gn:.2f} {it / (time.time() - t0):.2f} it/s", flush=True)
    mod.save(Path(a.out) / "model.npz"); log("train", f"checkpoint em {Path(a.out) / 'model.npz'}", LM); return hist

# ═══════════════════════════ solver estilo AlphaGeometry: DD+AR  ⟷  LM propõe construção auxiliar ═══════════════════════════
def parse_defs(text):
    defs = []
    for cl in [c.strip() for c in text.split(";") if c.strip()]:
        lhs, rhs = cl.split("=", 1); kind, *args = rhs.split(); names = lhs.split()
        if kind == "triangle": defs += [(n, "triangle", ()) for n in names]
        else: defs.append((names[0], kind, tuple(args)))
    return defs
def parse_goal(text):
    t = text.split(); return canon(tuple(t)) if t and t[0] in ARITY and len(t) == 1 + ARITY[t[0]] else None
def realize(defs, rng, tries=40):
    for _ in range(tries):
        P = [(rng.uniform(-5, 5), rng.uniform(-5, 5)) for _ in range(3)]
        if abs(area2(*P)) < 6 or min(dist(P[0], P[1]), dist(P[1], P[2]), dist(P[0], P[2])) < 1.8: continue
        C = {"a": P[0], "b": P[1], "c": P[2]}; giv = []; ok = True
        for n, k, a in defs:
            if k == "triangle": continue
            x = CONS[k][1]([C[q] for q in a], rng)
            if x is None or any(dist(x, q) < 5e-3 for q in C.values()): ok = False; break
            C[n] = x; giv += CONS[k][2](n, list(a))
        if ok: return C, giv
    return None
def add_aux(C, giv, name, kind, args, rng, tries=12):
    if kind not in CONS or kind == "triangle" or len(args) != CONS[kind][0] or len(set(args)) != len(args) or any(q not in C for q in args) or name in C: return None
    for _ in range(tries):
        x = CONS[kind][1]([C[q] for q in args], rng)
        if x is not None and all(dist(x, q) > 5e-3 for q in C.values()) and abs(x[0]) < 60 and abs(x[1]) < 60:
            C2 = dict(C); C2[name] = x; return C2, giv + CONS[kind][2](name, list(args))
    return None
def random_propose(C, K, rng):
    names = list(CONS); w = [CONS_W[n] for n in names]; out, seen = [], set()
    for _ in range(K * 6):
        k = rng.choices(names, w)[0]; n = CONS[k][0]
        if len(C) < n: continue
        a = tuple(rng.sample(sorted(C), n)); key = (k, tuple(norm_args(k, a)))
        if key not in seen: seen.add(key); out.append((0.0, k, list(key[1])))
        if len(out) >= K: break
    return out
def lm_propose(model, prefix, pts, newname, K):
    """Busca em feixe com gramática restrita: <novo> = <construção> <args existentes distintos> ;"""
    pts = sorted(pts); beams = [(0.0, [])]; done = []
    while beams:
        byl = {}
        for sc, tk in beams: byl.setdefault(len(tk), []).append((sc, tk))
        nxt = []
        for n, grp in byl.items():
            ids = np.array([prefix + [TOK[t] for t in tk] for _, tk in grp], dtype=np.int64)
            lg = model.forward(ids[:, :model.T], keep=False)[0][:, -1].astype(np.float64); lg -= lg.max(-1, keepdims=True); lp = lg - np.log(np.exp(lg).sum(-1, keepdims=True))
            for (sc, tk), row in zip(grp, lp):
                if n == 0: al = [newname]
                elif n == 1: al = ["="]
                elif n == 2: al = [k for k in CONS]
                else:
                    k = CONS[tk[2]][0]
                    al = [p for p in pts if p not in tk[3:]] if n - 3 < k else [";"]
                for t in al:
                    nt = tk + [t]; s2 = sc + float(row[TOK[t]])
                    (done if t == ";" else nxt).append((s2, nt))
        beams = sorted(nxt, key=lambda x: -x[0])[:K]
    done.sort(key=lambda x: -x[0]); return [(sc, tk[2], tk[3:-1]) for sc, tk in done[:K]]

def solve(prob, goal, mode="lm", model=None, K=6, depth=2, seed=0, budget=2.0, maxfacts=500):
    """-> dict(solved, depth, aux). mode ∈ {ddar, random, lm}. Cada candidato é realizado numericamente no MESMO diagrama."""
    rng = random.Random(seed); defs = parse_defs(prob); g = parse_goal(goal); R = realize(defs, rng)
    if R is None or g is None: return dict(solved=False, depth=-1, aux=[], err="realize/parse")
    C, giv = R; t0 = time.time(); close = lambda C_, g_: Closure(C_, [f for f in g_], maxfacts, time.time() + budget).close()
    if not num_check(g, C): return dict(solved=False, depth=-1, aux=[], err="goal falso no diagrama")
    if close(C, giv).proves(g): return dict(solved=True, depth=0, aux=[], secs=time.time() - t0)
    if mode == "ddar": return dict(solved=False, depth=0, aux=[], secs=time.time() - t0)
    states = [(0.0, C, giv, [], [])]; ptok = [BOS] + [TOK[t] for t in prob.split()] + [TOK["?"]] + [TOK[t] for t in goal.split()] + [AUXT] if mode == "lm" else None
    for dep in range(1, depth + 1):
        nxt = []
        for sc, C0, g0, aux, toks in states:
            nm = LET[len(C0)] if len(C0) < 26 else None
            if nm is None: continue
            props = lm_propose(model, ptok + toks, C0, nm, K) if mode == "lm" else random_propose(C0, K, rng)
            for s2, kind, args in props:
                r = add_aux(C0, g0, nm, kind, args, rng)
                if r is None: continue
                C1, g1 = r; a2 = aux + [f"{nm} = {kind} " + " ".join(args)]; cl = close(C1, g1)
                if cl.proves(g): return dict(solved=True, depth=dep, aux=a2, secs=time.time() - t0)
                nxt.append((sc + s2, C1, g1, a2, toks + [TOK[t] for t in f"{nm} = {kind} {' '.join(args)} ;".split()]))
        if mode == "lm": nxt.sort(key=lambda x: -x[0])
        else: rng.shuffle(nxt)
        states = nxt[:K]
        if not states: break
    return dict(solved=False, depth=depth, aux=[], secs=time.time() - t0)

def cmd_eval(a):
    out = Path(a.out); mod = Model.load(out / "model.npz") if (out / "model.npz").exists() and a.lm else None; rng = random.Random(a.seed + 777)
    train_h = set()
    for f in (out / "clean").glob("*.tsv.gz") if (out / "clean").exists() else []:
        with gzip.open(f, "rt") as fh: train_h |= {rec_hash(*ln.split("\t")[:2]) for ln in fh}
    cfg = Cfg(); cfg.require_aux = True; cfg.goals_per_diagram = 3; items = []; st = {}; tries = 0
    while len(items) < a.n and tries < a.n * 400:
        tries += 1
        for r in make_records(rng, cfg, st):
            if "need=1" in r[4] and rec_hash(r[0], r[1]) not in train_h and r[2]: items.append(r)
    log("eval", f"{len(items)} problemas que EXIGEM aux (verificado: DD+AR sem aux não prova), disjuntos do treino ({len(train_h):,} hashes)", MG)
    res = {}
    for mode in ("ddar", "random") + (("lm",) if mod else ()):
        t = time.time(); ok = [solve(r[0], r[1], mode, mod, a.K, a.depth, a.seed + i) for i, r in enumerate(items)]
        res[mode] = dict(solved=sum(x["solved"] for x in ok), n=len(ok), secs=round(time.time() - t, 1))
        log("eval", f"{mode:7s} solve@{a.K}×d{a.depth}: {res[mode]['solved']}/{len(ok)}  ({res[mode]['secs']}s)", LM if mode == "lm" else CY)
    (out / "eval.json").write_text(json.dumps(res, indent=1)); return res

# ═══════════════════════════ adaptador do benchmark do AlphaGeometry (imo_ag_30 / jgex_ag_231) ═══════════════════════════
def _unit(v): n = math.hypot(*v); return (v[0] / n, v[1] / n) if n > 1e-12 else (1.0, 0.0)
def _bis(P): u, v = _unit(sub(P[0], P[1])), _unit(sub(P[2], P[1])); return ("L", P[1], (u[0] + v[0], u[1] + v[1]))
def _incenter(P):
    a, b, c = P; l1, l2 = _bis((b, a, c)), _bis((a, b, c)); return ("P", _inter(l1[1], (l1[1][0] + l1[2][0], l1[1][1] + l1[2][1]), l2[1], (l2[1][0] + l2[2][0], l2[1][1] + l2[2][1])))
def _eqtri(P, r): b, c = P; m = lerp(b, c, .5); d = _perp(sub(c, b)); t = (r.choice((-1, 1))) * math.sqrt(3) / 2; return ("P", (m[0] + t * d[0], m[1] + t * d[1]))
AGS = {  # nome: (nargs, locus(P[,rng]) , facts(x,a))   locus: ('L',pt,dir) | ('C',centro,raio) | ('P',ponto|None)
    "on_line": (2, lambda P, r: ("L", P[0], sub(P[1], P[0])), lambda x, a: [mk_coll(x, a[0], a[1])]),
    "on_pline": (3, lambda P, r: ("L", P[0], sub(P[2], P[1])), lambda x, a: [mk_para(a[0], x, a[1], a[2])]),
    "on_tline": (3, lambda P, r: ("L", P[0], _perp(sub(P[2], P[1]))), lambda x, a: [mk_perp(a[0], x, a[1], a[2])]),
    "on_bline": (2, lambda P, r: ("L", lerp(P[0], P[1], .5), _perp(sub(P[1], P[0]))), lambda x, a: [mk_cong(x, a[0], x, a[1])]),
    "on_circle": (2, lambda P, r: ("C", P[0], dist(P[0], P[1])), lambda x, a: [mk_cong(a[0], x, a[0], a[1])]),
    "on_dia": (2, lambda P, r: ("C", lerp(P[0], P[1], .5), dist(P[0], P[1]) / 2), lambda x, a: [mk_perp(x, a[0], x, a[1])]),
    "angle_bisector": (3, lambda P, r: _bis(P), lambda x, a: [mk_eqang(a[1], a[0], a[1], x, a[1], x, a[1], a[2])]),
    "lc_tangent": (2, lambda P, r: ("L", P[0], _perp(sub(P[1], P[0]))), lambda x, a: [mk_perp(a[0], x, a[0], a[1])]),
    "eqdistance": (3, lambda P, r: ("C", P[0], dist(P[1], P[2])), lambda x, a: [mk_cong(x, a[0], a[1], a[2])]),
    "midpoint": (2, lambda P, r: ("P", lerp(P[0], P[1], .5)), lambda x, a: [mk_midp(x, a[0], a[1])]),
    "foot": (3, lambda P, r: ("P", _foot(*P)), lambda x, a: [mk_coll(x, a[1], a[2]), mk_perp(a[0], x, a[1], a[2])]),
    "circle": (3, lambda P, r: ("P", _circum(*P)), lambda x, a: [mk_cong(x, a[0], x, a[1]), mk_cong(x, a[1], x, a[2])]),
    "orthocenter": (3, lambda P, r: ("P", _orth(*P)), lambda x, a: [mk_perp(a[0], x, a[1], a[2]), mk_perp(a[1], x, a[0], a[2])]),
    "reflect": (3, lambda P, r: ("P", (lambda f: None if f is None else (2 * f[0] - P[0][0], 2 * f[1] - P[0][1]))(_foot(*P))), lambda x, a: [mk_cong(a[1], a[0], a[1], x), mk_cong(a[2], a[0], a[2], x), mk_perp(a[1], a[2], a[0], x)]),
    "mirror": (2, lambda P, r: ("P", (2 * P[1][0] - P[0][0], 2 * P[1][1] - P[0][1])), lambda x, a: [mk_midp(a[1], a[0], x)]),
    "parallelogram": (3, lambda P, r: ("P", (P[0][0] + P[2][0] - P[1][0], P[0][1] + P[2][1] - P[1][1])), lambda x, a: [mk_para(a[0], a[1], a[2], x), mk_para(a[0], x, a[1], a[2])]),
    "intersection_ll": (4, lambda P, r: ("P", _inter(*P)), lambda x, a: [mk_coll(x, a[0], a[1]), mk_coll(x, a[2], a[3])]),
    "eq_triangle": (2, lambda P, r: _eqtri(P, r), lambda x, a: [mk_cong(x, a[0], a[0], a[1]), mk_cong(a[0], a[1], a[1], x), mk_eqang(a[0], x, a[0], a[1], a[1], a[0], a[1], x), mk_eqang(x, a[1], x, a[0], a[0], x, a[0], a[1])]),
    "incenter": (3, lambda P, r: _incenter(P), lambda x, a: [mk_eqang(a[0], a[1], a[0], x, a[0], x, a[0], a[2]), mk_eqang(a[2], a[0], a[2], x, a[2], x, a[2], a[1]), mk_eqang(a[1], a[2], a[1], x, a[1], x, a[1], a[0])]),
}
AG_ALIAS = {"circumcenter": "circle"}
def _ll(p, d, q, e):
    den = cross(d, e)
    if abs(den) < 1e-9 * (math.hypot(*d) * math.hypot(*e) + 1e-12): return []
    t = cross(sub(q, p), e) / den; return [(p[0] + t * d[0], p[1] + t * d[1])]
def _lc(p, d, o, R):
    d = _unit(d); f = sub(p, o); b = dot(f, d); c = dot(f, f) - R * R; disc = b * b - c
    if disc < 0: return []
    q = math.sqrt(disc); return [(p[0] + (-b + sg * q) * d[0], p[1] + (-b + sg * q) * d[1]) for sg in (1, -1)]
def _cc(o1, r1, o2, r2):
    D = dist(o1, o2)
    if D < 1e-9 or D > r1 + r2 or D < abs(r1 - r2): return []
    a = (r1 * r1 - r2 * r2 + D * D) / (2 * D); h = math.sqrt(max(r1 * r1 - a * a, 0)); u = _unit(sub(o2, o1)); m = (o1[0] + a * u[0], o1[1] + a * u[1])
    return [(m[0] - h * u[1], m[1] + h * u[0]), (m[0] + h * u[1], m[1] - h * u[0])]
def _meet(A, B):
    if A[0] == "L" and B[0] == "L": return _ll(A[1], A[2], B[1], B[2])
    if A[0] == "L": return _lc(A[1], A[2], B[1], B[2])
    if B[0] == "L": return _lc(B[1], B[2], A[1], A[2])
    return _cc(A[1], A[2], B[1], B[2])
def _on(L, x): return abs(cross(sub(x, L[1]), L[2])) < 1e-6 * (math.hypot(*L[2]) + 1) if L[0] == "L" else abs(dist(x, L[1]) - L[2]) < 1e-6 * (L[2] + 1)
def ag_parse(line):
    pre, goal = line.split("?"); out = []
    for cl in [c.strip() for c in pre.split(";") if c.strip()]:
        lhs, rhs = cl.split("=", 1); cons = [c.strip().split() for c in rhs.split(",") if c.strip()]; out.append((lhs.split(), cons))
    return out, goal.split()
def ag_goal(g):
    t, a = g[0], g[1:]
    if t == "contri": return [mk_simtri(*a), mk_cong(a[0], a[1], a[3], a[4])]
    if t in MK and len(a) == ARITY[t]: return [MK[t](*a)]
    return None
def ag_build(clauses, rng):
    """-> (C, givens) | motivo str. Pontos definidos por 0/1/2 lugares geométricos (interseção numérica)."""
    C, giv = {}, []; box = lambda: (rng.uniform(-6, 6), rng.uniform(-6, 6))
    for names, cons in clauses:
        k0 = cons[0][0]
        if k0 in ("triangle", "free", "segment"):
            for n in names: C[n] = box()
            if k0 == "triangle" and abs(area2(*(C[n] for n in names))) < 3: return "triângulo degenerado"
            continue
        if k0 in ("iso_triangle", "r_triangle"):
            a, b, c = names; C[b], C[c] = box(), box()
            if k0 == "iso_triangle": m = lerp(C[b], C[c], .5); d = _perp(sub(C[c], C[b])); t = _rt(rng, .4, 1.5); C[a] = (m[0] + t * d[0], m[1] + t * d[1]); giv += [mk_cong(a, b, a, c), mk_eqang(b, a, b, c, c, b, c, a)]
            else: d = _perp(sub(C[c], C[b])); t = _rt(rng, .3, 1.5); C[a] = (C[b][0] + t * d[0], C[b][1] + t * d[1]); C[a] = (C[b][0] + 0.0, C[b][1]) if False else C[a]; giv.append(mk_perp(a, b, a, c)); C[a] = _r_tri(C[b], C[c], rng)
            continue
        x = names[0]; loci = []; fixed = None
        for c in cons:
            nm = AG_ALIAS.get(c[0], c[0])
            if nm not in AGS: return f"construção não suportada: {c[0]}"
            n, fn, ff = AGS[nm]; args = c[2:] if len(c) - 1 > n else c[1:]
            if len(args) != n or any(q not in C for q in args): return f"aridade/ponto indefinido em {c[0]}"
            lc = fn([C[q] for q in args], rng); giv += ff(x, list(args))
            if lc[0] == "P":
                if lc[1] is None: return "ponto degenerado"
                fixed = lc[1]
            else: loci.append(lc)
        if fixed is not None: pt = fixed
        elif not loci: pt = box()
        elif len(loci) == 1:
            L = loci[0]
            if L[0] == "L": t = _rt(rng, .3, 2.0); pt = (L[1][0] + t * L[2][0] / (math.hypot(*L[2]) + 1e-12) * 3, L[1][1] + t * L[2][1] / (math.hypot(*L[2]) + 1e-12) * 3)
            else: th = rng.uniform(0, 6.283); pt = (L[1][0] + L[2] * math.cos(th), L[1][1] + L[2] * math.sin(th))
        else:
            cand = [q for q in _meet(loci[0], loci[1]) if all(_on(L, q) for L in loci[2:])]
            cand = [q for q in cand if all(dist(q, w) > 1e-5 for w in C.values())] or cand
            if not cand: return "loci sem interseção"
            pt = rng.choice(cand)
        if any(dist(pt, w) < 1e-5 for w in C.values()) or abs(pt[0]) > 200 or abs(pt[1]) > 200: return "ponto coincidente/distante"
        C[x] = pt
    return C, giv
def _r_tri(b, c, rng):  # a com ângulo reto em a: no círculo de diâmetro bc
    m = lerp(b, c, .5); R = dist(b, c) / 2; th = rng.uniform(0.3, 2.8) * rng.choice((-1, 1)); u = _unit(sub(c, b)); v = _perp(u)
    return (m[0] + R * (math.cos(th) * u[0] + math.sin(th) * v[0]), m[1] + R * (math.cos(th) * u[1] + math.sin(th) * v[1]))

def cmd_agbench(a):
    tot = {}; rows = []; lines = [l for l in Path(a.file).read_text().split("\n")]; probs = [(lines[i].strip(), lines[i + 1]) for i in range(0, len(lines) - 1, 2) if lines[i].strip()]
    if a.limit: probs = probs[:a.limit]
    log("agbench", f"{len(probs)} problemas de {a.file}  (timeout {a.timeout}s/problema, {a.tries} diagramas)", MG)
    for name, text in probs:
        try: clauses, g = ag_parse(text)
        except Exception as e: rows.append((name, "parse", str(e))); continue
        goal = ag_goal(g)
        if goal is None: rows.append((name, "N/S", f"meta não suportada: {g[0]}")); continue
        status, det = "N/S", ""; t0 = time.time()
        for k in range(a.tries):
            R = ag_build(clauses, random.Random(f"{a.seed}:{name}:{k}"))
            if isinstance(R, str): det = R; continue
            C, giv = R
            if not all(num_check(x, C, 1e-5) for x in goal): status, det = "FALSO", "meta falsa no diagrama (modelagem/ruído)"; continue
            if not all(num_check(x, C, 1e-5) for x in giv): status, det = "FALSO", "premissa falsa no diagrama"; continue
            cl = Closure(C, giv, a.maxfacts, time.time() + a.timeout).close(rounds=a.rounds); ok = all(cl.proves(x) for x in goal)
            tot["_facts"] = tot.get("_facts", 0) + len(cl.fl); tot["_false"] = tot.get("_false", 0) + sum(not num_check(x, C, 1e-5) for x in cl.fl)
            status, det = ("OK", f"{len(cl.fl)} fatos, {time.time() - t0:.1f}s") if ok else ("--", f"{len(cl.fl)} fatos, {time.time() - t0:.1f}s"); break
        rows.append((name, status, det)); tot[status] = tot.get(status, 0) + 1
        print(f"  {_c({'OK': LM, '--': AM, 'N/S': CY}.get(status, MG), f'{status:>4}', True)} {name:34s} {det}", flush=True)
    sup = sum(v for k, v in tot.items() if k in ("OK", "--")); ok = tot.get("OK", 0)
    log("agbench", f"auditoria de solidez nos diagramas do benchmark: {tot.get('_false', 0)} fatos falsos de {tot.get('_facts', 0):,} derivados", LM if not tot.get("_false") else MG)
    log("agbench", f"RESOLVIDOS {ok}/{len(probs)} | expressáveis+verdadeiros {sup} | não-suportados {tot.get('N/S', 0)} | falsos/modelagem {tot.get('FALSO', 0)}", LM)
    print(_c(AM, "Referência publicada (paper): DDAR 14/30 e AlphaGeometry 25/30 em IMO-AG-30; DDAR 198/231 em JGEX-AG-231 (motor completo de 43 regras)."))
    return tot

# ═══════════════════════════ bench / selftest / CLI ═══════════════════════════
def cmd_bench(a):
    cfg = Cfg(); cfg.require_aux = a.require_aux; st = {}; rng = random.Random(a.seed); recs = []; t = time.time()
    for _ in range(a.diagrams): recs += make_records(rng, cfg, st)
    dt = time.time() - t; rps = len(recs) / dt; raw = "\n".join("\t".join(r) for r in recs).encode(); gz = len(gzip.compress(raw, 3))
    toks = sum(len(encode(r[0], r[1], r[2], r[3])) for r in recs) / max(len(recs), 1); aux = sum("need=1" in r[4] for r in recs) / max(len(recs), 1)
    uniq = len({rec_hash(r[0], r[1]) for r in recs}) / max(len(recs), 1)
    log("bench", f"1 núcleo: {rps:.1f} registros/s ({len(recs)} em {dt:.0f}s)  únicos={uniq:.1%}  com-aux={aux:.1%}  tokens/reg={toks:.0f}  {gz / max(len(recs), 1):.0f} B/reg (gz)", MG)
    log("bench", f"funil: {st}", CY)
    if len(recs) < 30: print(_c(AM, f"AVISO: só {len(recs)} registros na amostra — projeção ruidosa; aumente --diagrams."))
    print(_c(AM, "\nPROJEÇÃO (extrapolação linear da vazão MEDIDA; NÃO é promessa — rede/IO/dedupe cruzado não incluídos)", True))
    print(f"{'alvo':>10} | " + " | ".join(f"{c:>9,} núcleos" for c in (8, 64, 1000, 100000)) + " |  núcleo-horas |  disco gz | RAM dedupe(8B/hash)")
    for N in (10 ** 7, 10 ** 8, 3 * 10 ** 8):
        core_s = N / max(rps, 1e-9) / max(uniq, 1e-9); print(f"{N:>10,} | " + " | ".join(f"{core_s / c / 3600:>8.1f}h       " for c in (8, 64, 1000, 100000)) + f" | {core_s / 3600:>13,.0f} | {N * gz / max(len(recs), 1) / 1e9:>7.1f}GB | {N * 8 / 1e9:>6.1f}GB")
    P = PRESETS["ag151m"]; n = 151.7e6; tk = 10 ** 8 * toks
    print(_c(CY, f"\nTreino (preset ag151m, {n / 1e6:.0f}M params) sobre 100M registros ≈ {tk / 1e9:.1f}B tokens/época ≈ {6 * n * tk:.2e} FLOPs (6·N·D). "
             f"A 40% de MFU numa GPU de ~312 TFLOPs bf16 ⇒ ≈ {6 * n * tk / (312e12 * .4) / 3600:,.0f} h-GPU/época. Treino em NumPy: só presets tiny/small/base (use `tokenize` p/ exportar uint8 e treinar em framework GPU)."))
    return dict(rps=rps, uniq=uniq, aux=aux)

def cmd_selftest(a):
    import tempfile, shutil, itertools as it
    res = []; tmp = Path(tempfile.mkdtemp(prefix="geoforge_"))
    def T(name, fn):
        t = time.time()
        try: msg = fn() or ""; res.append((name, True, msg, time.time() - t)); print(_c(LM, "[PASS]", True), name, _c(AM, f"{time.time() - t:.1f}s"), _c(CY, msg), flush=True)
        except Exception as e:
            import traceback; res.append((name, False, repr(e), time.time() - t)); print(_c(MG, "[FAIL]", True), name, repr(e)); traceback.print_exc(limit=3)
    def need_(c, m="falhou"):
        if not c: raise AssertionError(m)
    def canon_t():
        for t in ("eqangle", "eqratio"):
            base = [("a", "b"), ("c", "d"), ("e", "f"), ("g", "h")]; f = MK[t]; ref = f(*[p for l in base for p in l]); r = random.Random(1)
            for _ in range(50):
                o = _orbit_min(tuple(base)); l = list(it.product([0], [0])); x, y, z, w = [tuple(reversed(q)) if r.random() < .5 else q for q in base]
                need_(f(*x, *z, *y, *w) == ref and f(*z, *w, *x, *y) == ref and f(*y, *x, *w, *z) == ref, f"{t} orbita")
        need_(mk_simtri("a", "b", "c", "p", "q", "r") == mk_simtri("p", "q", "r", "a", "b", "c") == mk_simtri("b", "a", "c", "q", "p", "r"), "simtri")
        return "órbitas de eqangle/eqratio/simtri"
    def build(defs, tri=((0., 0.), (6., 0.), (2., 4.))):
        C = {"a": tri[0], "b": tri[1], "c": tri[2]}; giv = []
        for x, k, ar in defs: C[x] = CONS[k][1]([C[q] for q in ar], random.Random(3)); giv += CONS[k][2](x, list(ar))
        return C, giv
    def thm():
        out = []
        cases = [("ortico cíclico", [("d", "foot", "abc"), ("e", "foot", "bac")], mk_cyc("a", "b", "d", "e")),
                 ("base média", [("d", "midp", "ab"), ("e", "midp", "ac")], mk_para("d", "e", "b", "c")),
                 ("circuncentro ⟂ lado", [("o", "circ", "abc"), ("m", "midp", "bc")], mk_perp("o", "m", "b", "c")),
                 ("Tales", [("m", "midp", "ab"), ("d", "foot", "abc")], mk_cong("m", "d", "m", "a")),
                 ("ortocentro", [("h", "orth", "abc"), ("d", "foot", "abc")], mk_coll("a", "h", "d"))]
        for nm, d, g in cases:
            C, giv = build(d); cl = Closure(C, giv).close(); need_(cl.proves(g), f"não provou: {nm}"); need_(all(num_check(x, C) for _, _, x in cl.explain(g)), nm); out.append(nm)
        C, giv = build([("d", "midp", "ab"), ("e", "midp", "ac")]); cl = Closure(C, giv).close()
        for bad in (mk_para("d", "e", "a", "b"), mk_perp("d", "e", "b", "c"), mk_cong("d", "e", "a", "b")): need_(not cl.proves(bad), f"provou FALSO {bad}")
        return "; ".join(out) + "; falsos recusados"
    def sound():
        rng = random.Random(int(a.seed)); cfg = Cfg(); n = bad = 0; per = {}
        for _ in range(a.audit):
            d = build_diagram(rng, cfg)
            if not d: continue
            defs, C, giv = d; cl = Closure(C, [f for f, _ in giv], 500).close()
            for st in cl.fl:
                n += 1
                if not num_check(st, C): bad += 1; per[cl.facts[st][0]] = per.get(cl.facts[st][0], 0) + 1
        need_(bad == 0, f"{bad}/{n} fatos FALSOS {per}"); return f"{n:,} fatos derivados, 0 falsos no diagrama"
    def roundtrip():
        rng = random.Random(a.seed + 5); cfg = Cfg(); cfg.require_aux = True; recs = []; st = {}; k = 0
        while len(recs) < 15 and k < 3000: k += 1; recs += [r for r in make_records(rng, cfg, st) if "need=1" in r[4]]
        need_(recs, "nenhum registro com aux"); ok = nodd = tot = 0
        for r in recs:
            defs = parse_defs(r[0]); g = parse_goal(r[1]); R = realize(defs, random.Random(9)); need_(g is not None)
            if R is None: continue
            C, giv = R; tot += 1
            if num_check(g, C) and not Closure(C, giv, 500).close().proves(g): nodd += 1
            for cl_ in [c for c in r[2].split(";") if c.strip()]:
                lhs, rhs = cl_.split("="); kind, *ar = rhs.split(); x = add_aux(C, giv, lhs.strip(), kind, ar, random.Random(9)); need_(x, "aux irrealizável"); C, giv = x
            ok += Closure(C, giv, 500).close().proves(g)
        need_(tot and ok / tot >= .9 and nodd / tot >= .9, f"suficiência={ok}/{tot} necessidade={nodd}/{tot}")
        return f"{ok}/{tot} provados COM aux; {nodd}/{tot} NÃO provados sem aux (re-realização aleatória do texto)"
    def tokz():
        r = ("a b c = triangle ; d = midp a b", "perp a b c d", "e = foot c a b", "ar_ang perp a b c d , coll a b c => para a b c d ."); ids = encode(*r)
        need_(decode(ids) == "<bos> " + " ".join([r[0], "?", r[1], "AUX", r[2], "PROOF", r[3]]) + " <eos>", "roundtrip"); need_(len(VOCAB) < 256 and len(set(VOCAB)) == len(VOCAB)); return f"V={len(VOCAB)}"
    def determ():
        outs = []
        for i in (1, 2):
            d = tmp / f"d{i}"; _chunk_job((str(d), 0, 42, dict(), 15, NB)); L = []
            for f in sorted((d / "raw").rglob("*.tsv.gz")):
                with gzip.open(f, "rt") as fh: L += fh.read().splitlines()
            outs.append(sorted(L))
        need_(outs[0] == outs[1] and outs[0], "chunk não determinístico"); return f"{len(outs[0])} registros idênticos em 2 execuções"
    def dedupe_t():
        d = tmp / "dd"; (d / "raw" / "b000").mkdir(parents=True); L = ["p\tg\tx\ty\tt=para;n=1", "p\tg\tx\ty\tt=para;n=1", "q\th\tx\ty\tt=perp;n=1"]
        with gzip.open(d / "raw" / "b000" / "w.tsv.gz", "wt") as f: f.write("\n".join(L) + "\n")
        r = cmd_dedupe(argparse.Namespace(out=str(d), workers=1, max_type_frac=1.0, only_aux=False)); need_(r["unique"] == 2, f"único={r['unique']}"); return "duplicata removida"
    def grad():
        m = Model(V=20, T=12, d=16, L=2, H=2, seed=1, dtype=np.float64); r = np.random.default_rng(0)
        for k in m.P: m.P[k] += r.standard_normal(m.P[k].shape) * 0.05
        x = r.integers(1, 20, (3, 10)); t = np.roll(x, -1, 1); w = (r.random((3, 10)) > .2).astype(np.float64); _, Gr = m.loss_grad(x, t, w); worst = 0
        for k in m.P:
            for _ in range(3):
                ix = tuple(r.integers(0, s) for s in m.P[k].shape); o = m.P[k][ix]; e = 1e-5
                m.P[k][ix] = o + e; lp = m.loss_grad(x, t, w)[0]; m.P[k][ix] = o - e; lm = m.loss_grad(x, t, w)[0]; m.P[k][ix] = o
                nu, an = (lp - lm) / (2 * e), Gr[k][ix]; worst = max(worst, abs(nu - an) / (abs(nu) + abs(an) + 1e-8))
        need_(worst < 1e-3, f"gradcheck {worst:.2e}"); return f"pior erro relativo {worst:.1e}"
    def e2e():
        d = tmp / "e2e"; cmd_gen(argparse.Namespace(out=str(d), n=a.e2e_diag, chunk=30, shards=1, shard=0, workers=1, seed=3, min_pts=6, max_pts=11, min_steps=3, max_steps=14, require_aux=False, goals=3, keep_noaux=.5))
        cmd_dedupe(argparse.Namespace(out=str(d), workers=1, max_type_frac=.5, only_aux=False)); m = cmd_tokenize(argparse.Namespace(out=str(d), maxlen=384, val_pct=5, target="full")); need_(m["train"] > 20, "poucos dados")
        h = cmd_train(argparse.Namespace(out=str(d), preset="tiny", steps=40, batch=8, lr=2e-3, wd=.01, warmup=5, seed=0, loss_on="target", log_every=20)); need_(np.mean(h[-8:]) < np.mean(h[:4]) - .3, f"loss não caiu {h[0]:.2f}->{np.mean(h[-8:]):.2f}")
        r = cmd_eval(argparse.Namespace(out=str(d), lm=True, n=3, K=3, depth=1, seed=1)); need_(r["ddar"]["solved"] == 0, "DD+AR resolveu problema que exige aux?"); return f"loss {h[0]:.2f}->{np.mean(h[-8:]):.2f}; eval roda"
    for nm, fn in (("canonização", canon_t), ("teoremas clássicos (+falsos recusados)", thm), ("solidez numérica de TODOS os fatos derivados", sound), ("texto⟷motor: suficiência e necessidade do aux", roundtrip),
                   ("tokenização roundtrip", tokz), ("gradcheck do transformer (float64)", grad), ("determinismo do chunk", determ), ("dedupe", dedupe_t), ("e2e gen→dedupe→tok→train→eval", e2e)):
        if getattr(a,"quick",False) and nm.startswith("e2e "):
            log("selftest", "Treinamento e2e ignorado (--quick)", AM)
            continue
        T(nm, fn)
    shutil.rmtree(tmp, ignore_errors=True); okn = sum(r[1] for r in res)
    print(_c(LM if okn == len(res) else MG, f"\nSELFTEST {okn}/{len(res)}", True)); return 0 if okn == len(res) else 1

def main(argv=None):
    ap = argparse.ArgumentParser(description="geoforge — dados sintéticos de geometria + treino/avaliação estilo AlphaGeometry"); sp = ap.add_subparsers(dest="cmd", required=True)
    g = sp.add_parser("gen"); g.add_argument("--out", required=True); g.add_argument("--n", type=int, default=2000, help="nº de DIAGRAMAS"); g.add_argument("--chunk", type=int, default=500)
    g.add_argument("--workers", type=int, default=os.cpu_count() or 1); g.add_argument("--shard", type=int, default=0); g.add_argument("--shards", type=int, default=1); g.add_argument("--seed", type=int, default=0)
    g.add_argument("--min-pts", type=int, default=6); g.add_argument("--max-pts", type=int, default=11); g.add_argument("--min-steps", type=int, default=3); g.add_argument("--max-steps", type=int, default=14)
    g.add_argument("--goals", type=int, default=3); g.add_argument("--keep-noaux", type=float, default=.25); g.add_argument("--require-aux", action="store_true")
    d = sp.add_parser("dedupe"); d.add_argument("--out", required=True); d.add_argument("--workers", type=int, default=os.cpu_count() or 1); d.add_argument("--max-type-frac", type=float, default=.30); d.add_argument("--only-aux", action="store_true")
    k = sp.add_parser("tokenize"); k.add_argument("--out", required=True); k.add_argument("--maxlen", type=int, default=384); k.add_argument("--val-pct", type=int, default=2); k.add_argument("--target", choices=("full", "aux"), default="full")
    t = sp.add_parser("train"); t.add_argument("--out", required=True); t.add_argument("--preset", choices=[p for p in PRESETS if p != "ag151m"], default="small"); t.add_argument("--steps", type=int, default=2000)
    t.add_argument("--batch", type=int, default=16); t.add_argument("--lr", type=float, default=1e-3); t.add_argument("--wd", type=float, default=.01); t.add_argument("--warmup", type=int, default=100); t.add_argument("--seed", type=int, default=0)
    t.add_argument("--loss-on", choices=("target", "all"), default="target"); t.add_argument("--log-every", type=int, default=50)
    e = sp.add_parser("eval"); e.add_argument("--out", required=True); e.add_argument("--n", type=int, default=50); e.add_argument("--K", type=int, default=8); e.add_argument("--depth", type=int, default=2); e.add_argument("--seed", type=int, default=0); e.add_argument("--no-lm", dest="lm", action="store_false")
    s = sp.add_parser("solve"); s.add_argument("--problem", required=True); s.add_argument("--goal", required=True); s.add_argument("--mode", choices=("ddar", "random", "lm"), default="ddar"); s.add_argument("--model"); s.add_argument("--K", type=int, default=8); s.add_argument("--depth", type=int, default=2)
    ab = sp.add_parser("agbench", help="roda o benchmark do AlphaGeometry (imo_ag_30.txt / jgex_ag_231.txt)"); ab.add_argument("--file", required=True); ab.add_argument("--timeout", type=float, default=20); ab.add_argument("--tries", type=int, default=25)
    ab.add_argument("--maxfacts", type=int, default=2500); ab.add_argument("--rounds", type=int, default=6); ab.add_argument("--limit", type=int, default=0); ab.add_argument("--seed", type=int, default=0)
    b = sp.add_parser("bench"); b.add_argument("--diagrams", type=int, default=150); b.add_argument("--seed", type=int, default=0); b.add_argument("--require-aux", action="store_true")
    z = sp.add_parser("selftest"); z.add_argument("--seed", type=int, default=0); z.add_argument("--audit", type=int, default=300); z.add_argument("--e2e-diag", type=int, default=150); z.add_argument("--quick", action="store_true", help="pula treino e2e, mantém testes matemáticos e gradiente")
    phase = sp.add_parser("phase1-test", help="testes formais da Fase 1")
    cs = sp.add_parser("certified-solve", help="solver formal com certificado independente")
    cs.add_argument("--given",action="append",default=[],help="fato assumido (repetível)")
    cs.add_argument("--goal",required=True);cs.add_argument("--out")
    ck = sp.add_parser("check-proof", help="valida um certificado JSON")
    ck.add_argument("--file", required=True)
    f = sp.add_parser("formal-parse", help="mostra a AST formalizada como JSON")
    f.add_argument("--text", required=True)
    xx = sp.add_parser("phase23-test", help="testes das extensões das Fases 2 e 3")
    yy = sp.add_parser("phase3-gen", help="gera teoremas com provas verificadas (JSONL/GZIP)")
    yy.add_argument("--out", required=True); yy.add_argument("--n", type=int, default=200)
    yy.add_argument("--seed", type=int, default=0); yy.add_argument("--max-points", type=int, default=12)
    yy.add_argument("--maxfacts", type=int, default=450); yy.add_argument("--shard-size", type=int, default=1000)
    yy.add_argument("--holdout", type=int, default=20)
    yy.add_argument("--dedupe", choices=("none","exact","structural"), default="exact")
    yy.add_argument("--resume", action="store_true")
    yy.add_argument("--workers",type=int,default=1,help="geração em processos, com resultados determinísticos por índice")
    vv = sp.add_parser("phase3-verify", help="verifica independentemente as provas de um dataset")
    vv.add_argument("--out", required=True)
    dd2 = sp.add_parser("ddar2-certified", help="motor incremental com regras da fase 2 certificadas")
    dd2.add_argument("--given", action="append", default=[]); dd2.add_argument("--goal",required=True)
    dd2.add_argument("--maxfacts",type=int,default=2500); dd2.add_argument("--timeout",type=float,default=20.)
    dd2.add_argument("--out")
    ap2 = sp.add_parser("ag2-parse", help="importa linguagem formal do DDAR2 oficial")
    ap2s = ap2.add_mutually_exclusive_group(required=True)
    ap2s.add_argument("--file"); ap2s.add_argument("--text")
    ao = sp.add_parser("ag2-official", help="executa DDAR2 oficial instalado à parte")
    aos = ao.add_mutually_exclusive_group(required=True)
    aos.add_argument("--file"); aos.add_argument("--text")
    ao.add_argument("--official-dir",required=True)
    ao.add_argument("--timeout",type=float,default=120.)
    p = sp.add_parser("pipeline", help="demo ponta a ponta pequeno"); p.add_argument("--out", required=True); p.add_argument("--n", type=int, default=1500); p.add_argument("--steps", type=int, default=300)
    A = ap.parse_args(argv)
    if A.cmd in ("train", "eval", "selftest", "pipeline") and np is None: sys.exit("NumPy é necessário para train/eval/selftest")
    if A.cmd == "ag2-parse": return cmd_ag2_parse_public(A)
    if A.cmd == "ag2-official": return cmd_ag2_official_public(A)
    if A.cmd == "phase23-test": return cmd_phase23_test(A)
    if A.cmd == "phase3-gen": return cmd_phase3_gen(A)
    if A.cmd == "phase3-verify": return cmd_phase3_verify(A)
    if A.cmd == "ddar2-certified": return cmd_ddar2_certified(A)
    if A.cmd == "phase1-test": return cmd_phase1_test(A)
    if A.cmd == "certified-solve": return cmd_certified_solve(A)
    if A.cmd == "check-proof":
        ok, reason = ProofCheckerV2().verify(ProofJSONExporter.load(A.file))
        print(json.dumps({"verified":ok,"reason":reason},ensure_ascii=False)); return 0 if ok else 1
    if A.cmd == "formal-parse":
        print(json.dumps(GeometryPhase1API().parse(A.text).to_dict(),ensure_ascii=False,indent=2)); return 0
    if A.cmd == "gen": cmd_gen(A)
    elif A.cmd == "dedupe": cmd_dedupe(A)
    elif A.cmd == "tokenize": cmd_tokenize(A)
    elif A.cmd == "train": cmd_train(A)
    elif A.cmd == "eval": cmd_eval(A)
    elif A.cmd == "solve":
        mod = Model.load(A.model) if A.model else None; print(json.dumps(solve(A.problem, A.goal, A.mode, mod, A.K, A.depth), ensure_ascii=False))
    elif A.cmd == "bench": cmd_bench(A)
    elif A.cmd == "agbench": cmd_agbench(A)
    elif A.cmd == "selftest": return cmd_selftest(A)
    elif A.cmd == "pipeline":
        ns = lambda **k: argparse.Namespace(**k)
        cmd_gen(ns(out=A.out, n=A.n, chunk=250, shards=1, shard=0, workers=os.cpu_count() or 1, seed=0, min_pts=6, max_pts=11, min_steps=3, max_steps=14, require_aux=False, goals=3, keep_noaux=.4))
        cmd_dedupe(ns(out=A.out, workers=os.cpu_count() or 1, max_type_frac=.35, only_aux=False)); cmd_tokenize(ns(out=A.out, maxlen=384, val_pct=3, target="full"))
        cmd_train(ns(out=A.out, preset="small", steps=A.steps, batch=8, lr=1e-3, wd=.01, warmup=20, seed=0, loss_on="target", log_every=25)); cmd_eval(ns(out=A.out, lm=True, n=20, K=6, depth=2, seed=0))
    return 0
# ═════════════════════ FASE 1: NÚCLEO FORMAL E CERTIFICADOR ═════════════════════
# API aditiva, sem alterar o formato do dataset/LM legado. A validade formal
# é responsabilidade do ProofChecker; num_check é APENAS um filtro numérico.
from dataclasses import dataclass, field
from collections import defaultdict
from typing import Any, Mapping, Optional

_POINT = re.compile(r"^[A-Za-z][A-Za-z0-9_]*$|^\*$")
_TYPES = frozenset(("point", "line", "circle", "segment", "angle", "scalar"))

class GeometrySyntaxError(ValueError):
    """Texto ou árvore geométrica não está de acordo com a gramática."""

class GeometryProofError(ValueError):
    """Passo da demonstração não foi justificado pelo núcleo formal."""

@dataclass(frozen=True)
class PredicateSpec:
    name: str
    arg_types: tuple
    symmetric: bool = False

class GeometryRegistry:
    """Vocabulário tipado extensível. O núcleo antigo permanece compatível."""
    def __init__(self):
        self.predicates: dict[str, PredicateSpec] = {}
        for nm, n in ARITY.items():
            self.register(nm, ("point",) * n)
        for nm, n in {
            "ncoll": 3, "distinct": 2, "overlap": 2, "noverlap": 2,
            "sameclock": 6, "lessthan": 4, "circle": 4,
            "eqangle6": 6, "eqratio6": 6, "eqratio3": 6,
        }.items():
            self.register(nm, ("point",) * n)
        # Expressões lineares são ASTs tipadas, não listas rígidas de pontos.
        for nm in ("angeq", "distmeq", "distseq", "aconst", "rconst",
                   "acompute", "rcompute"):
            self.register(nm, ("scalar",))
    def register(self, name, types, symmetric=False):
        if not _POINT.fullmatch(name) or any(t not in _TYPES for t in types):
            raise GeometrySyntaxError(f"especificação inválida: {name!r}")
        self.predicates[name] = PredicateSpec(name, tuple(types), symmetric)
    def validate(self, name, args):
        spec = self.predicates.get(name)
        if spec is None:
            raise GeometrySyntaxError(f"predicado desconhecido: {name}")
        if len(args) != len(spec.arg_types):
            raise GeometrySyntaxError(f"{name}: esperado {len(spec.arg_types)} argumento(s), recebido {len(args)}")
        for token, typ in zip(args, spec.arg_types):
            if typ == "point" and not _POINT.fullmatch(token):
                raise GeometrySyntaxError(f"nome de ponto inválido: {token!r}")
        return spec

GEOMETRY_REGISTRY = GeometryRegistry()

@dataclass(frozen=True)
class GeoFact:
    kind: str
    args: tuple[str, ...]
    def __post_init__(self):
        GEOMETRY_REGISTRY.validate(self.kind, self.args)
    @classmethod
    def from_tuple(cls, fact):
        return cls(str(fact[0]), tuple(str(x) for x in fact[1:]))
    @property
    def legacy(self):
        t = (self.kind, *self.args)
        return canon(t) if self.kind in MK else t
    def __str__(self):
        return " ".join((self.kind, *self.args))

@dataclass(frozen=True)
class GeoConstruction:
    targets: tuple[str, ...]
    operator: str
    arguments: tuple[str, ...]
    def __post_init__(self):
        if not self.targets or any(not _POINT.fullmatch(x) or x == "*" for x in self.targets):
            raise GeometrySyntaxError("nomes de construção inválidos")
        if not _POINT.fullmatch(self.operator):
            raise GeometrySyntaxError("operador de construção inválido")
    def __str__(self):
        return f"{' '.join(self.targets)} = {self.operator}" + (" " + " ".join(self.arguments) if self.arguments else "")

@dataclass(frozen=True)
class GeometryAST:
    constructions: tuple[GeoConstruction, ...] = ()
    hypotheses: tuple[GeoFact, ...] = ()
    goal: Optional[GeoFact] = None
    points: tuple[str, ...] = ()
    def to_dict(self):
        return {"constructions": [dict(targets=list(x.targets), operator=x.operator,
                                       arguments=list(x.arguments)) for x in self.constructions],
                "hypotheses": [str(x) for x in self.hypotheses],
                "goal": str(self.goal) if self.goal else None,
                "points": list(self.points)}

class GeometryLexer:
    """Quebra sentenças do DSL em palavras, pontuação e expressões simples."""
    _pat = re.compile(r"=>|!=|<=|>=|[;=+*/(),?\-]|[A-Za-z][A-Za-z0-9_]*|\d+(?:/\d+)?|\S")
    def tokenize(self, source):
        return tuple(self._pat.findall(source))

class GeometryParser:
    """Aceita construções históricas, 'given ...', 'prove ...' e '? ...'."""
    def __init__(self, registry=None): self.registry = registry or GEOMETRY_REGISTRY
    def fact(self, source):
        tokens = source.strip().replace(",", " ").split()
        if not tokens: raise GeometrySyntaxError("fato vazio")
        self.registry.validate(tokens[0], tokens[1:])
        return GeoFact(tokens[0], tuple(tokens[1:]))
    def parse(self, source):
        cons, hyps, goal, points = [], [], None, set()
        source = re.sub(r"\?\s*(?=[A-Za-z])", "; prove ", source)
        for clause in (s.strip() for s in source.split(";")):
            if not clause: continue
            if clause.startswith(("given ", "assume ")):
                f = self.fact(clause.split(None, 1)[1]); hyps.append(f)
                points.update(x for x in f.args if _POINT.fullmatch(x))
            elif clause.startswith(("prove ", "goal ")):
                if goal is not None: raise GeometrySyntaxError("duas conclusões no mesmo problema")
                goal = self.fact(clause.split(None, 1)[1]); points.update(goal.args)
            elif "=" in clause:
                left, right = clause.split("=", 1)
                t, a = right.split(None, 1) if len(right.split(None, 1)) == 2 else (right.strip(), "")
                cs = GeoConstruction(tuple(left.split()), t, tuple(a.split()))
                cons.append(cs); points.update(cs.targets)
                points.update(x for x in cs.arguments if _POINT.fullmatch(x))
            else:
                f = self.fact(clause); hyps.append(f); points.update(f.args)
        return GeometryAST(tuple(cons), tuple(hyps), goal, tuple(sorted(points)))

class GeometryTypeChecker:
    """Rejeita referências futuras e nomes duplicados, sem inventar pré-condições."""
    def validate(self, ast: GeometryAST, free_points=()):
        known = set(free_points)
        for item in ast.constructions:
            if len(set(item.targets)) != len(item.targets) or any(x in known for x in item.targets):
                raise GeometrySyntaxError(f"ponto redefinido: {item}")
            if item.operator == "triangle":
                if len(item.targets) != 3 or item.arguments:
                    raise GeometrySyntaxError("triangle deve introduzir exatamente 3 pontos")
            elif item.operator not in CONS and item.operator not in globals().get("AGS", {}):
                # Operadores customizados podem ser registrados em outra camada.
                raise GeometrySyntaxError(f"construção desconhecida: {item.operator}")
            else:
                n = CONS[item.operator][0] if item.operator in CONS else AGS[item.operator][0]
                if len(item.arguments) != n:
                    raise GeometrySyntaxError(f"aridade inválida: {item}")
                if not all(x in known for x in item.arguments):
                    raise GeometrySyntaxError(f"referência anterior inexistente: {item}")
            known.update(item.targets)
        for fact in (*ast.hypotheses, *((ast.goal,) if ast.goal is not None else ())):
            for point in fact.args:
                if _POINT.fullmatch(point) and point != "*" and point not in known:
                    # Permite enunciados puramente declarativos, sem construções.
                    if ast.constructions: raise GeometrySyntaxError(f"ponto não declarado: {point}")
        return True

class VariableScope:
    def __init__(self): self.frames = [set()]
    def enter(self): self.frames.append(set())
    def declare(self, name):
        if any(name in frame for frame in self.frames):
            raise GeometrySyntaxError(f"nome repetido: {name}")
        self.frames[-1].add(name)
    def contains(self, name): return any(name in f for f in self.frames)
    def exit(self):
        if len(self.frames) == 1: raise GeometrySyntaxError("não se pode sair do escopo global")
        self.frames.pop()

class GeometryCanonicalizer:
    def fact(self, fact):
        g = fact if isinstance(fact, GeoFact) else GeoFact.from_tuple(fact)
        return GeoFact.from_tuple(g.legacy)
    def goal(self, goal): return self.fact(goal)
    def statement(self, fact): return str(self.fact(fact))

class GeometryDSLSerializer:
    def dumps(self, ast):
        entries = [str(c) for c in ast.constructions]
        entries += ["given " + str(f) for f in ast.hypotheses]
        if ast.goal: entries.append("prove " + str(ast.goal))
        return " ; ".join(entries)
    def loads(self, text): return GeometryParser().parse(text)

class LinearExpression:
    """Combinação racional esparsa. Não aproxima frações por ponto flutuante."""
    def __init__(self, terms=None, constant=0):
        d = defaultdict(Fraction)
        for key, value in (terms or {}).items(): d[str(key)] += Fraction(value)
        self.terms = {k:v for k,v in d.items() if v}
        self.constant = Fraction(constant)
    def __add__(self, other):
        if not isinstance(other, LinearExpression): other = LinearExpression(constant=other)
        d = defaultdict(Fraction, self.terms)
        for k, v in other.terms.items(): d[k] += v
        return LinearExpression(d, self.constant + other.constant)
    def __neg__(self): return self * -1
    def __sub__(self, other): return self + (-other if isinstance(other, LinearExpression) else -Fraction(other))
    def __mul__(self, scalar):
        scalar = Fraction(scalar)
        return LinearExpression({k:v * scalar for k,v in self.terms.items()}, self.constant * scalar)
    __rmul__ = __mul__
    def __eq__(self, other):
        return isinstance(other, LinearExpression) and self.terms == other.terms and self.constant == other.constant
    def to_dict(self): return {"terms": {k:str(v) for k,v in sorted(self.terms.items())}, "constant":str(self.constant)}

class LinearExpressionParser:
    """Gramática segura: '2*AB - CD + 3/2*EF - 1/3', sem eval()."""
    _term = re.compile(r"(?P<sign>[+\-]?)\s*(?:(?P<coef>\d+(?:/\d+)?)\s*\*\s*)?(?P<name>[A-Za-z][A-Za-z0-9_]*|\d+(?:/\d+)?)")
    def parse(self, source):
        result = LinearExpression(); pos = 0
        source = source.strip().replace(" ", "")
        for match in self._term.finditer(source):
            if match.start() != pos: raise GeometrySyntaxError(f"expressão inválida perto de: {source[pos:]}")
            pos = match.end(); sign = -1 if match["sign"] == "-" else 1
            coef = Fraction(match["coef"] or 1) * sign
            if match["name"][0].isdigit(): result += LinearExpression(constant=coef * Fraction(match["name"]))
            else: result += LinearExpression({match["name"]:coef})
        if pos != len(source) or pos == 0: raise GeometrySyntaxError(f"expressão inválida: {source}")
        return result

class GeometryUnionFind:
    def __init__(self): self.parent = {}; self.rank = {}
    def add(self, x):
        if x not in self.parent: self.parent[x], self.rank[x] = x, 0
    def find(self, x):
        self.add(x)
        if self.parent[x] != x: self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb: return False
        if self.rank[ra] < self.rank[rb]: ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]: self.rank[ra] += 1
        return True

@dataclass(frozen=True)
class PointNode:
    name: str

@dataclass(frozen=True)
class LineNode:
    points: frozenset[str]

@dataclass(frozen=True)
class CircleNode:
    points: frozenset[str]

@dataclass(frozen=True)
class SegmentNode:
    ends: tuple[str,str]

@dataclass(frozen=True)
class AngleNode:
    legs: tuple[tuple[str,str],tuple[str,str]]

@dataclass(frozen=True)
class TriangleNode:
    vertices: tuple[str,str,str]

@dataclass(frozen=True)
class PredicateNode:
    fact: GeoFact

@dataclass(frozen=True)
class ConstructionNode:
    construction: GeoConstruction

@dataclass(frozen=True)
class ProofDependencyNode:
    output: GeoFact
    inputs: tuple[GeoFact,...]

class FactIndex:
    def __init__(self): self.by_kind = defaultdict(set); self.by_point = defaultdict(set)
    def add(self, fact):
        self.by_kind[fact.kind].add(fact)
        for p in fact.args: self.by_point[p].add(fact)
    def query(self, kind=None, point=None):
        if kind is None and point is None: return set().union(*self.by_kind.values()) if self.by_kind else set()
        if kind is None: return set(self.by_point.get(point, ()))
        if point is None: return set(self.by_kind.get(kind, ()))
        return self.by_kind.get(kind, set()) & self.by_point.get(point, set())

class GeometryGraph:
    """Grafo simbólico; equivalência explícita NÃO é inferida de coordenadas."""
    def __init__(self):
        self.points: dict[str, PointNode] = {}
        self.facts: set[GeoFact] = set()
        self.index = FactIndex()
        self.aliases = GeometryUnionFind()
        self.dependencies: dict[GeoFact, tuple[GeoFact,...]] = {}
        self.lines: set[LineNode] = set()
        self.circles: set[CircleNode] = set()
        self.length_classes = GeometryUnionFind()
        self.parallel_classes = GeometryUnionFind()
        self.similar_triangles = GeometryUnionFind()
        self.congruent_triangles = GeometryUnionFind()
    def add_point(self, name):
        if not _POINT.fullmatch(name) or name == "*": raise GeometrySyntaxError(f"ponto inválido: {name}")
        self.points.setdefault(name, PointNode(name)); self.aliases.add(name)
    def add_fact(self, fact, parents=()):
        fact = GeometryCanonicalizer().fact(fact)
        for name in fact.args:
            if _POINT.fullmatch(name) and name != "*": self.add_point(name)
        if fact in self.facts: return False
        self.facts.add(fact); self.index.add(fact)
        self.dependencies[fact] = tuple(GeometryCanonicalizer().fact(p) for p in parents)
        if fact.kind == "overlap": self.aliases.union(*fact.args)
        if fact.kind == "coll": self.lines.add(LineNode(frozenset(fact.args)))
        if fact.kind == "cyclic": self.circles.add(CircleNode(frozenset(fact.args)))
        if fact.kind == "cong":
            a,b,c,d = fact.args; self.length_classes.union(L2(a,b), L2(c,d))
        if fact.kind == "para":
            a,b,c,d = fact.args; self.parallel_classes.union(L2(a,b), L2(c,d))
        return True
    def equivalent_points(self, a, b): return self.aliases.find(a) == self.aliases.find(b)
    def facts_at_point(self, name): return self.index.query(point=name)
    def facts_of_kind(self, name): return self.index.query(kind=name)
    def canonical_state_hash(self):
        data = '\n'.join(sorted(map(str,self.facts)))
        return hashlib.sha256(data.encode()).hexdigest()

class ExactLinearSystem:
    """Eliminação gaussiana racional com testemunho de combinação linear."""
    def __init__(self): self.rows = {}; self.equations = []
    @staticmethod
    def _clean(row): return {str(k):Fraction(v) for k,v in row.items() if Fraction(v)}
    def _reduce(self, row, trace):
        v = self._clean(row); witness = defaultdict(Fraction, trace)
        for pivot in sorted(self.rows):
            if pivot not in v: continue
            base, combination = self.rows[pivot]
            fac = v[pivot]
            for k, x in base.items():
                v[k] = v.get(k,Fraction()) - fac*x
                if not v[k]: del v[k]
            for k, x in combination.items():
                witness[k] -= fac*x
                if not witness[k]: del witness[k]
        return v, dict(witness)
    def add(self, row, label):
        if label in (x[0] for x in self.equations): raise ValueError("rótulo de equação duplicado")
        self.equations.append((label,self._clean(row)))
        v, witness = self._reduce(row, {label:Fraction(1)})
        if not v: return False
        pivot = min(v); d = v[pivot]
        self.rows[pivot] = ({k:x/d for k,x in v.items()}, {k:x/d for k,x in witness.items()})
        return True
    def prove(self, target):
        remainder, witness = self._reduce(target,{})
        return (not remainder, {k:-v for k,v in witness.items() if v})
    def check_witness(self, target, coefficients):
        expr = defaultdict(Fraction)
        for label, row in self.equations:
            for k,v in row.items(): expr[k] += Fraction(coefficients.get(label,0))*v
        return self._clean(expr)==self._clean(target)

class AngleLattice:
    """Congruências inteiras mod pi: combinações só com coeficientes INTEIROS.

    A constante 'K' denota pi/2 e a relação 2K=0 é um axioma do módulo pi.
    Não permite divisão imprópria de equações congruenciais por 2.
    """
    def __init__(self): self.equations=[]
    def add(self, equation, label):
        row = {str(k):int(v) for k,v in equation.items() if int(v)}
        if any(Fraction(v).denominator != 1 for v in equation.values()):
            raise GeometrySyntaxError("coeficientes angulares devem ser inteiros")
        if label in {x[0] for x in self.equations}: raise ValueError("rótulo duplicado")
        self.equations.append((label,row))
    @staticmethod
    def _combine(a,b,factor):
        out = defaultdict(int,a)
        for k,v in b.items(): out[k] += factor*v
        return {k:v for k,v in out.items() if v}
    @staticmethod
    def _pivot(row): return min(row, key=lambda k:(k == "K", k))
    def prove(self, target):
        """Decide pertinência à rede inteira via eliminação Euclidiana."""
        source = list(self.equations) + [("__mod_pi__",{"K":2})]
        rows = [(dict(row), {name:1}) for name,row in source if row]
        pivots = {}
        while rows:
            order = sorted({k for row,_ in rows for k in row},key=lambda k:(k=="K",k))
            if not order: break
            col = order[0]; hits = [(r,c) for r,c in rows if r.get(col)]
            others = [(r,c) for r,c in rows if not r.get(col)]
            pivot, certificate = hits.pop(0)
            while hits:
                r, cert = hits.pop()
                x,y = pivot[col],r[col]
                q = y//x
                r = self._combine(r,pivot,-q)
                cert = self._combine(cert,certificate,-q)
                if r.get(col):
                    if abs(r[col]) < abs(pivot[col]):
                        hits.append((pivot,certificate)); pivot,certificate=r,cert
                    else: hits.append((r,cert))
                elif r: others.append((r,cert))
            if pivot[col] < 0:
                pivot = {k:-v for k,v in pivot.items()}; certificate={k:-v for k,v in certificate.items()}
            pivots[col] = (pivot,certificate)
            rows = others
        vec = {str(k):int(v) for k,v in target.items() if int(v)}
        trace = {}
        for col in sorted(pivots,key=lambda k:(k=="K",k)):
            if col not in vec: continue
            pivot, cert = pivots[col]
            q, rem = divmod(vec[col],pivot[col])
            if rem: return False, {}
            vec = self._combine(vec,pivot,-q)
            trace = self._combine(trace,cert,q)
        return not vec, trace if not vec else {}
    def check_witness(self,target,trace):
        rows = dict(self.equations); rows["__mod_pi__"]={"K":2}
        v={}
        for label, k in trace.items():
            if label not in rows or not isinstance(k,int): return False
            v=self._combine(v,rows[label],k)
        return v == {str(k):int(x) for k,x in target.items() if int(x)}

class AlgebraProofSystem:
    """Álgebra exata certificável: direções mod pi e log-distâncias."""
    def __init__(self): self.angles=AngleLattice(); self.loglengths=ExactLinearSystem(); self.distances=ExactLinearSystem()
    def add_angle(self,eq,label): self.angles.add(eq,label)
    def add_loglength(self,eq,label): return self.loglengths.add(eq,label)
    def add_distance(self,eq,label): return self.distances.add(eq,label)

class NonDegeneracyGuard:
    @staticmethod
    def required_for(fact):
        kind= fact.kind if isinstance(fact, GeoFact) else fact[0]
        names= fact.args if isinstance(fact, GeoFact) else fact[1:]
        if kind in ("para","perp","cong","eqangle","eqratio"):
            return frozenset(L2(names[i],names[i+1]) for i in range(0,len(names),2))
        if kind == "midp": return frozenset((L2(names[1],names[2]),))
        if kind == "coll": return frozenset(L2(a,b) for a,b in itertools.combinations(names,2))
        if kind == "simtri":
            return frozenset(L2(a,b) for tri in (names[:3],names[3:]) for a,b in itertools.combinations(tri,2))
        if kind == "cyclic": return frozenset(L2(a,b) for a,b in itertools.combinations(names,2))
        return frozenset()

class NumericalGeometryGuard:
    """Verificação numérica conservadora. Nunca fornece prova universal."""
    @staticmethod
    def check(stmt, coords, eps=1e-7):
        if any(x not in coords for x in stmt[1:]): return False
        names=stmt[1:]; t=stmt[0]
        points=[coords[x] for x in names]
        if not all(math.isfinite(q) for pt in points for q in pt): return False
        scale=max(1.0,max((dist(a,b) for a,b in itertools.combinations(points,2)),default=1))
        z=eps*scale
        if t == "coll":
            if len(set(names))<3 or any(dist(a,b)<=z for a,b in itertools.combinations(points,2)):
                return False
        if t in ("para","perp","cong","eqangle","eqratio"):
            if any(dist(coords[names[i]],coords[names[i+1]]) <= z for i in range(0,len(names),2)):
                return False
        if t == "midp" and dist(points[1],points[2]) <= z: return False
        if t == "cyclic":
            if any(dist(a,b)<=z for a,b in itertools.combinations(points,2)): return False
            if max(abs(area2(*tri)) for tri in itertools.combinations(points,3)) <= eps*scale*scale:
                return False
        if t == "simtri":
            if abs(area2(*points[:3]))<=eps*scale*scale or abs(area2(*points[3:]))<=eps*scale*scale:
                return False
        return bool(num_check_legacy(stmt,coords,eps))

# Substitui a verificação legada por uma guarda que impede segmentos nulos e
# dados não finitos. A função numérica não se transforma em critério de prova.
num_check_legacy = num_check
def num_check(s,C,eps=1e-6):
    return NumericalGeometryGuard.check(s,C,eps)

@dataclass(frozen=True)
class ProofStep:
    conclusion: GeoFact
    rule: str
    premises: tuple[GeoFact,...] = ()
    data: tuple[tuple[str,str],...] = ()
    def to_dict(self):
        return {"conclusion":str(self.conclusion),"rule":self.rule,
                "premises":[str(q) for q in self.premises],"data":dict(self.data)}

@dataclass(frozen=True)
class ProofCertificate:
    assumptions: tuple[GeoFact,...]
    goal: GeoFact
    steps: tuple[ProofStep,...]
    metadata: Mapping[str,Any] = field(default_factory=dict)
    def to_dict(self):
        return {"schema":"geoforge-proof-v1", "assumptions":[str(x) for x in self.assumptions],
                "goal":str(self.goal),"steps":[x.to_dict() for x in self.steps],
                "metadata":dict(self.metadata)}
    def to_json(self): return json.dumps(self.to_dict(),ensure_ascii=False,indent=2)
    @classmethod
    def from_dict(cls,raw):
        if raw.get("schema")!="geoforge-proof-v1": raise GeometrySyntaxError("versão de certificado não suportada")
        p=GeometryParser(); assumptions=tuple(p.fact(x) for x in raw["assumptions"])
        goal=p.fact(raw["goal"]); steps=[]
        for row in raw["steps"]:
            steps.append(ProofStep(p.fact(row["conclusion"]),row["rule"],
                                   tuple(p.fact(x) for x in row["premises"]),
                                   tuple(sorted(row.get("data",{}).items()))))
        return cls(assumptions,goal,tuple(steps),raw.get("metadata",{}))
    @classmethod
    def from_closure(cls,closure,goal):
        """Exporta rastros legados; a exportação NÃO certifica sua solidez."""
        if goal not in closure.facts: raise GeometryProofError("meta não deduzida")
        trace=closure.explain(goal)
        assumptions=tuple(GeoFact.from_tuple(x) for x in sorted(closure.given))
        steps=tuple(ProofStep(GeoFact.from_tuple(output),rule,
                             tuple(GeoFact.from_tuple(q) for q in prem))
                    for rule,prem,output in trace if rule!="given")
        return cls(assumptions,GeoFact.from_tuple(goal),steps,{"source":"legacy-closure", "certified":False})

class ProofChecker:
    """Núcleo separado: só aceita regras verificáveis a partir de premissas.

    Regras experimentais do motor legado não são confiadas automaticamente.
    Condições como ncoll e distinct são hipóteses EXPLÍCITAS da prova.
    """
    def __init__(self): self.parser=GeometryParser()
    @staticmethod
    def _canon(f): return GeometryCanonicalizer().fact(f)
    @staticmethod
    def _noncoll(known,a,b,c):
        return GeoFact("ncoll",tuple((a,b,c))) in known or any(
            x.kind=="ncoll" and set(x.args)=={a,b,c} for x in known)
    @classmethod
    def _distinct(cls,known,a,b):
        if a==b: return False
        return (GeoFact("distinct",(a,b)) in known or GeoFact("distinct",(b,a)) in known
                or GeoFact("noverlap",(a,b)) in known or GeoFact("noverlap",(b,a)) in known
                or any(f.kind=="ncoll" and a in f.args and b in f.args for f in known))
    @classmethod
    def _rule(cls,step,known):
        s=step.conclusion; p=step.premises
        if step.rule=="midp_coll" and len(p)==1:
            m=p[0]
            return m.kind=="midp" and s.legacy==mk_coll(*m.args)
        if step.rule=="midline" and len(p)==2 and all(f.kind=="midp" for f in p) and s.kind=="para":
            u,v=p; e1,e2=set(u.args[1:]),set(v.args[1:]); shared=e1&e2
            if len(shared)!=1 or u.args[0]==v.args[0]: return False
            a=next(iter(shared)); b=next(iter(e1-shared)); c=next(iter(e2-shared))
            return cls._noncoll(known,a,b,c) and s.legacy==mk_para(u.args[0],v.args[0],b,c)
        if step.rule=="para_shared_coll" and len(p)==1 and p[0].kind=="para" and s.kind=="coll":
            a,b,c,d=p[0].args
            if len({a,b,c,d})!=3: return False
            shared=set((a,b))&set((c,d))
            return (len(shared)==1 and cls._distinct(known,a,b)
                    and cls._distinct(known,c,d) and s.legacy==mk_coll(*set((a,b,c,d))))
        if step.rule=="coll_cong_midp" and len(p)==2 and s.kind=="midp":
            coll=next((x for x in p if x.kind=="coll"),None)
            cong=next((x for x in p if x.kind=="cong"),None)
            if coll is None or cong is None: return False
            m,a,b=s.args
            return (set(coll.args)=={m,a,b} and
                    cong.legacy==mk_cong(m,a,m,b) and cls._distinct(known,a,b))
        if step.rule=="coll_merge" and s.kind=="coll" and len(p)>0 and all(x.kind=="coll" for x in p):
            # Duas relações colineares podem ser fundidas se compartilharem
            # DOIS pontos comprovadamente distintos (não só dois nomes).
            sets=[set(x.args) for x in p]
            changed=True
            while changed:
                changed=False
                for i in range(len(sets)):
                    for j in range(i+1,len(sets)):
                        common=sets[i]&sets[j]
                        if any(cls._distinct(known,a,b) for a,b in itertools.combinations(common,2)):
                            sets[i]|=sets[j]; sets.pop(j); changed=True; break
                    if changed:break
            return any(set(s.args)<=group for group in sets)
        if step.rule=="cyclic_merge" and s.kind=="cyclic" and len(p)>0 and all(x.kind=="cyclic" for x in p):
            sets=[set(x.args) for x in p]; changed=True
            while changed:
                changed=False
                for i in range(len(sets)):
                    for j in range(i+1,len(sets)):
                        common=sets[i]&sets[j]
                        if any(cls._noncoll(known,*tri) for tri in itertools.combinations(common,3)):
                            sets[i]|=sets[j]; sets.pop(j); changed=True; break
                    if changed: break
            return any(set(s.args)<=group for group in sets)
        return False
    def verify(self,certificate,raise_on_error=False):
        if isinstance(certificate,dict): certificate=ProofCertificate.from_dict(certificate)
        if not isinstance(certificate,ProofCertificate): raise TypeError("certificado esperado")
        consistent, message = GeometryAssumptionConsistency.check(certificate.assumptions)
        if not consistent:
            if raise_on_error: raise GeometryProofError(message)
            return False,message
        known={self._canon(f) for f in certificate.assumptions}
        for i,step in enumerate(certificate.steps,1):
            f=self._canon(step.conclusion); ps=tuple(self._canon(p) for p in step.premises)
            if any(p not in known for p in ps):
                reason=f"passo {i}: premissa não demonstrada"
                if raise_on_error:raise GeometryProofError(reason)
                return False,reason
            checked=ProofStep(f,step.rule,ps,step.data)
            if step.rule == "given":
                result=f in known
            elif step.rule in ("ar_ang","ar_len"):
                result=self._check_algebra(checked,known)
            else: result=self._rule(checked,known)
            if not result:
                reason=f"passo {i}: regra '{step.rule}' não certificada para {f}"
                if raise_on_error:raise GeometryProofError(reason)
                return False,reason
            known.add(f)
        if self._canon(certificate.goal) not in known:
            reason="meta não alcançada"
            if raise_on_error: raise GeometryProofError(reason)
            return False,reason
        return True,"prova certificada"
    @classmethod
    def _check_algebra(cls,step,known):
        # Para evitar um falso teorema, só relações de ângulos entre retas não
        # degeneradas ou de log-comprimentos não nulos entram no sistema exato.
        if step.conclusion.kind not in ("para","perp","cong","eqangle","eqratio"):
            return False
        ps=step.premises
        if not ps: return False
        nonzero=lambda a,b: cls._distinct(known,a,b)
        for fact in (*ps,step.conclusion):
            if any(not nonzero(a,b) for a,b in NonDegeneracyGuard.required_for(fact)):
                return False
            if fact.kind == "cyclic" and not any(
                cls._noncoll(known,*tri) for tri in itertools.combinations(fact.args,3)):
                return False
            if fact.kind == "simtri" and not all(
                cls._noncoll(known,*tri) for tri in (fact.args[:3],fact.args[3:])):
                return False
        vi=VarIdx()
        rows=[]; wanted=[]
        for j,fact in enumerate(ps):
            for t,r in stmt_rows(fact.legacy,vi):
                rows.append((t,{str(k) if k!=0 else "K":_sg(v) for k,v in r.items()},f"p{j}"))
        for t,r in stmt_rows(step.conclusion.legacy,vi):
            wanted.append((t,{str(k) if k!=0 else "K":_sg(v) for k,v in r.items()}))
        if not wanted: return False
        aa=AngleLattice(); ll=ExactLinearSystem()
        for i,(t,r,label) in enumerate(rows):
            label=f"{label}_{i}"
            if t=="a": aa.add(r,label)
            if t=="l": ll.add(r,label)
        return all((aa.prove(r)[0] if t=="a" else ll.prove(r)[0]) for t,r in wanted)

class ProofJSONExporter:
    @staticmethod
    def dump(certificate,path): Path(path).write_text(certificate.to_json(),encoding="utf-8")
    @staticmethod
    def load(path): return ProofCertificate.from_dict(json.loads(Path(path).read_text(encoding="utf-8")))

class ProofReplayEngine:
    def replay(self,path): return ProofChecker().verify(ProofJSONExporter.load(path))

class ProofDependencyDAG:
    def __init__(self,certificate):
        self.nodes={step.conclusion:step.premises for step in certificate.steps}
    def ancestors(self,goal):
        seen=set(); stack=[goal]
        while stack:
            node=stack.pop()
            if node in seen: continue
            seen.add(node); stack.extend(self.nodes.get(node,()))
        return seen

class ProofMinimizer:
    def minimize(self,certificate):
        needed=ProofDependencyDAG(certificate).ancestors(certificate.goal)
        return ProofCertificate(certificate.assumptions,certificate.goal,
                                tuple(s for s in certificate.steps if s.conclusion in needed),
                                certificate.metadata)

class NumericalCounterexampleFinder:
    """Contraexemplos refutam; ausência de contraexemplo NÃO comprova."""
    def find(self,claim,diagram_factory,trials=100,seed=0):
        rng=random.Random(seed)
        for _ in range(trials):
            coords=diagram_factory(rng)
            if coords is not None and not num_check(claim,coords):return coords
        return None

class GeometryPhase1API:
    """Entrada unificada para explorar o subsistema formal e emitir provas."""
    def __init__(self):
        self.parser=GeometryParser(); self.types=GeometryTypeChecker()
        self.checker=ProofChecker()
    def parse(self,text):
        ast=self.parser.parse(text); self.types.validate(ast); return ast
    def verify_json(self,text): return self.checker.verify(ProofCertificate.from_dict(json.loads(text)))


class GeometryAssumptionConsistency:
    """Detecta contradições estruturais explícitas; não decide toda a geometria."""
    @staticmethod
    def check(facts):
        fs={GeometryCanonicalizer().fact(f) for f in facts}
        same=GeometryUnionFind()
        for f in fs:
            if f.kind=="overlap":same.union(*f.args)
        for f in fs:
            if f.kind in ("distinct","noverlap") and same.find(f.args[0])==same.find(f.args[1]):
                return False,f"{f}: simultaneamente coincidentes e distintos"
            if f.kind=="ncoll" and len({same.find(p) for p in f.args})!=3:
                return False,f"{f}: três pontos não distintos"
            if f.kind=="ncoll" and any(x.kind=="coll" and set(x.args)==set(f.args) for x in fs):
                return False,f"{f}: colineares e não colineares"
        return True,"nenhuma contradição estrutural explícita detectada"

class CertifiedDeductionEngine:
    """Motor formal PEQUENO e independente do Closure legado.

    Não executa uma regra antes de ProofChecker validá-la. Aceita premissas
    explícitas de não degenerescência, e emite certificados replayáveis.
    Esta API não pretende reproduzir a cobertura DDAR2 da Fase 2.
    """
    def __init__(self,assumptions,maxfacts=2000):
        self.assumptions=tuple(GeometryCanonicalizer().fact(x) for x in assumptions)
        ok,reason=GeometryAssumptionConsistency.check(self.assumptions)
        if not ok:raise GeometryProofError(reason)
        self.known=set(self.assumptions); self.steps=[]; self.graph=GeometryGraph()
        self.checker=ProofChecker(); self.maxfacts=maxfacts
        for fact in self.assumptions:self.graph.add_fact(fact)
    def add(self,conclusion,rule,premises):
        f=GeometryCanonicalizer().fact(conclusion)
        if f in self.known or len(self.known)>=self.maxfacts:return False
        ps=tuple(GeometryCanonicalizer().fact(x) for x in premises)
        if not all(p in self.known for p in ps):return False
        step=ProofStep(f,rule,ps)
        if not self.checker._rule(step,self.known):return False
        self.known.add(f);self.graph.add_fact(f,ps);self.steps.append(step)
        return True
    def close(self,rounds=12):
        for _ in range(rounds):
            count=0
            mids=tuple(x for x in self.known if x.kind=="midp")
            for m in mids:
                count+=self.add(GeoFact("coll",tuple(m.args)),"midp_coll",(m,))
            for u,v in itertools.combinations(mids,2):
                e1,e2=set(u.args[1:]),set(v.args[1:]);shared=e1&e2
                if len(shared)!=1 or u.args[0]==v.args[0]:continue
                a=next(iter(shared));b=next(iter(e1-shared));c=next(iter(e2-shared))
                count+=self.add(GeoFact.from_tuple(mk_para(u.args[0],v.args[0],b,c)),"midline",(u,v))
            colls=tuple(x for x in self.known if x.kind=="coll")
            congs=tuple(x for x in self.known if x.kind=="cong")
            for col in colls:
                for m,a,b in itertools.permutations(col.args,3):
                    for cg in congs:
                        if cg.legacy==mk_cong(m,a,m,b):
                            count+=self.add(GeoFact.from_tuple(mk_midp(m,a,b)),"coll_cong_midp",(col,cg))
            paras=tuple(x for x in self.known if x.kind=="para")
            for p in paras:
                a,b,c,d=p.args
                if len({a,b,c,d})==3:
                    count+=self.add(GeoFact.from_tuple(mk_coll(*set((a,b,c,d)))),"para_shared_coll",(p,))
            if not count:break
        return self
    def certificate(self,goal):
        g=GeometryCanonicalizer().fact(goal)
        if g not in self.known:return None
        cert=ProofCertificate(self.assumptions,g,tuple(self.steps),{"engine":"certified-phase1"})
        cert=ProofMinimizer().minimize(cert)
        ok,reason=self.checker.verify(cert)
        if not ok:raise GeometryProofError(f"erro interno de certificação: {reason}")
        return cert

class AlgebraicCertificateVerifier:
    """Testemunhos lineares exatos podem ser reproduzidos sem o solver."""
    @staticmethod
    def rational(equations,target,witness):
        s=ExactLinearSystem()
        for label,row in equations:s.add(row,label)
        return s.check_witness(target,witness)
    @staticmethod
    def angles(equations,target,witness):
        s=AngleLattice()
        for label,row in equations:s.add(row,label)
        return s.check_witness(target,witness)

class FormalGeometryCompiler:
    """Compila predicados e equações tipadas sem usar eval()."""
    def __init__(self): self.expressions=LinearExpressionParser()
    def compile_relation(self,kind,relation):
        if kind not in ("angeq","distmeq","distseq"):
            raise GeometrySyntaxError(f"equação não suportada: {kind}")
        parts=relation.split("=")
        if len(parts)!=2:raise GeometrySyntaxError("equação precisa ter exatamente um sinal =")
        return self.expressions.parse(parts[0])-self.expressions.parse(parts[1])
    def compile_fact(self,statement):
        item=GeometryParser().fact(statement)
        if item.kind in ("angeq","distmeq","distseq"):
            return item,self.compile_relation(item.kind,item.args[0])
        return item,None

class GeometryProofAuditor:
    """Audita rastros sem elevar uma verificação numérica a prova formal."""
    def audit_closure(self,closure,goal):
        cert=ProofCertificate.from_closure(closure,goal)
        ok,reason=ProofChecker().verify(cert)
        return {"deduced_by_legacy":True,"formally_verified":ok,
                "reason":reason,"certificate":cert.to_dict()}


def cmd_certified_solve(a):
    parser=GeometryParser()
    givens=tuple(parser.fact(text) for text in a.given)
    goal=parser.fact(a.goal)
    try:
        engine=CertifiedDeductionEngine(givens).close()
        cert=engine.certificate(goal)
    except (GeometryProofError,GeometrySyntaxError) as exc:
        print(json.dumps({"solved":False,"reason":str(exc)},ensure_ascii=False))
        return 1
    if cert is None:
        print(json.dumps({"solved":False,"reason":"não demonstrado pelo núcleo certificado da Fase 1"},ensure_ascii=False))
        return 1
    if a.out:ProofJSONExporter.dump(cert,a.out)
    print(json.dumps({"solved":True,"certificate":cert.to_dict()},ensure_ascii=False,indent=2))
    return 0


# ── AST adicional: lugares geométricos, incógnitas e equações ──
@dataclass(frozen=True)
class FreePointPlaceholder:
    token: str = "*"
    def __post_init__(self):
        if self.token != "*": raise GeometrySyntaxError("único marcador livre aceito: *")

@dataclass(frozen=True)
class LocusExpression:
    moving_point: str
    predicate: GeoFact
    def __post_init__(self):
        if not _POINT.fullmatch(self.moving_point): raise GeometrySyntaxError("ponto móvel inválido")
        if self.moving_point not in self.predicate.args:
            raise GeometrySyntaxError("o ponto móvel precisa ocorrer no lugar geométrico")

@dataclass(frozen=True)
class NonConstructiveStatement:
    constraints: tuple[GeoFact,...]
    quantified_points: tuple[str,...] = ()
    def __post_init__(self):
        if not self.constraints: raise GeometrySyntaxError("restrições vazias")
        if any(not _POINT.fullmatch(x) for x in self.quantified_points):
            raise GeometrySyntaxError("quantificação com ponto inválido")

class GoalNormalizer(GeometryCanonicalizer):
    pass

class AG1AG2Compatibility:
    """Importação de enunciados legados; não inventa suporte a novos operadores."""
    def __init__(self): self.parser=GeometryParser(); self.serializer=GeometryDSLSerializer()
    def parse_legacy_problem(self,problem,goal):
        ast=self.parser.parse(problem + "; prove " + goal)
        GeometryTypeChecker().validate(ast)
        return ast
    def export_legacy_goal(self,goal):
        f=GeometryCanonicalizer().fact(goal)
        if f.kind not in ARITY:
            raise GeometrySyntaxError("meta fora do subconjunto legado")
        return str(f)

# ── índices semânticos para fatos geométricos ──
class IncidenceIndex:
    def __init__(self): self.point_to_lines=defaultdict(set); self.point_to_circles=defaultdict(set)
    def add_line(self,points):
        key=frozenset(points)
        for p in key:self.point_to_lines[p].add(key)
    def add_circle(self,points):
        key=frozenset(points)
        for p in key:self.point_to_circles[p].add(key)
    def lines_through(self,point): return self.point_to_lines.get(point,set()).copy()
    def circles_through(self,point): return self.point_to_circles.get(point,set()).copy()

class PerpendicularityIndex:
    def __init__(self): self.by_line=defaultdict(set)
    def add(self,a,b,c,d):
        p,q=L2(a,b),L2(c,d)
        self.by_line[p].add(q);self.by_line[q].add(p)
    def partners(self,a,b): return self.by_line.get(L2(a,b),set()).copy()

class GeometryGraphIndex:
    def __init__(self): self.incidence=IncidenceIndex();self.perpendicular=PerpendicularityIndex()
    def populate(self,graph):
        for f in graph.facts:
            if f.kind=="coll":self.incidence.add_line(f.args)
            if f.kind=="cyclic":self.incidence.add_circle(f.args)
            if f.kind=="perp":self.perpendicular.add(*f.args)
        return self

class GraphStateHasher:
    @staticmethod
    def hash(graph):
        # Identificadores equivalentes são normalizados pelo menor apelido.
        classes=defaultdict(set)
        for p in graph.points: classes[graph.aliases.find(p)].add(p)
        names={n:min(v) for v in classes.values() for n in v}
        entries=[]
        for f in graph.facts:
            tup=(f.kind,*(names.get(p,p) for p in f.args))
            try: tup=GeoFact.from_tuple(tup).legacy
            except GeometrySyntaxError:pass
            entries.append(" ".join(tup))
        return hashlib.sha256("\n".join(sorted(entries)).encode()).hexdigest()

class PersistentGeometryState:
    """Estado imutável por deltas; adequado a ramos de busca independentes."""
    __slots__=("parent","delta","depth")
    def __init__(self,parent=None,delta=()):
        self.parent=parent;self.delta=frozenset(delta)
        self.depth=(parent.depth+1 if parent is not None else 0)
    def add(self, facts):return PersistentGeometryState(self,facts)
    def facts(self):
        result=set();cur=self
        while cur is not None:
            result.update(cur.delta);cur=cur.parent
        return frozenset(result)

class SymbolicPointSubstitution:
    """Substituições suportadas por overlap; não introduz novas hipóteses."""
    @staticmethod
    def substitute(fact,aliases):
        original=fact if isinstance(fact,GeoFact) else GeoFact.from_tuple(fact)
        new=GeoFact(original.kind,tuple(aliases.find(x) if x in aliases.parent else x for x in original.args))
        # Quando a substituição destrói uma reta, o resultado não é bem tipado.
        if len(set(new.args)) < len(set(original.args)) and original.kind in ("coll","para","perp","cyclic","simtri","eqangle","eqratio"):
            return None
        return GeometryCanonicalizer().fact(new)

# ── camadas específicas sobre a álgebra certificável ──
class AngleEquationSystem(AngleLattice):
    """Equações inteiras de direções modulo pi (sem divisão imprópria)."""

class LogDistanceEquationSystem(ExactLinearSystem):
    """Combinações racionais de log-comprimentos com comprimentos > 0."""

class DistanceEquationSystem(ExactLinearSystem):
    """Combinações racionais de distâncias não assinadas."""

class RatioEquationSystem(LogDistanceEquationSystem):
    """AB/CD = EF/GH traduz-se em L_AB-L_CD-L_EF+L_GH=0."""
    def add_ratio(self,a,b,c,d,label):
        row=defaultdict(int)
        for seg,coef in ((a,1),(b,-1),(c,-1),(d,1)):
            row[str(seg)]+=coef
        return self.add(row,label)
    def proves_ratio(self,a,b,c,d):
        row=defaultdict(int)
        for seg,coef in ((a,1),(b,-1),(c,-1),(d,1)):
            row[str(seg)]+=coef
        return self.prove(row)

class ExactConstantRepresentation:
    @staticmethod
    def rational(x):return Fraction(x)
    @staticmethod
    def half_turns(number):
        """Ângulo expresso como um múltiplo racional exato de π."""
        return Fraction(number)

class AlgebraicNormalForm:
    @staticmethod
    def linear(expression):
        return tuple(sorted(expression.terms.items())),expression.constant
    @staticmethod
    def equation(row):
        return tuple(sorted((str(k),Fraction(v)) for k,v in row.items() if Fraction(v)))

class EquationEntailment:
    @staticmethod
    def rational(equations,target):
        system=ExactLinearSystem()
        for i,eq in enumerate(equations):system.add(eq,f"eq{i}")
        return system.prove(target)
    @staticmethod
    def modulo_pi(equations,target):
        system=AngleLattice()
        for i,eq in enumerate(equations):system.add(eq,f"eq{i}")
        return system.prove(target)

class AlgebraicProofTrace:
    def __init__(self,equations,goal,coefficients):
        self.equations=tuple(equations);self.goal=dict(goal)
        self.coefficients=dict(coefficients)
    def verify(self):
        return AlgebraicCertificateVerifier.rational(self.equations,self.goal,self.coefficients)

class AlgebraicDependencyPruner:
    """Remove equações desnecessárias sem perder a implicação racional exata."""
    @staticmethod
    def prune(equations,target):
        remaining=list(equations)
        for item in tuple(remaining):
            subset=[q for q in remaining if q is not item]
            system=ExactLinearSystem()
            for label,row in subset:system.add(row,label)
            if system.prove(target)[0]:remaining=subset
        return tuple(remaining)

class PolynomialEquationInterface:
    """Verifica pertença a ideal polinomial com SymPy opcional.

    Pertença ao ideal fornece certificado suficiente de igualdade algébrica;
    não decide automaticamente todos os enunciados de geometria real.
    """
    @staticmethod
    def polynomial_consequence(generators,target,variables):
        try:
            import sympy as sp
        except ImportError as exc:
            raise RuntimeError("instale sympy para verificação polinomial opcional") from exc
        names=sp.symbols(" ".join(variables))
        if not isinstance(names,tuple): names=(names,)
        symbols=dict(zip(variables,names))
        # Só entradas já tipadas como expressões SymPy (sem sympify de texto arbitrário).
        gb=sp.groebner(tuple(generators),*names,order='lex')
        return gb.reduce(target)[1]==0

class ModularArithmeticAccelerator:
    @staticmethod
    def reduce(row,prime=2147483647):
        if prime < 3:raise ValueError("módulo inválido")
        return {k:int(Fraction(v).numerator*pow(Fraction(v).denominator,-1,prime))%prime
                for k,v in row.items() if Fraction(v)}

class ModularResultCertification:
    """Resultados de GF(p) só são certificados refazendo a inferência em Q."""
    @staticmethod
    def certify(equations,target):
        return EquationEntailment.rational(equations,target)[0]

class AlgebraDifferentialTests:
    """Teste aleatório de testemunho: um resultado aceito precisa ser reconstruível."""
    @staticmethod
    def run(iterations=100,seed=0):
        rng=random.Random(seed)
        for _ in range(iterations):
            s=ExactLinearSystem();ang=AngleLattice()
            for j in range(3):
                row={q:rng.randint(-3,3) for q in ("a","b","K")}
                s.add(row,f"r{j}");ang.add(row,f"r{j}")
            for _ in range(4):
                goal={q:rng.randint(-4,4) for q in ("a","b","K")}
                ok,w=s.prove(goal)
                if ok and not s.check_witness(goal,w):return False
                ok,w=ang.prove(goal)
                if ok and not ang.check_witness(goal,w):return False
        return True


def cmd_phase1_test(a=None):
    """Testes determinísticos e adversariais para os invariantes da Fase 1."""
    import tempfile
    assert GeometryParser().parse("a b c = triangle ; d = midp a b ; prove midp d a b").goal.kind=="midp"
    assert GeometryDSLSerializer().loads(GeometryDSLSerializer().dumps(GeometryParser().parse("given ncoll a b c ; prove para d e b c"))).goal.kind=="para"
    assert LinearExpressionParser().parse("2*AB-CD+3/2*EF-1/3") == LinearExpression({"AB":2,"CD":-1,"EF":Fraction(3,2)},Fraction(-1,3))
    assert not num_check(("perp","a","a","b","c"),{"a":(0.,0.),"b":(1.,0.),"c":(0.,1.)})
    assert not num_check(("para","a","a","b","c"),{"a":(0.,0.),"b":(1.,0.),"c":(0.,1.)})
    assert not num_check(("coll","a","a","b"),{"a":(0.,0.),"b":(1.,0.)})
    g=GeometryGraph(); g.add_fact(GeoFact("overlap",("a","b")))
    assert g.equivalent_points("a","b") and not g.equivalent_points("a","c")
    assert len(g.facts_of_kind("overlap"))==1
    r=ExactLinearSystem(); r.add({"x":2,"y":1},"r1"); r.add({"y":1},"r2")
    success,w=r.prove({"x":2}); assert success and r.check_witness({"x":2},w)
    bad,w=r.prove({"z":1}); assert not bad
    ag=AngleLattice(); ag.add({"x":2},"twice")
    assert not ag.prove({"x":1})[0], "divisão ilegal de congruências angulares"
    ag.add({"x":1,"K":-1},"right")
    success,trace=ag.prove({"x":2}); assert success and ag.check_witness({"x":2},trace)
    P=GeometryParser(); assumptions=tuple(P.fact(s) for s in (
        "midp d a b","midp e a c","ncoll a b c"))
    step=ProofStep(P.fact("para d e b c"),"midline",assumptions[:2])
    cert=ProofCertificate(assumptions,step.conclusion,(step,))
    assert ProofChecker().verify(cert)[0]
    # A falsificação de uma hipótese lateral anula a certificação.
    forged=ProofCertificate(assumptions[:2],step.conclusion,(step,))
    assert not ProofChecker().verify(forged)[0]
    forged2=ProofCertificate(assumptions,P.fact("perp d e b c"),(ProofStep(P.fact("perp d e b c"),"midline",assumptions[:2]),))
    assert not ProofChecker().verify(forged2)[0]
    assert ProofChecker().verify(ProofCertificate.from_dict(json.loads(cert.to_json())))[0]
    mini=ProofMinimizer().minimize(cert); assert len(mini.steps)==1
    with tempfile.TemporaryDirectory() as d:
        f=Path(d)/"cert.json"; ProofJSONExporter.dump(cert,f)
        assert ProofReplayEngine().replay(f)[0]
    # Dedução algébrica exata de paralelismo por duas perpendicularidades.
    hyp=tuple(P.fact(s) for s in (
        "perp a b c d","perp c d e f", "distinct a b", "distinct c d", "distinct e f"))
    right=ProofStep(P.fact("para a b e f"),"ar_ang",hyp[:2])
    assert ProofChecker().verify(ProofCertificate(hyp,right.conclusion,(right,)))[0]
    bad=ProofStep(P.fact("para a b c d"),"ar_ang",hyp[:2])
    assert not ProofChecker().verify(ProofCertificate(hyp,bad.conclusion,(bad,)))[0]
    ce=CertifiedDeductionEngine(assumptions).close().certificate(P.fact("para d e b c"))
    assert ce is not None and ProofChecker().verify(ce)[0]
    assert not GeometryAssumptionConsistency.check((P.fact("coll a b c"),P.fact("ncoll a b c")))[0]
    assert FormalGeometryCompiler().compile_relation("distmeq","2*AB-CD=EF")==LinearExpression({"AB":2,"CD":-1,"EF":-1})
    assert AlgebraDifferentialTests.run(20)
    assert GraphStateHasher.hash(g) == GraphStateHasher.hash(g)
    assert len(PersistentGeometryState(delta=("a",)).add(("b",)).facts())==2
    assert GeometryTypeChecker().validate(P.parse("a b c = triangle ; d = midp a b ; prove midp d a b"))
    try: GeometryTypeChecker().validate(P.parse("a b c = triangle ; d = midp a q"))
    except GeometrySyntaxError: pass
    else: raise AssertionError("referência futura não rejeitada")
    try: LinearExpressionParser().parse("x**2")
    except GeometrySyntaxError: pass
    else: raise AssertionError("expressão inválida aceita")
    log("phase1", "Testes formais: AST, tipos, álgebra racional, congruência angular inteira, grafo, degenerescência e certificados PASSARAM", LM)
    return 0



# ═════════════════════ FASES 2–3: EXTENSÕES VERIFICÁVEIS ═════════════════════
# Este módulo é uma implementação ORIGINAL de um subconjunto certificado de
# DDAR2, um construtor de múltiplas restrições e um gerador de teoremas.
# NÃO declara paridade com o DDAR2 oficial nem reproduz toda a geração do AG2.
# As operações numéricas localizam pontos; apenas ProofCheckerV2 certifica fatos.
from collections import deque, Counter

@dataclass(frozen=True)
class ConstructionConstraint:
    """Restringe o ponto-alvo X: on_line(X,A,B), on_circle(X,O,P), etc."""
    operator: str
    args: tuple[str, ...]
    def __post_init__(self):
        allowed = {"on_line":2,"on_circle":2,"parallel":3,"perpendicular":3,
                   "perp_bisector":2,"angle_bisector":3,"eqdist":3,
                   "midpoint":2,"foot":3,"circumcenter":3,
                   "orthocenter":3,"reflection":3,"parallelogram":3,
                   "incenter":3,"centroid":3}
        if self.operator not in allowed or len(self.args)!=allowed[self.operator]:
            raise GeometrySyntaxError(f"restrição desconhecida ou aridade incorreta: {self}")
        if any(not _POINT.fullmatch(x) or x=='*' for x in self.args):
            raise GeometrySyntaxError("restrição possui ponto inválido")

@dataclass(frozen=True)
class ConstructionResult:
    point: tuple[float,float]
    candidates: tuple[tuple[float,float], ...]
    unique: bool
    constraints: tuple[ConstructionConstraint, ...]

class ConstructionSolver2:
    """Interseções e construtores determinísticos; nunca confunde figura com prova."""
    DIRECT = {"midpoint", "foot", "circumcenter", "orthocenter",
              "reflection", "parallelogram", "incenter", "centroid"}
    def __init__(self, tol=1.e-8): self.tol=tol
    def _known(self,c,coords):
        if any(a not in coords for a in c.args):
            raise GeometrySyntaxError(f"ponto anterior não definido: {c}")
        return [coords[a] for a in c.args]
    def locus(self,c,coords):
        p=self._known(c,coords); name=c.operator
        if name=="on_line": return ('L',p[0],sub(p[1],p[0]))
        if name=="parallel": return ('L',p[0],sub(p[2],p[1]))
        if name=="perpendicular": return ('L',p[0],_perp(sub(p[2],p[1])))
        if name=="perp_bisector": return ('L',lerp(*p,.5),_perp(sub(p[1],p[0])))
        if name=="on_circle":return ('C',p[0],dist(p[0],p[1]))
        if name=="eqdist":return ('C',p[0],dist(p[1],p[2]))
        if name=="angle_bisector":
            u=sub(p[0],p[1]);v=sub(p[2],p[1]); lu=math.hypot(*u);lv=math.hypot(*v)
            if min(lu,lv)<=self.tol:raise GeometrySyntaxError('ângulo indefinido')
            d=(u[0]/lu+v[0]/lv,u[1]/lu+v[1]/lv)
            return ('L',p[1],d)
        raise GeometrySyntaxError('construção direta não é um lugar geométrico')
    def _direct(self,c,coords):
        p=self._known(c,coords); k=c.operator
        if k=='midpoint':return lerp(p[0],p[1],.5)
        if k=='foot':return _foot(*p)
        if k=='circumcenter':return _circum(*p)
        if k=='orthocenter':return _orth(*p)
        if k=='reflection':
            f=_foot(*p)
            return None if f is None else (2*f[0]-p[0][0],2*f[1]-p[0][1])
        if k=='parallelogram':return _r_par(p,None)
        if k=='centroid':return ((p[0][0]+p[1][0]+p[2][0])/3,(p[0][1]+p[1][1]+p[2][1])/3)
        if k=='incenter':return _incenter(p)[1]
        raise GeometrySyntaxError('construção direta desconhecida')
    def _valid_locus(self,p,l):
        if l[0]=='L':
            v=sub(p,l[1]);n=math.hypot(*l[2]);
            return n>self.tol and abs(cross(v,l[2]))<=self.tol*max(1.,n*math.hypot(*v))
        return l[2]>self.tol and abs(dist(p,l[1])-l[2])<=self.tol*max(1.,l[2])
    def construct(self,target,constraints,coords,branch=0,allow_overlap=False,
                  require_unique=False,rng=None):
        cs=tuple(constraints)
        if not cs or target in coords:raise GeometrySyntaxError('alvo já definido ou sem restrições')
        if len(cs)==1 and cs[0].operator in self.DIRECT:
            pt=self._direct(cs[0],coords)
            if pt is None:raise GeometrySyntaxError('construção indefinida')
            candidates=[pt]
        else:
            if any(c.operator in self.DIRECT for c in cs):
                direct=[self._direct(c,coords) for c in cs if c.operator in self.DIRECT]
                if any(q is None or dist(q,direct[0])>self.tol for q in direct):
                    raise GeometrySyntaxError('construções diretas inconsistentes')
                candidates=[direct[0]]
                constraints_locus=[self.locus(c,coords) for c in cs if c.operator not in self.DIRECT]
                candidates=[q for q in candidates if all(self._valid_locus(q,l) for l in constraints_locus)]
            else:
                loci=[self.locus(c,coords) for c in cs]
                if any((l[0]=='L' and math.hypot(*l[2])<=self.tol) or
                       (l[0]=='C' and l[2]<=self.tol) for l in loci):
                    raise GeometrySyntaxError('reta ou circunferência degenerada')
                if len(loci)<2:
                    if rng is None:raise GeometrySyntaxError('lugar geométrico sem ponto único; use rng')
                    l=loci[0]
                    if l[0]=='L':
                        t=rng.uniform(-2,2);candidates=[(l[1][0]+t*l[2][0],l[1][1]+t*l[2][1])]
                    else:
                        t=rng.uniform(0,2*math.pi);candidates=[(l[1][0]+l[2]*math.cos(t),l[1][1]+l[2]*math.sin(t))]
                else:
                    candidates=[q for q in _meet(loci[0],loci[1]) if
                                all(self._valid_locus(q,l) for l in loci)]
        unique=[]
        for q in candidates:
            if q is None or not all(math.isfinite(t) for t in q):continue
            if not allow_overlap and any(dist(q,old)<=self.tol for old in coords.values()):continue
            if not any(dist(q,old)<=self.tol for old in unique):unique.append(tuple(float(v) for v in q))
        unique.sort()
        if not unique:raise GeometrySyntaxError('restrições incompatíveis ou solução degenerada')
        if require_unique and len(unique)!=1:raise GeometrySyntaxError('construção ambígua')
        if branch<0 or branch>=len(unique):raise GeometrySyntaxError('ramo inexistente')
        return ConstructionResult(unique[branch],tuple(unique),len(unique)==1,cs)
    def realize_program(self,coords,instructions):
        state=dict(coords)
        for target, cs, branch in instructions:
            state[target]=self.construct(target,cs,state,branch=branch).point
        return state

class GeometryGraph2(GeometryGraph):
    """Índices estruturais e dependências de fatos, sem inferência baseada em coordenadas."""
    def __init__(self):
        super().__init__();self.by_pair=defaultdict(set);self.by_triple=defaultdict(set)
        self.by_rule=defaultdict(set)
    def add_fact(self,fact,parents=(),rule='given'):
        f=GeometryCanonicalizer().fact(fact)
        ok=super().add_fact(f,parents)
        if ok:
            for a,b in itertools.combinations(sorted(set(f.args)),2):
                self.by_pair[frozenset((a,b))].add(f)
            for tri in itertools.combinations(sorted(set(f.args)),3):
                self.by_triple[frozenset(tri)].add(f)
            self.by_rule[rule].add(f)
        return ok
    def common_facts(self,*points):
        if len(points)==2:return set(self.by_pair.get(frozenset(points),()))
        if len(points)==3:return set(self.by_triple.get(frozenset(points),()))
        return set.intersection(*(self.facts_at_point(p) for p in points)) if points else set(self.facts)
    def line_components(self):
        lines=[set(f.args) for f in self.facts_of_kind('coll')]
        changed=True
        while changed:
            changed=False
            for i in range(len(lines)):
                for j in range(i+1,len(lines)):
                    shared=lines[i]&lines[j]
                    if len(shared)>=2 and any(ProofChecker._distinct(self.facts,a,b) for a,b in itertools.combinations(shared,2)):
                        lines[i]|=lines[j];lines.pop(j);changed=True;break
                if changed:break
        return tuple(frozenset(x) for x in lines)
    def circle_components(self):
        circles=[set(f.args) for f in self.facts_of_kind('cyclic')]
        changed=True
        while changed:
            changed=False
            for i in range(len(circles)):
                for j in range(i+1,len(circles)):
                    shared=circles[i]&circles[j]
                    if len(shared)>=3 and any(ProofChecker._noncoll(self.facts,*t) for t in itertools.combinations(shared,3)):
                        circles[i]|=circles[j];circles.pop(j);changed=True;break
                if changed:break
        return tuple(frozenset(x) for x in circles)

class ProofCheckerV2(ProofChecker):
    """Verificador de regras extras. Não confia no gerador ou no solver."""
    @classmethod
    def _rule(cls,step,known):
        if super()._rule(step,known):return True
        s=step.conclusion;p=step.premises;k=step.rule
        if k=='midp_cong' and len(p)==1 and p[0].kind=='midp' and s.kind=='cong':
            m,a,b=p[0].args
            return cls._distinct(known,a,b) and s.legacy==mk_cong(m,a,m,b)
        if k in ('perp_pair_para','para_pair_para','para_perp_pair') and len(p)==2:
            types=tuple(sorted(x.kind for x in p))
            want={'perp_pair_para':(('perp','perp'),'para'),
                  'para_pair_para':(('para','para'),'para'),
                  'para_perp_pair':(('para','perp'),'perp')}
            if (types,s.kind)!=want[k]:return False
            x1,x2=p
            segs1=[frozenset(x1.args[:2]),frozenset(x1.args[2:])]
            segs2=[frozenset(x2.args[:2]),frozenset(x2.args[2:])]
            for i in (0,1):
                for j in (0,1):
                    if segs1[i]!=segs2[j]:continue
                    a=sorted(segs1[1-i]);b=sorted(segs2[1-j]);common=sorted(segs1[i])
                    if not all(cls._distinct(known,*line) for line in (a,b,common)):continue
                    wanted=mk_para(*a,*b) if s.kind=='para' else mk_perp(*a,*b)
                    if s.legacy==wanted:return True
            return False
        if k in ('thales','thales_converse') and len(p)==2:
            m=next((f for f in p if f.kind=='midp'),None)
            other=next((f for f in p if f is not m),None)
            if m is None:return False
            center,a,c=m.args
            for b in {x for q in p for x in q.args}-{center,a,c}:
                if not cls._noncoll(known,a,b,c):continue
                if k=='thales' and other.kind=='perp' and s.kind=='cong':
                    if other.legacy==mk_perp(a,b,b,c) and s.legacy==mk_cong(center,a,center,b):return True
                if k=='thales_converse' and other.kind=='cong' and s.kind=='perp':
                    if other.legacy==mk_cong(center,a,center,b) and s.legacy==mk_perp(a,b,b,c):return True
            return False
        if k=='circle_center' and len(p)==3 and s.kind=='cyclic' and all(x.kind=='cong' for x in p):
            pts=set(s.args)
            if len(pts)!=4:return False
            possible=set(x for f in p for x in f.args)-pts
            for o in possible:
                edges=set(); valid=True
                for f in p:
                    segs=(set(f.args[:2]),set(f.args[2:]))
                    if not all(o in seg and len(seg)==2 for seg in segs):valid=False;break
                    a=next(iter(segs[0]-{o}));b=next(iter(segs[1]-{o}))
                    if a not in pts or b not in pts or not cls._distinct(known,o,a) or not cls._distinct(known,o,b):
                        valid=False;break
                    edges.add(frozenset((a,b)))
                if not valid:continue
                allpts={next(iter(pts))};change=True
                while change:
                    change=False
                    for e in edges:
                        if e&allpts and not e<=allpts:allpts|=e;change=True
                if allpts==pts and any(cls._noncoll(known,*t) for t in itertools.combinations(sorted(pts),3)):
                    return True
            return False
        if k=='midpoint_parallelogram' and len(p)==2 and s.kind=='para' and all(x.kind=='midp' for x in p):
            u,v=p
            if u.args[0]!=v.args[0] or len(set(u.args[1:]+v.args[1:]))!=4:return False
            a,c=u.args[1:];b,d=v.args[1:]
            return cls._noncoll(known,a,b,c) and s.legacy in (mk_para(a,b,c,d),mk_para(b,c,d,a))
        if k=='circle_inscribed_angle' and len(p)==1 and p[0].kind=='cyclic' and s.kind=='eqangle':
            q=p[0].args
            for a,b in itertools.combinations(q,2):
                c,d=tuple(x for x in q if x not in (a,b))
                if not cls._noncoll(known,c,a,b) or not cls._noncoll(known,d,a,b):continue
                if s.legacy==mk_eqang(c,a,c,b,d,a,d,b):return True
            return False
        return False

class CertifiedDDAR2Engine:
    """Fechamento de um subconjunto demonstrável de DDAR2 com agenda incremental.

    A meta não provada retorna None. Regras oficiais não reproduzidas não são
    improvisadas: a verificação independente recusa qualquer passo desconhecido.
    """
    def __init__(self,assumptions,maxfacts=2500,deadline=None):
        self.assumptions=tuple(GeometryCanonicalizer().fact(x) for x in assumptions)
        ok,reason=GeometryAssumptionConsistency.check(self.assumptions)
        if not ok:raise GeometryProofError(reason)
        self.checker=ProofCheckerV2();self.graph=GeometryGraph2();self.known=set()
        self.queue=deque();self.steps=[];self.maxfacts=maxfacts;self.deadline=deadline
        self.by_kind=defaultdict(set)
        for f in self.assumptions:self._remember(f,None)
    def _remember(self,f,step):
        if f in self.known:return False
        self.known.add(f);self.queue.append(f);self.by_kind[f.kind].add(f)
        self.graph.add_fact(f,() if step is None else step.premises,rule='given' if step is None else step.rule)
        if step is not None:self.steps.append(step)
        return True
    def add(self,conclusion,rule,premises):
        f=GeometryCanonicalizer().fact(conclusion)
        if f in self.known or len(self.known)>=self.maxfacts:return False
        ps=tuple(GeometryCanonicalizer().fact(p) for p in premises)
        if not all(x in self.known for x in ps):return False
        step=ProofStep(f,rule,ps)
        if not self.checker._rule(step,self.known):return False
        return self._remember(f,step)
    def _fact(self,kind,*args):
        return GeoFact.from_tuple((kind,*args))
    def _pair(self,x,y):
        # O terceiro segmento emerge de duas relações que compartilham o mesmo.
        k={('perp','perp'):('para','perp_pair_para'),
           ('para','para'):('para','para_pair_para'),
           ('para','perp'):('perp','para_perp_pair'),
           ('perp','para'):('perp','para_perp_pair')}.get((x.kind,y.kind))
        if k is None:return
        s1=[frozenset(x.args[:2]),frozenset(x.args[2:])]
        s2=[frozenset(y.args[:2]),frozenset(y.args[2:])]
        for i,j in itertools.product((0,1),repeat=2):
            if s1[i]!=s2[j]:continue
            a=sorted(s1[1-i]);b=sorted(s2[1-j])
            if len(a)==2 and len(b)==2:
                self.add(self._fact(k[0],*a,*b),k[1],(x,y))
    def _midpoints(self,u):
        for v in sorted(self.by_kind['midp'],key=str):
            if v==u:continue
            e1,e2=set(u.args[1:]),set(v.args[1:]);sh=e1&e2
            if len(sh)==1 and u.args[0]!=v.args[0]:
                a=next(iter(sh));b=next(iter(e1-sh));c=next(iter(e2-sh))
                self.add(self._fact('para',u.args[0],v.args[0],b,c),'midline',(u,v))
            if u.args[0]==v.args[0] and not sh:
                a,c=u.args[1:];b,d=v.args[1:]
                for args in ((a,b,c,d),(b,c,d,a)):
                    self.add(self._fact('para',*args),'midpoint_parallelogram',(u,v))
        self.add(self._fact('coll',*u.args),'midp_coll',(u,))
        m,a,b=u.args;self.add(self._fact('cong',m,a,m,b),'midp_cong',(u,))
        for x in sorted(self.by_kind['perp'],key=str):self._thales(u,x)
        for x in sorted(self.by_kind['cong'],key=str):self._thales(u,x)
    def _thales(self,mid,other):
        m,a,c=mid.args
        if other.kind=='perp':
            for b in set(other.args)-{m,a,c}:
                self.add(self._fact('cong',m,a,m,b),'thales',(mid,other))
        if other.kind=='cong':
            for b in set(other.args)-{m,a,c}:
                self.add(self._fact('perp',a,b,b,c),'thales_converse',(mid,other))
    def _circle(self):
        # Constroi um grafo de igualdade entre raios para cada centro O.
        edges=defaultdict(lambda:defaultdict(dict))
        for f in sorted(self.by_kind['cong'],key=str):
            seg1=set(f.args[:2]);seg2=set(f.args[2:])
            for o in seg1&seg2:
                if len(seg1)!=2 or len(seg2)!=2:continue
                a=next(iter(seg1-{o}));b=next(iter(seg2-{o}))
                edges[o][a][b]=f;edges[o][b][a]=f
        for o,graph in sorted(edges.items()):
            verts=sorted(graph)
            for quad in itertools.combinations(verts,4):
                target=set(quad); seen={quad[0]};path=[];queue=[quad[0]]
                while queue:
                    start=queue.pop(0)
                    for nxt,f in sorted(graph[start].items()):
                        if nxt not in target or nxt in seen:continue
                        seen.add(nxt);path.append(f);queue.append(nxt)
                if len(seen)==4 and len(path)==3:
                    self.add(self._fact('cyclic',*quad),'circle_center',tuple(path))
    def _cyclic_angles(self,cy):
        q=cy.args
        for a,b in itertools.combinations(q,2):
            c,d=(x for x in q if x not in (a,b))
            self.add(self._fact('eqangle',c,a,c,b,d,a,d,b),'circle_inscribed_angle',(cy,))
    def close(self,max_steps=30000):
        processed=0
        while self.queue and processed<max_steps and len(self.known)<self.maxfacts:
            if self.deadline is not None and time.monotonic()>self.deadline:break
            x=self.queue.popleft();processed+=1
            if x.kind=='midp':self._midpoints(x)
            if x.kind in ('para','perp'):
                for y in sorted(self.by_kind['para']|self.by_kind['perp'],key=str):
                    if x!=y:self._pair(x,y)
            if x.kind in ('midp','perp','cong'):
                if x.kind in ('perp','cong'):
                    for mid in sorted(self.by_kind['midp'],key=str):self._thales(mid,x)
                if x.kind=='cong':self._circle()
            if x.kind=='cyclic':self._cyclic_angles(x)
        return self
    def certificate(self,goal):
        f=GeometryCanonicalizer().fact(goal)
        if f not in self.known:return None
        cert=ProofMinimizer().minimize(ProofCertificate(self.assumptions,f,tuple(self.steps),
                             {'engine':'geoforge-certified-ddar2-subset','version':2}))
        ok,message=self.checker.verify(cert)
        if not ok:raise GeometryProofError(message)
        return cert
    def stats(self):return dict(facts=len(self.known),steps=len(self.steps),pending=len(self.queue),
                                predicates=dict(Counter(f.kind for f in self.known)))

@dataclass(frozen=True)
class MovingPointDependency:
    """Dependências sintáticas, não inferência de propriedades observadas no desenho."""
    fixed_points: frozenset[str]
    constructions: Mapping[str,tuple[ConstructionConstraint,...]]
    def moving(self):
        move=set();pending=dict(self.constructions)
        while pending:
            updated=False
            for point,cs in list(pending.items()):
                refs={x for c in cs for x in c.args}
                if refs<=self.fixed_points|set(self.constructions)-set(pending):
                    if refs&move:move.add(point)
                    del pending[point];updated=True
            if not updated:raise GeometrySyntaxError('ciclo ou referência de dependência não resolvida')
        return frozenset(move)

class LocusConstructionProver:
    """Certifica apenas invariantes explícitos por construção sobre objetos fixos."""
    def verify(self,claim,target,constraints,fixed_points,hypotheses=()):
        # Nomes diferentes não implicam pontos distintos: exigir prova explícita.
        fs=set(fixed_points)
        known={GeometryCanonicalizer().fact(x) for x in hypotheses}
        for c in constraints:
            if not set(c.args)<=fs:continue
            if c.operator=='on_line' and claim.kind=='coll' and set(claim.args)=={target,*c.args}:
                return ProofChecker._distinct(known,*c.args)
            if c.operator=='on_circle' and claim.kind=='cong':
                o,p=c.args
                return (claim.legacy==mk_cong(o,target,o,p)
                        and ProofChecker._distinct(known,o,p))
        return False

@dataclass(frozen=True)
class Phase3Config:
    count:int=200
    seed:int=0
    max_points:int=12
    maxfacts:int=450
    min_steps:int=1
    max_steps:int=30
    family_holdout:int=20
    max_trials_per_record:int=30
    workers:int=1
    def __post_init__(self):
        if self.count<0 or self.max_points<8 or self.max_points>25:
            raise ValueError('count>=0 e 8<=max_points<=25 obrigatórios')
        if not (0<=self.family_holdout<=100):raise ValueError('family_holdout deve estar entre 0 e 100')
        if not (1<=self.workers<=64):raise ValueError('workers deve estar entre 1 e 64')

class GeometryTemplateFactory:
    """Construções sintéticas derivadas de relações EXPLICITAMENTE assumidas.

    Não usa a validade de uma relação observada numericamente como teorema.
    As hipóteses ncoll/distinct aparecem no problema formal e são verificadas
    para o desenho amostrado antes da aceitação do registro.
    """
    families=('midline','parallel_transitive','perp_pair','para_perp',
              'thales','thales_converse','circle_center','midpoint_parallelogram',
              'double_midline','parallel_perpendicular_chain','circle_angle_chain',
              'parallelogram_perpendicular_chain')
    def __init__(self,seed=0):self.rng=random.Random(seed)
    def point(self):return (self.rng.uniform(-4,4),self.rng.uniform(-4,4))
    def triangle(self):
        for _ in range(100):
            a,b,c=self.point(),self.point(),self.point()
            if abs(area2(a,b,c))>1 and min(dist(a,b),dist(a,c),dist(b,c))>1:return a,b,c
        raise GeometryProofError('falha ao gerar triângulo não degenerado')
    def _make(self,family):
        p=GeometryParser(); C={}; giv=[];goal=None
        if family=='midline':
            C['a'],C['b'],C['c']=self.triangle()
            C['d']=lerp(C['a'],C['b'],.5);C['e']=lerp(C['a'],C['c'],.5)
            giv=['midp d a b','midp e a c','ncoll a b c']
            goal='para d e b c'
        elif family in ('parallel_transitive','perp_pair','para_perp'):
            origin,u,_=self.triangle();v=sub(u,origin);w=_perp(v)
            C['a']=origin;C['b']=u;C['c']=self.point();C['d']=(C['c'][0]+v[0],C['c'][1]+v[1])
            C['e']=self.point();C['f']=(C['e'][0]+v[0],C['e'][1]+v[1]);
            if family=='parallel_transitive':
                giv=['para a b c d','para c d e f'];goal='para a b e f'
            elif family=='perp_pair':
                C['b']=(origin[0]+w[0],origin[1]+w[1]);
                C['f']=(C['e'][0]+w[0],C['e'][1]+w[1])
                giv=['perp a b c d','perp c d e f'];goal='para a b e f'
            else:
                C['f']=(C['e'][0]+w[0],C['e'][1]+w[1])
                giv=['para a b c d','perp c d e f'];goal='perp a b e f'
        elif family in ('thales','thales_converse'):
            C['a'],C['c'],x=self.triangle();C['m']=lerp(C['a'],C['c'],.5)
            v=sub(C['a'],C['m']);theta=self.rng.uniform(.4,2.4)
            C['b']=(C['m'][0]+v[0]*math.cos(theta)-v[1]*math.sin(theta),
                     C['m'][1]+v[0]*math.sin(theta)+v[1]*math.cos(theta))
            giv=['midp m a c','ncoll a b c']
            if family=='thales':giv+=['perp a b b c'];goal='cong m a m b'
            else:giv+=['cong m a m b'];goal='perp a b b c'
        elif family=='circle_center':
            C['o']=self.point();r=self.rng.uniform(1.5,3)
            ph=self.rng.uniform(0,2*math.pi)
            for i,name in enumerate('abcd'):
                t=ph+i*math.pi/2+self.rng.uniform(-.09,.09)
                C[name]=(C['o'][0]+r*math.cos(t),C['o'][1]+r*math.sin(t))
            giv=['cong o a o b','cong o a o c','cong o a o d','ncoll a b c']
            goal='cyclic a b c d'
        elif family=='double_midline':
            C['a'],C['b'],C['c']=self.triangle();C['p']=self.point()
            if abs(area2(C['p'],C['b'],C['c']))<1.e-4:
                C['p']=(C['p'][0]+.17,C['p'][1]+.9)
            C['d']=lerp(C['a'],C['b'],.5);C['e']=lerp(C['a'],C['c'],.5)
            C['f']=lerp(C['p'],C['b'],.5);C['g']=lerp(C['p'],C['c'],.5)
            giv=['midp d a b','midp e a c','midp f p b','midp g p c',
                 'ncoll a b c','ncoll p b c']
            goal='para d e f g'
        elif family=='parallel_perpendicular_chain':
            origin,u,_=self.triangle();v=sub(u,origin);w=_perp(v)
            C['a']=origin;C['b']=(origin[0]+w[0],origin[1]+w[1])
            C['c']=self.point();C['d']=(C['c'][0]+v[0],C['c'][1]+v[1])
            C['e']=self.point();C['f']=(C['e'][0]+w[0],C['e'][1]+w[1])
            C['g']=self.point();C['h']=(C['g'][0]+w[0],C['g'][1]+w[1])
            giv=['perp a b c d','perp e f c d','para g h a b']
            goal='para g h e f'
        elif family=='circle_angle_chain':
            C['o']=self.point();r=self.rng.uniform(1.5,3)
            phi=self.rng.uniform(0,2*math.pi)
            for i,name in enumerate('abcd'):
                t=phi+i*math.pi/2+.07*self.rng.random()
                C[name]=(C['o'][0]+r*math.cos(t),C['o'][1]+r*math.sin(t))
            giv=['cong o a o b','cong o a o c','cong o a o d',
                 'ncoll a b c','ncoll d a b']
            goal='eqangle c a c b d a d b'
        elif family=='parallelogram_perpendicular_chain':
            C['a'],C['b'],C['c']=self.triangle()
            C['d']=(C['a'][0]+C['c'][0]-C['b'][0],C['a'][1]+C['c'][1]-C['b'][1]);
            C['m']=lerp(C['a'],C['c'],.5)
            C['e']=self.point();v=_perp(sub(C['b'],C['a']))
            C['f']=(C['e'][0]+v[0],C['e'][1]+v[1])
            giv=['midp m a c','midp m b d','ncoll a b c','perp a b e f']
            goal='perp c d e f'
        elif family=='midpoint_parallelogram':
            C['a'],C['b'],C['c']=self.triangle()
            C['d']=(C['a'][0]+C['c'][0]-C['b'][0],C['a'][1]+C['c'][1]-C['b'][1]);
            C['m']=lerp(C['a'],C['c'],.5)
            giv=['midp m a c','midp m b d','ncoll a b c']
            goal='para a b c d'
        else:raise GeometrySyntaxError('família desconhecida')
        # As hipóteses explícitas de não-degenerescência pertencem ao PROBLEMA.
        for a,b in itertools.combinations(sorted(C),2):
            if dist(C[a],C[b])>1e-5:giv.append('distinct '+a+' '+b)
        hypotheses=tuple(p.fact(f) for f in dict.fromkeys(giv))
        target=p.fact(goal)
        if not all(num_check(f.legacy,C) for f in hypotheses if f.kind in MK):
            raise GeometryProofError('hipóteses do template inválidas no diagrama')
        return C,hypotheses,target
    def build(self,family=None):
        family=family or self.rng.choice(self.families)
        return (family,*self._make(family))

class GeometryStructureFingerprint:
    """Hash Weisfeiler-Lehman de hipergrafo tipado: filtro, NÃO prova de isomorfismo."""
    @staticmethod
    def key(facts,goal,rounds=4):
        points=sorted({a for f in (*facts,goal) for a in f.args if _POINT.fullmatch(a)})
        labels={p:'point' for p in points}
        edges=tuple((*facts,goal))
        for _ in range(rounds):
            fresh={}
            for pt in points:
                neighborhood=[]
                for f in edges:
                    if pt not in f.args:continue
                    positions=tuple(i for i,a in enumerate(f.args) if a==pt)
                    neighborhood.append((f.kind,f is goal,positions,
                                         tuple(labels.get(x,'scalar') for x in f.args)))
                fresh[pt]=hashlib.sha256(json.dumps(sorted(neighborhood,key=str),sort_keys=True).encode()).hexdigest()
            labels=fresh
        signature=(tuple(sorted(labels.values())),tuple(sorted(Counter(f.kind for f in facts).items())),goal.kind)
        return hashlib.sha256(repr(signature).encode()).hexdigest()

class Phase3Generator:
    def __init__(self,config):
        self.cfg=config;self.factory=GeometryTemplateFactory(config.seed)
        self._names='abcdefghijklmnopqrstuvwxyz'
    def _extend(self,C,hypotheses):
        # Pontos médios adicionais são construções válidas e aumentam a
        # variabilidade dos diagramas. Eles não são marcados como necessários.
        max_extra=min(3,max(0,self.cfg.max_points-len(C)))
        if max_extra==0:return C,hypotheses
        count=self.factory.rng.randrange(max_extra+1)
        names=[x for x in self._names if x not in C]
        chosen=list(hypotheses)
        for _ in range(count):
            pair=None
            for __ in range(30):
                a,b=self.factory.rng.sample(list(C),2)
                pt=lerp(C[a],C[b],.5)
                if all(dist(pt,other)>1.e-5 for other in C.values()):
                    pair=(a,b,pt);break
            if pair is None or not names:break
            a,b,pt=pair;name=names.pop(0);C[name]=pt
            chosen.append(GeoFact('midp',(name,a,b)))
            for old in C:
                if old!=name:chosen.append(GeoFact('distinct',(name,old)))
        return C,tuple(chosen)
    def _relabel(self,C,hyps,goal):
        # Modificações de nomes não alteram a validade das provas.
        points=list(C)
        newnames=list(self._names[:len(points)]);self.factory.rng.shuffle(newnames)
        mapping=dict(zip(points,newnames))
        coords={mapping[k]:v for k,v in C.items()}
        remap=lambda f:GeoFact(f.kind,tuple(mapping.get(a,a) for a in f.args))
        return coords,tuple(remap(f) for f in hyps),remap(goal)
    def next_record(self,family=None):
        rng=self.factory.rng
        for _ in range(self.cfg.max_trials_per_record):
            family,C,assumptions,goal=self.factory.build(family)
            C,assumptions=self._extend(C,assumptions)
            C,assumptions,goal=self._relabel(C,assumptions,goal)
            engine=CertifiedDDAR2Engine(assumptions,maxfacts=self.cfg.maxfacts).close()
            certificate=engine.certificate(goal)
            if certificate is None:continue
            if not self.cfg.min_steps<=len(certificate.steps)<=self.cfg.max_steps:continue
            if not all(num_check(f.legacy,C) for f in engine.known if f.kind in MK):
                raise GeometryProofError('regra derivou fato falso em figura do template: '+family)
            ok,msg=ProofCheckerV2().verify(certificate)
            if not ok:raise GeometryProofError('certificado interno inválido: '+msg)
            name_data=tuple((k,tuple(round(v,9) for v in C[k])) for k in sorted(C))
            return {'schema':'geoforge-synthetic-v2','family':family,
                    'problem':{'hypotheses':[str(f) for f in assumptions],
                               'goal':str(goal),'points':sorted(C)},
                    'auxiliaries':[], 'auxiliary_necessity':'not_asserted',
                    'proof':certificate.to_dict(),
                    'metadata':{'steps':len(certificate.steps),'facts':len(engine.known),
                      'difficulty':len(certificate.steps)+math.log1p(len(engine.known)),
                      'structure_hash':GeometryStructureFingerprint.key(assumptions,goal),
                      'seed':self.cfg.seed,'coords_tested':True,'coordinates':dict(name_data)}}
        raise GeometryProofError('não foi possível gerar uma prova certificada dentro do orçamento')

class Phase3DatasetWriter:
    """JSONL/GZIP particionado, escrita atômica, retomada por manifesto e splits por família."""
    def __init__(self,out,shard_size=1000):
        if shard_size<1:raise ValueError('shard_size deve ser positivo')
        self.path=Path(out);self.shard_size=shard_size;self.path.mkdir(parents=True,exist_ok=True)
    @staticmethod
    def split(family,holdout):
        if not holdout:return 'train'
        value=int.from_bytes(hashlib.sha256(family.encode()).digest()[:4],'big')%100
        return 'val' if value<holdout else 'train'
    def write(self,config,unique='exact',resume=False):
        if unique not in ('none','exact','structural'):raise ValueError('modo de dedupe inválido')
        manifest_path=self.path/'phase3_manifest.json'
        if manifest_path.exists() and not resume:
            raise FileExistsError('manifesto já existe; use --resume ou diretório vazio')
        start=0;counts=Counter();seen=set();files=[]
        if resume and manifest_path.exists():
            old=json.loads(manifest_path.read_text(encoding='utf8'))
            if old['seed']!=config.seed or old['unique']!=unique or old['shard_size']!=self.shard_size:
                raise GeometrySyntaxError('configuração incompatível com retomada')
            start=old['generated'];counts.update(old['counts']);files=list(old['files'])
            for entry in files:
                with gzip.open(self.path/entry,'rt',encoding='utf8') as handle:
                    for line in handle:
                        r=json.loads(line)
                        if unique!='none':seen.add(self._key(r,unique))
        gen=Phase3Generator(config)
        # Avança o estado aleatório exatamente como na execução anterior.
        for i in range(start):gen.next_record(GeometryTemplateFactory.families[i%len(GeometryTemplateFactory.families)])
        buffers=defaultdict(list)
        for index in range(start,config.count):
            rec=gen.next_record(GeometryTemplateFactory.families[index%len(GeometryTemplateFactory.families)])
            key=self._key(rec,unique)
            if unique!='none' and key in seen:continue
            seen.add(key)
            dest=self.split(rec['family'],config.family_holdout)
            buffers[dest].append(rec);counts[dest]+=1
            if sum(map(len,buffers.values()))>=self.shard_size:
                files.extend(self._flush(buffers,len(files)));buffers.clear()
        if buffers:files.extend(self._flush(buffers,len(files)))
        manifest={'schema':'geoforge-phase3-manifest-v2','seed':config.seed,
                  'generated':config.count,'unique':unique,'shard_size':self.shard_size,
                  'files':files,'sha256':{name:hashlib.sha256((self.path/name).read_bytes()).hexdigest() for name in files},
                  'counts':dict(counts),'families':list(GeometryTemplateFactory.families),
                  'certified':True,'fully_ag2_compatible':False}
        self._atomic_json(manifest_path,manifest)
        return manifest
    @staticmethod
    def _key(rec,unique):
        if unique=='structural':return rec['metadata']['structure_hash']
        return hashlib.sha256(json.dumps(rec['problem'],sort_keys=True).encode()).hexdigest()
    def _flush(self,buffers,group):
        names=[]
        for split,records in sorted(buffers.items()):
            name=f'phase3_{split}_{group:06d}.jsonl.gz';path=self.path/name
            temp=path.with_name(path.name+'.part')
            with gzip.open(temp,'wt',encoding='utf-8') as fd:
                for rec in records:fd.write(json.dumps(rec,ensure_ascii=False,sort_keys=True)+'\n')
            os.replace(temp,path);names.append(name)
        return names
    @staticmethod
    def _atomic_json(path,data):
        temp=path.with_name(path.name+'.part')
        temp.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf8')
        os.replace(temp,path)

class Phase3DatasetAuditor:
    @staticmethod
    def verify(path):
        path=Path(path);manifest=json.loads((path/'phase3_manifest.json').read_text(encoding='utf8'))
        checker=ProofCheckerV2();total=0;types=Counter();bad=[]
        for shard in manifest['files']:
            expect=manifest.get('sha256',{}).get(shard)
            if expect and hashlib.sha256((path/shard).read_bytes()).hexdigest()!=expect:
                bad.append((shard,total+1,'sha256 divergente'));continue
            with gzip.open(path/shard,'rt',encoding='utf8') as fd:
                for line in fd:
                    total+=1;rec=json.loads(line)
                    cert=ProofCertificate.from_dict(rec['proof']);ok,reason=checker.verify(cert)
                    if not ok:bad.append((shard,total,reason))
                    if cert.goal.legacy!=GeometryParser().fact(rec['problem']['goal']).legacy:bad.append((shard,total,'meta inconsistente'))
                    types[rec['family']]+=1
        return {'total':total,'valid':total-len({e[1] for e in bad}),'errors':bad[:12],
                'families':dict(types),'reported':sum(manifest['counts'].values())}



@dataclass(frozen=True)
class GeometryProgram2:
    """Problema tipado composto de construções por múltiplas restrições."""
    initial_points: tuple[str,...]
    instructions: tuple[tuple[str,tuple[ConstructionConstraint,...]], ...]
    assumptions: tuple[GeoFact,...]
    goal: Optional[GeoFact]
    def to_dict(self):
        return dict(initial_points=list(self.initial_points),
                    instructions=[{'point':p,'constraints':[dict(operator=c.operator,args=list(c.args)) for c in cs]}
                                  for p,cs in self.instructions],
                    assumptions=[str(f) for f in self.assumptions],
                    goal=str(self.goal) if self.goal else None)

class GeometryParser2:
    """Exemplo: a b c = triangle ; x = on_line a b, on_circle c a ; prove coll x a b."""
    ALIASES={'midp':'midpoint','circ':'circumcenter','orth':'orthocenter',
             'onl':'on_line','onc':'on_circle','pline':'parallel','tline':'perpendicular',
             'bis':'perp_bisector','inter':'on_line'}
    def parse(self,source):
        giv=[];inst=[];initial=[];known=set();goal=None
        for fragment in source.split(';'):
            clause=fragment.strip()
            if not clause:continue
            if clause.startswith(('given ','assume ')):
                f=GeometryParser().fact(clause.split(None,1)[1]);giv.append(f);continue
            if clause.startswith(('prove ','goal ')):
                if goal is not None:raise GeometrySyntaxError('meta repetida')
                goal=GeometryParser().fact(clause.split(None,1)[1]);continue
            if '=' not in clause:raise GeometrySyntaxError('cláusula desconhecida: '+clause)
            left,right=(x.strip() for x in clause.split('=',1))
            if right=='triangle':
                names=left.split()
                if len(names)!=3 or any(not _POINT.fullmatch(x) or x in known for x in names):
                    raise GeometrySyntaxError('triangle requer três novos pontos distintos')
                known.update(names);initial.extend(names);continue
            if not _POINT.fullmatch(left) or left in known or left=='*':
                raise GeometrySyntaxError('alvo inválido ou repetido: '+left)
            parts=[]
            for section in right.split(','):
                tokens=section.strip().split()
                if not tokens:raise GeometrySyntaxError('restrição vazia')
                name=self.ALIASES.get(tokens[0],tokens[0]); args=tuple(tokens[1:])
                cc=ConstructionConstraint(name,args)
                if any(n not in known for n in args):
                    raise GeometrySyntaxError('argumento ainda não definido: '+section)
                parts.append(cc)
            inst.append((left,tuple(parts)));known.add(left)
        for f in (*giv,*((goal,) if goal is not None else ())):
            for pt in f.args:
                if _POINT.fullmatch(pt) and pt not in known:
                    raise GeometrySyntaxError('ponto não introduzido: '+pt)
        return GeometryProgram2(tuple(initial),tuple(inst),tuple(giv),goal)
    def realize(self,program,initial_coords,seed=0):
        if not all(x in initial_coords for x in program.initial_points):
            raise GeometrySyntaxError('coordenadas livres ausentes')
        coords=dict(initial_coords);solver=ConstructionSolver2()
        for target,conditions in program.instructions:
            coords[target]=solver.construct(target,conditions,coords,rng=random.Random(seed+len(coords))).point
        return coords

@dataclass(frozen=True)
class ConstraintSolveResult:
    coordinates: Mapping[str,tuple[float,float]]
    success: bool
    max_residual: float
    iterations: int
    attempts: int

class NumericalConstraintSolver2:
    """Minimização diferenciável por diferenças finitas e LM amortecido.

    Um diagrama numérico NÃO prova o teorema. Suporta relações de colinearidade,
    paralelismo, perpendicularidade, congruência, pontos médios e conciclicidade.
    """
    def __init__(self,tolerance=1.e-7,max_iterations=120,restarts=4):
        if np is None:raise RuntimeError('NumPy necessário para otimização numérica')
        self.tolerance=tolerance;self.max_iterations=max_iterations;self.restarts=restarts
    @staticmethod
    def _residual(fact,C):
        k=fact.kind;p=[C[x] for x in fact.args]
        if k=='coll':
            a,b,c=p;ab=sub(b,a);ac=sub(c,a)
            return [cross(ab,ac)/max(1.,math.hypot(*ab)*math.hypot(*ac))]
        if k in ('para','perp'):
            a,b,c,d=p;u=sub(b,a);v=sub(d,c);den=max(1.,math.hypot(*u)*math.hypot(*v))
            return [(cross(u,v) if k=='para' else dot(u,v))/den]
        if k=='cong':
            a,b,c,d=p;d1=dist(a,b);d2=dist(c,d)
            return [(d1-d2)/max(1.,d1,d2)]
        if k=='midp':
            m,a,b=p;h=lerp(a,b,.5)
            return [(m[0]-h[0])/max(1.,dist(a,b)),(m[1]-h[1])/max(1.,dist(a,b))]
        if k=='cyclic':
            o=_circum(*p[:3])
            return [10.] if o is None else [(dist(o,p[3])-dist(o,p[0]))/max(1.,dist(o,p[0]))]
        if k in ('distinct','noverlap'):
            return [max(0.,1.e-4-dist(*p))]
        if k=='ncoll':
            a,b,c=p;return [max(0.,1.e-4-abs(area2(a,b,c)))]
        raise GeometrySyntaxError('tipo de restrição não suportado numericamente: '+k)
    def solve(self,initial,free_points,constraints,seed=0):
        import numpy as _np
        fixed=frozenset(free_points);names=sorted(set(initial)-fixed)
        if any(x not in initial for f in constraints for x in f.args):
            raise GeometrySyntaxError('referência não presente no estado inicial')
        if self.restarts<1 or self.max_iterations<1:
            raise ValueError('restarts e max_iterations devem ser positivos')
        x0=_np.array([v for n in names for v in initial[n]],dtype=float)
        rng=_np.random.default_rng(seed)
        def reconstruct(x):
            coord=dict(initial)
            for i,n in enumerate(names):coord[n]=(float(x[2*i]),float(x[2*i+1]))
            return coord
        def residual(x):
            coords=reconstruct(x)
            return _np.array([v for f in constraints for v in self._residual(f,coords)],dtype=float)
        best=(float('inf'),x0.copy(),0)
        if not names:
            rr=residual(x0);score=float(_np.max(_np.abs(rr),initial=0.))
            return ConstraintSolveResult(reconstruct(x0),score<=self.tolerance,score,0,1)
        for attempt in range(max(1,self.restarts)):
            x=x0.copy() if attempt==0 else x0+rng.normal(0,1.,size=x0.shape)
            lam=1.e-2
            for iteration in range(self.max_iterations):
                r=residual(x);err=float(_np.max(_np.abs(r),initial=0.))
                if err<best[0]:best=(err,x.copy(),iteration)
                if err<=self.tolerance:break
                jac=_np.empty((len(r),len(x)),dtype=float)
                for j in range(len(x)):
                    h=1.e-5*max(1.,abs(x[j]));e=_np.zeros_like(x);e[j]=h
                    jac[:,j]=(residual(x+e)-residual(x-e))/(2*h)
                lhs=jac.T@jac+lam*_np.eye(len(x));rhs=-jac.T@r
                try:dx=_np.linalg.solve(lhs,rhs)
                except _np.linalg.LinAlgError:break
                new=x+dx
                if float(_np.dot(residual(new),residual(new)))<float(_np.dot(r,r)):
                    x=new;lam=max(1.e-9,lam/3.)
                else:lam=min(1.e9,lam*5)
        error,x,step=best
        return ConstraintSolveResult(reconstruct(x),error<=self.tolerance,error,step+1,max(1,self.restarts))

def cmd_phase23_test(a):
    """Testes adversariais, templates e serialização dos módulos novos."""
    import tempfile
    s=ConstructionSolver2(); C={'a':(0.,0.),'b':(4.,0.),'c':(2.,-4.),
                                'o':(0.,0.),'p':(2.,0.),'q':(0.,2.)}
    r=s.construct('x',[ConstructionConstraint('on_line',('a','b')),
                       ConstructionConstraint('on_line',('c','q'))],C)
    assert abs(r.point[1])<1e-8 and abs(r.point[0]-2./3)<1e-8
    result=s.construct('x',[ConstructionConstraint('on_circle',('o','p')),
                             ConstructionConstraint('on_line',('a','b'))],C,allow_overlap=True)
    assert len(result.candidates)==2
    try:s.construct('x',[ConstructionConstraint('on_circle',('o','p')),
                          ConstructionConstraint('on_line',('a','b'))],C,allow_overlap=True,require_unique=True)
    except GeometrySyntaxError:pass
    else:raise AssertionError('interseção ambígua aceita como única')
    assert abs(s.construct('m',[ConstructionConstraint('midpoint',('a','b'))],C,allow_overlap=True).point[0]-2)<1e-10
    assert LocusConstructionProver().verify(GeoFact('coll',('x','a','b')),'x',
                (ConstructionConstraint('on_line',('a','b')),),('a','b'),
                (GeoFact('distinct',('a','b')),))
    program=GeometryParser2().parse('a b c = triangle ; x = on_line a b, on_circle c a ; prove coll x a b')
    assert program.instructions[0][1][0].operator=='on_line'
    coords=GeometryParser2().realize(program,{'a':(0.,0.),'b':(4.,0.),'c':(1.,2.)})
    assert abs(coords['x'][1])<1.e-8
    numerical=NumericalConstraintSolver2(max_iterations=50,restarts=2).solve(
        {'a':(0.,0.),'b':(4.,0.),'c':(1.,3.),'m':(3.,2.)},('a','b','c'),
        (GeoFact('midp',('m','a','b')),))
    assert numerical.success and dist(numerical.coordinates['m'],(2.,0.))<1.e-5
    for seed in range(10):
        g=GeometryTemplateFactory(seed)
        for family in g.families:
            _,coords,assumptions,goal=g.build(family)
            e=CertifiedDDAR2Engine(assumptions).close()
            cert=e.certificate(goal)
            assert cert is not None,(family,seed)
            assert ProofCheckerV2().verify(cert)[0],(family,seed)
            assert num_check(goal.legacy,coords),(family,seed)
            assert all(num_check(f.legacy,coords) for f in e.known if f.kind in MK),(family,seed)
    # Certificado falsificado e hipóteses laterais omitidas DEVEM ser rejeitados.
    parser=GeometryParser()
    a1=parser.fact('perp a b c d');a2=parser.fact('perp c d e f')
    goal=parser.fact('para a b e f')
    fake=ProofCertificate((a1,a2),goal,(ProofStep(goal,'perp_pair_para',(a1,a2)),))
    assert not ProofCheckerV2().verify(fake)[0]
    with tempfile.TemporaryDirectory() as tmp:
        cf=Phase3Config(count=18,seed=21)
        writer=Phase3DatasetWriter(tmp,shard_size=7)
        result=writer.write(cf,unique='exact')
        report=Phase3DatasetAuditor.verify(tmp)
        assert report['total']==sum(result['counts'].values()) and report['valid']==report['total']
        assert report['total']>0
        result2=writer.write(Phase3Config(count=21,seed=21),unique='exact',resume=True)
        report2=Phase3DatasetAuditor.verify(tmp)
        assert report2['valid']==report2['total']
    log('phase23','Construções, DDAR certificado, locus restrito e dados reprodutíveis OK',LM)
    return 0

def cmd_phase3_gen(a):
    cf=Phase3Config(count=a.n,seed=a.seed,max_points=a.max_points,
                  maxfacts=a.maxfacts,family_holdout=a.holdout,workers=a.workers)
    result=Phase3DatasetWriter(a.out,shard_size=a.shard_size).write(
        cf,unique=a.dedupe,resume=a.resume)
    print(json.dumps(result,ensure_ascii=False,indent=2))
    return 0

def cmd_phase3_verify(a):
    report=Phase3DatasetAuditor.verify(a.out)
    print(json.dumps(report,ensure_ascii=False,indent=2))
    return 0 if not report['errors'] and report['total']==report['reported'] else 1

def cmd_ddar2_certified(a):
    parser=GeometryParser();givens=tuple(parser.fact(x) for x in a.given)
    goal=parser.fact(a.goal)
    eng=CertifiedDDAR2Engine(givens,maxfacts=a.maxfacts,deadline=time.monotonic()+a.timeout).close()
    cert=eng.certificate(goal)
    if cert is None:
        print(json.dumps({'solved':False,'reason':'não demonstrado pelo subconjunto certificado',
                          'stats':eng.stats()},ensure_ascii=False,indent=2));return 1
    if a.out:ProofJSONExporter.dump(cert,a.out)
    print(json.dumps({'solved':True,'certificate':cert.to_dict(),'stats':eng.stats()},
                     ensure_ascii=False,indent=2));return 0

# ═════════════════════════════════════════════════════════════════════════════
# FASES 2–3: REGRAS CERTIFICADAS ADICIONAIS + SÍNTESE ESTOCÁSTICA
# Cada regra abaixo é verificada novamente em ProofCheckerV2 sem confiar nas
# coordenadas numéricas. Construção por coordenadas não é usada como prova.
# Isto AMPLIA o subconjunto DDAR; NÃO é a implementação completa do DDAR2.
# ═════════════════════════════════════════════════════════════════════════════

_PROOF_RULE_V2 = ProofCheckerV2._rule.__func__

def _proof_rule_extended(cls, step, known):
    if _PROOF_RULE_V2(cls, step, known):
        return True
    s, ps, r = step.conclusion, step.premises, step.rule
    if r == 'cong_chain' and s.kind == 'cong' and len(ps) == 2 and all(x.kind == 'cong' for x in ps):
        edges = []
        for f in ps:
            e1, e2 = frozenset(f.args[:2]), frozenset(f.args[2:])
            if len(e1) != 2 or len(e2) != 2 or not all(cls._distinct(known, *tuple(e)) for e in (e1,e2)):
                return False
            edges.append((e1,e2))
        for a,b in edges[0], (edges[0][1],edges[0][0]):
            for c,d in edges[1], (edges[1][1],edges[1][0]):
                if b == c and s.legacy == mk_cong(*sorted(a),*sorted(d)):
                    return True
        return False
    if r == 'midpoint_converse' and len(ps) == 2 and s.kind == 'midp':
        co = next((x for x in ps if x.kind == 'coll'), None)
        cg = next((x for x in ps if x.kind == 'cong'), None)
        if co is None or cg is None: return False
        m,a,b = s.args
        return (len({m,a,b}) == 3 and cls._distinct(known,a,b) and
                set(co.args) == {m,a,b} and cg.legacy == mk_cong(m,a,m,b))
    if r == 'parallel_shared_collinear' and len(ps) == 1 and ps[0].kind == 'para' and s.kind == 'coll':
        a,b,c,d = ps[0].args
        if len({a,b,c,d}) != 3: return False
        shared = set((a,b)) & set((c,d))
        return (len(shared) == 1 and cls._distinct(known,a,b) and
                cls._distinct(known,c,d) and set(s.args) == {a,b,c,d})
    if r == 'cyclic_converse' and len(ps) == 1 and ps[0].kind == 'eqangle' and s.kind == 'cyclic':
        if len(set(s.args)) != 4: return False
        for a,b in itertools.combinations(s.args,2):
            c,d = (x for x in s.args if x not in (a,b))
            if (cls._noncoll(known,a,b,c) and cls._noncoll(known,a,b,d)
                    and ps[0].legacy == mk_eqang(c,a,c,b,d,a,d,b)):
                return True
        return False
    if r == 'parallelogram_opposite_sides' and len(ps) == 2 and s.kind == 'cong' and all(x.kind=='midp' for x in ps):
        u,v = ps
        if u.args[0] != v.args[0] or len(set(u.args[1:]+v.args[1:])) != 4: return False
        a,c = u.args[1:]; b,d = v.args[1:]
        return (cls._noncoll(known,a,b,c) and
                s.legacy in (mk_cong(a,b,c,d), mk_cong(b,c,d,a)))
    if r == 'midpoint_radius_distinct' and len(ps) == 1 and s.kind in ('distinct','noverlap') and ps[0].kind=='midp':
        m,a,b = ps[0].args
        return (cls._distinct(known,a,b) and
                frozenset(s.args) in (frozenset((m,a)),frozenset((m,b))))
    return False

ProofCheckerV2._rule = classmethod(_proof_rule_extended)

class ExtendedCertifiedDDAR2Engine(CertifiedDDAR2Engine):
    """Dedução incremental suplementar, sempre certificada passo a passo.

    Regras adicionais são submetidas ao mesmo ProofCheckerV2 independente.
    A agenda guarda fatos novos; varreduras globais são limitadas por maxfacts
    e pelo deadline. Ausência de prova não significa refutação.
    """
    def _midpoints(self,u):
        super()._midpoints(u)
        m,a,b=u.args
        for other in sorted(self.by_kind['midp'],key=str):
            if u == other or u.args[0] != other.args[0]:continue
            if set(u.args[1:]) & set(other.args[1:]):continue
            x,y=other.args[1:]
            for args in ((a,x,b,y),(x,b,y,a)):
                self.add(self._fact('cong',*args),'parallelogram_opposite_sides',(u,other))
        for x in (a,b):
            self.add(self._fact('distinct',m,x),'midpoint_radius_distinct',(u,))
    def _cong_combine(self,f):
        base = (frozenset(f.args[:2]),frozenset(f.args[2:]))
        for g in sorted(self.by_kind['cong'],key=str):
            if g==f:continue
            other=(frozenset(g.args[:2]),frozenset(g.args[2:]))
            for x,y in (base,(base[1],base[0])):
                for u,v in (other,(other[1],other[0])):
                    if y==u and len(x)==len(v)==2 and x!=v:
                        self.add(self._fact('cong',*sorted(x),*sorted(v)),'cong_chain',(f,g))
    def _midpoint_converse(self,f):
        if f.kind not in ('coll','cong'):return
        coll = self.by_kind['coll'] if f.kind=='cong' else (f,)
        congs = self.by_kind['cong'] if f.kind=='coll' else (f,)
        for co in sorted(coll,key=str):
            for m,a,b in itertools.permutations(co.args,3):
                target=mk_cong(m,a,m,b)
                for cg in sorted(congs,key=str):
                    if cg.legacy == target:
                        self.add(self._fact('midp',m,a,b),'midpoint_converse',(co,cg))
    def _cyclic_converse(self,f):
        if f.kind!='eqangle':return
        pts=sorted(set(f.args))
        if len(pts)!=4:return
        for quad in itertools.combinations(pts,4):
            self.add(self._fact('cyclic',*quad),'cyclic_converse',(f,))
    def _shared_parallel(self,f):
        if f.kind!='para':return
        if len(set(f.args))!=3:return
        self.add(self._fact('coll',*sorted(set(f.args))),'parallel_shared_collinear',(f,))
    def close(self,max_steps=30000):
        # Executa a agenda original, e em seguida a agenda das novas regras
        # até ponto fixo limitado. O rastreamento _new_processed evita executar
        # novamente todos os combinadores para a mesma afirmação.
        self._new_processed=getattr(self,'_new_processed',set())
        iterations=0
        while iterations<6:
            prev=len(self.known)
            super().close(max_steps=max_steps)
            outstanding=sorted(self.known-self._new_processed,key=str)
            for f in outstanding:
                if self.deadline is not None and time.monotonic()>self.deadline:break
                if len(self.known)>=self.maxfacts:break
                self._new_processed.add(f)
                if f.kind in ('coll','cong'):
                    self._midpoint_converse(f)
                if f.kind=='cong': self._cong_combine(f)
                if f.kind=='eqangle':self._cyclic_converse(f)
                if f.kind=='para':self._shared_parallel(f)
            iterations+=1
            if len(self.known)==prev:break
        return self
    def certificate(self,goal):
        cert=super().certificate(goal)
        if cert is None:return None
        return ProofCertificate(cert.assumptions,cert.goal,cert.steps,
                                {**cert.metadata,'engine':'geoforge-certified-ddar2-extended','checker':'ProofCheckerV2'})

CertifiedDDAR2Engine = ExtendedCertifiedDDAR2Engine

class StochasticSyntheticFactory:
    """Geração NÃO-template: constrói famílias de problemas com comprimentos,
    centros, retas e cadeia de relações de comprimento variável.
    Nada além das hipóteses declaradas é aceito como verdade formal.
    """
    families=('random_direction_chain','random_midline_chain','random_radius_graph')
    def __init__(self,rng):self.rng=rng
    def _p(self):return (self.rng.uniform(-9,9),self.rng.uniform(-9,9))
    def _good_point(self,coords,pt):
        return all(dist(pt,q)>.2 for q in coords.values())
    def build(self, family,max_points):
        p=GeometryParser()
        if family=='random_direction_chain':
            length=self.rng.randint(3,max(3,min(10,max_points//2)))
            C={};v=(self.rng.uniform(1.,4.),self.rng.uniform(1.,4.))
            directions=[self.rng.randrange(2) for _ in range(length)]
            for i in range(length):
                a,b=f'p{i}',f'q{i}'
                for _ in range(200):
                    root=self._p();u=v if directions[i]==0 else _perp(v)
                    end=(root[0]+u[0],root[1]+u[1])
                    if self._good_point(C,root) and self._good_point(C,end) and dist(root,end)>1:
                        C[a],C[b]=root,end;break
                else:raise GeometryProofError('não foi possível construir cadeia')
            giv=[]
            for i in range(length-1):
                type_='para' if directions[i]==directions[i+1] else 'perp'
                giv.append(f'{type_} p{i} q{i} p{i+1} q{i+1}')
            goal=f"{'para' if directions[0]==directions[-1] else 'perp'} p0 q0 p{length-1} q{length-1}"
        elif family=='random_midline_chain':
            origin=self._p();v=(self.rng.uniform(2,4),self.rng.uniform(1,3))
            w=_perp(v)
            C={'a':origin,'b':(origin[0]+v[0],origin[1]+v[1]),
               'c':(origin[0]+w[0],origin[1]+w[1])}
            C['d']=lerp(C['a'],C['b'],.5); C['e']=lerp(C['a'],C['c'],.5)
            giv=['midp d a b','midp e a c','ncoll a b c']
            end=1+self.rng.randrange(max(1,min(5,(max_points-len(C))//2)))
            prev=('b','c');orientation=0
            for i in range(end):
                u=self.rng.randrange(2);orientation^=u
                base=self._p();vec=sub(C[prev[1]],C[prev[0]])
                if u:vec=_perp(vec)
                a,b=f'p{i}',f'q{i}'
                C[a]=base; C[b]=(base[0]+vec[0],base[1]+vec[1])
                giv.append(f"{'perp' if u else 'para'} {prev[0]} {prev[1]} {a} {b}")
                prev=a,b
            goal=f"{'perp' if orientation else 'para'} d e {prev[0]} {prev[1]}"
        elif family=='random_radius_graph':
            n=min(max_points-1,self.rng.randint(5,9))
            o=self._p();radius=self.rng.uniform(2,3.5)
            C={'o':o};angle=self.rng.uniform(0,.15)
            for i in range(n):
                theta=angle+2*math.pi*i/n+.01*self.rng.random()
                C[f'p{i}']=(o[0]+radius*math.cos(theta),o[1]+radius*math.sin(theta))
            nodes=list(range(n));self.rng.shuffle(nodes)
            edges=[];visited=[nodes[0]]
            for v in nodes[1:]:
                u=self.rng.choice(visited);edges.append((u,v));visited.append(v)
            giv=[f'cong o p{u} o p{v}' for u,v in edges]
            chosen=sorted(self.rng.sample(range(n),4))
            giv.append('ncoll '+ ' '.join(f'p{x}' for x in chosen[:3]))
            goal='cyclic '+ ' '.join(f'p{x}' for x in chosen)
        else:raise GeometrySyntaxError('família estocástica desconhecida')
        for a,b in itertools.combinations(sorted(C),2):
            if dist(C[a],C[b])>1.e-5:
                giv.append('distinct '+a+' '+b)
        facts=tuple(p.fact(x) for x in dict.fromkeys(giv));goal=p.fact(goal)
        # Verifica numericamente TODAS as hipóteses relevantes.
        if not all(num_check(f.legacy,C) for f in facts if f.kind in MK):
            raise GeometryProofError('hipótese geométrica não satisfaz a figura')
        return family,C,facts,goal

class Phase3GeneratorAdvanced(Phase3Generator):
    """Alterna 12 famílias clássicas com famílias combinatórias de dimensão variável.

    O motor aceita apenas conclusões com provas formalmente verificadas.
    A estrutura de saída mantém compatibilidade com phase3-gen/phase3-verify.
    """
    def next_record(self,family=None):
        if family is None:
            family=self.factory.rng.choice((*GeometryTemplateFactory.families,*StochasticSyntheticFactory.families))
        if family in GeometryTemplateFactory.families:
            return super().next_record(family)
        rng=self.factory.rng;f=StochasticSyntheticFactory(rng)
        for _ in range(self.cfg.max_trials_per_record):
            try:family,C,assumptions,goal=f.build(family,self.cfg.max_points)
            except (GeometryProofError,GeometrySyntaxError):continue
            C,assumptions,goal=self._relabel_unbounded(C,assumptions,goal)
            eng=CertifiedDDAR2Engine(assumptions,maxfacts=self.cfg.maxfacts).close()
            cert=eng.certificate(goal)
            if cert is None or not self.cfg.min_steps<=len(cert.steps)<=self.cfg.max_steps:continue
            ok,msg=ProofCheckerV2().verify(cert)
            if not ok:raise GeometryProofError('certificado inválido: '+msg)
            if not all(num_check(x.legacy,C) for x in eng.known if x.kind in MK):
                raise GeometryProofError('conclusão incompatível com diagrama numérico')
            return {'schema':'geoforge-synthetic-v3','family':family,
                'problem':{'hypotheses':[str(x) for x in assumptions],
                           'goal':str(goal),'points':sorted(C)},
                'auxiliaries':[], 'auxiliary_necessity':'not_asserted',
                'proof':cert.to_dict(),
                'metadata':{'steps':len(cert.steps),'facts':len(eng.known),
                    'difficulty':len(cert.steps)+math.log1p(len(eng.known)),
                    'structure_hash':GeometryStructureFingerprint.key(assumptions,goal),
                    'seed':self.cfg.seed,'coords_tested':True,
                    'coordinates':{k:list(map(float,C[k])) for k in sorted(C)}}}
        raise GeometryProofError('gerador não encontrou problema demonstrável: '+family)
    def _relabel_unbounded(self,C,facts,goal):
        names=list(C)
        new=[chr(ord('a')+i) if i<26 else 'p'+str(i) for i in range(len(names))]
        self.factory.rng.shuffle(new)
        mapping=dict(zip(names,new));remap=lambda f:GeoFact(f.kind,tuple(mapping.get(x,x) for x in f.args))
        return {mapping[k]:v for k,v in C.items()},tuple(map(remap,facts)),remap(goal)

Phase3Generator = Phase3GeneratorAdvanced

# Correção: o amostrador expõe também famílias estocásticas ao escalonador da
# fábrica de dados, sem duplicar seus códigos nas doze famílias clássicas.
_ORIGINAL_PHASE3_WRITE = Phase3DatasetWriter.write

def _phase3_write_advanced(self,config,unique='exact',resume=False):
    # Mantém o formato do manifesto e a escrita atômica, mas acrescenta novos
    # tipos no escalonador. Usa fluxo de RNG determinístico por item para que
    # a retomada não dependa de PYTHONHASHSEED.
    if unique not in ('none','exact','structural'):raise ValueError('modo de dedupe inválido')
    all_families=(*GeometryTemplateFactory.families,*StochasticSyntheticFactory.families)
    manifest_path=self.path/'phase3_manifest.json'
    if manifest_path.exists() and not resume:
        raise FileExistsError('manifesto já existe; use --resume ou diretório vazio')
    start=0;counts=Counter();seen=set();files=[]
    if resume and manifest_path.exists():
        old=json.loads(manifest_path.read_text(encoding='utf8'))
        if (old['seed']!=config.seed or old['unique']!=unique or old['shard_size']!=self.shard_size
                or old.get('families')!=list(all_families)
                or old.get('config_max_points',config.max_points)!=config.max_points
                or old.get('config_maxfacts',config.maxfacts)!=config.maxfacts):
            raise GeometrySyntaxError('configuração incompatível com retomada')
        start=old['generated'];counts.update(old['counts']);files=list(old['files'])
        for entry in files:
            if (hashlib.sha256((self.path/entry).read_bytes()).hexdigest()!=old['sha256'][entry]):
                raise GeometryProofError('shard corrompido durante a retomada: '+entry)
            with gzip.open(self.path/entry,'rt',encoding='utf8') as handle:
                for line in handle:
                    rec=json.loads(line)
                    if unique!='none':seen.add(self._key(rec,unique))
    buffers=defaultdict(list)
    for index in range(start,config.count):
        # Gerador independente por índice: O(1) de avanço em cada retomada.
        # O índice é misturado com seed por SHA-256 (e não por hash()).
        derived=int.from_bytes(hashlib.sha256(f'{config.seed}:{index}'.encode()).digest()[:8],'big')
        cfg=Phase3Config(count=1,seed=derived,max_points=config.max_points,
             maxfacts=config.maxfacts,min_steps=config.min_steps,max_steps=config.max_steps,
             family_holdout=config.family_holdout,max_trials_per_record=config.max_trials_per_record)
        gen=Phase3Generator(cfg)
        fam=all_families[index%len(all_families)]
        rec=gen.next_record(fam)
        key=self._key(rec,unique)
        if unique!='none' and key in seen:continue
        seen.add(key)
        dest=self.split(rec['family'],config.family_holdout)
        buffers[dest].append(rec);counts[dest]+=1
        if sum(map(len,buffers.values()))>=self.shard_size:
            files.extend(self._flush(buffers,len(files)));buffers.clear()
    if buffers:files.extend(self._flush(buffers,len(files)))
    manifest={'schema':'geoforge-phase3-manifest-v3','seed':config.seed,
             'generated':config.count,'unique':unique,'shard_size':self.shard_size,
             'files':files,'sha256':{name:hashlib.sha256((self.path/name).read_bytes()).hexdigest() for name in files},
             'counts':dict(counts),'families':list(all_families),
             'certified':True,'fully_ag2_compatible':False,
             'config_max_points':config.max_points,'config_maxfacts':config.maxfacts,
             'generator':'stochastic+certified-templates','replay_mode':'sha256-per-index'}
    self._atomic_json(manifest_path,manifest)
    return manifest

Phase3DatasetWriter.write = _phase3_write_advanced

_ORIGINAL_PHASE3_VERIFY = Phase3DatasetAuditor.verify

def _phase3_verify_advanced(path):
    report=_ORIGINAL_PHASE3_VERIFY(path)
    manifest=json.loads((Path(path)/'phase3_manifest.json').read_text(encoding='utf8'))
    seen=set();errors=list(report['errors']);cnt=0
    families=set(manifest['families'])
    for shard in manifest['files']:
        if not (Path(path)/shard).is_file():
            errors.append((shard,0,'arquivo inexistente'));continue
        if hashlib.sha256((Path(path)/shard).read_bytes()).hexdigest()!=manifest['sha256'][shard]:
            continue
        with gzip.open(Path(path)/shard,'rt',encoding='utf8') as fp:
            for line in fp:
                cnt+=1;rec=json.loads(line)
                if rec['family'] not in families:errors.append((shard,cnt,'família inválida'))
                if Phase3DatasetWriter.split(rec['family'],manifest.get('holdout',20)) not in shard:
                    # Manifestos antigos não gravaram porcentagem de holdout.
                    if manifest.get('holdout') is not None:
                        errors.append((shard,cnt,'split incorreto'))
                facts=tuple(GeometryParser().fact(x) for x in rec['problem']['hypotheses'])
                goal=GeometryParser().fact(rec['problem']['goal'])
                if (GeometryStructureFingerprint.key(facts,goal)!=rec['metadata']['structure_hash']):
                    errors.append((shard,cnt,'estrutura adulterada'))
                coords=rec.get('metadata',{}).get('coordinates')
                if coords:
                    if any(not num_check(x.legacy,coords) for x in facts if x.kind in MK):
                        errors.append((shard,cnt,'hipótese numérica falsa'))
                    if goal.kind in MK and not num_check(goal.legacy,coords):
                        errors.append((shard,cnt,'conclusão numérica falsa'))
                unique=manifest['unique']
                if unique!='none':
                    key=Phase3DatasetWriter._key(rec,unique)
                    if key in seen:errors.append((shard,cnt,'duplicata do dataset'))
                    seen.add(key)
    report['errors']=errors[:30]
    report['valid']=max(0,report['total']-len({(x[0],x[1]) for x in errors}))
    report['integrity_checks']='proof + sha256 + structure + coordinates + dedupe'
    return report

Phase3DatasetAuditor.verify = staticmethod(_phase3_verify_advanced)

# ═══════ FASE 2: SUBSTITUIÇÃO CERTIFICADA DE PONTOS COINCIDENTES ═══════
_PREVIOUS_RULE_V3 = ProofCheckerV2._rule.__func__

def _proof_rule_point_substitution(cls, step, known):
    if _PREVIOUS_RULE_V3(cls,step,known):return True
    s,p=step.conclusion,step.premises
    if step.rule=='overlap_transitive' and len(p)==2 and s.kind=='overlap' and all(x.kind=='overlap' for x in p):
        uf=GeometryUnionFind()
        for fact in p:uf.union(*fact.args)
        return (s.args[0]!=s.args[1] and uf.find(s.args[0])==uf.find(s.args[1])
                and all(x in {a for z in p for a in z.args} for x in s.args))
    if step.rule=='overlap_substitute' and len(p)==2:
        eq=next((f for f in p if f.kind=='overlap'),None)
        old=next((f for f in p if f is not eq),None)
        if eq is None or old is None or s.kind!=old.kind:return False
        if old.kind in ('overlap','ncoll','distinct','noverlap','lessthan','sameclock'):
            return False
        a,b=eq.args
        for x,y in ((a,b),(b,a)):
            for i,name in enumerate(old.args):
                if name!=x:continue
                args=list(old.args);args[i]=y
                try:replaced=GeoFact(old.kind,tuple(args))
                except GeometrySyntaxError:continue
                if s.legacy != replaced.legacy:continue
                if any(not cls._distinct(known,*seg) for seg in NonDegeneracyGuard.required_for(s)):
                    continue
                if s.kind=='cyclic' and len(set(s.args))!=4:continue
                if s.kind=='simtri' and len(set(s.args[:3]))!=3:continue
                return True
        return False
    return False

ProofCheckerV2._rule=classmethod(_proof_rule_point_substitution)

class FullerCertifiedDDAR2Engine(CertifiedDDAR2Engine):
    """Expande equivalências de pontos sob prova (sem identidade numérica)."""
    def add(self,conclusion,rule,premises):
        f=GeometryCanonicalizer().fact(conclusion)
        if f not in self.known:
            consistent,_=GeometryAssumptionConsistency.check((*self.known,f))
            if not consistent:return False
        return super().add(f,rule,premises)
    def _overlaps(self,f):
        if f.kind=='overlap':
            for g in sorted(self.by_kind['overlap'],key=str):
                if f!=g:
                    for a,b in itertools.permutations(sorted(set(f.args+g.args)),2):
                        self.add(self._fact('overlap',a,b),'overlap_transitive',(f,g))
            bases=tuple(sorted(self.known,key=str))
            for base in bases:
                if base.kind=='overlap':continue
                for i,x in enumerate(base.args):
                    for a,b in ((f.args[0],f.args[1]),(f.args[1],f.args[0])):
                        if x==a:
                            args=list(base.args);args[i]=b
                            try:sub=GeoFact(base.kind,tuple(args))
                            except GeometrySyntaxError:continue
                            self.add(sub,'overlap_substitute',(f,base))
        elif f.kind in ('coll','para','perp','cong','midp','cyclic','eqangle','eqratio'):
            for eq in sorted(self.by_kind['overlap'],key=str):
                for i,x in enumerate(f.args):
                    for a,b in ((eq.args[0],eq.args[1]),(eq.args[1],eq.args[0])):
                        if x!=a:continue
                        args=list(f.args);args[i]=b
                        try:sub=GeoFact(f.kind,tuple(args))
                        except GeometrySyntaxError:continue
                        self.add(sub,'overlap_substitute',(eq,f))
    def close(self,max_steps=30000):
        if not hasattr(self,'_overlap_processed'):self._overlap_processed=set()
        for _ in range(4):
            old=len(self.known)
            super().close(max_steps=max_steps)
            todo=sorted(self.known-self._overlap_processed,key=str)
            for f in todo:
                if len(self.known)>=self.maxfacts or (self.deadline and time.monotonic()>self.deadline):break
                self._overlap_processed.add(f)
                if self.by_kind['overlap']:self._overlaps(f)
            if len(self.known)==old:break
        return self
CertifiedDDAR2Engine = FullerCertifiedDDAR2Engine

# ═══════ FASE 2: ESTENDER O GERADOR DE DIAGRAMAS NÃO CONSTRUTIVOS ═══════
_OLD_RESIDUAL_V2=NumericalConstraintSolver2._residual

def _residual_geometric_extended(fact,C):
    k=fact.kind
    if k in ('eqangle','eqratio','sameclock','lessthan','overlap'):
        p=[C[x] for x in fact.args]
        if k=='overlap':
            return [(p[0][i]-p[1][i])/max(1.,dist(*p)) for i in range(2)]
        if k=='sameclock':
            u=area2(*p[:3]);v=area2(*p[3:])
            return [max(0.,1.e-5-min(abs(u),abs(v))),
                    max(0.,1.e-5-((u*v)/max(1.,abs(u*v))))]
        if k=='lessthan':
            d1=dist(p[0],p[1]);d2=dist(p[2],p[3])
            return [max(0.,d1-d2+1.e-5)/max(1.,d1,d2)]
        if k=='eqangle':
            dirs=[sub(p[i+1],p[i]) for i in range(0,8,2)]
            if any(math.hypot(*u)<1.e-9 for u in dirs):return [1.]
            a1=math.atan2(cross(dirs[0],dirs[1]),dot(dirs[0],dirs[1]))
            a2=math.atan2(cross(dirs[2],dirs[3]),dot(dirs[2],dirs[3]))
            return [math.sin(a1-a2)]
        if k=='eqratio':
            d=[dist(p[i],p[i+1]) for i in (0,2,4,6)]
            if min(d)<1.e-9:return [1.]
            return [math.log(d[0])-math.log(d[1])-math.log(d[2])+math.log(d[3])]
    return _OLD_RESIDUAL_V2(fact,C)

NumericalConstraintSolver2._residual=staticmethod(_residual_geometric_extended)

# ═══════ FASE 3: DIAGRAMAS ALEATÓRIOS E MINERAÇÃO DE PROVAS ═══════
class RandomDiagramProofMiner:
    """Gera diagramas ALEATÓRIOS com as 12 construções de CONS e busca
    demonstrações certificadas entre as conclusões do próprio fechamento.

    As condições auxiliares de ncoll/distinct são explicitadas e minimizadas.
    A verificação do certificado é independente da realização numérica.
    """
    def __init__(self,seed,max_points=14,maxfacts=700,budget_s=.65):
        self.rng=random.Random(seed)
        self.max_points=max_points;self.maxfacts=maxfacts;self.budget_s=budget_s
    def next(self,seed=0,attempts=75):
        cfg=Cfg();cfg.min_pts=7;cfg.max_pts=min(20,self.max_points)
        parser=GeometryParser();checker=ProofCheckerV2()
        for _ in range(attempts):
            output=build_diagram(self.rng,cfg)
            if output is None:continue
            defs,C,given=output
            # Premissas originais decorrentes das construções aleatórias.
            originals=[]
            for st,_pt in given:
                try:originals.append(GeoFact.from_tuple(st))
                except GeometrySyntaxError:pass
            conditions=[]
            for a,b in itertools.combinations(sorted(C),2):
                if dist(C[a],C[b])>1.e-5:conditions.append(GeoFact('distinct',(a,b)))
            for a,b,c in itertools.combinations(sorted(C),3):
                if abs(area2(C[a],C[b],C[c]))>1.e-3:
                    conditions.append(GeoFact('ncoll',(a,b,c)))
            hypotheses=tuple(dict.fromkeys((*originals,*conditions)))
            if len(hypotheses)>600:continue
            eng=CertifiedDDAR2Engine(hypotheses,maxfacts=self.maxfacts,
                 deadline=time.monotonic()+self.budget_s).close()
            targets=sorted((f for f in eng.known if f not in hypotheses and
                     f.kind in ('para','perp','cyclic','cong','midp','eqangle','eqratio')), key=str)
            self.rng.shuffle(targets)
            for goal in targets[:10]:
                cert=eng.certificate(goal)
                if cert is None or not cert.steps:continue
                if not num_check(goal.legacy,C):continue
                # Diminui primeiro condições de orientação/não-degenerescência
                # irrelevantes para os passos do certificado.
                active={x for st in cert.steps for x in st.premises}
                points={x for f in (*active,goal) for x in f.args}
                selected=[f for f in hypotheses if f in active or
                          (f.kind in ('distinct','ncoll') and set(f.args)<=points)]
                other=[f for f in selected if f not in active]
                newcert=ProofCertificate(tuple(selected),cert.goal,cert.steps,cert.metadata)
                # Condições adicionais são testadas de forma exata no checker.
                if not checker.verify(newcert)[0]:continue
                for f in other:
                    trial=[x for x in selected if x!=f]
                    tc=ProofCertificate(tuple(trial),goal,cert.steps,cert.metadata)
                    if checker.verify(tc)[0]:selected=trial
                cert=ProofCertificate(tuple(selected),goal,cert.steps,
                           {'engine':'random-diagram-miner','proof_source':'verified'})
                if checker.verify(cert)[0]:
                    return defs,C,tuple(selected),goal,cert
        raise GeometryProofError('não encontrou objetivo certificado no orçamento')

# Atualiza o gerador existente sem modificar seu formato externo.
_PREV_ADVANCED_NEXT = Phase3GeneratorAdvanced.next_record

def _advanced_next_with_random(self,family=None):
    if family != 'random_construction_diagram':
        return _PREV_ADVANCED_NEXT(self,family)
    miner=RandomDiagramProofMiner(self.cfg.seed,self.cfg.max_points,self.cfg.maxfacts)
    defs,C,hyp,goal,cert=miner.next()
    defs_data=[{'point':p,'operator':op,'args':list(args)} for p,op,args in defs]
    return {'schema':'geoforge-synthetic-v3','family':family,
            'problem':{'hypotheses':[str(x) for x in hyp], 'goal':str(goal), 'points':sorted(C)},
            'auxiliaries':[], 'auxiliary_necessity':'not_asserted',
            'proof':cert.to_dict(),
            'metadata':{'steps':len(cert.steps),'facts':len(hyp)+len(cert.steps),
                        'difficulty':len(cert.steps)+math.log1p(len(C)),
                        'structure_hash':GeometryStructureFingerprint.key(hyp,goal),
                        'seed':self.cfg.seed,'coords_tested':True,
                        'coordinates':{k:list(map(float,C[k])) for k in sorted(C)},
                        'construction_sequence':defs_data,'construction_source':'random-diagram'}}

Phase3GeneratorAdvanced.next_record=_advanced_next_with_random
# Define a 16ª família e integra-a ao escalonador estocástico; a lista do
# manifesto é agora derivada uma única vez desta tupla.
StochasticSyntheticFactory.families=(*StochasticSyntheticFactory.families,'random_construction_diagram')

# ═══════ ADAPTADOR DE COMPATIBILIDADE COM O DDAR2 PÚBLICO ═══════
# Reconhece o formato serializado real do repositório alphageometry2.
# A execução integral do DDAR2 depende dos arquivos oficiais, sob Apache-2.0.
@dataclass(frozen=True)
class AG2RawPredicate:
    name: str
    points: tuple[str,...]
    constants: tuple[Fraction,...]=()
    def __str__(self):
        return ' '.join((self.name,*self.points,*(str(v) for v in self.constants)))

@dataclass(frozen=True)
class AG2RawProblem:
    points: Mapping[str,tuple[float,float]]
    predicates: tuple[AG2RawPredicate,...]
    goal: AG2RawPredicate

class AG2PublicProblemParser:
    """Parser estrito do AGProblem.pstring() do repositório AlphaGeometry2.

    Retém constantes como Fraction, não avalia código e preserva pontos duplos.
    Não confunde suporte sintático com capacidade matemática de inferência.
    """
    @staticmethod
    def _predicate(source):
        tokens=source.strip().split()
        if not tokens:raise GeometrySyntaxError('predicado oficial vazio')
        points=[];constants=[]
        for t in tokens[1:]:
            try:
                if 'pi/' in t:
                    numerator,denominator=t.split('pi/')
                    value=Fraction(int(numerator)*180,int(denominator))
                else:value=Fraction(t)
            except (ValueError,ZeroDivisionError):
                points.append(t)
            else:constants.append(value)
        return AG2RawPredicate(tokens[0],tuple(points),tuple(constants))
    def parse(self,text):
        if text.count('?')!=1:
            raise GeometrySyntaxError('problema AG2 deve ter uma única interrogação separando a meta')
        lhs,rhs=text.split('?',1)
        goal=self._predicate(rhs)
        points={};prem=[]
        for clause in lhs.split(';'):
            if not clause.strip():continue
            if clause.count('=')!=1:raise GeometrySyntaxError('declaração AG2 necessita sinal =')
            declared,preds=clause.split('=',1)
            for token in declared.split():
                if '@' not in token:raise GeometrySyntaxError('ponto sem coordenadas: '+token)
                name,xy=token.rsplit('@',1)
                if name in points:raise GeometrySyntaxError('ponto redefinido: '+name)
                a,b=xy.split('_',1)
                x,y=float(a),float(b)
                if not all(map(math.isfinite,(x,y))):raise GeometrySyntaxError('coordenadas não finitas')
                points[name]=(x,y)
            for p in preds.split(','):
                if p.strip():prem.append(self._predicate(p))
        if not points:raise GeometrySyntaxError('problema AG2 sem pontos')
        if any(x not in points for f in (*prem,goal) for x in f.points if x!='*'):
            raise GeometrySyntaxError('predicado usa ponto não declarado')
        return AG2RawProblem(points,tuple(prem),goal)

class AG2OfficialCoreBridge:
    """Executa o DDAR2 OFICIAL, separadamente, quando o checkout existe.

    Este adaptador evita anunciar a implementação parcial local como DDAR2.
    O sub-processo usa os arquivos oficiais ddar.py, parse.py,
    numericals.py e elimination.py, sem modificar sua semântica.
    """
    @staticmethod
    def run(problem_text,official_dir,timeout=120):
        import subprocess
        directory=Path(official_dir).resolve()
        required=('ddar.py','elimination.py','numericals.py','parse.py')
        missing=[x for x in required if not (directory/x).is_file()]
        if missing:raise FileNotFoundError('repositório AG2 incompleto: '+', '.join(missing))
        # O subprocesso só executa código do repositório que o usuário
        # explicitamente instalou. Entrada do problema segue pelo stdin.
        script='''import sys,json
from parse import AGProblem
from ddar import DDAR
try:
    prob=AGProblem.parse(sys.stdin.read())
    core=DDAR(prob.points)
    for f in prob.preds:core.force_pred(f)
    core.deduction_closure()
    print(json.dumps({'solved':bool(core.check_pred(prob.goal)),
                      'engine':'Google DeepMind public DDAR2',
                      'points':len(prob.points),'premises':len(prob.preds)}))
except Exception as ex:
    print(json.dumps({'solved':False,'engine':'Google DeepMind public DDAR2',
                      'error':str(ex)}))
    sys.exit(2)
'''
        out=subprocess.run([sys.executable,'-c',script],input=problem_text,text=True,
                cwd=directory,capture_output=True,timeout=timeout,check=False)
        if out.returncode not in (0,2):
            raise RuntimeError('DDAR2 retornou erro: '+out.stderr[-3000:])
        lines=[x for x in out.stdout.splitlines() if x.lstrip().startswith('{')]
        if not lines:raise RuntimeError('DDAR2 não produziu resultado JSON: '+out.stderr[-2000:])
        result=json.loads(lines[-1])
        result['stderr_tail']=out.stderr[-1000:]
        return result

def cmd_ag2_parse_public(a):
    text=(Path(a.file).read_text(encoding='utf8') if a.file else a.text)
    prob=AG2PublicProblemParser().parse(text)
    supports=set(GEOMETRY_REGISTRY.predicates)
    result={'points':len(prob.points),'predicates':len(prob.predicates),
            'goal':str(prob.goal),'predicate_types':dict(Counter(f.name for f in prob.predicates)),
            'unsupported_by_local_certifier':sorted(set(f.name for f in (*prob.predicates,prob.goal))
                                                -{'coll','perp','para','cong','midp','cyclic','eqangle','eqratio','ncoll','distinct','overlap','noverlap'}),
            'has_overlapping_coordinates':any(dist(x,y)<=1.e-10 for x,y in itertools.combinations(prob.points.values(),2))}
    print(json.dumps(result,ensure_ascii=False,indent=2))
    return 0

def cmd_ag2_official_public(a):
    text=(Path(a.file).read_text(encoding='utf8') if a.file else a.text)
    AG2PublicProblemParser().parse(text)
    result=AG2OfficialCoreBridge.run(text,a.official_dir,a.timeout)
    print(json.dumps(result,ensure_ascii=False,indent=2))
    return 0 if result.get('solved') else 1

# ═══════ FASE 3: ESCALA, SHARDS DETERMINÍSTICOS E EXECUÇÃO PARALELA ═══════
from concurrent.futures import ProcessPoolExecutor

def _phase3_generate_index(job):
    index,seed,max_points,maxfacts,min_steps,max_steps,holdout,max_trials,all_families=job
    derived=int.from_bytes(hashlib.sha256(f'{seed}:{index}'.encode()).digest()[:8],'big')
    cfg=Phase3Config(count=1,seed=derived,max_points=max_points,
         maxfacts=maxfacts,min_steps=min_steps,max_steps=max_steps,
         family_holdout=holdout,max_trials_per_record=max_trials)
    rec=Phase3Generator(cfg).next_record(all_families[index%len(all_families)])
    return index,rec

def _phase3_write_parallel(self,config,unique='exact',resume=False):
    if unique not in ('none','exact','structural'):raise ValueError('modo de dedupe inválido')
    families=(*GeometryTemplateFactory.families,*StochasticSyntheticFactory.families)
    manifest_path=self.path/'phase3_manifest.json'
    if manifest_path.exists() and not resume:raise FileExistsError('use --resume ou outro diretório')
    start=0;counts=Counter();seen=set();files=[]
    if resume and manifest_path.exists():
        old=json.loads(manifest_path.read_text(encoding='utf8'))
        if (old['seed']!=config.seed or old['unique']!=unique or old['shard_size']!=self.shard_size
            or old['families']!=list(families)
            or old.get('config_max_points',config.max_points)!=config.max_points
            or old.get('config_maxfacts',config.maxfacts)!=config.maxfacts
            or old.get('holdout',config.family_holdout)!=config.family_holdout):
            raise GeometrySyntaxError('retomada com configurações divergentes')
        start=old['generated'];counts.update(old['counts']);files=list(old['files'])
        for entry in files:
            path=self.path/entry
            if hashlib.sha256(path.read_bytes()).hexdigest()!=old['sha256'][entry]:
                raise GeometryProofError('shard corrompido: '+entry)
            if unique!='none':
                with gzip.open(path,'rt',encoding='utf8') as fp:
                    for line in fp:
                        seen.add(self._key(json.loads(line),unique))
    def jobs():
        for index in range(start,config.count):
            yield (index,config.seed,config.max_points,config.maxfacts,
                   config.min_steps,config.max_steps,config.family_holdout,
                   config.max_trials_per_record,families)
    buffers=defaultdict(list)
    def consume(iterator):
        for index,rec in iterator:
            key=self._key(rec,unique)
            if unique!='none' and key in seen:continue
            seen.add(key)
            dest=self.split(rec['family'],config.family_holdout)
            buffers[dest].append(rec);counts[dest]+=1
            if sum(map(len,buffers.values()))>=self.shard_size:
                files.extend(self._flush(buffers,len(files)));buffers.clear()
    if config.workers==1:
        consume(map(_phase3_generate_index,jobs()))
    else:
        # executor.map preserva ordem de índice, tornando a geração de registros
        # idêntica com 1 ou N processos (sem depender da ordem de conclusão).
        with ProcessPoolExecutor(max_workers=config.workers) as pool:
            consume(pool.map(_phase3_generate_index,jobs(),chunksize=2))
    if buffers:files.extend(self._flush(buffers,len(files)))
    manifest={'schema':'geoforge-phase3-manifest-v4','seed':config.seed,
              'generated':config.count,'unique':unique,'shard_size':self.shard_size,
              'files':files,
              'sha256':{n:hashlib.sha256((self.path/n).read_bytes()).hexdigest() for n in files},
              'counts':dict(counts),'families':list(families),
              'certified':True,'fully_ag2_compatible':False,
              'config_max_points':config.max_points,'config_maxfacts':config.maxfacts,
              'holdout':config.family_holdout,
              'generator':'random construction + certified stochastic/composed problems',
              'replay_mode':'sha256-per-index',
              'workers_on_last_run':config.workers}
    self._atomic_json(manifest_path,manifest)
    return manifest

Phase3DatasetWriter.write=_phase3_write_parallel

def _phase3_deterministic_flush(self,buffers,group):
    names=[]
    for split,records in sorted(buffers.items()):
        filename=f'phase3_{split}_{group:06d}.jsonl.gz'
        target=self.path/filename;temporary=target.with_name(target.name+'.part')
        # gzip.GzipFile(mtime=0) fixa os cabeçalhos e garante hash reprodutível
        # mesmo em execuções separadas por dias ou em processos diferentes.
        with open(temporary,'wb') as raw:
            with gzip.GzipFile(filename='',fileobj=raw,mode='wb',mtime=0,compresslevel=6) as gz:
                with io.TextIOWrapper(gz,encoding='utf8') as fp:
                    for rec in records:
                        fp.write(json.dumps(rec,ensure_ascii=False,sort_keys=True)+'\n')
        os.replace(temporary,target);names.append(filename)
    return names

Phase3DatasetWriter._flush=_phase3_deterministic_flush

# Auditoria completa das premissas numéricas nos datasets sintéticos.
def _phase3_check_numeric_hypothesis(f,C,eps=1.e-6):
    try:p=[C[x] for x in f.args]
    except KeyError:return False
    if f.kind in MK:return num_check(f.legacy,C,eps)
    if f.kind in ('distinct','noverlap'):
        return len(p)==2 and dist(*p)>eps
    if f.kind=='overlap':
        return len(p)==2 and dist(*p)<=eps
    if f.kind=='ncoll':
        return len(p)==3 and abs(area2(*p))>eps
    if f.kind=='sameclock':
        if len(p)!=6:return False
        x=area2(*p[:3]);y=area2(*p[3:]);return abs(x)>eps and abs(y)>eps and x*y>0
    if f.kind=='lessthan':
        return len(p)==4 and dist(*p[:2])+eps<dist(*p[2:])
    # Este dataset não produz outros predicados. Fatos desconhecidos não
    # podem receber rótulo "numericamente validados" silenciosamente.
    return False

_PREVIOUS_DATASET_AUDIT=Phase3DatasetAuditor.verify

def _phase3_audit_all_hypotheses(path):
    report=_PREVIOUS_DATASET_AUDIT(path);errors=list(report['errors']);n=0
    manifest=json.loads((Path(path)/'phase3_manifest.json').read_text(encoding='utf8'))
    for name in manifest['files']:
        p=Path(path)/name
        if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=manifest['sha256'][name]:continue
        with gzip.open(p,'rt',encoding='utf8') as f:
            for line in f:
                n+=1;record=json.loads(line)
                coords=record.get('metadata',{}).get('coordinates')
                if coords is None:continue
                for source in record['problem']['hypotheses']:
                    fact=GeometryParser().fact(source)
                    if not _phase3_check_numeric_hypothesis(fact,coords):
                        errors.append((name,n,'hipótese numérica incompatível: '+source));break
                goal=GeometryParser().fact(record['problem']['goal'])
                if goal.kind in MK and not _phase3_check_numeric_hypothesis(goal,coords):
                    errors.append((name,n,'meta numérica incompatível'))
    report['errors']=errors[:40]
    report['valid']=max(0,report['total']-len({(x[0],x[1]) for x in errors}))
    report['integrity_checks']='proof + sha256 + structure + all numeric hypotheses + dedupe'
    return report

Phase3DatasetAuditor.verify=staticmethod(_phase3_audit_all_hypotheses)

# ══════ SEM TREINAMENTO: HIPÓTESES LATERAIS INFERIDAS E CERTIFICADAS ══════
# Distinções podem ser *consequências* de um predicado geométrico bem definido.
# Cada nova regra é aceita apenas quando o ProofChecker reconstrói a dedução.
_PROOF_RULE_BEFORE_GUARDS = ProofCheckerV2._rule.__func__

def _proof_rule_guard_consequence(cls, step, known):
    if _PROOF_RULE_BEFORE_GUARDS(cls,step,known):return True
    ps=step.premises;s=step.conclusion;k=step.rule
    if len(ps)!=1:return False
    base=ps[0]
    if k=='segment_nonzero_from_relation' and base.kind in ('para','perp') and s.kind in ('distinct','noverlap'):
        return (frozenset(s.args) in (frozenset(base.args[:2]),frozenset(base.args[2:]))
                and len(set(s.args))==2)
    if k=='cyclic_ncoll' and base.kind=='cyclic' and s.kind=='ncoll':
        return len(set(base.args))==4 and len(set(s.args))==3 and set(s.args)<=set(base.args)
    if k=='ncoll_distinct' and base.kind=='ncoll' and s.kind in ('distinct','noverlap'):
        return len(set(base.args))==3 and len(set(s.args))==2 and set(s.args)<=set(base.args)
    return False

ProofCheckerV2._rule=classmethod(_proof_rule_guard_consequence)

_PREVIOUS_PROOF_RULE_WITH_GUARDS=ProofCheckerV2._rule.__func__

def _proof_rule_explicit_guard_deps(cls,step,known):
    if _PREVIOUS_PROOF_RULE_WITH_GUARDS(cls,step,known):return True
    p=step.premises
    if step.rule=='guarded_line_pair':
        geometries=tuple(x for x in p if x.kind in ('para','perp'))
        guards=tuple(x for x in p if x.kind in ('distinct','noverlap'))
        if len(geometries)!=2 or len(guards)!=3 or len(p)!=5:return False
        orig={('para','para'):('para','para_pair_para'),
              ('perp','perp'):('para','perp_pair_para'),
              ('para','perp'):('perp','para_perp_pair'),
              ('perp','para'):('perp','para_perp_pair')}.get(tuple(x.kind for x in geometries))
        if orig is None or step.conclusion.kind!=orig[0]:return False
        trial=ProofStep(step.conclusion,orig[1],geometries)
        return _PREVIOUS_PROOF_RULE_WITH_GUARDS(cls,trial,set(known)|set(guards))
    if step.rule=='guarded_cyclic_angle':
        cycles=tuple(x for x in p if x.kind=='cyclic')
        noncoll=tuple(x for x in p if x.kind=='ncoll')
        if len(cycles)!=1 or len(noncoll)!=2 or len(p)!=3:return False
        trial=ProofStep(step.conclusion,'circle_inscribed_angle',cycles)
        return _PREVIOUS_PROOF_RULE_WITH_GUARDS(cls,trial,set(known)|set(noncoll))
    return False

ProofCheckerV2._rule=classmethod(_proof_rule_explicit_guard_deps)

class GuardAwareCertifiedDDAR2Engine(CertifiedDDAR2Engine):
    """Include nondegeneracy facts in every dependent proof certificate."""
    def _pair(self,x,y):
        # An independent proof checker must see the side-guards as actual
        # dependencies, not rely on other facts happened to be present in RAM.
        if x.kind not in ('para','perp') or y.kind not in ('para','perp'):return
        patterns={('para','para'):'para',('perp','perp'):'para',
                  ('para','perp'):'perp',('perp','para'):'perp'}
        result=patterns[x.kind,y.kind]
        xx=(frozenset(x.args[:2]),frozenset(x.args[2:]))
        yy=(frozenset(y.args[:2]),frozenset(y.args[2:]))
        for i,j in itertools.product((0,1),repeat=2):
            if xx[i]!=yy[j]:continue
            segments=(xx[i],xx[1-i],yy[1-j])
            if any(len(z)!=2 for z in segments):continue
            guards=tuple(self._fact('distinct',*sorted(seg)) for seg in segments)
            if not all(g in self.known for g in guards):continue
            self.add(self._fact(result,*sorted(xx[1-i]),*sorted(yy[1-j])),
                     'guarded_line_pair',(x,y,*guards))
    def _cyclic_angles(self,cy):
        for a,b in itertools.combinations(cy.args,2):
            c,d=(x for x in cy.args if x not in (a,b))
            guard_groups=(frozenset((c,a,b)),frozenset((d,a,b)))
            guards=tuple(next((z for z in self.by_kind['ncoll']
                               if frozenset(z.args)==needed),None)
                         for needed in guard_groups)
            if all(g is not None for g in guards):
                self.add(self._fact('eqangle',c,a,c,b,d,a,d,b),
                         'guarded_cyclic_angle',(cy,*guards))
    def close(self,max_steps=30000):
        for f in tuple(sorted(self.assumptions,key=str)):
            if f.kind in ('para','perp'):
                a,b,c,d=f.args
                for u,v in ((a,b),(c,d)):
                    if u!=v:self.add(self._fact('distinct',u,v),
                                     'segment_nonzero_from_relation',(f,))
            elif f.kind=='cyclic' and len(set(f.args))==4:
                for triple in itertools.combinations(f.args,3):
                    self.add(self._fact('ncoll',*triple),'cyclic_ncoll',(f,))
        for fact in tuple(sorted(self.by_kind['ncoll'],key=str)):
            for u,v in itertools.combinations(fact.args,2):
                self.add(self._fact('distinct',u,v),'ncoll_distinct',(fact,))
        return super().close(max_steps=max_steps)

CertifiedDDAR2Engine=GuardAwareCertifiedDDAR2Engine

# ---------------------------------------------------------------------------
# GeoForge extension integration (research modules, optional dependencies).
# The historical commands remain backwards compatible. The new "upgrade"
# namespace is deliberately explicit so no existing argument is hijacked.
# ---------------------------------------------------------------------------
_GEOFORGE_LEGACY_MAIN = main

def main(argv=None):
    arguments = list(sys.argv[1:] if argv is None else argv)
    if arguments and arguments[0] == "upgrade":
        from geoforge_upgrade_suite.upgrade_cli import main as extended_main
        return extended_main(arguments[1:])
    return _GEOFORGE_LEGACY_MAIN(argv)

if __name__ == "__main__":
    sys.exit(main())
