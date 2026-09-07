import pytest

@pytest.mark.smoke
def test_testcases1():
    assert 1 == 1

test_data = {
    "test1": {"a": 10, "b": 5},
    "test2": {"a": 20, "b": 10},
    "test3": {"a": 35, "b": 25},
    "test4":{"a":200,"b":199}
}

@pytest.mark.parametrize("test_name, data", test_data.items())
@pytest.mark.regression
def test_greater_than(test_name, data):
    a = data["a"]
    b = data["b"]

    assert a > b
