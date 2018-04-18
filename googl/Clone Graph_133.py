# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node: return None
        cloned = {node: UndirectedGraphNode(node.label)}
        queue = collections.deque([(node, cloned[node])])
        while queue:
            nodesrc, nodeclone = queue.popleft()
            for neib in nodesrc.neighbors:
                if neib not in cloned:
                    cloned[neib] = UndirectedGraphNode(neib.label)
                    queue.append((neib, cloned[neib]))
                nodeclone.neighbors.append(cloned[neib])
        return cloned[node]
                