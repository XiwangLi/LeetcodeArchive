class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        res, curr, sign, stack = 0, 0, 1, [1]
        for i in s + '+':

            if i.isdigit():
                curr = curr * 10 + int(i)
            elif i == '+' or i == '-':
                res += curr * sign * stack[-1]
                sign = 1 if i == '+' else -1
                curr = 0
            elif i == '(':
                stack.append(sign * stack[-1])
                sign = 1
            elif i == ')':
                res += curr * sign * stack[-1]
                stack.pop()
                curr = 0
            print i, sign, stack, res
        return res

model = Solution()
print model.calculate('3-(2+(9-4) + 1)')