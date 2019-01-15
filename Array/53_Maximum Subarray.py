# Given an integer array nums, find the contiguous subarray 
# (containing at least one number) which has the largest sum and return its sum.

# Example:

# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        gmax = lmax = -float('inf')
        for num in nums:
        	lmax = max(num, lmax + num)
        	gmax = max(gmax, lmax)
        	#print (num, lmax, gmax)

        return gmax

test = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
print (test.maxSubArray(nums))



