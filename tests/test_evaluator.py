from junior_apogee_app.evaluator import Evaluator


def test_evaluator_structure():
    ev = Evaluator()
    res = ev.run({"foo": "bar"})
    assert "layer_a" in res
    assert "layer_b" in res
    assert "layer_c" in res
