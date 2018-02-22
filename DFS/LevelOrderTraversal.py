# 102. Binary Tree Level Order Traversal

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        res = []
        self.DFSleveloder(root, 0, res)
        return res
    
    def DFSleveloder(self, root, layer, res):
        if not root:
            return []
        if len(res) == layer: res.append([])
        res[layer].append(root.val)
        self.DFSleveloder(root.left, layer + 1, res)
        self.DFSleveloder(root.right, layer + 1, res)


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
		if not root: return []
        queue, res = [root], []
        while queue:
            size = len(queue)            
            level = []
            for _ in range(size):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level)
        return res		
		