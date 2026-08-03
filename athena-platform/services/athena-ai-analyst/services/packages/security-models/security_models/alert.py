from datetime import datetime
from enum import Enum

from pydantic import BaseModel


class AlertStatus(str, Enum):
    NEW = "new"
    ANALYZING = "analyzing"
    COMPLETED = "completed"


class Severity(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class Alert(BaseModel):
    id: str

    source: str

    event_type: str

    timestamp: datetime

    severity: Severity

    description: str | None = None

    raw_event: dict

    status: AlertStatus = AlertStatus.NEW