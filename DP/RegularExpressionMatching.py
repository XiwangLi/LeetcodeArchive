#Regular Expression Matching
# T[i][j] =
# T[i-1][j-1]   if p[j-1] == '.' or s[i-1]==p[j-1]  Case 1
# T[i][j-1]     if  p[j-1] == '*' (p[j-2] show once) Case 2
# T[i][j-2]     if  p[j-1] == '*' (p[j-2] not show) Case 3
# T[i-1][j]     if  p[j-1] == '*' and s[i-1] == p[j-2] Case 4

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        DP = [[False] * (n + 1) for _ in range((m + 1))]
        DP[0][0] = True
        for i in range(2, len(DP[0])):
            if p[i - 1] == '*':
                DP[0][i] = DP[0][i - 2] 
            
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == '.' or s[i - 1] == p[j - 1]:   #case 1
                    DP[i][j] = DP[i - 1][j - 1]   #case 2
                elif p[j - 1] == '*':
                    DP[i][j] = DP[i][j -2] or DP[i][j - 1] or (DP[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))  #Case 3 and Case 4
                else:
                    DP[i][j] == False
        return DP[-1][-1]       
                    