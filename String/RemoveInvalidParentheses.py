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