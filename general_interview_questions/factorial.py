import math

import pytest

"""
The factorial function (symbol: !) says to multiply a series
of descending natural numbers. Examples:

4! = 4 × 3 × 2 × 1 = 24
7! = 7 × 6 × 5 × 4 × 3 × 2 × 1 = 5040
1! = 1
"""
def fact(n):
    if n == 0:
        return 1
    else:
        return (n * fact(n-1))


@pytest.mark.parametrize('n', [
    (0),
    (1),
    (4),
    (8),
    (22),
])
def test_factorial(n):
    assert fact(n) == math.factorial(n)


