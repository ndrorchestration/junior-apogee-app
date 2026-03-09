from __future__ import annotations

from typing import Any, Dict, List

from .agents import Agent
from .evaluator import Evaluator


class Orchestrator:
    """Simple orchestration engine that runs agents and evaluates their output."""

    def __init__(self, agents: List[Agent]) -> None:
        self.agents = agents
        self.evaluator = Evaluator()

    def execute(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """Run each agent in sequence and then evaluate the task.

        This implementation is intentionally simplistic; a real system would
        dispatch tasks asynchronously and handle failures.
        """
        results: Dict[str, Any] = {}
        for agent in self.agents:
            results[agent.name] = agent.run(task)
        evaluation = self.evaluator.run(task)
        return {"agent_results": results, "evaluation": evaluation}
