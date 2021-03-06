# Maximum Subarray I
class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        # write your code here
        if not nums: return 0
        currSum, maxSum = -float('inf'), -float('inf') 
        for num in nums:
            currSum = max(currSum + num, num)
            maxSum = max(maxSum, currSum)
        return maxSum

# ............ Maximum Subarray II.......
class Solution:
    """
    @param: nums: A list of integers
    @return: An integer denotes the sum of max two non-overlapping subarrays
    """
    def maxTwoSubArrays(self, nums):
        # write your code here
        n = len(nums)
        left = [0] * n
        leftMax = [0] * n
        right = [0] * n
        rightMax= [0] * n
    
        left[0] = nums[0]
        leftMax[0] = nums[0]
    
        for i in range(1, n):
            left[i] = max(nums[i], left[i-1] + nums[i])
            leftMax[i] = max(left[i], leftMax[i-1])
    
        right[n - 1] = -float('inf')
        rightMax[n - 1] = -float('inf')
    
        for i in range(n-2, -1, -1):
            right[i] = max(right[i+1] + nums[i+1], nums[i+1])
            rightMax[i] = max(right[i], rightMax[i+1])
        print leftMax, rightMax    
        mx = -float('inf')
        for i in range(n - 1):
            mx = max(leftMax[i]+rightMax[i], mx)
        return mx
    
    # The n2 method is easy to think of
         if not nums: return 0
        left = [0] * len(nums)
        right = [0] * len(nums)
        for i in range(len(nums) - 1):
            left[i] = self.maxSubArray(nums[: i + 1])  #find the maxSubarry for from left
            right[i] = self.maxSubArray(nums[i + 1 : ])  #find the maxSubarry for from right
        maxSum =  -float('inf')
        for i in range(len(left) - 1):
            currsum = left[i] + right[i]
            maxSum = max(maxSum, currsum)
        return maxSum
    
    
    def maxSubArray(self, nums):
        if not nums: return 0
        cSum= gmax = -float('inf')
        for i in range(len(nums)):
            cSum = max(cSum + nums[i], nums[i])
            gmax = max(gmax, cSum)
        return gmax
