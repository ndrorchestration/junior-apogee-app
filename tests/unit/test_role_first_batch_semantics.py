import pytest

from src.junior_apogee.evaluation.engine import EvaluationEngine


def test_empty_batch_fails_closed_without_inventing_actor_identity():
    engine = EvaluationEngine()

    with pytest.raises(ValueError, match="empty batch has no actor provenance"):
        engine.evaluate_batch([], [])
