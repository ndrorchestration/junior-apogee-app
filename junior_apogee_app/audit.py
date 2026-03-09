from __future__ import annotations

from typing import Any, Dict


def log_action(action: str, details: Dict[str, Any]) -> None:
    """Simple audit logger that could be extended to write to a file or service."""
    print(f"AUDIT: {action} -> {details}")
