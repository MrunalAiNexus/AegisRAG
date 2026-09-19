from dataclasses import dataclass, asdict
from typing import Any

@dataclass
class QueryResult:
    configuration: str
    answer: str
    risk_level: str
    security_action: str
    sources: list[str]
    security_analysis: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
