# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.

# Example 1:

# Input: "()"
# Output: true
# Example 2:

# Input: "()[]{}"
# Output: true
# Example 3:

# Input: "(]"
# Output: false
# Example 4:

# Input: "([)]"
# Output: false
# Example 5:

# Input: "{[]}"
# Output: true

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        pair = {'(':')', '[':']', '{':'}'}
        if len(s) % 2: return False
        for string in s:
            if string in pair:
            	stack.append(string)
            else:
            	if not stack or pair[stack[-1]] != string:
            		return False
            	stack.pop()
        return not stack

test = Solution()
nums = '()[]{}'
print (test.isValid(nums))




