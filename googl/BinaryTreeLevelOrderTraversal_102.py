# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
        	return []
        res = []
        self.dfs(root, 0, res)
        return res

    def dfs(self, root, level, res):
    	if not root:
    		return 
    	if len(res) <= level:
    		res.append([])
    	res[level].append(root.val)
    	self.dfs(root.left, level + 1, res)
    	self.dfs(root.right, level + 1, res)

    def levelOrderII(self, root):
    	if not root: return []
    	queue = [root]
    	res = []
    	while queue:
    		size = len(queue)
    		temp = []
    		for _ in range(size):
    			node = queue.pop(0)
    			temp.append(node.val)
    			if node.left:
    				queue.append(node.left)
    			if node.right:
    				queue.append(node.right)
    		res.append(temp)
    	return res

