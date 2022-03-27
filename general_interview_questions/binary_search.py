import pytest

class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1


@pytest.mark.parametrize('nums, target, expected', [
    ([-1,0,3,5,9,12], 9, 4),
    ([-1,0,3,5,9,12], 2, -1)
])
def test_search(nums, target, expected):
    sol = Solution()
    assert sol.search(nums, target) == expected