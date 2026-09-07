Pytest learning project

This small project demonstrates pytest basics:
- simple assertions
- parametrized tests
- markers (smoke, slow)
- xfail and skip
- fixtures (function/module/autouse, indirect parametrization)
- pytest hooks (skip slow by default unless --runslow)

Setup

1. (Optional) create and activate a virtualenv
   python -m venv .venv
   source .venv/bin/activate  # macOS / Linux

2. Install dependencies:
   pip install -r requirements.txt

Running tests

- Run all tests:
    pytest

- Run only smoke tests:
    pytest -m smoke

- Run slow tests (they are skipped by default):
    pytest -m slow --runslow

- Run tests matching a keyword (e.g. add):
    pytest -k add

- See xfail/skip summary:
    pytest -rxs

- Run with -s to see hook/fixture print statements:
    pytest -s

Files

- src/calculator.py : simple functions to test
- test_project_pytest/ : test files and conftest with fixtures/hooks
- pytest.ini : registers markers and default pytest options
