"""Small audited rule portfolio. NOT the complete Google DDAR2 rule set."""
from dataclasses import dataclass
from geoforge_core.ast import Predicate

@dataclass(frozen=True)
class Rule:
    name: str
    premises: tuple[Predicate,...]
    conclusion: Predicate

def default_rules():
    # Letter case for pattern variables is not significant; these are schematic.
    p=Predicate
    return (
        Rule("midline", (p("midp",("m","a","b")),p("midp",("n","a","c")),
                         p("ncoll",("a","b","c"))),p("para",("m","n","b","c"))),
        Rule("midpoint_collinear",(p("midp",("m","a","b")),p("noverlap",("a","b"))),
             p("coll",("m","a","b"))),
        Rule("cong_symmetric",(p("cong",("a","b","c","d")),),
             p("cong",("c","d","a","b"))),
        Rule("para_symmetric",(p("para",("a","b","c","d")),),
             p("para",("c","d","a","b"))),
    )
