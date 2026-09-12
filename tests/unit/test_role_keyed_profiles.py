from src.junior_apogee.agents.profiles import (
    AGENT_BASELINES,
    ALL_AGENTS,
    ROLE_BASELINES,
    ROLE_PROFILES,
    get_agent,
    get_profile_for_role,
    list_agents,
    list_role_profiles,
)
from src.junior_apogee.models import AgentName
from src.junior_apogee.roles import AgentRole, role_for_agent_name


def test_role_profiles_are_complete_and_role_keyed():
    assert set(ROLE_PROFILES) == set(AgentRole)
    for role, profile in ROLE_PROFILES.items():
        assert profile.role is role


def test_legacy_agent_registry_is_a_compatibility_projection_of_role_profiles():
    assert set(ALL_AGENTS) == set(AgentName)
    for legacy_name, profile in ALL_AGENTS.items():
        role = role_for_agent_name(legacy_name)
        assert profile is ROLE_PROFILES[role]
        assert get_agent(legacy_name) is get_profile_for_role(role)


def test_role_and_legacy_listing_return_same_profile_objects_once_each():
    legacy_profiles = list_agents()
    role_profiles = list_role_profiles()

    assert len(legacy_profiles) == len(role_profiles) == len(AgentRole)
    assert {id(profile) for profile in legacy_profiles} == {
        id(profile) for profile in role_profiles
    }


def test_role_baselines_are_canonical_and_legacy_baselines_are_projection():
    assert set(ROLE_BASELINES) == set(AgentRole)
    assert set(AGENT_BASELINES) == set(AgentName)

    for legacy_name, baseline in AGENT_BASELINES.items():
        role = role_for_agent_name(legacy_name)
        assert baseline is ROLE_BASELINES[role]


def test_role_keying_does_not_change_profile_configuration():
    expected = {
        AgentRole.EVALUATION_ORCHESTRATOR: ("claude-3-5-sonnet", 0.0, 8192),
        AgentRole.RESEARCH_SYNTHESIS: ("claude-3-5-sonnet", 0.0, 8192),
        AgentRole.MULTI_AGENT_COORDINATION: ("claude-3-5-sonnet", 0.1, 4096),
        AgentRole.GOVERNANCE_COMPLIANCE_REVIEW: ("claude-3-5-sonnet", 0.0, 4096),
        AgentRole.UNCERTAINTY_HUMAN_ESCALATION: ("claude-3-5-sonnet", 0.0, 2048),
    }

    for role, (backend, temperature, max_tokens) in expected.items():
        profile = get_profile_for_role(role)
        assert (profile.model_backend, profile.temperature, profile.max_tokens) == (
            backend,
            temperature,
            max_tokens,
        )
