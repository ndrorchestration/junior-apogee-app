"""Functional role identities for the AI Evaluation Workbench.

These IDs describe repository-local behavior. They do not inherit DGAF authority
from historical persona names and they do not establish authorization, safety,
compliance, or certification.
"""

from __future__ import annotations

from enum import Enum
from typing import Dict, FrozenSet

from .models import AgentName


class AgentRole(str, Enum):
    """Stable workbench-local functional role identifiers."""

    EVALUATION_ORCHESTRATOR = "workbench.role.evaluation-orchestrator"
    RESEARCH_SYNTHESIS = "workbench.role.research-synthesis"
    MULTI_AGENT_COORDINATION = "workbench.role.multi-agent-coordination"
    GOVERNANCE_COMPLIANCE_REVIEW = "workbench.role.governance-compliance-review"
    UNCERTAINTY_HUMAN_ESCALATION = "workbench.role.uncertainty-human-escalation"


LEGACY_AGENT_ROLE: Dict[AgentName, AgentRole] = {
    AgentName.APOGEE: AgentRole.EVALUATION_ORCHESTRATOR,
    AgentName.PRODIGY: AgentRole.RESEARCH_SYNTHESIS,
    AgentName.RECIPROCITY: AgentRole.MULTI_AGENT_COORDINATION,
    AgentName.COLLEEN: AgentRole.GOVERNANCE_COMPLIANCE_REVIEW,
    AgentName.DEMIJOULE: AgentRole.UNCERTAINTY_HUMAN_ESCALATION,
}


ROLE_CAPABILITIES: Dict[AgentRole, FrozenSet[str]] = {
    AgentRole.EVALUATION_ORCHESTRATOR: frozenset(
        {
            "workbench.cap.evaluation.orchestrate",
            "workbench.cap.task.route",
            "workbench.cap.result.aggregate",
        }
    ),
    AgentRole.RESEARCH_SYNTHESIS: frozenset(
        {
            "workbench.cap.research.synthesize",
            "workbench.cap.evidence.summarize",
        }
    ),
    AgentRole.MULTI_AGENT_COORDINATION: frozenset(
        {
            "workbench.cap.agent.coordinate",
            "workbench.cap.handoff.route",
        }
    ),
    AgentRole.GOVERNANCE_COMPLIANCE_REVIEW: frozenset(
        {
            "workbench.cap.governance.review",
            "workbench.cap.compliance.check",
            "workbench.cap.notification.prepare",
        }
    ),
    AgentRole.UNCERTAINTY_HUMAN_ESCALATION: frozenset(
        {
            "workbench.cap.uncertainty.detect",
            "workbench.cap.human-review.escalate",
        }
    ),
}


def role_for_agent_name(name: AgentName) -> AgentRole:
    """Translate a compatibility identity to its functional workbench role."""

    return LEGACY_AGENT_ROLE[name]
