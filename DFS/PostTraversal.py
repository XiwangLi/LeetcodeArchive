# 145. Binary Tree Postorder Traversal

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        stack, res, visit = [root], [], root
        while stack:
            node = stack[-1]
            if node:
                if (not node.right and not node.left) or (node.left == visit or node.right == visit):
                    node = stack.pop()
                    res.append(node.val)
                    visit = node
                else:
                    if node.right:
                        stack.append(node.right)
                    if node.left:
                        stack.append(node.left)
        return res
		
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
		stack, res = [root], []
        while stack:
            node = stack.pop()
            if node:
                res.insert(0, node.val)
                stack.append(node.left)
                stack.append(node.right)
        return res