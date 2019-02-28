class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        m, n = len(A), len(B)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        res = 0
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    res = max(res, dp[i][j])
        return res


A=[1,2,3,2,1]
B=[3,2,1,4,7]

test = Solution()
print(test.findLength(A, B))