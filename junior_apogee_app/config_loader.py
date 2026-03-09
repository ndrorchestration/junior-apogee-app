import yaml
from pathlib import Path
from typing import Any, Dict, Union

from .models import Config


def load_yaml(path: Path) -> Dict[str, Any]:
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def load_config(name: str, config_dir: Path = Path(__file__).parent.parent / "config") -> Union[Dict[str, Any], Config]:
    """Read a YAML config file by name.

    By default returns a raw dictionary; if you pass ``validate=True`` it will
    return a :class:`~junior_apogee_app.models.Config` instance.
    """
    path = config_dir / f"{name}.yaml"
    data = load_yaml(path)
    return data


def load_full_config(config_dir: Path = Path(__file__).parent.parent / "config") -> Config:
    """Load and validate all top‑level config files into a single object."""
    # Merge pieces; incomplete simplistic version
    cf = Config(
        task_families=load_yaml(config_dir / "task_families.yaml").get("task_families"),
        metrics=load_yaml(config_dir / "metrics.yaml"),
        agents=load_yaml(config_dir / "agents.yaml").get("agents"),
    )
    return cf
