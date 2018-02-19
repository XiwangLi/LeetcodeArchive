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
