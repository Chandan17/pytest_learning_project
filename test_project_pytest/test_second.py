import pytest

@pytest.mark.regressionwwe
def test_secondtest():
    a =5
    b= 5
    assert a==b

@pytest.mark.smoke
def test_secondtest1():
    a = 4
    b = 4
    assert a == b