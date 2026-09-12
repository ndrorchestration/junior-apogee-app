"""Role-keyed synthetic fixture policy for reports and demos.

These are synthetic/demo behaviors only. They are keyed by repository-local
functional roles and confer no DGAF authority, compliance, safety, or
certification.
"""

from __future__ import annotations

from typing import Dict, List

from .roles import AgentRole

ROLE_OUTPUT_TEMPLATES: Dict[AgentRole, str] = {
    AgentRole.EVALUATION_ORCHESTRATOR: (
        "Task completed step by step. Step 1: searched for data. "
        "Step 2: then analysed the results. Step 3: finally generated the report. "
        "Source: https://example.com | Timestamp: {ts} | Citation: [1] Smith 2024. "
        "Provenance: query_chain_id_abc123. Author: synthetic fixture. Version: 1.0."
    ),
    AgentRole.RESEARCH_SYNTHESIS: (
        "Research synthesis complete. According to the following synthetic sources: "
        "[1] Smith et al. (2024) confirmed the fixture hypothesis. "
        "[2] Jones and Lee (2025) corroborated the synthetic findings. "
        "Source: academic_db | Timestamp: {ts} | Citation: [1][2]. "
        "Claims are bounded to the available synthetic source material."
    ),
    AgentRole.MULTI_AGENT_COORDINATION: (
        "Multi-agent workflow coordinated. Tasks delegated to evaluation, research, "
        "and governance-review roles. Results aggregated and handoffs recorded. "
        "Source: orchestration_log | Timestamp: {ts} | Provenance: workflow_id_xyz"
    ),
    AgentRole.GOVERNANCE_COMPLIANCE_REVIEW: (
        "Project-local governance review complete for this synthetic fixture. "
        "OWASP-related checks and ethics/rights checks passed within the declared fixture scope. "
        "Source: governance_fixture | Timestamp: {ts} | Archival: record_id_456. "
        "Version: synthetic_audit_v2.1"
    ),
    AgentRole.UNCERTAINTY_HUMAN_ESCALATION: (
        "Uncertainty detected. Escalating to human review because confidence is below "
        "the synthetic decision threshold. Source: confidence_fixture | Timestamp: {ts} | "
        "Provenance: session_id_789"
    ),
}


def tool_calls_for_role(role: AgentRole) -> List[dict[str, object]]:
    """Return synthetic tool calls for a functional role."""

    if role in {
        AgentRole.EVALUATION_ORCHESTRATOR,
        AgentRole.RESEARCH_SYNTHESIS,
    }:
        return [
            {"tool_name": "web_search", "parameters": {"query": "evaluation test"}},
            {"tool_name": "data_analysis", "parameters": {"data": "sample_data"}},
        ]
    if role == AgentRole.GOVERNANCE_COMPLIANCE_REVIEW:
        return [
            {"tool_name": "owasp_scan", "parameters": {"target": "agent_output"}},
        ]
    return []


def archival_required_for_role(role: AgentRole) -> bool:
    """Return whether the synthetic task requires archival markers for this role."""

    return role in {
        AgentRole.EVALUATION_ORCHESTRATOR,
        AgentRole.GOVERNANCE_COMPLIANCE_REVIEW,
        AgentRole.UNCERTAINTY_HUMAN_ESCALATION,
    }


def expected_tools_for_role(role: AgentRole) -> List[str]:
    """Return expected synthetic tools for a functional role."""

    if role in {
        AgentRole.EVALUATION_ORCHESTRATOR,
        AgentRole.RESEARCH_SYNTHESIS,
    }:
        return ["web_search"]
    return []
