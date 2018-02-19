# # 5: Wildcard Matching
# isMatch("aa","a") → false
# isMatch("aa","aa") → true
# isMatch("aaa","aa") → false
# isMatch("aa", "*") → true
# isMatch("aa", "a*") → true
# isMatch("ab", "?*") → true
# isMatch("aab", "c*a*b") → false
# 
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).

# In[110]:

# this is a string with 2D DP problem 
# if * then do not need to match S and P, just need to check previous match dp[i-1][j] or dp[i][j-1]
# if ? need s[i-1] == p[j-1]
# The DP is (m +1 X n + 1). The base case DP[0][i]: the first i char of P isMatch the 0 char of S: So only if p[i-1] == '*' 
# The base case DP[j][0]: The 0 char of P isMatch the first j of S. So it is FALSE

def isMatch( s, p):
    m, n = len(s), len(p)
    dp = [[False]*(n+1) for _ in range (m+1)]
    dp[0][0] = True

    for i in range (1, n+1):
        if p[i-1] == '*':
            dp[0][i] = dp[0][i-1]  

    for i in range (1, m+1):
        for j in range (1, n+1):
            if p[j-1] == '*': 
                dp[i][j] = dp[i-1][j] or dp[i][j-1]  #'*' can matches any sequence of characters (including the empty sequence 
            else:
                dp[i][j] = dp[i-1][j-1] and (p[j-1] == '?' or s[i-1] == p[j-1])
    return dp[-1][-1]

isMatch('aa', '*')