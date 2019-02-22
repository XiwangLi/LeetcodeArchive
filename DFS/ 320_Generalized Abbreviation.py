class Solution:
    """
    @param word: the given word
    @return: the generalized abbreviations of a word
    """
    def generateAbbreviations(self, word):
        # Write your code here
        res = [word]
        self.dfs(word, 0, res)
        return res
        
    
    def dfs(self, word, pos, res):
        for i in range(pos, len(word)):
            for j in range(1, len(word) - i + 1):
                firstpart = word[:i]
                path = firstpart + str(j) + word[i + j :]
                res.append(path)
                self.dfs(path, i + len(str(j)) + 1, res)

test = Solution()

print(test.generateAbbreviations('word'))