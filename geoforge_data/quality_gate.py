"""Reject records without an independently verified proof of the advertised goal."""
from geoforge_prover.certificates import load,verify_json
from geoforge_core.parser_ag2 import parse_predicate
from geoforge_core.canonical import canonical
class CertificateQualityGate:
    def validate(self,problem_goal,certificate_json):
        try:
            proof=load(certificate_json)
            return canonical(proof.goal)==canonical(parse_predicate(problem_goal)) and verify_json(certificate_json)
        except (ValueError,KeyError,TypeError):
            return False
