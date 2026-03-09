from junior_apogee_app.plugins import discover_plugins


def test_no_plugins(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    assert discover_plugins() == []
