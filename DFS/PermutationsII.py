# Permutation II 
# repeated values


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
		if nums is None:
            return []

        if len(nums) == 0:
            return [[]]
            
        res = []
        self.dfs_Perm(res, [], sorted(nums)) #we need to sort the list first, to put repeated values together
        return res
        
    def dfs_Perm(self, res, path, nums):
        if not nums: 
            res.append(path)
        else:
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:  # if repeated values, then continue: do not repeat, becasue it was taken at i -1
                    continue
                self.dfs_Perm(res, path + [nums[i]], nums[:i] + nums[i+1:])  
				                  # pick nums[i]     the remaining nums
# This mathed is very good, as it changed the nums to be nums[:i] + nums[i+1:], then we can have another method to avoid this.
# By add another list to record that this value has been taken/used or not

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = []
        used = [False] * len(nums)
        self.dfs(sorted(nums), [], used, res)
        return res
    
    def dfs(self, nums, temp, used, res):
        if len(temp) == len(nums):
            res.append(temp[:])  #shallow copy as we will modify "temp" later

        for i in xrange(len(nums)):
            if used[i]: 
                continue
            if i>0 and nums[i] == nums[i-1] and used[i - 1]: #nums[i-1] is the same as nums[i] and nums[i -1] has been used
                continue
            used[i] = True
            self.dfs(nums, temp + [nums[i]], used, res)
            used[i] = False