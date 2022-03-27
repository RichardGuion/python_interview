import pytest

def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    # this fails for negative numbers, -321 becomes 123-
    rev = str(x)[::-1]
    return int(rev)


def reverse1(x):
    rev = str(x)[::-1]
    if x < 0:
        rev = rev.replace('-', '')
        rev_num = int(rev) * -1
    else:
        rev_num = int(rev)
    if rev_num < -2 ** 31 or rev_num > (2 ** 31) - 1:
        return 0
    return rev_num


def reverse2(x):
    rev_num = 0
    rev_str = str(x)[::-1]
    # delete the trailing - if it exists
    if x < 0:
        rev_str = rev_str.replace('-', '')
    for index in range(len(rev_str)):
        rev_num += int(rev_str[len(rev_str) - (index+1)]) * (10**index)
    if x < 0:
        rev_num *= -1
    if rev_num < -2**31 or rev_num > (2**31)-1:
        return 0
    return rev_num


def reverse_mod(x):
    result = 0
    is_neg = (x < 0)
    if is_neg:
        x *= -1
    while x != 0:
        last_num = x % 10
        result = (result * 10) + last_num
        x = x // 10
    rev_num = (result * -1) if is_neg else result
    if rev_num < -2**31 or rev_num > (2**31)-1:
        return 0
    return rev_num


@pytest.mark.parametrize("given_int, expected_int", [
    (123, 321),
    (-321, -123),
    (1534236469, 0)
])
def test_reverse1(given_int, expected_int):
    assert reverse1(given_int) == expected_int


@pytest.mark.parametrize("given_int, expected_int", [
    (123, 321),
    (-321, -123),
    (1534236469, 0)
])
def test_reverse2(given_int, expected_int):
    assert reverse2(given_int) == expected_int


@pytest.mark.parametrize("given_int, expected_int", [
    (123, 321),
    (-321, -123),
    (1534236469, 0)
])
def test_reverse_mod(given_int, expected_int):
    assert reverse_mod(given_int) == expected_int
