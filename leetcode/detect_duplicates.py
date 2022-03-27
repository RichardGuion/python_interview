import pytest

'''
https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/578/

Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
'''


def containsDuplicate(nums):
    return len(set(nums)) != len(nums)


def containsDuplicate2(nums):
    found_numbers = []
    for index in range(0, len(nums)):
        if nums[index] in found_numbers:
            return True
        else:
            found_numbers.append(nums[index])
    return False


def containsDuplicate3(nums):
    found = {}
    for num in nums:
        if num in found:
            return True
        else:
            found[num] = 1
    return False


@pytest.mark.parametrize("num_list, expected", [
    ([1,2,3,1], True),
    ([1,2,3,4], False),
    ([1,1,1,3,3,4,3,2,4,2], True)
])
def test_duplicates(num_list, expected):
    assert containsDuplicate(num_list) == expected


@pytest.mark.parametrize("num_list, expected", [
    ([1,2,3,1], True),
    ([1,2,3,4], False),
    ([1,1,1,3,3,4,3,2,4,2], True)
])
def test_duplicates2(num_list, expected):
    assert containsDuplicate2(num_list) == expected


@pytest.mark.parametrize("num_list, expected", [
    ([1,2,3,1], True),
    ([1,2,3,4], False),
    ([1,1,1,3,3,4,3,2,4,2], True)
])
def test_duplicates3(num_list, expected):
    assert containsDuplicate3(num_list) == expected
