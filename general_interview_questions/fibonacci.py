"""
The Fibonacci Sequence is the series of numbers:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

The next number is found by adding up the two numbers before it.

The 2 is found by adding the two numbers before it (1+1)
The 3 is found by adding the two numbers before it (1+2),
And the 5 is (2+3),
and so on!
"""


# standard way is O(2 nth power) time
# space complexity C2C: O(n) - we have one path in memory until call stack unwinds
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


# Def fib_loop(n):
# Numbers = []
# For index in 0..n:
# If index == 0:
# Numbers[index] = 0
# Elif Index == 1:
# Numbers[index] = 1
# Else:
# Numbers[index] = Numbers[index-1] + Numbers[index-2]
# Return Numbers[index-2] + Numbers[index-1]


# uses memoization, with is O(n) time
# space complexity C2C: O(n), because we do have it memory
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


memo = {}
z = fib_memo(9, memo)
print(f'fib_memo(9) = {z}')
print(f'memo = {memo}')

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


z = fib_lru(9)
print(f'fib_lru(9) = {z}')
