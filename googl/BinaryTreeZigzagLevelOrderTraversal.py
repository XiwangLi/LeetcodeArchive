class Solution(object):
    def zigzagLevelOrder(self, root):
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
    	if level % 2 == 0:
    		res[level].append(root.val)
    	if level % 2:
    		res[level].insert(0, root.val)
    	self.dfs(root.left, level + 1, res)
    	self.dfs(root.right, level + 1, res)