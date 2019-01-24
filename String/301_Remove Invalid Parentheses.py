class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        visit, queue, res = set([]), [s], []
        valid = False
        while queue:
            print (queue)
            string = queue.pop(0)
            if self.validPare(string):
                res.append(string)
                valid = True
            elif not valid:
                for i in range(len(string)):
                    if string[i] == '(' or string[i] == ')':
                        temp = string[:i] + string[i + 1 :]
                        if temp not in visit:
                            visit.add(temp)
                            queue.append(temp)
        return res
        
            
        
    def validPare(self, strings):
        count = 0
        for str in strings:
            if str == '(':
                count += 1
            elif str == ')':
                if count == 0:
                    return False
                count -= 1
        return count == 0
        
test = Solution()
nums = '(a)())()'
print (test.removeInvalidParentheses(nums))