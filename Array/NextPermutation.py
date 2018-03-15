class Solution:
    """
    @param nums: An array of integers
    @return: nothing
    """
# I have to say, I cannot find the solution myself. I found the ideas from other people
# The logic is find traverse backward to find out index i where nums[i] < nums[i  + 1]
# then find the first index j (from backward), where nums[j] > nums[i]
# then reverse nums[i : j]
    def nextPermutation(self, nums):
        # write your code here
        left = len(nums) - 2
        while left >= 0:
            if nums[left] < nums[left + 1]:
                break
            left -= 1
        if left >= 0:
            right = left + 1
            while right < len(nums) and nums[right] > nums[left]:
                right += 1
            nums[left], nums[right - 1] = nums[right - 1], nums[left]
            nums[left + 1 :] = reversed(nums[left + 1 :])
        else:
            return nums.reverse()

test = Solution()
nums = [1, 2, 7, 4, 3, 1]
test.nextPermutation(nums)
print nums