# Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

# Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

# Example 1:
# Input: [1, 2, 2, 3, 1]
# Output: 2
# Explanation: 
# The input array has a degree of 2 because both elements 1 and 2 appear twice.
# Of the subarrays that have the same degree:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# The shortest length is 2. So return 2.


# Example 2:
# Input: [1,2,2,3,1,4,2]
# Output: 6
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import collections
        dic = collections.Counter(nums) #{1:2, 2:2, 3:1}
        first, last = {}, {}
        degree = max(dic.values()) #2
        res = len(nums)

        for i, val in enumerate(nums):
        	if val not in first:
        		first[val] = i #{1:0, 2:1, 3:3}
        	last[val] = i #{1:4, 2:2, 3:3}

        for item in dic:
        	if dic[item] == degree:
        		res = min(res, last[item] - first[item] + 1)
        return res

test = Solution()
nums = [1,2,2,3,1,4,2]
print (test.findShortestSubArray(nums))




