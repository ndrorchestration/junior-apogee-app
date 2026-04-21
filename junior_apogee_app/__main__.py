"""Allow `python -m junior_apogee_app` to invoke the CLI."""
from __future__ import annotations

from junior_apogee_app.cli import cli

if __name__ == "__main__":  # pragma: no cover
    cli()
