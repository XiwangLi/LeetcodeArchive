class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Input: [1, 2, 2, 3, 1]
        Output: 2
        """
        import collections
        res = len(nums)
        first, last = {}, {}
        dic = collections.Counter(nums) #{1:2, 2:2,3:1}
        degree = max(dic.values())

        for i, val in enumerate(nums):
            if val not in first:
                first[val] = i
            last[val] = i

        for val in dic:
            if dic[val] == degree:
                res = min(res, last[val] - first[val] + 1)
        return res

model = Solution()
print model.findShortestSubArray([1, 2, 2, 3, 1])



