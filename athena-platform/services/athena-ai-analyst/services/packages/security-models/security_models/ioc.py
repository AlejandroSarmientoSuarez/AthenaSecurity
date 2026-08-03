from enum import Enum

from pydantic import BaseModel


class IOCType(str, Enum):
    IP = "ip"
    DOMAIN = "domain"
    URL = "url"
    HASH = "hash"
    EMAIL = "email"
    HOSTNAME = "hostname"


class IOC(BaseModel):
    type: IOCType

    value: str

    confidence: float

    reputation: str | None = None