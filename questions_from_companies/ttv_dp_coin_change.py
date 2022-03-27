import sys

import pytest

'''
https://www.hackerrank.com/challenges/ctci-coin-change/problem

Video on memoization by Gayle Laakmann McDowell
https://www.youtube.com/watch?v=P8Xa2BitN3I

Given a number of dollars and an array of denominations of coins, determine how many ways you can make change. 
For example, making change for n == 12 dollars from coin denominations coins == [1,2,5,10], there are 15 ways to make change:

1 1 1 1 1 1 1 1 1 1 1 	1 1 5 5			1 1 1 1 1 1 1 5
1 1 1 1 1 1 1 1 1 1 2	2 5 5
1 1 1 1 1 1 1 1 2 2	1 1 10
1 1 1 1 1 1 2 2 2	2 10
1 1 1 1 2 2 2 2		2 2 2 1 5
1 1 2 2 2 2 2       	2 2 1 1 1 5
2 2 2 2 2 2          	2 1 1 1 1 1 5
'''

# this seems to work well without recursion
def make_change(coins, n):
    print(f'make_change for {n}, coins = {coins}')
    results = [0 for _ in range(n + 1)]
    results[0] = 1
    for coin in coins:
        print(f'outer loop, coin is {coin}')
        print(f'range is: {range(coin, n + 1):}')
        for i in range(coin, n + 1):
            print(f'inner loop, i is {i}')
            print(f'results[{i}] += {results[i - coin]}')
            results[i] += results[i - coin]
            print(f'results[{i}] == {results[i]}')
            print(f'   ')
    print(f'results array for {coins} == {results}')
    return results[n]


@pytest.mark.parametrize("coins, n, expected_value", [
    ([1, 2, 3], 4, 4),
    ([2, 5, 3, 6], 10, 5)
])
def test_make_change(coins, n, expected_value):
    assert make_change(coins, n) == expected_value


