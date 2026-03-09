from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Type


class Agent(ABC):
    """Base class for all agents participating in the evaluation."""

    name: str

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def run(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """Execute a task and return result."""
        pass


# simple registry to keep track of available agent classes
_agent_registry: List[Type[Agent]] = []


def register_agent(cls: Type[Agent]) -> Type[Agent]:
    """Class decorator registering an Agent implementation.

    Usage::

        @register_agent
        class MyAgent(Agent):
            ...
    """
    _agent_registry.append(cls)
    return cls


def list_agents() -> List[str]:
    """Return the names of all registered agent types."""
    return [cls.__name__ for cls in _agent_registry]

