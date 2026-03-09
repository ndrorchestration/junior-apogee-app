from click.testing import CliRunner
from junior_apogee_app.cli import cli


def test_simulate_command():
    runner = CliRunner()
    result = runner.invoke(cli, ["simulate"])
    assert result.exit_code == 0
    assert "Simulation mode" in result.output
