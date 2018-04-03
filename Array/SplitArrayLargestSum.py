class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        left, right = max(nums), sum(nums)
        while left + 1 < right:
            mid = left + (right - left) / 2
            if self.validcut(nums, m, mid):
                right = mid
            else:
                left = mid
        if self.validcut(nums, m, left):
            return left
        if self.validcut(nums, m, right):
            return right
        
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
