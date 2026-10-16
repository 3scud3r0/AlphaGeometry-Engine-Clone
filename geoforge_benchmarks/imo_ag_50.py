"""IMO-AG-50 adapter: external corpus required."""
from .official_loader import load_lines,require_count
COUNT=50
def load(path):return require_count(load_lines(path),COUNT)
