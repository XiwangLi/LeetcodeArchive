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
print model.validTree(5, edges)              