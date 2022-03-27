import pytest

def plusOne(digits):
    real_number = 0
    for power in range(len(digits)):
        real_number += digits[len(digits) - (1 + power)] * (10**power)
    real_number += 1
    return [int(i) for i in str(real_number)]


def plusOne2(digits):
    digits_str = [str(i) for i in digits]
    num = int("".join(digits_str))
    return [int(i) for i in str(num + 1)]


@pytest.mark.parametrize("digits, expected_output", [
    ([1,2,3], [1,2,4]),
    ([4,3,2,1], [4,3,2,2]),
    ([1, 0, 0], [1, 0, 1]),
    ([9, 9], [1, 0, 0])
])
def test_plus_one(digits, expected_output):
    assert plusOne(digits) == expected_output


@pytest.mark.parametrize("digits, expected_output", [
    ([1,2,3], [1,2,4]),
    ([4,3,2,1], [4,3,2,2]),
    ([1, 0, 0], [1, 0, 1]),
    ([9, 9], [1, 0, 0])
])
def test_plus_one2(digits, expected_output):
    assert plusOne2(digits) == expected_output
