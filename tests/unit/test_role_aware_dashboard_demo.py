from app import app, generate_demo_task_results
from src.junior_apogee.roles import AgentRole


def test_snapshot_payload_preserves_agent_and_exposes_role():
    client = app.test_client()
    response = client.get("/api/v1/snapshot")

    assert response.status_code == 200
    payload = response.get_json()
    assert payload["agent_summaries"]
    for row in payload["agent_summaries"]:
        assert row["agent"]
        assert row["role"] in {role.value for role in AgentRole}


def test_agent_catalog_exposes_functional_role_without_removing_name():
    client = app.test_client()
    response = client.get("/api/v1/agents")

    assert response.status_code == 200
    payload = response.get_json()
    assert payload
    for row in payload:
        assert row["name"]
        assert row["role"] in {role.value for role in AgentRole}


def test_demo_task_results_expose_role_and_keep_actor_identity():
    rows = generate_demo_task_results()
    assert rows
    for row in rows:
        assert row["agent"]
        assert row["role"] in {role.value for role in AgentRole}
