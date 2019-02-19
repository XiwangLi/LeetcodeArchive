class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(k, n, 1, [], res)
        return res

    def dfs(self, k, n, idx, path, res):
    	if len(path)== k and sum(path) == n:
    		res.append(path)
    	for i in range(idx, 10):
    		self.dfs(k, n, i + 1, path + [i], res)

test = Solution()
print(test.combinationSum3(3, 7))