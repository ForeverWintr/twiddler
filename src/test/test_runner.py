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
