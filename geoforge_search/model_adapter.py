"""Optional neural proposer with strict grammar validation."""
from geoforge_core.parser_ag2 import parse_predicate
from geoforge_core.type_system import check_predicate

class ModelAdapter:
    def __init__(self,proposer):
        if not callable(proposer):raise TypeError("proposer must be callable")
        self.proposer=proposer
    def propose(self,problem,limit=10):
        results=[]
        for line in self.proposer(problem):
            if len(results)>=limit:break
            try:results.append(check_predicate(parse_predicate(line)))
            except ValueError:continue
        return tuple(results)
