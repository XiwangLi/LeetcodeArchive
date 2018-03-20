class Solution(object):
    def countCornerRectangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid: return 0
        m, n = len(grid), len(grid[0])
        res = 0
        for i in range(m):
            for j in range(i + 1, m):
                cnt = 0
                for k in range(n):
                    if grid[i][k] == 1 and grid[j][k] == 1:
                        cnt += 1
                res += cnt * (cnt - 1) / 2
        return res
        
# count the total '1's at the same col, at row i and j
# the toal rect at row i and j are then cnt * (cnt - 1) / 2

grid = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
model = Solution()
print model.countCornerRectangles(grid)

grid = [[1, 0, 0, 1, 0],
 [0, 0, 1, 0, 1],
 [0, 0, 0, 1, 0],
 [1, 0, 1, 0, 1]]
model = Solution()
print model.countCornerRectangles(grid)