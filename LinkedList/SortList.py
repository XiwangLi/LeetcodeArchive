"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param: head: The head of linked list.
    @return: You should return the head of the sorted linked list, using constant space complexity.
    """
    def sortList(self, head):
        # write your code here
        if not head or not head.next: return head
        pre, slow, fast = head, head, head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        pre.next = None
        h1 = self.sortList(head)
        h2 = self.sortList(slow)
        return self.merge(h1, h2)
        
    def merge(self, h1, h2):
        if not h1: return h2
        if not h2: return h1
        dummy = ListNode(None)
        curr = dummy
        while h1 and h2:
            if h1.val <= h2.val:
                curr.next = h1
                curr = curr.next
                h1 = h1.next
            else:
                curr.next = h2
                curr = curr.next
                h2 = h2.next
        curr.next = h1 or h2
        return dummy.next