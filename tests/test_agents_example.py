from junior_apogee_app.agents import list_agents


def test_example_agents_registered():
    names = list_agents()
    assert "ApogeeAgent" in names
    assert "ProdigyAgent" in names
