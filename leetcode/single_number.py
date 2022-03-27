import pytest
from collections import defaultdict
from operator import itemgetter


# conventional using dictionary
def singleNumber(nums):
    print(f'nums =' + ', '.join(str(x) for x in nums))
    number_frequency = defaultdict(int)
    for num in nums:
        number_frequency[num] += 1
    for num,freq in sorted(number_frequency.items(), key=itemgetter(1)):
        if freq == 1:
            return num
    return None


# compact O(1) using XOR
def singleNumber2(nums):
    res = 0
    for num in nums:
        res ^= num
    if res in nums:
        return res
    else:
        return None


@pytest.mark.parametrize("number_list, expected", [
    ([2,2,1], 1),
    ([4,1,2,1,2], 4),
    ([1,1,2,2,3,3], None)
])
def test_single_number(number_list, expected):
    assert singleNumber(number_list) == expected


@pytest.mark.parametrize("number_list, expected", [
    ([2,2,1], 1),
    ([4,1,2,1,2], 4),
    ([1,1,2,2,3,3], None)
])
def test_single_number2(number_list, expected):
    assert singleNumber2(number_list) == expected
