"""Replay JSON certificates with the small independent rule kernel."""
from geoforge_prover.certificates import verify_json
def checked_result(certificate):
    try:return bool(verify_json(certificate))
    except (TypeError,ValueError,KeyError):return False
