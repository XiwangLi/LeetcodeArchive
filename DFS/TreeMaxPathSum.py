# Binary Tree Maximum Path Sum
# Does not need to  go through the root or leaf

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = [-float('inf')]
        self.DFSpathSum(root, res)
        return res[0]        
        
    def DFSpathSum(self, root, res):
        if not root: 
            return 0
        left = max(self.DFSpathSum(root.left, res), 0)  #results from the left subtree
        right = max(self.DFSpathSum(root.right, res), 0) #results from the right subtree
        res[0] = max(res[0], left + right + root.val)  # update the final results      
        return max(left, right) + root.val  #return to the parent node