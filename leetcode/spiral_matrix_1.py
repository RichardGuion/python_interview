import pytest

'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''

def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    # not all solutions covered by this case, I adapted it from spiral matrix 2 solution
    list_nums = []
    rows = len(matrix)
    if rows == 0:
        return list_nums
    cols = len(matrix[0])

    if cols == 1:
        for row_index in range(rows):
            list_nums.append(matrix[row_index][0])
    elif rows == 1:
        return matrix[0]
    else:
        traverse = rows
        if cols < rows:
            traverse = cols
        for circle_index in range(traverse-1):  # circle index
            for i1 in range(circle_index,cols-circle_index-1):
                list_nums.append(matrix[circle_index][i1])
            for i2 in range(circle_index,rows-circle_index-1):
                list_nums.append(matrix[i2][cols-circle_index-1])
            for i3 in range(circle_index, cols-circle_index-1):
                list_nums.append(matrix[rows-circle_index-1][cols-i3-1])
            for i4 in range(circle_index, rows-circle_index-1):
                list_nums.append(matrix[rows-i4-1][circle_index])
        if rows == cols and rows%2 != 0:
            list_nums.append(matrix[rows//2][rows//2])
    return list_nums


def spiralOrder2(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    if not matrix:
        return []
    rowBegin = 0
    rowEnd = len(matrix)
    colBegin = 0
    colEnd = len(matrix[0])
    res = []
    while rowBegin < rowEnd and colBegin < colEnd:
        if colBegin == colEnd:
            break
        for i in range(colBegin, colEnd):
            res.append(matrix[rowBegin][i])
        rowBegin += 1

        if rowBegin == rowEnd:
            break
        for i in range(rowBegin, rowEnd):
            res.append(matrix[i][colEnd - 1])
        colEnd -= 1

        if colEnd == colBegin:
            break
        for i in range(colEnd - 1, colBegin - 1, -1):
            res.append(matrix[rowEnd - 1][i])
        rowEnd -= 1

        if rowEnd == rowBegin:
            break
        for i in range(rowEnd - 1, rowBegin - 1, -1):
            res.append(matrix[i][colBegin])
        colBegin += 1

    return res


def get_index(rows, cols):
    rowBegin = 0
    rowEnd = rows
    colBegin = 0
    colEnd = cols
    while rowBegin < rowEnd and colBegin < colEnd:
        if colBegin == colEnd:
            break
        # forward thru the columns
        for col in range(colBegin, colEnd):
            yield col, rowBegin
        rowBegin += 1

        if rowBegin == rowEnd:
            break
        # forward thru the rows
        for row in range(rowBegin, rowEnd):
            yield colEnd - 1, row
        colEnd -= 1

        if colEnd == colBegin:
            break
        # backward thru the columns
        for col in range(colEnd - 1, colBegin - 1, -1):
            yield col, rowEnd - 1
        rowEnd -= 1

        if rowEnd == rowBegin:
            break
        # backward thru the rows
        for row in range(rowEnd - 1, rowBegin - 1, -1):
            yield colBegin, row
        colBegin += 1


def spiral_order_iterator(matrix):
    matrix_order = []
    if len(matrix) == 0:
        return matrix_order

    for x,y in get_index(len(matrix), len(matrix[0])):
        print(f'x is {x}, y is {y}')
        print(matrix[y][x])
        matrix_order.append(matrix[y][x])
    print(matrix_order)
    return matrix_order


@pytest.mark.parametrize('matrix, expected', [
    ([], []),
    ([[1]], [1]),
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1,2,3,6,9,8,7,4,5]),
    ([[1, 2, 3, 4], [5, 6, 7, 8], [9,10,11,12]], [1,2,3,4,8,12,11,10,9,5,6,7]),
    ([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
    ([[1,11],[2,12],[3,13],[4,14],[5,15],[6,16],[7,17],[8,18],[9,19],[10,20]], [1, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 10, 9, 8, 7, 6, 5, 4, 3, 2]),
    ([[1,2,3,4,5,6,7,8,9,10]], [1,2,3,4,5,6,7,8,9,10]),
    ([[1,2,3,4,5,6,7,8,9,10],[11,12,13,14,15,16,17,18,19,20]], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11]),
    ([[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]], [2,3,4,7,10,13,16,15,14,11,8,5,6,9,12])
])
def test_spiral(matrix, expected):
    assert spiralOrder2(matrix) == expected


@pytest.mark.parametrize('matrix, expected', [
    ([], []),
    ([[1]], [1]),
    ([[1, 2], [3, 4]], [1, 2, 4, 3]),
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5]),
    ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]),
    ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]),
    ([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
    ([[1, 11], [2, 12], [3, 13], [4, 14], [5, 15], [6, 16], [7, 17], [8, 18], [9, 19], [10, 20]],
     [1, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 10, 9, 8, 7, 6, 5, 4, 3, 2]),
    ([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
    ([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]],
     [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11]),
    ([[2, 3, 4], [5, 6, 7], [8, 9, 10], [11, 12, 13], [14, 15, 16]],
     [2, 3, 4, 7, 10, 13, 16, 15, 14, 11, 8, 5, 6, 9, 12])
])
def test_spiral_iterator(matrix, expected):
    assert spiral_order_iterator(matrix) == expected