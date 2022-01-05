from pathlib import Path
import sys

from twiddler import runner


def test_runner_run():
    sleep = runner.Argument(0.001, name="sleep")
    r = runner.Runner([sys.executable, "sample_cli.py"], Path("."), [sleep])

    r.launch()
    assert 0
