from __future__ import annotations

import sqlite3
from pathlib import Path
from typing import Any, Dict

DB_PATH = Path(__file__).parent.parent / "data" / "results.db"


def _ensure_db() -> None:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        """CREATE TABLE IF NOT EXISTS results (
             task_id TEXT PRIMARY KEY,
             data TEXT
         )"""
    )
    conn.commit()
    conn.close()


def save_result(task_id: str, data: Dict[str, Any]) -> None:
    _ensure_db()
    conn = sqlite3.connect(DB_PATH)
    conn.execute("INSERT OR REPLACE INTO results (task_id, data) VALUES (?, ?)",
                 (task_id, str(data)))
    conn.commit()
    conn.close()
