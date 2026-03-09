from __future__ import annotations

from pydantic import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment variables or an env file."""

    api_key: str = ""
    agent_endpoint: str = ""
    environment: str = "development"  # development, staging, production

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
