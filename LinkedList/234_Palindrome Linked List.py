# Given a singly linked list, determine if it is a palindrome.

# Example 1:

# Input: 1->2
# Output: false
# Example 2:

# Input: 1->2->2->1
# Output: true


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        prev=None
        slow, fast= head, head  
        
        while fast and fast.next:  # reverse the first half and compare with the second half
            fast=fast.next.next
            slow.next, prev, slow=prev,slow,slow.next
        if fast:
            slow=slow.next
        
        while slow:
            if slow.val != prev.val:
                    return False
            slow=slow.next
            prev=prev.next
            
        return True


  
    