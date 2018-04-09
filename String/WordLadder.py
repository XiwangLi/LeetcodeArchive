<<<<<<< HEAD
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        import string
        wordDict = set(wordList)
        if endWord not in wordDict:
            return 0
        s1, s2 = {beginWord}, {endWord}
        step = 0
        while len(s1) and len(s2):
            step += 1
            tempwords = set()
            for word in s1:
                newWords = [word[:i] + c + word[i + 1:] for c in string.ascii_lowercase for i in range(len(word))]
                for newWord in newWords:
                    if newWord in s2:
                        return step + 1
                    if newWord in wordDict:
                        wordDict.remove(newWord)
                        tempwords.add(newWord)
                    elif newWord not in wordDict:
                        continue
            s1 = tempwords
        return 0

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

model = Solution()
=======
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        import string
        wordDict = set(wordList)
        if endWord not in wordDict:
            return 0
        s1, s2 = {beginWord}, {endWord}
        step = 0
        while len(s1) and len(s2):
            step += 1
            tempwords = set()
            for word in s1:
                newWords = [word[:i] + c + word[i + 1:] for c in string.ascii_lowercase for i in range(len(word))]
                for newWord in newWords:
                    if newWord in s2:
                        return step + 1
                    if newWord in wordDict:
                        wordDict.remove(newWord)
                        tempwords.add(newWord)
                    elif newWord not in wordDict:
                        continue
            s1 = tempwords
        return 0

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

model = Solution()
>>>>>>> 939b0502f1c705121dae8d24aaecb61943ad3e7d
print model.ladderLength(beginWord, endWord, wordList)