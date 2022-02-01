from pathlib import Path
import sys
import asyncio

import pytest

from twiddler import runner


@pytest.mark.asyncio
async def test_runner_run():
    sleep = runner.Argument(0.001, name="sleep")
    r = runner.Runner([sys.executable, "sample_cli.py"], Path("."), [sleep])

    p = await r.launch()
    assert 0
