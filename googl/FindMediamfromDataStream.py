from heapq import *
class MedianFinder(object):
    

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.left_maxheap = []
        self.right_minheap = []
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if len(self.left_maxheap) == len(self.right_minheap):
            heappush(self.right_minheap, -heappushpop(self.left_maxheap, -num))
        else:
            heappush(self.left_maxheap, -heappushpop(self.right_minheap, num))
        

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.left_maxheap) == len(self.right_minheap):
            return (-self.left_maxheap[0] + self.right_minheap[0]) / 2.0
        else:
            return self.right_minheap[0] * 1.0
        


# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
for i in [2, 3, 4, 6, 8, 5]:
    obj.addNum(i)
param_2 = obj.findMedian()
print param_2