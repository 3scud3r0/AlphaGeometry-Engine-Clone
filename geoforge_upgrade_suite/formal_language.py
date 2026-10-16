#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Conservative Portuguese/English geometry-to-DSL formalization.

Every recognized statement is traceable to an explicit source span. Unknown
phrases result in an explicit UNSUPPORTED diagnosis; they are NOT silently
translated by guessing. This is a deterministic parser, not the AG2 Gemini
natural-language formalizer.
"""
from __future__ import annotations
from dataclasses import dataclass,field
from typing import Any,Mapping,Sequence
from collections import defaultdict
import hashlib
import json
import re
import unicodedata

class FormalizationError(ValueError):pass


def ascii_fold(text:str)->str:
    return ''.join(c for c in unicodedata.normalize('NFD',text) if unicodedata.category(c)!='Mn')


def simplify(text:str)->str:
    result=ascii_fold(text).lower()
    result=re.sub(r'\s+',' ',result)
    return result.strip()


@dataclass(frozen=True)
class SourceEvidence:
    start:int
    stop:int
    original:str
    normalized:str
    predicate:str
    def __post_init__(self):
        if not 0<=self.start<=self.stop:raise FormalizationError('invalid source offsets')


@dataclass(frozen=True)
class FormalProblem:
    hypotheses:tuple[str,...]
    goal:str|None
    evidence:tuple[SourceEvidence,...]
    unsupported:tuple[str,...]
    points:tuple[str,...]
    source_language:str
    def is_complete(self):
        return bool(self.goal) and not self.unsupported
    def to_dict(self):
        return {'hypotheses':self.hypotheses,'goal':self.goal,
                'evidence':[x.__dict__ for x in self.evidence],
                'unsupported':self.unsupported,'points':self.points,
                'language':self.source_language,'complete':self.is_complete()}


@dataclass(frozen=True)
class PatternSpec:
    rule:str
    regex:str
    dsl_kind:str
    group_order:tuple[str,...]
    language:str='both'
    def compile(self):return re.compile(self.regex,re.IGNORECASE)


POINT=r'(?P<{g}>[A-Z][A-Za-z0-9_]*)'
SEGMENT=r'(?P<{g}>[A-Z][A-Za-z0-9_]*)'


PATTERNS=(
 PatternSpec('midpoint_pt',r'(?P<m>[A-Z])\s+(?:e|is)\s+(?:o\s+)?(?:ponto\s+medio|midpoint)\s+(?:de|do|of)\s+(?P<a>[A-Z])(?P<b>[A-Z])','midp',('m','a','b')),
 PatternSpec('midpoint_alt',r'(?:o\s+)?ponto\s+medio\s+de\s+(?P<a>[A-Z])(?P<b>[A-Z])\s+(?:e|eh)\s+(?P<m>[A-Z])','midp',('m','a','b'),'pt'),
 PatternSpec('parallel_pt',r'(?P<a>[A-Z])(?P<b>[A-Z])\s+(?:e|is)\s+(?:paralel[oa]|parallel)\s+(?:a|ao|to)\s+(?P<c>[A-Z])(?P<d>[A-Z])','para',('a','b','c','d')),
 PatternSpec('parallel_alt',r'(?P<a>[A-Z])(?P<b>[A-Z])\s*//\s*(?P<c>[A-Z])(?P<d>[A-Z])','para',('a','b','c','d')),
 PatternSpec('perp_pt',r'(?P<a>[A-Z])(?P<b>[A-Z])\s+(?:e|is)\s+(?:perpendicular|ortogonal)\s+(?:a|ao|to)\s+(?P<c>[A-Z])(?P<d>[A-Z])','perp',('a','b','c','d')),
 PatternSpec('perp_symbol',r'(?P<a>[A-Z])(?P<b>[A-Z])\s*(?:⊥|\\perp)\s*(?P<c>[A-Z])(?P<d>[A-Z])','perp',('a','b','c','d')),
 PatternSpec('equal_segments',r'(?P<a>[A-Z])(?P<b>[A-Z])\s*=\s*(?P<c>[A-Z])(?P<d>[A-Z])','cong',('a','b','c','d')),
 PatternSpec('coll_pt',r'(?P<a>[A-Z]),?\s+(?P<b>[A-Z])\s+e\s+(?P<c>[A-Z])\s+(?:sao\s+)?colineares','coll',('a','b','c'),'pt'),
 PatternSpec('coll_en',r'(?P<a>[A-Z]),?\s+(?P<b>[A-Z])\s+and\s+(?P<c>[A-Z])\s+are\s+collinear','coll',('a','b','c'),'en'),
 PatternSpec('cyclic_pt',r'(?P<a>[A-Z]),?\s+(?P<b>[A-Z]),?\s+(?P<c>[A-Z])\s+e\s+(?P<d>[A-Z])\s+(?:sao\s+)?concilicos','cyclic',('a','b','c','d'),'pt'),
 PatternSpec('cyclic_en',r'(?P<a>[A-Z]),?\s+(?P<b>[A-Z]),?\s+(?P<c>[A-Z])\s+and\s+(?P<d>[A-Z])\s+are\s+concyclic','cyclic',('a','b','c','d'),'en'),
 PatternSpec('distinct_pt',r'(?P<a>[A-Z])\s+e\s+(?P<b>[A-Z])\s+(?:sao\s+)?distintos','distinct',('a','b'),'pt'),
 PatternSpec('distinct_en',r'(?P<a>[A-Z])\s+and\s+(?P<b>[A-Z])\s+are\s+distinct','distinct',('a','b'),'en'),
 PatternSpec('same_pt',r'(?P<a>[A-Z])\s+e\s+(?P<b>[A-Z])\s+(?:sao|representam)\s+(?:o\s+)?mesmo\s+ponto','overlap',('a','b'),'pt'),
)


def normalize_geometry_clause(text:str)->str:
    # Unlike global lowercasing, point names remain upper-case.
    return re.sub(r'\s+',' ',ascii_fold(text).strip()).rstrip(' .;:')


class GeometricRelationExtractor:
    def __init__(self,patterns=PATTERNS):
        self.patterns=tuple(patterns)
        self.compiled=[(x,x.compile()) for x in self.patterns]
    def recognize(self,clause:str):
        source=normalize_geometry_clause(clause)
        for rule,rx in self.compiled:
            matched=rx.fullmatch(source)
            if not matched:continue
            parts=[matched.group(g) for g in rule.group_order]
            if any(len(p)!=1 or not p.isupper() for p in parts):continue
            if rule.dsl_kind in ('coll','cyclic') and len(set(parts))!=len(parts):
                raise FormalizationError('repeated points require explicit nondegeneracy semantics')
            return rule.dsl_kind+' '+' '.join(parts),rule.rule
        raise FormalizationError('unsupported natural-language geometry clause: '+clause)


class GoalExtractor:
    PREFIXES=(
        r'^(?:prove|show|demonstrate|demostre|mostre|prove\s+que|demonstre\s+que|mostrar\s+que)\s+',
        r'^(?:conclua\s+que|conclude\s+that|show\s+that)\s+',
    )
    def split_goal(self,clause:str):
        text=normalize_geometry_clause(clause)
        for rule in self.PREFIXES:
            m=re.match(rule,text,re.IGNORECASE)
            if m:return text[m.end():],True
        return text,False


class NaturalLanguageGeometryParser:
    """Conservative clauses with explicit goal markers.

    Supports a small, testable subset. Multi-sentence implicit goals are not
    guessed.  Returns unsupported clauses for user review.
    """
    def __init__(self):
        self.extractor=GeometricRelationExtractor()
        self.goal_extractor=GoalExtractor()
    def parse(self,text:str)->FormalProblem:
        if not isinstance(text,str):raise TypeError('text required')
        # Split on semicolon/newline/full stop not within a fraction or word.
        clauses=[(m.start(),m.group().strip()) for m in re.finditer(r'[^;\n.]+',text)
                 if m.group().strip()]
        hyps=[];goal=None;evidence=[];unsupported=[]
        for start,clause in clauses:
            raw,goal_flag=self.goal_extractor.split_goal(clause)
            try:statement,rule=self.extractor.recognize(raw)
            except FormalizationError as ex:
                unsupported.append(clause);continue
            if goal_flag:
                if goal is not None:unsupported.append('multiple explicit goals: '+clause)
                else:goal=statement
            else:hyps.append(statement)
            evidence.append(SourceEvidence(start,start+len(clause),clause,
                                           normalize_geometry_clause(clause),statement))
        points=tuple(sorted({x for p in (*hyps,*((goal,) if goal else ()))
                             for x in p.split()[1:]}))
        language='pt' if re.search(r'\b(?:ponto|medio|demonstre|colineares|sao)\b',
                      simplify(text)) else 'en'
        return FormalProblem(tuple(dict.fromkeys(hyps)),goal,tuple(evidence),
                             tuple(unsupported),points,language)


class NLToDSLTranslator:
    def translate(self,text:str)->tuple[str,FormalProblem]:
        result=NaturalLanguageGeometryParser().parse(text)
        clauses=['given '+s for s in result.hypotheses]
        if result.goal:clauses.append('prove '+result.goal)
        return ' ; '.join(clauses),result


class LaTeXGeometryParser:
    r"""Only explicit AB \parallel CD, AB \perp CD, AB=CD statements."""
    def parse(self,text):
        clean=text.replace('$','').replace(r'\(','').replace(r'\)','')
        clean=clean.replace(r'\parallel','//').replace(r'\perp','⊥')
        clean=re.sub(r'\\overline\{([A-Z])([A-Z])\}',r'\1\2',clean)
        clean=re.sub(r'\s+',' ',clean).strip()
        return GeometricRelationExtractor().recognize(clean)[0]


class FormalizationConsistencyChecker:
    """Syntactic consistency checks, NOT full geometric satisfiability."""
    def check(self,problem:FormalProblem):
        errors=[];warnings=list(problem.unsupported)
        if not problem.goal:errors.append('goal not specified')
        hyps=set(problem.hypotheses)
        for f in hyps:
            a=f.split();k=a[0]
            if k=='distinct' and a[1]==a[2]:errors.append('a point cannot be distinct from itself')
            if k=='overlap' and 'distinct '+' '.join(a[1:]) in hyps:
                errors.append('point overlap contradicts distinctness')
            if k in ('para','perp') and (a[1]==a[2] or a[3]==a[4]):
                errors.append('zero segment in parallel/perpendicular statement')
        if problem.goal in hyps:
            warnings.append('the conclusion already appears as a hypothesis')
        return {'satisfiable_not_proven':not errors,'errors':errors,'warnings':warnings}


class MultilingualProblemInterface:
    def parse(self,text:str,language:str='auto'):
        if language not in ('auto','pt','en'):
            raise ValueError('unsupported language')
        p=NaturalLanguageGeometryParser().parse(text)
        if language!='auto' and p.source_language!=language:
            raise FormalizationError('language mismatch')
        return p


class NaturalLanguageProofGenerator:
    """Safe explicit translations of *known* rule names, no invented steps."""
    RULES={
     'midline':'Pelo teorema da base média, os segmentos são paralelos.',
     'midp_coll':'Um ponto médio pertence à reta que une os extremos.',
     'midp_cong':'Um ponto médio divide o segmento em duas partes iguais.',
     'perp_pair_para':'Retas perpendiculares à mesma reta são paralelas.',
     'para_pair_para':'Retas paralelas à mesma reta são paralelas.',
     'circle_inscribed_angle':'Ângulos inscritos na mesma corda são congruentes.',
    }
    def render(self,certificate:Mapping):
        lines=['Hipóteses:']
        lines.extend(' - '+x for x in certificate.get('assumptions',()))
        lines.append('Demonstração:')
        for i,step in enumerate(certificate.get('steps',()),1):
            rule=step.get('rule','')
            human=self.RULES.get(rule,'Aplicação formal da regra: '+rule)
            lines.append(f'{i}. {human} Conclusão: {step.get("conclusion","")}.')
        lines.append('Objetivo formal: '+certificate.get('goal',''))
        return '\n'.join(lines)


__all__=[name for name in globals() if not name.startswith('_') and name not in {
    'Any','Mapping','Sequence','dataclass','field','defaultdict','hashlib',
    'json','re','unicodedata'}]
