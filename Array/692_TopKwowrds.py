class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        import collections, heapq
        res = []
        count = collections.Counter(words)
        heap = [(-n, word) for word, n in count.items()]
        heap.sort(key=lambda w: w[0])
       
        # heapq.heapify(heap)
        # for _ in range(k):
        #     res.append(heapq.heappop(heap)[1])


        return [word for num, word in heap[:k]]
     


test = Solution()
words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 2

print (test.topKFrequent(words, k))