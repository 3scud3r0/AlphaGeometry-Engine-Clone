"""Load locally supplied official problem lists with source checksums."""
from pathlib import Path
import hashlib
from dataclasses import dataclass
@dataclass(frozen=True)
class Corpus:
    source:str
    sha256:str
    problems:tuple[str,...]

def load_lines(path):
    p=Path(path)
    if not p.is_file():raise FileNotFoundError(str(p))
    blob=p.read_bytes()
    lines=tuple(s.strip() for s in blob.decode("utf-8-sig").splitlines()
                if s.strip() and not s.lstrip().startswith("#"))
    if not lines:raise ValueError("empty benchmark corpus")
    return Corpus(str(p),hashlib.sha256(blob).hexdigest(),lines)

def require_count(corpus,expected):
    if len(corpus.problems)!=expected:
        raise ValueError(f"expected {expected} benchmark problems, got {len(corpus.problems)}")
    return corpus
