# 129. Sum Root to Leaf Numbers
# This problem is similar to the path sum, but just to change the pure sum to the "represents the number"

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = [0]
        self.DFSsumNumber(root, 0, res)
        return res[0]
        
    def DFSsumNumber(self, root, temp, res):
        if not root: return 0
        if not root.left and not root.right:
            temp = temp * 10 + root.val
            res[0] += temp
            return 
        self.DFSsumNumber(root.left, temp * 10 + root.val, res)
        self.DFSsumNumber(root.right, temp * 10 + root.val, res)