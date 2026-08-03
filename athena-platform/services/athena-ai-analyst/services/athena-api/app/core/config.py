from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application configuration."""

    app_name: str = "Athena AI Analyst"

    app_version: str = "0.1.0"

    environment: str = Field(default="development")

    debug: bool = True

    api_prefix: str = "/api/v1"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    """Return cached application settings."""
    return Settings()


settings = get_settings()