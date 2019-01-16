# Given a list of non-negative numbers and a target integer k, 
# write a function to check if the array has a continuous subarray of size 
# at least 2 that sums up to the multiple of k, that is, sums up to n*k where n is also an integer.

# Example 1:
# Input: [23, 2, 4, 6, 7],  k=6
# Output: True
# Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.

# Example 2:
# Input: [23, 2, 6, 4, 7],  k=6
# Output: True
# Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.

# Note:
# The length of the array won't exceed 10,000.
# You may assume the sum of all the numbers is in the range of a signed 32-bit integer.

class Solution(object):
    def checkSubarraySum(self, nums, k):
    	presum = [0]
    	for num in nums:
    		cursum = presum[-1] + num
    		if k: cursum %= k
    		presum.append(cursum)

    	seen = set()
    	for i in range(len(presum) - 3, -1, -1):
    		seen.add(presum[i + 2])
    		if presum[i] in seen:
    			return True
    	return False




test = Solution()
nums = [0, 0]
print (test.checkSubarraySum(nums, 0))


# Since we are interested in quantities of the form A[L] + A[L+1] + ... + A[R], let's use a standard technique of 
# keeping a prefix sum P[i] = sum(A[:i]), so that we can quickly query A[L] + A[L+1] + ... + A[R] = P[R+1] - P[L].

# Now, we would like to know if P[R+1] - P[L] = 0 (mod k) is solvable with 0 <= L < R < len(A). 
# This means: For any 0 <= L < len(A), we would like to know if there is some L + 2 <= X < len(A) with P[X] = P[L].

# This can be solved in linear time: at decreasing time i, we've now seen in total all elements in P[i+2:], 
# and we want to know if P[i] is something we've seen before. 
# If we have, then indeed P[i] = P[j] for j >= i + 2 as desired.

# Of course, there is the pesky "mod k" part. When k is zero, the modulus should be ignored, otherwise we should consider values of P modulo abs(k).

