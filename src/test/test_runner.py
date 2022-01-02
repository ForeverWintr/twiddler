from twiddler import runner


def test_runner_run():
    sleep = runner.Argument(0.001, name="sleep")
    r = runner.Runner("")
    assert 0
