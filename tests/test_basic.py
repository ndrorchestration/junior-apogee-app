from junior_apogee_app.agents import Agent


class DummyAgent(Agent):
    def run(self, task):
        return {"result": "ok"}


def test_dummy_agent():
    agent = DummyAgent("dummy")
    res = agent.run({})
    assert res == {"result": "ok"}
