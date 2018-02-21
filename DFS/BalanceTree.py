# 110. Balanced Binary Tree
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        left = self.MaxHeight(root.left)
        right = self.MaxHeight(root.right)
        return abs(left - right) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)
        
        
    def MaxHeight(self, root):
        if not root:
            return 0
        left = self.MaxHeight(root.left)
        right = self.MaxHeight(root.right)
        return max(left, right) + 1