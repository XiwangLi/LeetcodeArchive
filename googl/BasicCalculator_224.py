class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """

        res, curr, sign, stack = 0, 0, 1, [1]
        for i in s:

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
        res += sign * curr
        return res

    def calculateII(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        num, sign, stack = 0, '+', []
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            if (not s[i].isdigit() and not s[i].isspace()) or i == len(s)-1:
            	print 'test'
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop()*num)
                else: # '/'
                    temp = stack.pop()
                    if temp == 0:
                    	signloc = 0
                    elif temp > 0:
                    	signloc = 1
                    else: 
                    	signloc = -1
                    #sign = cmp (temp, 0)
                    stack.append(signloc * (abs(temp) / num))
                sign = s[i]
                print sign, stack
                num = 0
        return sum(stack)




model = Solution()
print model.calculate2('3+5 / 2')
