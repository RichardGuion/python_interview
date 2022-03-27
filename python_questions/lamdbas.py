import pytest

def list_squared_by_map(list1):
    # alternative to using list comprehension
    # [(x, x ** 2) for x in list1]
    return list(map(lambda x: x**2, list1))

def lambda_argument(func, x):
    return func(x)

def lamdba_multiplier(n):
  return lambda a : a * n


def test_list_squared_by_map():
    assert list_squared_by_map(range(10)) == [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

def test_lamda_argument():
    assert lambda_argument(lambda a : a + 10, 5) == 15

def test_lamdba_multiplier():
    mydoubler = lamdba_multiplier(2)
    mytripler = lamdba_multiplier(3)
    assert mydoubler(11) == 22
    assert mytripler(11) == 33



