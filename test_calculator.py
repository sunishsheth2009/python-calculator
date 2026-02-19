import pytest

import calculator


def test_add():
    assert calculator.add(2, 3) == 5


def test_subtract():
    assert calculator.subtract(5, 2) == 3


def test_multiply():
    assert calculator.multiply(4, 3) == 12


def test_divide():
    assert calculator.divide(10, 2) == 5


def test_divide_by_zero_raises_value_error():
    with pytest.raises(ValueError, match="divide by zero"):
        calculator.divide(1, 0)
