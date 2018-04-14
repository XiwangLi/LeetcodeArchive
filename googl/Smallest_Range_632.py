import heapq
class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        pq = [(row[0], i, 0) for i, row in enumerate(nums)]
        heapq.heapify(pq)
        res = -1e9, 1e9
        right = max(row[0] for row in nums)
        
        while pq:
            print 'pq', pq
            left, i, j = heapq.heappop(pq)
            if right - left < res[1] - res[0]:
                res = left, right
            if j + 1 == len(nums[i]):
                return res
            leftnew = nums[i][j + 1]
            right = max(right, leftnew)
            heapq.heappush(pq, (leftnew, i, j + 1))

A = [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
model = Solution()
print model.smallestRange(A)