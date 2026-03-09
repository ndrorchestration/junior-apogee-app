from junior_apogee_app.persistence import save_result
import os
from pathlib import Path


def test_save_result(tmp_path, monkeypatch):
    # override DB path to temporary location
    from junior_apogee_app import persistence

    monkeypatch.setattr(persistence, "DB_PATH", tmp_path / "results.db")
    save_result("task1", {"foo": "bar"})
    assert (tmp_path / "results.db").exists()
