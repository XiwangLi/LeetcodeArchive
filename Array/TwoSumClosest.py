<<<<<<< HEAD
class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        left, right = max(nums), sum(nums)
        while left <= right:
            mid = left + (right - left) / 2
            if self.validcut(nums, m, mid):
                right = mid - 1
            else:
                left = mid + 1
        return left
    
    def validcut(self, nums, m, maxsum):
        totalsum, count = 0, 1
        for i in range(len(nums)):
            if totalsum + nums[i] <= maxsum:
                totalsum += nums[i]
            else:
                count += 1
                totalsum = nums[i]
            if count > m:
                return False
        
        return True


model = Solution()
print model.splitArray([7,2,5,10,8], 2)
=======
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





     
>>>>>>> 939b0502f1c705121dae8d24aaecb61943ad3e7d
