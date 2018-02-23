# Flatten Binary Tree to Linked List
# Leetcode 114
# The key idea is 1: store the right subtree, 2 flaten the left subtree, 
#                 3. join the flat left subtree 4. flatten the right subtree
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
		if not root: return []
		right = root.right
		if root.left:
			self.flatten(root.left)
			tail = root.left
			while tail.right:
				tail = tail.right
			root.left, root.right, tail.right = None, root.left, right
		self.flatten(root.right)


class Solution(object):  # Divide & Conquer
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root: return
        self.flatten(root.left)  #flat left subtree
        self.flatten(root.right) # flat right subtree
        node = root
        if not node.left:
            return
        node = node.left  
        while node.right: #find the tail of left tree
            node = node.right
        node.right, root.left, root.right  = root.right, None, root.left  #flat the smallest tree