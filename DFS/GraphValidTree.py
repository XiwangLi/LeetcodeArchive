<<<<<<< HEAD
class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        neirblist = {i : [] for i in range(n)}
        for u, v in edges:
            neirblist[u].append(v)
            neirblist[v].append(u)
        visited = set([0])
        if not self.dfsNVisit(neirblist, visited, 0, -1):
            return False        
        if len(visited) != n:
            return False
        return True
    
    def dfsNVisit(self, neirblist, visited, node, parent):
        for neirb in neirblist[node]:
            if neirb == parent: continue
            if neirb in visited: return False
            visited.add(neirb)
            if not self.dfsNVisit(neirblist, visited, neirb, node):
                return False
        return True

edges = [[0, 1], [0, 2], [0, 3], [1, 4]]        
model = Solution()
=======
class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        neirblist = {i : [] for i in range(n)}
        for u, v in edges:
            neirblist[u].append(v)
            neirblist[v].append(u)
        visited = set([])
        if self.dfsVisit(neirblist, visited, 0, -1):
            return False
        if len(visited) != n:
            return False
        return True
    
    def dfsVisit(self, neirblist, visited, node, parent):
        visited.add(node)
        for neirb in neirblist[node]:
            if neirb not in visited:
                if self.dfsVisit(neirblist, visited, neirb, node):
                    return True
            elif neirb in visited and neirb != parent:
                return True
        return False

edges = [[0, 1], [0, 2], [0, 3], [1, 4]]        
model = Solution()
>>>>>>> 939b0502f1c705121dae8d24aaecb61943ad3e7d
print model.validTree(5, edges)              