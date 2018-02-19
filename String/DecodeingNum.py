# # 3: Decode Ways
# 
# For example,
# Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).
# The number of ways decoding "12" is 2.

# This is a string + Dynamic problem question. As we need to count the decode ways from the frist str to ith str

def numDecodings(s):
    if not s or len(s) == 0 or s[0] == '0': return 0
    DP = [0] * (len(s) + 1)
    DP[0] = 1
    for i in range(1, len(s) + 1):
        if s[i - 1] != '0':
            DP[i] += DP[i - 1] #one char 
        if i > 1 and s[i - 2 : i] >= '10' and s[i - 2 : i] <= '26':
            DP[i] += DP[i - 2] #two char
    return DP[-1]

print numDecodings('12')