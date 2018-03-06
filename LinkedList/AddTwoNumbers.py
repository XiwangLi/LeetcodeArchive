class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head=ListNode(0)
        curr=head
        val=0
        ten=0
        while l1 or l2 or val:
            if l1:
                val+=l1.val
                l1=l1.next
            if l2:
                val+=l2.val
                l2=l2.next
            curr.next=ListNode(val%10)
            curr=curr.next            
            val=val//10
        return head.next