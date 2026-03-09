from __future__ import annotations

from typing import Any, Dict

from .evaluation import LayerA, LayerB, LayerC


class Evaluator:
    """Convenience wrapper that runs the three evaluation layers on a task."""

    def __init__(self) -> None:
        self.layer_a = LayerA()
        self.layer_b = LayerB()
        self.layer_c = LayerC()

    def run(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """Evaluate a single task through all three layers."""
        result_a = self.layer_a.evaluate(task)
        result_b = self.layer_b.evaluate(task)
        result_c = self.layer_c.evaluate(task)
        return {"layer_a": result_a, "layer_b": result_b, "layer_c": result_c}
