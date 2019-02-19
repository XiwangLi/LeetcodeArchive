# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

# Example:

# Input: n = 4, k = 2
# Output:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(n, k, 1, [], res)
        return res
        
    def dfs(self, n, k, idx, path, res):
    	if len(path) == k:
    		res.append(path)
    		return
    	for i in range(idx, n+1):
    		self.dfs(n, k, i+1, path + [i], res)

test = Solution()
print(test.combine(4, 2))