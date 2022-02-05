from pathlib import Path
import sys
import asyncio

import pytest

from twiddler import runner


@pytest.mark.asyncio
async def test_runner_run():
    sleep = runner.Argument(0.001, name="sleep")
    r = runner.Runner([sys.executable, "sample_cli.py", "asdf"], path=Path("."), arguments=[sleep])

    p = await r.launch()
    r = await p.wait()
    assert r == 0

    assert 0


def test_runner_command_line():
    sleep = runner.Argument(0.001, name="sleep")
    r = runner.Runner(["python", "sample_cli.py", "asdf"], path=Path("."), arguments=[sleep])

    assert r.command_line() == "python sample_cli.py asdf --sleep 0.001"


def test_arg_tick_count():
    assert runner.Argument(0, name="", min=-5, max=5).tick_count == 11
