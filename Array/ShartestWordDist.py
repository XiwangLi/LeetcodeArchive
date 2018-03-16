class WordDistance(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.dic = {}
        for i, w in enumerate(words):
            self.dic[w] = self.dic.get(w, []) + [i] #get a hash set for all the index of each word               

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        w1, w2 = self.dic[word1], self.dic[word2]
        m, n, i, j, length = len(w1), len(w2), 0, 0, float('inf')
        while i < m and j < n: 
        #find the min dist from w1[i] - w2[j]
        #We do not need two for loops as w1 and w2 are sorted
            length = min(length, abs(w1[i] - w2[j]))
            if w1[i] < w2[j]:
                i += 1
            else:
                j += 1
        return length
            
        


# Your WordDistance object will be instantiated and called as such:
words = ["practice", "makes", "perfect", "coding", "makes"]
word1 = 'coding'
word2 = 'practice'
obj = WordDistance(words)
print obj.shortest(word1,word2)