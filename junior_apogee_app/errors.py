"""Custom exception hierarchy for the application."""

from __future__ import annotations


class AppError(Exception):
    """Base class for all application-specific errors."""


class ConfigurationError(AppError):
    """Raised when configuration validation fails."""


class EvaluationError(AppError):
    """Raised during evaluation of a task."""


class AgentError(AppError):
    """Problem raised by an agent implementation."""
