"""Unit tests for calculator arithmetic functions."""

import pytest

from app.operations import add, divide, multiply, subtract


@pytest.mark.parametrize(
    "function,a,b,expected",
    [
        (add, 2, 3, 5),
        (add, -2, 3, 1),
        (subtract, 8, 3, 5),
        (subtract, 3, 8, -5),
        (multiply, 4, 3, 12),
        (multiply, -4, 3, -12),
        (divide, 10, 2, 5),
        (divide, 7, 2, 3.5),
    ],
)
def test_arithmetic_functions(function, a, b, expected):
    assert function(a, b) == pytest.approx(expected)


def test_divide_by_zero_raises_value_error():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)
        