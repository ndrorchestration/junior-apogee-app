from __future__ import annotations

import sys
from loguru import logger

from .settings import Settings


def configure_logging() -> None:
    """Configure loguru based on application settings."""
    settings = Settings()
    level = "DEBUG" if settings.environment == "development" else "INFO"
    logger.remove()
    logger.add(sys.stderr, level=level, backtrace=True, diagnose=True)
