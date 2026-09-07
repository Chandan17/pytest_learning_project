import pytest
from src.calculator import add, multiply

@pytest.mark.parametrize("a,b,expected", [(1,2,3),(2,3,5),(0,5,5)], ids=["1+2","2+3","0+5"])
def test_add_param(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize("a,b,expected", [
    pytest.param(2, 3, 6, id="2*3"),
    pytest.param(0, 5, 0, id="0*5"),
    pytest.param(-1, 3, -3, id="-1*3"),
])
def test_multiply_param(a, b, expected):
    assert multiply(a, b) == expected


# indirect parametrization: sample_data fixture in conftest will receive the param
@pytest.mark.parametrize("sample_data,expected", [ (10,10), (20,20) ], indirect=["sample_data"])
def test_indirect_fixture(sample_data, expected):
    assert sample_data == expected
