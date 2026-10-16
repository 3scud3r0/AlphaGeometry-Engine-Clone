"""Import user-specified diagram annotations, not visual guesses."""
from geoforge_core.ast import Predicate
from geoforge_core.parser_ag2 import parse_predicate
from geoforge_core.type_system import check_predicate

def parse_annotations(annotations):
    if not isinstance(annotations,(list,tuple)):
        raise ValueError("annotations must be an explicit list")
    return tuple(check_predicate(parse_predicate(x)) for x in annotations)
