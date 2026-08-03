from enum import Enum

from pydantic import BaseModel


class SeverityLevel(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class RiskAssessment(BaseModel):
    severity: SeverityLevel

    confidence: float

    impact: float

    likelihood: float