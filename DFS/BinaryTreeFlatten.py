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