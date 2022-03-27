import pytest

def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    for index in reversed(range(len(nums))):
        if nums[index] == 0:
            del nums[index]
            nums.append(0)


def moveZeroes2(nums):
    num_zeroes = nums.count(0)
    if num_zeroes != len(nums):
        for i in range(num_zeroes):
            zero_index = nums.index(0)
            if zero_index != (len(nums) - 1):
                del nums[zero_index]
                nums.append(0)


def moveZeroes3(nums):
    place = 0  # records the position of "0"
    for x in nums:
        if x != 0:
            nums[place] = x  # One operation total.
            place += 1
    for index in range(place, len(nums)):
        if nums[index] != 0:  # At most one operation per step.
            nums[index] = 0


@pytest.mark.parametrize("num_list, expected_output", [
    ([0,1,0,3,12], [1,3,12,0,0]),
    ([1,2,0,4,0], [1,2,4,0,0]),
    ([0,0], [0,0]),
    ([], [])
])
def test_move_zeroes(num_list, expected_output):
    moveZeroes(num_list)
    assert num_list == expected_output


@pytest.mark.parametrize("num_list, expected_output", [
    ([0,1,0,3,12], [1,3,12,0,0]),
    ([1,2,0,4,0], [1,2,4,0,0]),
    ([0,0], [0,0]),
    ([], [])
])
def test_move_zeroes2(num_list, expected_output):
    moveZeroes2(num_list)
    assert num_list == expected_output


@pytest.mark.parametrize("num_list, expected_output", [
    ([0,1,0,3,12], [1,3,12,0,0]),
    ([1,2,0,4,0], [1,2,4,0,0]),
    ([0,0], [0,0]),
    ([], [])
])
def test_move_zeroes3(num_list, expected_output):
    moveZeroes3(num_list)
    assert num_list == expected_output
