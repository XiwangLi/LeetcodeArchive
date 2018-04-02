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
