from datetime import datetime

from pydantic import BaseModel


class Evidence(BaseModel):
    type: str

    source: str

    value: str

    relevance: float

    timestamp: datetime