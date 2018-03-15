class Solution:
    """
    @param nums: An integer array
    @return: nothing
    """
    def recoverRotatedSortedArray(self, nums):
        # write your code here
        pos = -1
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                pos = i
                break
        
        if pos == -1: return
        self.reverse(nums, 0, i)
        self.reverse(nums, pos + 1, len(nums) - 1)
        self.reverse(nums, 0, len(nums) - 1)
        
    
    def reverse(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        

model = Solution()    
nums = [1, 2, 3, 4, 5, 6]
model.recoverRotatedSortedArray(nums)
print nums
