class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        curr, n = root, 0
        while curr:
            curr, n = curr.next, n + 1
        partssize, longerparts = n // k, n % k
        res = [partssize + 1] *  longerparts + [partssize] * (k - longerparts)
        pre, curr = None, root
        for idx, nums in enumerate(res): 
            res[idx] = curr
            for _ in range(nums):
                pre, curr = curr, curr.next
            if pre:
                pre.next = None
        return res