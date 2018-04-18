class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        import heapq
        events = sorted([(L, -H, R) for L, R, H in buildings] + [(R, 0, None) for _, R, _ in buildings])
        res, hqHR = [[0, 0]], [(0, float('inf'))] # hqHR (negH, R)
        
        for x, negH, R in events:
            while x >= hqHR[0][1]:
                heapq.heappop(hqHR)
            
            if negH:
                heapq.heappush(hqHR, (negH, R))
            if res[-1][1] + hqHR[0][0]:
                res += [x, -hqHR[0][0]],
        return res[1:]



model = Solution()

print model.getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]])