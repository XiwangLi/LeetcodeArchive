#N-Queens
def solveNQueens(n):
	res = []
	NQ_DFS(n, 0, [-1] * n, [], res)
	#print res
	return res


def NQ_DFS(n, irow, ipos, path, res):
	if irow == n:
		res.append(path)
		return
	for i in range(n):
		ipos[irow] = i
		if notCheck(ipos, irow):
			temp = '.'*n
			NQ_DFS(n, irow + 1, ipos, path + [temp[:i] + 'Q' + temp[i + 1:]], res)

def notCheck(pos, irow):
	for i in range(irow):
		if pos[i] == pos[irow] or abs(pos[i] - pos[irow]) == irow - i:
			return False
	return True


solveNQueens(4)