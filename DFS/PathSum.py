# Path Sum I

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root: return False
        if not root.left and not root.right:
            return sum == root.val
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)

# path Sum II

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        self.DFSpathSum(root, [], sum, res)
        return res
        
    def DFSpathSum(self, root, path, sum, res):
        if not root: 
            return
        if not root.left and not root.right and sum == root.val:
            res.append(path + [root.val])
            return
        self.DFSpathSum(root.left, path + [root.val], sum - root.val, res) 
        self.DFSpathSum(root.right, path + [root.val], sum - root.val, res)