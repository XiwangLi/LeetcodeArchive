<<<<<<< HEAD
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





     
=======
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        sub = [nums[0]]
        
        for val in nums:
            if val <= sub[0]:
                sub[0] = val
            elif val > sub[-1]:
                sub += val,
            else:
                bc_idx = self.bc(sub, val, 0, len(sub))
                sub[bc_idx] = min(val, sub[bc_idx])
        return len(sub)
    
    def bc(self, sub, val, left, right):         
        while left + 1 < right:
            mid = left + (right - left) / 2
            if sub[mid] < val:
                left = mid
            else:
                right = mid
        return right
model = Solution()
print model.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])
>>>>>>> 939b0502f1c705121dae8d24aaecb61943ad3e7d
