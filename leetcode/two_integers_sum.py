import pytest

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for current_index in range(len(nums)-1):
        for second_index in range(len(nums)):
            if current_index == second_index:
                continue
            if nums[current_index] + nums[second_index] == target:
                return [current_index, second_index]


def twoSum2(nums, target):
    dic = {}
    for i in range(len(nums)):
        key = nums[i]
        complement = target - key
        if complement in dic.keys():
            return [dic[complement], i]
        dic[key] = i


@pytest.mark.parametrize("num_list, target, expected_output", [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([1, 11, 15, 7, 2], 9, [3, 4])
])
def test_two_sum(num_list, target, expected_output):
    assert twoSum(num_list, target) == expected_output


@pytest.mark.parametrize("num_list, target, expected_output", [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([1, 11, 15, 7, 2], 9, [3, 4])
])
def test_two_sum2(num_list, target, expected_output):
    assert twoSum2(num_list, target) == expected_output
