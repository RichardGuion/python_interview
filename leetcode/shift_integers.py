import pytest

def rotate(nums, k):
    print(f'before shift nums = ' + ', '.join(str(x) for x in nums))
    for index in range(0, k):
        last_num = nums[len(nums) - 1]
        del nums[len(nums) - 1]
        nums.insert(0, last_num)
    print(f'after shift nums = ' + ', '.join(str(x) for x in nums))
    return nums

def rotate(nums, k):
    nums[:k], nums[k:] = nums[len(nums)-k:], nums[:len(nums)-k]

@pytest.mark.parametrize("num_list, k, expected_num_list", [
    ([1,2,3,4,5,6,7], 3, [5,6,7,1,2,3,4])
])
def test_rotate(num_list, k, expected_num_list):
    rotate(num_list, k)
    assert num_list == expected_num_list
