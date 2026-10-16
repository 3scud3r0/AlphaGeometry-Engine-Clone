"""IMO Shortlist 30 adapter: external corpus required."""
from .official_loader import load_lines,require_count
COUNT=30
def load(path):return require_count(load_lines(path),COUNT)
