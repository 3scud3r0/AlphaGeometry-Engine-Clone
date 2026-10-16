"""Global deadline/expansion budgeting used across search workers."""
from dataclasses import dataclass
import time

class BudgetExpired(TimeoutError):pass

@dataclass
class Budget:
    seconds: float = 5.0
    expansions: int = 1000
    def __post_init__(self):
        if self.seconds<=0 or self.expansions<1:raise ValueError("positive budget required")
        self.deadline=time.monotonic()+self.seconds
        self.used=0
    def consume(self,cost=1):
        if self.used+cost>self.expansions or time.monotonic()>self.deadline:
            raise BudgetExpired("global search budget exhausted")
        self.used+=cost
