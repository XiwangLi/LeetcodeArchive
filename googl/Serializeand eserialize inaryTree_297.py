# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        #from collections import deque
        if not root:
            return ''
        queue = deque()
        queue.append(root)
        vals = []
        while queue:
            node = queue.popleft()
            if not node:
                vals.append('#')
                continue
            else:
                vals.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)
        return ','.join(vals)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        #from collections import deque
        if len(data) == 0:
            return None
        nodes = data.split(',')
        root = TreeNode(int(nodes[0]))
        queue = deque()
        queue.append(root)
        pos = 1
        while len(queue) > 0:
            curr = queue.popleft()
            if nodes[pos] != '#':
                left = TreeNode(int(nodes[pos]))
                curr.left = left
                queue.append(left)
            pos += 1
            if nodes[pos] != '#':
                right = TreeNode(int(nodes[pos]))
                curr.right = right
                queue.append(right)
            pos += 1
        return root
                
                
                
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))