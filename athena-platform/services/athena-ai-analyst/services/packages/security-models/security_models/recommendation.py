from pydantic import BaseModel


class Recommendation(BaseModel):
    priority: str

    description: str

    requires_approval: bool = True