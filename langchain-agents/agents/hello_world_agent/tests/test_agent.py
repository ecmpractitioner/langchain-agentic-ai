from agents.hello_world.agent import run


def test_run_returns_value():
    assert run() is None or isinstance(run(), str)
