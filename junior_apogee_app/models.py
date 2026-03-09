from __future__ import annotations

from pydantic import BaseModel
from typing import List, Dict, Any, Optional


class TaskFamily(BaseModel):
    name: str
    description: Optional[str]
    success_criteria: str


class Task(BaseModel):
    """A concrete task instance to be evaluated."""

    id: str
    family: str
    payload: Dict[str, Any]
    tenant: Optional[str]


class Result(BaseModel):
    """Result returned by an agent or evaluation layer."""

    task_id: str
    data: Dict[str, Any]
    success: bool


class Metric(BaseModel):
    name: str
    value: float
    tenant: Optional[str]


class MetricsConfig(BaseModel):
    task_success: float
    faithfulness: float
    tool_accuracy: float


class AgentConfig(BaseModel):
    name: str
    type: Optional[str]
    tenant: Optional[str]


class Config(BaseModel):
    task_families: Optional[List[TaskFamily]]
    metrics: Optional[MetricsConfig]
    agents: Optional[List[AgentConfig]]
    tenant: Optional[str]

