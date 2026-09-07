import pytest
from src.calculator import add, divide


def test_add():
    assert add(1, 2) == 3


def test_divide_normal():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
