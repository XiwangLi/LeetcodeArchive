# Permutations

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
		
        if not nums: return []
        results = []
        self.DFSpermute(nums, 0, results)
        return results
        
    def DFSpermute(self, nums, idx, results):
        if idx == len(nums):
            results.append(nums[:])
            return
        
        for i in range(idx, len(nums)):
            nums[idx], nums[i] = nums[i], nums[idx]  #picking each element to position idx
            self.DFSpermute(nums, idx + 1, results)
            nums[idx], nums[i] = nums[i], nums[idx]  #return to the orignal "nums" for other permutation