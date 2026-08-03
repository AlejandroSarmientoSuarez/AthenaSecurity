from pydantic import BaseModel


class Threat(BaseModel):
    name: str

    category: str

    mitre_technique: str

    confidence: float

    description: str