
# coding: utf-8

## 1: Implement strStr()  Leetcode 28
# The first question is StrStr. It is the first problem in almost all the books of pactice material
# The brute force way of solve this problem is very easy and the time-complexity is O(m*n). 
# Everybody will say, the brute force O(m*n) method is not good. We want better one. People recommended KMP. 
# I also tried KMP,but it is so hard to follow. So here I will try another algorithem called Robin-Karp. 
# The whole idea is to scan over the string and adding the new one/deleting the first one at the same time

def strstrBF(haystack, needle):
    m, n = len(haystack), len(needle)
    for i in range(m -n + 1):
        if haystack[i: i + n] == needle:
            return i
    return -1

def RobinKarp(haystack, needle):
    base = 26
    # calculate the hash for haystack (the first n-lenght substring) and needle 
    hash_h = reduce(lambda h, c: h * base + ord(c), haystack[: len(needle)], 0)
    hash_n = reduce(lambda h, c: h * base + ord(c), needle, 0)
    power = max(base ** (len(needle) - 1), 0) # in case len(needle) is 0, how many time that ord(c) mutiplied by base
    for i in range(len(needle),  len(haystack)):  #then scan the whole string ahead
        if hash_h == hash_n: 
            return i - len(needle)
        hash_h -= power * ord(haystack[i - len(needle)])        # substract the first chara
        hash_h = hash_h * base + ord(haystack[i])
    if hash_h == hash_n: 
        return len(haystack) - len(needle)    # check the last substring
    return -1

print strstrBF('haystack', 'yst')
print RobinKarp('haystack', 'yst')


## 2: Reverse Words in a String II
# The key idea of solving this problem is to "reverse the string TWICE"
# Given s = "the sky is blue",
# reverse onceL eht yks si eulb ---> find the space and reverse the word
# reverse twice: blue is sky the --> reverse the whole string

def reverseWords(s):
    s.split()
    idx = 0       
    for i in range (len(s)):
        if s[i] == ' ':
            s[idx : i] = reversed(s[idx : i])
            idx = i + 1
    s[idx :] = reversed(s[idx : ])
    s.reverse()


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


# # 4: String to Integer (atoi)
# this problem is not hard, but there are some corner cases. 
# 1: with sign or not
# 2: number larger/smaller the sysMAX, sysMIN
# 3 non digital str
def myAtoi(st):
    ls = list(st.strip())
    if len(st) == 0: return 0
    sign = -1 if ls[0] == '-' else 1
    if ls[0] == '-' or ls[0] == '+':
        ls = ls[1 :]
    ans, i = 0, 0
    while i < len(ls) and ls[i].isdigit():
        ans = ans * 10 + int(ls[i])
        i += 1    
    return min(2147483647, ans*sign) if ans*sign > 0 else max(-2147483648, ans*sign)


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


# # 6: Remove Invalid Parentheses
# "()())()" -> ["()()()", "(())()"] 
# 
# "(a)())()" -> ["(a)()()", "(a())()"]
# 
# ")(" -> [""]
# This problem is a follow up question of "valid parentheses"
# The idea is to romove each parentheses and then check ""valid" or not, if valid, save it to result list.
# One thing to pay attention: cannot save duplicate combination in the result list

def removeInvalidParentheses(s):
    visited, res, queue = set([]), [], [s]
    valid = False
    while queue:
        
        string = queue.pop(0)
        if validParentheses(string):
            res.append(string)           
            valid = True
        elif not valid:  
        #cannot use else. we only want to remove one char, So once it is valid, do not remove par
            for i in range(len(string)):
                if string[i] == '(' or string[i] == ')':
                    temp = string[:i] + string[i + 1 :]
                    if temp not in visited:
                        visited.add(temp)
                        queue.append(temp)
    return res

def validParentheses(s):
    count = 0
    for c in s:
        if c == '(': count += 1
        elif c == ')':
            if count == 0: 
                return False
            count -= 1
    return count == 0

removeInvalidParentheses("()())()")


## 7: Longest Substring Without Repeating Characters
# Given "abcabcbb", the answer is "abc", which the length is 3.
# This type of long substring, sublist, sub... can use two-pointer methods
# use a fast pointer to count each char as save it to a hashtable
# While Val[fast].count > 1, use slow point to remove the val[fast]

def lengthOfLongestSubstring(s):
    slow, fast = 0, 0
    hashmap = {}
    maxlen = 0
    while fast < len(s):
        if s[fast] in hashmap:
            hashmap[s[fast]] = hashmap.get(s[fast], 0) + 1
        else:
            hashmap[s[fast]] = 1
        while  hashmap.get(s[fast], 0)  > 1:
            hashmap[s[slow]]= hashmap.get(s[slow], 0)- 1                   
            slow += 1
        maxlen = max(maxlen, fast - slow + 1)
        fast +=1
    return maxlen

lengthOfLongestSubstring('abcabcbb')


## 8: Longest Substring with At Most Two Distinct Characters
# For example, Given s = “eceba”,
# T is "ece" which its length is 3.

# Different to P7, this problem requires the lenth of the hashmap <= 2
# When the count of one char <= 0, we need remove this char from hashmap

def lengthOfLongestSubstringTwoDistinct(s):
    slow, fast = 0, 0
    hashmap = {}
    maxlen = 0
    while fast < len(s):
        if s[fast] in hashmap:
            hashmap[s[fast]] = hashmap.get(s[fast], 0) + 1
        else:
            hashmap[s[fast]] = 1
        while len(hashmap) > 2:
            hashmap[s[slow]]= hashmap.get(s[slow], 0) - 1                   
            if hashmap.get(s[slow], 0) <= 0:
                del hashmap[s[slow]]
            slow += 1
        maxlen = max(maxlen, fast - slow + 1)
        fast += 1
    return maxlen


lengthOfLongestSubstringTwoDistinct('eceba')


## 9: Letter Combinations of a Phone Number
# 
# Input:Digit string "23"
# 
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
#This is a string + DFS problem  
# This types of combination or permutation can be solved using DFS
def letterCombinations(digits):  
    if not digits:
        return []
    res = []
    dic = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
    dfs(dic, digits,0, '', res)
    return res

def dfs(dic, digits, digidx, path, res):
    if len(path) == len(digits):
        res.append(path)
    for i in range(digidx, len(digits)):
        for c in dic[digits[i]]:
            dfs(dic, digits, i+1, path+c, res)
    
letterCombinations('23')        


## 10: Generate Parentheses

# This is also a DFS problem
# binary tree adding ( or adding )

def generateParenthesis(n):
    res=[]
    ParenDFS(n, 0, 0, '', res)
    return res

def ParenDFS(n, idxL, idxR, sol, res):
    if idxL == n and idxR == n:
        res.append(sol)        
    if idxL < n:
        ParenDFS(n, idxL + 1, idxR, sol + '(', res)
    if idxR < idxL:
        ParenDFS(n, idxL, idxR + 1, sol + ')', res) 

generateParenthesis(4)

