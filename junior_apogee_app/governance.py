from __future__ import annotations

from typing import Callable, Dict, List, Any

_checks: List[Callable[[Dict[str, Any]], bool]] = []


def register_check(func: Callable[[Dict[str, Any]], bool]) -> Callable[[Dict[str, Any]], bool]:
    """Decorator to register a governance check function."""
    _checks.append(func)
    return func


def run_checks(result: Dict[str, Any]) -> Dict[str, bool]:
    """Execute all registered governance checks against a result.

    Returns a mapping from check name to boolean pass/fail.
    """
    return {func.__name__: func(result) for func in _checks}


# example check
@register_check
def no_hallucination(result: Dict[str, Any]) -> bool:
    # placeholder: real check would inspect text for hallucinations
    return True
