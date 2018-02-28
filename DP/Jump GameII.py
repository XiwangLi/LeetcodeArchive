#Jump Game II
# THe t: O(n2), s:O(n) mathod is easy to think of

class Solution:
    """
    @param A: A list of integers
    @return: An integer
    """
    def jump(self, A):
    	DP = float('inf') * len(A)
    	DP[-1] = 0
    	for i in range(len(A) - 2, -1, -1):
    		for j in range(1, A[i] + 1):
    			if i + j >= len(A):
    				DP[i] = 0
    			else:
    				DP[i] = min(DP[i], DP[i + j])
    		DP[i] += 1
    	return DP[0]
# This brute force will exceed the time
# Here is the t: O(n), s: O(1) method
# The key idea is the store farest jump and then start from the "farest + 1"
class Solution:
    """
    @param A: A list of integers
    @return: An integer
    """
    def jump(self, A):
    	start, end, maxend, step, n = 0, 0, 0, 0, len(A)
    	while end < n - 1:
    		step += 1
    		for i in range(start, end + 1):
    			if i + A[i] >= n - 1:
    				return step
    			else:
    				maxend = max(maxend, i + A[i])
    		start, end = end + 1, maxend
    	return step
