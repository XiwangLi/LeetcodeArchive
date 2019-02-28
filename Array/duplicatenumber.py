class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # lo, hi= 1, len(nums)-1       
        # while lo < hi:
        #     mid = lo + (hi - lo)/2 
        #     cnt = 0
        #     for num in nums:
        #         if num <= mid: cnt+=1
        #     if cnt <= mid: lo=mid+1
        #     else: hi=mid
        # return lo
                
        
        
        
        slow, fast = 0, 0       
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast: break 
        print ()      
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]           
        return slow


test = Solution()
print (test.findDuplicate([1, 3, 4, 2, 2]))