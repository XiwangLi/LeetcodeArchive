class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        res={}
        self.findWords(0, s, wordDict, res)
        print res
        return res[0]
    
    def findWords(self, start, s, wordDict, res):
        if start in res:
            return res[start]
        res[start] = []        
        for i in range(start, len(s)):
            word=s[start:i+1]            
            if word in wordDict:
                if i+1 == len(s):
                    res[start].append(word)
                else:
                    for x in self.findWords(i+1, s, wordDict, res):
                        res[start].append(word + ' ' + x)
        return res[start]
            
model = Solution()
print model.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])