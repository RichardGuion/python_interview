import pytest

'''
  Problem: given a left / right range of numbers, find the find numbers in this range
  and return a list of odd numbers back to the caller
'''

def oddNumbers(l, r):
    odd = []
    for i in range(l, r+1):
        if i % 2 != 0:
            odd.append(i)
    return odd


@pytest.mark.parametrize("l, r, expected", [
    (2, 5, [3, 5]),
    (3, 9, [3, 5, 7, 9]),
    (2, 2, []),
    [1, 1, [1]]
])
def test_odd(l, r, expected):
    assert oddNumbers(l,r) == expected
