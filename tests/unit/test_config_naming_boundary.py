"""Regression tests for the current-facing naming boundary."""

from junior_apogee.config import _normalize_legacy_labels


def test_legacy_display_label_normalizes_recursively() -> None:
    legacy = {
        "agent": "Apogee",
        "name": "Apogee Task Completion",
        "tags": ["apogee", "evaluation"],
        "nested": {"owner": "Apogee"},
    }

    normalized = _normalize_legacy_labels(legacy)

    assert normalized == {
        "agent": "Evaluation Orchestrator",
        "name": "Evaluation Orchestrator Task Completion",
        "tags": ["evaluation-orchestrator", "evaluation"],
        "nested": {"owner": "Evaluation Orchestrator"},
    }


def test_current_labels_pass_through_unchanged() -> None:
    current = {
        "agent": "Evaluation Orchestrator",
        "tags": ["evaluation-orchestrator", "reasoning"],
    }

    assert _normalize_legacy_labels(current) == current
