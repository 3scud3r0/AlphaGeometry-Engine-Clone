"""JGEX-AG-231 adapter: external corpus required."""
from .official_loader import load_lines,require_count
COUNT=231
def load(path):return require_count(load_lines(path),COUNT)
