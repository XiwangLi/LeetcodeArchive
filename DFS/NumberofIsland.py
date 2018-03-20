class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
# the key idea is to expand the island from land (i, j) from four directions
# and count new island when there is a break  
        if not grid: return 0
        m, n = len(grid), len(grid[0])
        res = 0
        for i in range(m):
        	for j in range(n):
        		if grid[i][i] == '1':
        			self.island(grid, i, j)
        			res += 1
        return res




    def island(self, gird, x, y):
    	if x < 0 or x > len(grid) or y < 0 or y > len(grid[0]) or grid[x][y] != '1':
    		return
    	grid[x][y] = -1
    	self.island(grid, x - 1, y)
    	self.island(grid, x + 1, y)
    	self.island(grid, x, y - 1)
    	self.island(grid, x, y + 1)

grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
model = Solution()
print model.numIslands(grid)