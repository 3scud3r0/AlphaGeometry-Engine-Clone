"""Stable syntactic hashes; structural isomorphism remains an open extension."""
import hashlib,json
from geoforge_core.canonical import canonical

def content_hash(premises,goal):
    payload={"premises":sorted(set(canonical(p).serialize() for p in premises)),
             "goal":canonical(goal).serialize()}
    return hashlib.sha256(json.dumps(payload,sort_keys=True).encode()).hexdigest()

class HashDeduplicator:
    def __init__(self):self.seen=set()
    def add(self,key):
        if key in self.seen:return False
        self.seen.add(key);return True
