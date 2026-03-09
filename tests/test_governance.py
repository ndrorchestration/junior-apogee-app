from junior_apogee_app.governance import run_checks, register_check


def test_run_checks_empty():
    res = run_checks({})
    assert isinstance(res, dict)


# register a temporary check for testing
@register_check
def _always_pass(_):
    return True


def test_run_checks_with_registered():
    res = run_checks({})
    assert "_always_pass" in res
    assert res["_always_pass"] is True
