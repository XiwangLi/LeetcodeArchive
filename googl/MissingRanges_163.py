class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        res = []
        nums.append(upper + 1)
        nums.insert(0, lower - 1)
        for i in range(len(nums) - 1):
            left, right = nums[i], nums[i + 1]
            if right - left > 2:
                res.append(str(left + 1) + '->' + str(right - 1))
            elif right - left == 2:
                res.append(str(left + 1))
        return res

nums = [0, 1, 3, 50, 75]
lower = 0
upper = 99

model = Solution()
print model.findMissingRanges(nums, lower, upper)