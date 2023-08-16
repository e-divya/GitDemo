import pytest


@pytest.mark.smoke
def test_compStr():
    a = "Hello"
    assert a == "Hai", "Test failed as string mismatched"

@pytest.mark.skip
def test_compIntcreditcard():
    a = 2
    b = 4
    assert a+b == 6,"Sum is not equal"