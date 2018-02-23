# 25. Reverse Nodes in k-Group

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head: return head
        currk = head
        for _ in range(k - 1):
            if not currk:
                return head
            currk = currk.next
        if not currk: 
            return head
        else:
            newNode = self.reverseKGroup(currk.next, k)  #reverse the k + 1 (and after node)
        curr = head
        for _ in range(k):
            curr.next, newNode, curr = newNode,curr, curr.next # reserse node 1 to k
        return newNode