from datetime import datetime

from pydantic import BaseModel

from .recommendation import Recommendation


class Report(BaseModel):
    id: str

    summary: str

    technical_findings: list[str]

    recommendations: list[Recommendation]

    generated_at: datetime