class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
# The basic idea is to separate the word into two part
#check the left part as a whole in wordDict (for loop i)
#and then check the right part (s[j:i] in wordDict)        
        M = [False] * (len(s) + 1)
        for i in xrange(len(s) + 1):
            if s[:i] in wordDict:
                M[i] = True
                continue
            for j in range(1, i):
                if M[j] and s[j:i] in wordDict:
                    M[i] = True
                    break
        return M[-1]
