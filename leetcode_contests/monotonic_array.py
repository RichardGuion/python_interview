import pytest

'''
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

Return true if and only if the given array A is monotonic.

Example 1:

Input: [1,2,2,3]
Output: true
Example 2:

Input: [6,5,4,4]
Output: true
Example 3:

Input: [1,3,2]
Output: false
Example 4:

Input: [1,2,4,5]
Output: true
Example 5:

Input: [1,1,1]
Output: true
'''

class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        not_increasing = False
        for index in range(len(A)):
            if index > 0 and A[index] < A[index-1]:
                not_increasing = True
                break
        if not_increasing:
            A = list(reversed(A))
            for index in range(len(A)):
                if index > 0 and A[index] < A[index-1]:
                   return False
        return True

    def isMonotonic2(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        return A == sorted(A) or A == sorted(A, reverse=True)


@pytest.mark.parametrize('array, expected', [
    ([1,2,2,3], True),
    ([6,5,4,4], True),
    ([1,3,2], False),
    ([1,2,4,5], True),
    ([1,1,1], True),
    ([1,1,0], True)
])
def test_monotonic(array, expected):
    sol = Solution()
    assert sol.isMonotonic(array) == expected


@pytest.mark.parametrize('array, expected', [
    ([1,2,2,3], True),
    ([6,5,4,4], True),
    ([1,3,2], False),
    ([1,2,4,5], True),
    ([1,1,1], True),
    ([1,1,0], True)
])
def test_monotonic2(array, expected):
    sol = Solution()
    assert sol.isMonotonic2(array) == expected