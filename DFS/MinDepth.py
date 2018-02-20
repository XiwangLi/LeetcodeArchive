#Min Depth

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        depL = self.minDepth(root.left)
        depR = self.minDepth(root.right)
        return max(depL,depR) + 1 if depL == 0 or depR == 0 else min(depL, depR) + 1
		
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
		
		if not root: return 0
		if not root.left or root.right:
			return max(self.minDepth(root.left),self.minDepth(root.left)) + 1
		else:
			return min(self.minDepth(root.left),self.minDepth(root.left)) + 1
		