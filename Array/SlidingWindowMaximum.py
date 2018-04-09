<<<<<<< HEAD
import collections
from collections import deque
def maxSlidingWindow(nums, k):
    d = collections.deque()
    out = []
    for i, n in enumerate(nums):
    	print 'd1', d
        while d and nums[d[-1]] < n:
            d.pop()
        d += i,
        print 'd2------------------', d
        if d[0] == i - k:
            d.popleft()
            print 'd3  ---------------------------------', d
        if i >= k - 1:
            out += nums[d[0]],
    return out
nums = [1,3,-1,-3,5,3,6,7]
k = 3
=======
import collections
from collections import deque
def maxSlidingWindow(nums, k):
    d = collections.deque()
    out = []
    for i, n in enumerate(nums):
    	print 'd1', d
        while d and nums[d[-1]] < n:
            d.pop()
        d += i,
        print 'd2------------------', d
        if d[0] == i - k:
            d.popleft()
            print 'd3  ---------------------------------', d
        if i >= k - 1:
            out += nums[d[0]],
    return out
nums = [1,3,-1,-3,5,3,6,7]
k = 3
>>>>>>> 939b0502f1c705121dae8d24aaecb61943ad3e7d
print maxSlidingWindow(nums, k)