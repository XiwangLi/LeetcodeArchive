class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        res = []
        wordsdic = {word : i for i, word in enumerate(words)}
        for word, i in wordsdic.iteritems():
            for j in range(len(word) + 1):
                prefix = word[:j]
                surfix = word[j:]
                if self.isPalindrome(prefix):
                    reverse = surfix[::-1]
                    if reverse in wordsdic and reverse != word:
                        res.append((wordsdic[reverse], i))
                if j != len(word) and self.isPalindrome(surfix):
                    reverse = prefix[::-1]
                    if reverse in wordsdic and reverse != word:
                        res.append((i, wordsdic[reverse]))
        return res
               
    def isPalindrome(self, word):
        return word == word[::-1]
 
model = Solution()
print model.palindromePairs(["abcd", "dcba", "lls", "s", "sssll"])