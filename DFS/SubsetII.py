# Subset II 
# repeated values: We choose the first repeated value and jump over the other repeated values

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums: return []
        results = []
        self.dfs(sorted(nums), 0, [], results)
        return results
        
        
    def dfs(self, nums, idx, path, results):
        results.append(path)
        for i in range(idx, len(nums)):
            if i > 0 and nums[i] == nums[i - 1] and i != idx: # This is only differece from subset I.
                continue
            self.dfs(nums, i + 1, path + [nums[i]], results)