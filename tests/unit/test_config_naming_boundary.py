"""Regression tests for the current-facing naming boundary."""

from junior_apogee.config import (
    _normalize_legacy_labels,
    get_task_families_config,
)
from junior_apogee.roles import AgentRole


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


def test_task_family_config_exposes_canonical_functional_role() -> None:
    config = get_task_families_config()
    families = config["task_families"]

    assert families
    valid_roles = {role.value for role in AgentRole}
    for family in families:
        assert family["role"] in valid_roles
        # The actor field remains only as a compatibility/lineage input.
        assert family["agent"]
