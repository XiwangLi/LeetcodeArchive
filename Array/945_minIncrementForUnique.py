class Solution(object):
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # 1 1 2 2 3 7
        #   2             1
        #     3           1
        #       4         2
        #         5       2
        # 1 2 3 4 5 7
        
        A = sorted(A)
        res = 0
        for i in range(1, len(A)):
            pre, curr = A[i -1], A[i]
            if pre >= curr:
                res += pre - curr + 1
                A[i] = pre + 1
        return res 


test = Solution()
A = [3,2,1,2,1,7]
print (test.minIncrementForUnique(A))
        