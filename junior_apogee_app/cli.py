import click
import json

from .config_loader import load_config
from .benchmark import BenchmarkSuite
from .persistence import save_result
from .audit import log_action



@click.group()
def cli():
    """Junior Apogee App command‑line interface."""
    pass


@cli.command()
@click.argument("report", required=False, default="metrics")
def report(report: str):
    """Generate a report (stub)."""
    click.echo(f"Generating {report} report (stub).")


@cli.command()
def list_agents():
    """Print the names of registered agent classes."""
    from .agents import list_agents as _list

    names = _list()
    if names:
        click.echo("Available agents:")
        for n in names:
            click.echo(f" - {n}")
    else:
        click.echo("(no agents registered)")


@cli.command()
@click.option("--task", type=str, default="{}", help="JSON-encoded task to run")
def run(task: str):
    """Execute a simple evaluation run against a dummy task."""
    from .orchestrator import Orchestrator

    try:
        task_obj = json.loads(task)
    except json.JSONDecodeError:
        click.echo("Invalid JSON for --task", err=True)
        return

    orch = Orchestrator([])
    res = orch.execute(task_obj)
    # record and audit
    save_result(task_obj.get("id", ""), res)
    log_action("run", {"task": task_obj})
    click.echo(f"Result: {res}")


@cli.command()
def simulate():
    """Run the benchmarking simulation suite (stub)."""
    bs = BenchmarkSuite()
    click.echo("Simulation mode: no tasks ingested yet")

