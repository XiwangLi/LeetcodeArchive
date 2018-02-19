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