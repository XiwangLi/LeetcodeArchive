# Paint house II

class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs or not costs[0]: return 0
        n, k = len(costs), len(costs[0])
        min1, min2 = -1, -1  #store the min and the second min
        for i in range(n):
            last1, last2 = min1, min2 #save the min from last house: updating this house
            min1, min2 = -1, -1
            for j in range(k):
                if j != last1:  #if this color is not the min color then use it
                    costs[i][j] += 0 if last1 < 0 else costs[i - 1][last1]
                else: #if this color is the min color then use second min color
                    costs[i][j] += 0 if last2 < 0 else costs[i - 1][last2]
                if min1 < 0 or costs[i][j] < costs[i][min1]:
                    min2 = min1
                    min1 = j
                elif min2 < 0 or costs[i][j] < costs[i][min2]:
                    min2 = j
        return costs[-1][min1]
