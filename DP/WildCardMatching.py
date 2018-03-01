#WildCard Matching
# T[i][j] = 
# T[i - 1][j - i] if s[i - 1] == p[j - 1] or p[j - 1] =='?' Case 1
# T[i - 1][j] or T[i][j - 1] if p[j - 1] =='*'  Case 2

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        DP = [[False] * (n + 1) for _ in range(m + 1)]
        DP[0][0] = True
        
        for i in range(1, n + 1):
            if p[i - 1] == '*':
                DP[0][i] = DP[0][i - 1]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    DP[i][j] = DP[i][j - 1] or DP[i - 1][j]  # Case 1
                else:
                    DP[i][j] = DP[i -1][j - 1] and (p[j - 1] == '?' or s[i - 1] == p[j - 1])  # Case 2
        return DP[-1][-1] 
        
        