"""
The Fibonacci Sequence is the series of numbers:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

The next number is found by adding up the two numbers before it.

The 2 is found by adding the two numbers before it (1+1)
The 3 is found by adding the two numbers before it (1+2),
And the 5 is (2+3),
and so on!
"""

import pytest


# standard way is O(2 nth power) time
# space complexity C2C: O(n) - we have one path in memory until call stack unwinds
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


@pytest.mark.parametrize("number, expected", [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
    (7, 13),
    (8, 21),
    (9, 34)
])
def test_fib(number, expected):
    assert (fib(number) == expected)


# fibonacci can also be done in a simple loop, without recursion
# it is asked much less but once I was startled by the request to do this method,
# after explaining both the recursion and memoization examples
def fib_loop(n):
    numbers = {}
    index = 0
    for index in range(n + 1):
        if index < 2:
            numbers[index] = index
        else:
            numbers[index] = numbers[index - 2] + numbers[index - 1]

    if index > 1:
        return numbers[index - 2] + numbers[index - 1]
    else:
        return index


@pytest.mark.parametrize("number, expected", [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
    (7, 13),
    (8, 21),
    (9, 34)
])
def test_fib_loop(number, expected):
    assert (fib_loop(number) == expected)


# uses memoization, with is O(n) time
# space complexity C2C: O(n), because we do have it in memory
# Video on memoization by Gayle Laakmann McDowell
# https://www.youtube.com/watch?v=P8Xa2BitN3I
def fib_memo(n, memo):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        if n not in memo:
            memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]


# Create memo data structure
memo = {}


@pytest.mark.parametrize("number, expected", [
    (0, 0),
    (9, 34),  # after this call, the memo cache should be populated and remaining values returned fast
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
    (7, 13),
    (8, 21),
])
def test_fib_memo(number, expected):
    assert (fib_memo(number, memo) == expected)


# this python decorator does a cache for you
# which effectively is memoization
from functools import lru_cache


@lru_cache(maxsize=1000)
def fib_lru(n):
    if type(n) != int:
        raise TypeError('n must be a positive int')
    if n < 0:
        raise ValueError('n must be a positive int')

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_lru(n - 1) + fib_lru(n - 2)


@pytest.mark.parametrize("number, expected", [
    (0, 0),
    (9, 34),  # after this call, the memo cache should be populated and remaining values returned fast
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
    (7, 13),
    (8, 21),
])
def test_fib_lru(number, expected):
    assert (fib_lru(number) == expected)
