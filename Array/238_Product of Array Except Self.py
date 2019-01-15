# 238. Product of Array Except Self
# Medium

# Given an array nums of n integers where n > 1,  
#return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

# Example:

# Input:  [1,2,3,4]
# Output: [24,12,8,6]
# Note: Please solve it without division and in O(n).

# Follow up:
# Could you solve it with constant space complexity? 
#(The output array does not count as extra space for the purpose of space complexity analysis.)

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

       # product of left variables * product of right variables+

       	leftproduct = 1
       	res = []
       	for i in range(len(nums)):
       		res.append(leftproduct)
       		leftproduct *= nums[i]

       	rightproduct = 1
       	for i in range(len(nums) - 1, -1, -1):
       		res[i] *= rightproduct
       		rightproduct *= nums[i]
       	return res       

test = Solution()
nums = [1,2,3,4]
print (test.productExceptSelf(nums))
