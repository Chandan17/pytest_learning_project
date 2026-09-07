import pytest
from src.calculator import add

@pytest.mark.smoke
def test_smoke_quick():
    assert add(0, 0) == 0


@pytest.mark.slow
def test_slow_example():
    # short sleep to demonstrate slow marker; normally set longer
    import time
    time.sleep(0.1)
    assert add(1, 1) == 2


@pytest.mark.xfail(reason="demonstrate xfail", strict=False)
def test_expected_fail():
    assert add(1, 1) == 3


@pytest.mark.skip(reason="demo skip")
def test_skipped():
    assert False
