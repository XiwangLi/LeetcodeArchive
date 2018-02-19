# Subset I
# no repeated values

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums: return []
        results = []
        self.dfs(nums, 0, [], results)
        return results
        
        
    def dfs(self, nums, idx, path, results):
        results.append(path)
        for i in range(idx, len(nums)):
            self.dfs(nums, i + 1, path + [nums[i]], results)  #pick value at each poistion or not