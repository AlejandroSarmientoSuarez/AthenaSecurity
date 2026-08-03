from enum import Enum

from pydantic import BaseModel

from .evidence import Evidence
from .ioc import IOC
from .recommendation import Recommendation
from .risk import RiskAssessment
from .threat import Threat


class InvestigationStatus(str, Enum):
    CREATED = "created"
    ANALYZING = "analyzing"
    REVIEW_REQUIRED = "review_required"
    COMPLETED = "completed"


class Investigation(BaseModel):
    id: str

    alert_id: str

    status: InvestigationStatus

    hypothesis: str

    iocs: list[IOC]

    threats: list[Threat]

    evidence: list[Evidence]

    risk: RiskAssessment

    recommendations: list[Recommendation]