# NextPermutation
# This is not a DFS problem, but related with Permutation, so I put it here
# The method is hard to think of but the code is easy. 
#The key is to find out the index, i, where nums[i+1] > nums[i] and find the last index, j where nums[j] > nums[i]
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums: return []
        i = len(nums) - 2
        while i >= 0:
            if nums[i] < nums[i + 1]:
                break
            i -= 1
        if i >= 0:
            j = i + 1
            while j <= len(nums) - 1 and nums[j] > nums[i]:
                j += 1
            nums[i], nums[j - 1] = nums[j - 1], nums[i]
            nums[i + 1 : ] = sorted(nums[i + 1 : ])        
        else:
            return nums.reverse()
        
