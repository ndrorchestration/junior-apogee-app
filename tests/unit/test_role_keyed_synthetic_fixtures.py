from src.junior_apogee.models import AgentName
from src.junior_apogee.roles import AgentRole, role_for_agent_name
from src.junior_apogee.synthetic_fixtures import (
    ROLE_OUTPUT_TEMPLATES,
    archival_required_for_role,
    expected_tools_for_role,
    tool_calls_for_role,
)


def test_every_functional_role_has_a_synthetic_output_template():
    assert set(ROLE_OUTPUT_TEMPLATES) == set(AgentRole)


def test_synthetic_tool_behavior_is_keyed_by_role_not_actor_identity():
    assert tool_calls_for_role(AgentRole.EVALUATION_ORCHESTRATOR)
    assert tool_calls_for_role(AgentRole.RESEARCH_SYNTHESIS)
    assert tool_calls_for_role(AgentRole.GOVERNANCE_COMPLIANCE_REVIEW)
    assert tool_calls_for_role(AgentRole.MULTI_AGENT_COORDINATION) == []
    assert tool_calls_for_role(AgentRole.UNCERTAINTY_HUMAN_ESCALATION) == []


def test_synthetic_task_policy_is_role_keyed():
    assert archival_required_for_role(AgentRole.EVALUATION_ORCHESTRATOR)
    assert archival_required_for_role(AgentRole.GOVERNANCE_COMPLIANCE_REVIEW)
    assert archival_required_for_role(AgentRole.UNCERTAINTY_HUMAN_ESCALATION)
    assert not archival_required_for_role(AgentRole.RESEARCH_SYNTHESIS)
    assert expected_tools_for_role(AgentRole.EVALUATION_ORCHESTRATOR) == ["web_search"]
    assert expected_tools_for_role(AgentRole.RESEARCH_SYNTHESIS) == ["web_search"]


def test_legacy_actor_projection_preserves_fixture_semantics():
    for actor in AgentName:
        role = role_for_agent_name(actor)
        assert role in ROLE_OUTPUT_TEMPLATES
        assert isinstance(tool_calls_for_role(role), list)
