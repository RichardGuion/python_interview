import pytest

def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    found_numbers = []
    for index in reversed(range(0, len(nums))):
        if nums[index] in found_numbers:
            del nums[index]
            continue
        else:
            found_numbers.append(nums[index])

@pytest.mark.parametrize("test_list, expected_list", [
    ([1, 1, 2], [1, 2]),
    ([1, 2, 3, 3], [1, 2, 3]),
    ([1, 2, 3, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([1, 2, 3, 3, 4, 5, 5, 6], [1, 2, 3, 4, 5, 6]),
])
def test_duplicates(test_list, expected_list):
    old_list = test_list.copy()
    removeDuplicates(test_list)
    print(f'{old_list} after removal = {test_list}')
    assert test_list == expected_list


