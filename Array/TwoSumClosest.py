class Solution(object):
    def twoSumCloset(self, nums, target):
        """
        :type nums: List[int]
        :rtype: int
        Given an array nums of n integers, 
        find two integers in nums such that the sum is closest to a given number, target.
        """
        if not nums or len(nums) < 2:
            return -1
        if len(nums) == 2:
            return target - nums[0] - nums[1]
        nums.sort()
        mindiff = float('inf')
        left, right = 0, len(nums) - 1
        while left < right:
            sums = nums[left] + nums[right]
            diff = abs(target - sums)
            if diff == 0:
                return 0
            if diff < mindiff:
                mindiff = diff
            if sums > target:
                right -= 1
            else:
                left += 1
        return mindiff
model = Solution()
print model.twoSumCloset([-1, 2, 1, -4], 4)





     
