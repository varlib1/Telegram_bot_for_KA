from pydantic import BaseModel, Field
from typing import List


class ImpactedEntity(BaseModel, frozen=True):
    type: str = Field(compare=True, hash=True)
    name: str = Field(compare=True, hash=True)
    entity: str = Field(compare=True, hash=True)


class ProblemNotification(BaseModel, frozen=True):
    MZone: str = Field(default_factory=str, compare=True, hash=True)
    ImpactedEntities: List[ImpactedEntity] = Field(default_factory=str, compare=True, hash=True)
    PID: str = Field(default_factory=str, compare=True, hash=True)
    ProblemDetailsHTML: str = Field(default_factory=str, compare=True, hash=True)
    ProblemDetailsMarkdown: str = Field(default_factory=str, compare=True, hash=True)
    ProblemDetailsText: str = Field(default_factory=str, compare=True, hash=True)
    ProblemID: str = Field(default_factory=int, compare=True, hash=True)
    ProblemImpact: str = Field(default_factory=str, compare=True, hash=True)
    ProblemSeverity: str = Field(default_factory=str, compare=True, hash=True)
    ProblemTitle: str = Field(default_factory=str, compare=True, hash=True)
    ProblemURL: str = Field(default_factory=str, compare=True, hash=True)
    State: str = Field(default_factory=str, compare=True, hash=True)
    Tags: str = Field(default_factory=str, compare=True, hash=True)
    chat_id: str = Field(default_factory=str, compare=True, hash=True)
    STATE_RESOLVED: str = Field(default_factory=str, compare=True, hash=True)
    STATE_OPEN: str = Field(default_factory=str, compare=True, hash=True)
