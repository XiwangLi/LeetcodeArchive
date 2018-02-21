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
=======
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

#PathSum III

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root: return 0
        res = 0
        return self.DFSpathSum(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum) 
        
    def DFSpathSum(self, root, sum):
        if not root:
            return 0
        res = 0
        if sum == root.val: res += 1
        res += self.DFSpathSum(root.left, sum - root.val)
        res += self.DFSpathSum(root.right, sum - root.val)
        return res

