from pydantic import BaseModel


class AIResponse(BaseModel):

    summary: str

    reasoning: str

    confidence: float

    mitre: list[str]

    recommendations: list[str]