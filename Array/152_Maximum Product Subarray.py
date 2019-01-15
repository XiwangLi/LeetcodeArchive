# Given an integer array nums, find the contiguous subarray within an array 
# (containing at least one number) which has the largest product.

# Example 1:

# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.

# Example 2:

# Input: [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        gmax = lmax = lmin = nums[0]
        for num in nums[1:]:
        	lmax_last = lmax
        	lmax = max(num, lmax * num, lmin * num)
        	lmin = min(num, lmin * num, lmax_last * num)
        	gmax = max(gmax, lmax)
        	print (num, lmax, lmin, gmax)
        return gmax

test = Solution()
nums = [-4,-3,-2]
print (test.maxProduct(nums))