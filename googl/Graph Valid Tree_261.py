class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        nerblist = {i : [] for i in range(n)}
        for u, v in edges:
        	nerblist[u].append(v)
        	nerblist[v].append(u)
        visit =set([0])
        if not self.dfsValid(nerblist, 0, -1, visit):
        	return False
        if len(visit) != n:
        	return False
        return True

    def dfsValid(self, nerblist, node, prenode, visit):
    	for nerb in nerblist[node]:
    		if nerb == prenode:
    			continue
    		if nerb in visit:
    			return False
    		else:
    			visit.add(nerb)
    		if not self.dfsValid(nerblist, nerb, node, visit):
    			return False
    	return True

model = Solution()
print model.validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]])