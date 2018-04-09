class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
        from Queue import PriorityQueue
        dummy = ListNode(None)
        curr = dummy
        q = PriorityQueue()
        
        for node in lists:
            if node:
                q.put((node.val, node))              
        while q.qsize() > 0:
            curr.next = q.get()[1]
            curr = curr.next
            if curr.next:
                q.put((curr.next.val, curr.next))
        return dummy.next