class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head: return None
        curr = head
        while curr:
            newNode = RandomListNode(curr.label)
            newNode.next = curr.next
            curr.next = newNode
            curr = curr.next.next
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        newHead = head.next
        pslow = head
        pfast = newHead
        while pfast.next and pslow.next:
            pslow.next = pfast.next
            pslow = pslow.next
            pfast.next = pslow.next
            pfast = pfast.next
        pfast.next = None
        pslow.next = None
        return newHead