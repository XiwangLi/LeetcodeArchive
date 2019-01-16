# Given an array of integers and an integer k, you need to find the total number of continuous subarrays 
# whose sum equals to k.

# Example 1:
# Input:nums = [1,1,1], k = 2
# Output: 2
# Note:
# The length of the array is in range [1, 20,000].
# The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        subsums = {0:1}
        count, currsum = 0, 0
        for num in nums:
        	currsum += num
        	count += subsums.get(currsum - k, 0)
        	subsums[currsum] = subsums.get(currsum, 0) + 1
        return count

        # count = 0
        # for i in range (len(nums)):
        # 	subsum = 0
        # 	for j in range(i, len(nums)):
        # 		subsum += nums[j]
        # 		if subsum == k:
        # 			count += 1
        # return count

test = Solution()
nums = [1,1,1]
print (test.subarraySum(nums, 2))

