import pytest

'''
On a 2 dimensional grid with R rows and C columns, we start at (r0, c0) facing east.

Here, the north-west corner of the grid is at the first row and column, and the south-east corner of the grid is at the last row and column.

Now, we walk in a clockwise spiral shape to visit every position in this grid. 

Whenever we would move outside the boundary of the grid, we continue our walk outside the grid (but may return to the grid boundary later.) 

Eventually, we reach all R * C spaces of the grid.

Return a list of coordinates representing the positions of the grid in the order they were visited.


Example 1:

Input: R = 1, C = 4, r0 = 0, c0 = 0
Output: [[0,0],[0,1],[0,2],[0,3]]

Example 2:

Input: R = 5, C = 6, r0 = 1, c0 = 4
Output: [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]

https://leetcode.com/problems/spiral-matrix-iii/discuss/

'''


def spiralMatrixIII(R, C, r0, c0):
    """
    :type R: int
    :type C: int
    :type r0: int
    :type c0: int
    :rtype: List[List[int]]
    """
    matrix = [[0 for x in range(C)] for y in range(R)]
    number_cells = R * C
    visited_cells = []
    pos_direction = True
    length_traversal = 0
    while len(visited_cells) < number_cells:
        matrix[r0][c0] = 1
        length_traversal += 1
        visited_cells.append([r0, c0])
        if pos_direction:
            if c0 + 1 < C:
                c0 += 1
            elif r0 + 1 < R:
                r0 += 1
                pos_direction = False
            else:
                # go down matrix to find first unvisited cell
                for r in range(r0, len(matrix)):
                    if matrix[r][c0] == 0:
                        r0 = r
                        break
                # not found we must search last row
                r0 = len(matrix) - 1
                for c in reversed(range(len(matrix[0]))):
                    if matrix[r0][c] == 0:
                        c0 = r
                        break
                pos_direction = False
        else:
            if c0 - 1 > 0:
                c0 -= 1
            elif r0 - 1 > 0:
                r0 -= 1
    print(visited_cells)
    return visited_cells


def spiralMatrixIII_2(R, C, r0, c0):
    """
    :type R: int
    :type C: int
    :type r0: int
    :type c0: int
    :rtype: List[List[int]]
    """

    def nxt(r, c):
        d = 1
        yield (r, c)
        while True:
            for i in range(d):
                c += 1
                yield (r, c)
            for i in range(d):
                r += 1
                yield (r, c)
            for i in range(d + 1):
                c -= 1
                yield (r, c)
            for i in range(d + 1):
                r -= 1
                yield (r, c)
            d += 2

    ret = []
    r, c = r0, c0
    for (r, c) in nxt(r0, c0):
        if 0 <= r < R and 0 <= c < C:
            ret.append([r, c])
        if len(ret) == R * C:
            break

    return ret


@pytest.mark.parametrize('R, C, r0, c0, expected', [
    (1, 4, 0, 0, [[0,0],[0,1],[0,2],[0,3]]),
    (5, 6, 1, 4, [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]])

])
def test_spiral_matrix(R, C, r0, c0, expected):
    assert spiralMatrixIII_2(R, C, r0, c0) == expected