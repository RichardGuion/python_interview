import pytest

'''
  https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/674/
  
  Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
'''


def intersect(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    if len(nums1) < len(nums2):
        lookup_list = nums1
        compare_list = nums2
    else:
        lookup_list = nums2
        compare_list = nums1

    intersect_list = []
    for num in lookup_list:
        if num in compare_list:
            intersect_list.append(num)
            compare_list.remove(num)

    return intersect_list


@pytest.mark.parametrize("num_list1, num_list2, expected_output", [
    ([1, 2, 2, 1], [2, 2], [2, 2]),
    ([4, 9, 5], [9, 4, 9, 8, 4], [4, 9]),
    ([1,2], [1,1], [1]),
    ([], [1,2], [])
])
def test_intersect(num_list1, num_list2, expected_output):
    assert intersect(num_list1, num_list2) == expected_output

# What if elements of nums2 are stored on disk, and the memory is
# limited such that you cannot load all elements into the memory at
# once?
#
# If only nums2 cannot fit in memory, put all elements of nums1 into a HashMap, read chunks of array that fit into the memory, and record the intersections.
#
# If both nums1 and nums2 are so huge that neither fit into the memory, sort them individually (external sort),
# then read 2 elements from each array at a time in memory, record intersections.

# I think the goal of this question is to test whether the interview understands some of the data engineering techniques. From a data engineer's perspective, basically there are three ideas to solve the question:
#
# Store the two strings in distributed system(whether self designed or not), then using MapReduce technique to solve the problem;
#
# Processing the Strings by chunk, which fits the memory, then deal with each chunk of data at a time;
#
# Processing the Strings by streaming, then check.
# https://en.wikipedia.org/wiki/External_sorting#External_merge_sort
# http://faculty.simpson.edu/lydia.sinapova/www/cmsc250/LN250_Weiss/L17-ExternalSortEX2.htm
