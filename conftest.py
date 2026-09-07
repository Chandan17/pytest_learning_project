import os
import sys
# ensure project root is on sys.path so `src` package resolves when tests run
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest

def pytest_addoption(parser):
    parser.addoption("--runslow", action="store_true", help="run slow tests")


def pytest_collection_modifyitems(config, items):
    """Skip tests marked as slow unless --runslow is given."""
    if config.getoption("--runslow"):
        return
    skip_slow = pytest.mark.skip(reason="need --runslow option to run")
    for item in items:
        if "slow" in item.keywords:
            item.add_marker(skip_slow)


@pytest.fixture(scope="module")
def module_resource():
    print("\n[setup] module resource")
    return {"name": "module_resource"}


@pytest.fixture
def sample_data(request):
    # used with indirect parametrization
    return request.param if hasattr(request, "param") else 42


@pytest.fixture(autouse=True)
def auto_fixture():
    # runs for every test (demonstration)
    pass


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # run the rest of the hookchain
    outcome = yield
    rep = outcome.get_result()
    # when a test call fails, print a short message (visible with -s)
    if rep.when == "call" and rep.failed:
        print(f"\n=== Test {item.name} FAILED ===")
