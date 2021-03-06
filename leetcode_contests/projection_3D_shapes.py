import pytest

'''
On a N * N grid, we place some 1 * 1 * 1 cubes that are axis-aligned with the x, y, and z axes.

Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).

Now we view the projection of these cubes onto the xy, yz, and zx planes.

A projection is like a shadow, that maps our 3 dimensional figure to a 2 dimensional plane. 

Here, we are viewing the "shadow" when looking at the cubes from the top, the front, and the side.

Return the total area of all three projections.

 

Example 1:

Input: [[2]]
Output: 5
Example 2:

Input: [[1,2],[3,4]]
Output: 17
Explanation: 
Here are the three projections ("shadows") of the shape made with each axis-aligned plane.

Example 3:

Input: [[1,0],[0,2]]
Output: 8
Example 4:

Input: [[1,1,1],[1,0,1],[1,1,1]]
Output: 14
Example 5:

Input: [[2,2,2],[2,1,2],[2,2,2]]
Output: 21

Many people were confused by this problem.
ok i found this that made it clear:

[[2]] means on top of grid cell (0, 0), there is a block with size 2.
[[1,2],[3,4]] means on top of grid cell (0, 0), there is a block with size 1.
on top of grid cell (0, 1), there is a block with size 2.
on top of grid cell (1, 0), there is a block with size 3.
on top of grid cell (1, 1), there is a block with size 4.

in example 2, you can see it clearly. ( i dont think its too clear from the example tbh...)

'''

class Solution:
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        xy,xz = 0,0
        yz = [0]*len(grid)
        for i in grid:
            xy += sum(1 for j in i if j)
            xz += max(i)
            yz = [max(j,k) for j,k in zip(i,yz)]
        return xy + xz + sum(yz)


    def projectionArea2(self, grid):
        return (sum(map(max, grid)) + sum(map(max, zip(*grid))) + sum(v > 0 for row in grid for v in row))


@pytest.mark.parametrize('grid, expected', [
    ([[2]], 5),
    ([[1,2],[3,4]], 17)
])
def test_projection(grid, expected):
    solution = Solution()
    assert solution.projectionArea2(grid) == expected