"""Stable exact-string contamination audit; geometric isomorphism not yet checked."""
from hashlib import sha256

def normalize(statement):
    return " ".join(statement.split())

def overlaps(training,heldout):
    hashes={sha256(normalize(x).encode()).hexdigest() for x in training}
    return tuple(x for x in heldout if sha256(normalize(x).encode()).hexdigest() in hashes)
