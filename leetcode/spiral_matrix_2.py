
import pytest

'''
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
'''


def generateMatrix(n):
    """
    :type n: int
    :rtype: List[List[int]]
    """
    if n == 0:
        return []

    if n == 1:
        return [[1]]

    matrix = [[0 for x in range(n)] for y in range(n)]
    total_cells = n*n
    visited_cells = 0
    row = 0
    col = 0
    num_rows = n
    num_cols = n
    while visited_cells < total_cells:
        for c in range(col, num_cols):
            visited_cells += 1
            matrix[row][c] = visited_cells
        for r in range(row+1, num_rows):
            visited_cells += 1
            matrix[r][c] = visited_cells
        for c in reversed(range(col, c)):
            visited_cells += 1
            matrix[r][c] = visited_cells
        for r in reversed(range(row+1, r)):
            visited_cells += 1
            matrix[r][c] = visited_cells
        num_cols -= 1
        num_rows -= 1
        row += 1
        col += 1
    return matrix


def generateMatrix2(n):
    """
    :type n: int
    :rtype: List[List[int]]
    """
    output = [[0]*n for i in range(n)]
    current_num = 1
    for cube_index in range((n+1)//2):  # circle index
        for forward_col in range(cube_index,n-cube_index-1):
            output[cube_index][forward_col] = current_num
            current_num += 1
        for downward_row in range(cube_index,n-cube_index-1):
            output[downward_row][n-cube_index-1] = current_num
            current_num += 1
        for reverse_col in range(n-cube_index-1, cube_index, -1):
            output[n-cube_index-1][reverse_col] = current_num
            current_num += 1
        for upward_row in range(n-cube_index-1, cube_index, -1):
            output[upward_row][cube_index] = current_num
            current_num += 1
    if n%2 != 0:
        output[n//2][n//2] = current_num
    return output


@pytest.mark.parametrize('n, expected', [
    (1, [[1]]),
    (3, [[1, 2, 3], [8, 9, 4], [7, 6, 5]]),
    (4, [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]])
])
def test_gen_matrix(n, expected):
    assert generateMatrix(n) == expected