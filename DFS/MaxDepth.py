# Max Depth of tree

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """		
		maxdep = [0]
        self.DFS(root, 1, maxdep)
        return maxdep[0]
        
    def DFS(self, root, currdep, maxdep):
        if not root: return
        maxdep[0] = max(maxdep[0], currdep)  # max depth
        self.DFS(root.left, currdep + 1, maxdep) # get the depth of the left subtree
        self.DFS(root.right, currdep + 1, maxdep) # get the depth of the right subtree