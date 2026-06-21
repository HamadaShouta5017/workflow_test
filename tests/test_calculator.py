import pytest

from src.calculator import add, divide, multiply, subtract


def test_add():
    assert add(2, 3) == 5
    assert add(-2, 3) == 1


def test_subtract():
    assert subtract(10, 4) == 6
    assert subtract(3, 7) == -4


def test_multiply():
    assert multiply(4, 5) == 20
    assert multiply(-3, 4) == -12


def test_divide():
    assert divide(10, 2) == 5
    assert divide(7, 2) == 3.5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)