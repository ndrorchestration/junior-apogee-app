from __future__ import annotations

from .agents import Agent, register_agent


@register_agent
class ApogeeAgent(Agent):
    def run(self, task):
        # simplistic stand-in logic
        return {"result": "apogee processed", "task": task}


@register_agent
class ProdigyAgent(Agent):
    def run(self, task):
        return {"result": "prodigy processed", "task": task}
