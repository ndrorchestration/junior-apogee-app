from src.junior_apogee.models import AgentConfig, AgentName, AgentRun
from src.junior_apogee.roles import (
    AgentRole,
    LEGACY_AGENT_ROLE,
    ROLE_CAPABILITIES,
    role_for_agent_name,
)


def test_workbench_roles_use_stable_functional_ids():
    values = [role.value for role in AgentRole]
    assert len(values) == len(set(values))
    assert all(value.startswith("workbench.role.") for value in values)
    assert set(AgentRole) == {
        AgentRole.EVALUATION_ORCHESTRATOR,
        AgentRole.RESEARCH_SYNTHESIS,
        AgentRole.MULTI_AGENT_COORDINATION,
        AgentRole.GOVERNANCE_COMPLIANCE_REVIEW,
        AgentRole.UNCERTAINTY_HUMAN_ESCALATION,
    }


def test_every_legacy_agent_name_resolves_to_exactly_one_role():
    assert set(LEGACY_AGENT_ROLE) == set(AgentName)
    assert len(set(LEGACY_AGENT_ROLE.values())) == len(AgentName)
    for legacy_name, role in LEGACY_AGENT_ROLE.items():
        assert role_for_agent_name(legacy_name) is role


def test_role_mapping_is_derived_from_workbench_behavior_not_dgaf_persona_names():
    assert role_for_agent_name(AgentName.APOGEE) is AgentRole.EVALUATION_ORCHESTRATOR
    assert role_for_agent_name(AgentName.PRODIGY) is AgentRole.RESEARCH_SYNTHESIS
    assert role_for_agent_name(AgentName.RECIPROCITY) is AgentRole.MULTI_AGENT_COORDINATION
    assert role_for_agent_name(AgentName.COLLEEN) is AgentRole.GOVERNANCE_COMPLIANCE_REVIEW
    assert role_for_agent_name(AgentName.DEMIJOULE) is AgentRole.UNCERTAINTY_HUMAN_ESCALATION


def test_each_role_has_explicit_repository_local_capabilities():
    assert set(ROLE_CAPABILITIES) == set(AgentRole)
    for role, capabilities in ROLE_CAPABILITIES.items():
        assert capabilities, f"role has no capabilities: {role.value}"
        assert all(capability.startswith("workbench.cap.") for capability in capabilities)


def test_legacy_models_expose_functional_role_without_breaking_legacy_input():
    config = AgentConfig(name=AgentName.PRODIGY, description="legacy-compatible")
    run = AgentRun(agent=AgentName.DEMIJOULE, task_id="t-role")

    assert config.name is AgentName.PRODIGY
    assert config.role is AgentRole.RESEARCH_SYNTHESIS
    assert run.agent is AgentName.DEMIJOULE
    assert run.role is AgentRole.UNCERTAINTY_HUMAN_ESCALATION


def test_legacy_identity_is_not_an_authority_transfer_channel():
    assert not hasattr(AgentRole, "SOVEREIGN")
    assert not hasattr(AgentRole, "AUTHORIZED")
    assert all("authority" not in capability for capabilities in ROLE_CAPABILITIES.values() for capability in capabilities)
