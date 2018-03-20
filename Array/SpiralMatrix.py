class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        if not matrix: return []
        res = []
        m, n = len(matrix), len(matrix[0])
        r0, c0 = 0, 0
        r1, c1 = m - 1, n - 1
        while r0 < r1 and c0 < c1:
            for j in range(c0, c1):
                res.append(matrix[r0][j])
            
            for i in range(r0, r1):
                res.append(matrix[i][c1])
            
            for j in range(c1, c0, -1):
                res.append(matrix[r1][j])
            
            for i in range(r1, r0, -1):
                res.append(matrix[i][c0])

            r0 += 1
            r1 -= 1
            c1 -= 1
            c0 += 1

        if r0 == r1 and c0 == c1:
            res.append(matrix[r0][c0])
        elif r0 == r1:
            for j in range(c0, c1 + 1):
                res.append(matrix[r0][j])
        elif c0 == c1:
            for i in range(r0, r1 + 1):
                res.append(matrix[i][c0])
        return res

    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n < 0:
            return []
        res = [[0] * n for _ in range(n)]
        rstart, cstart = 0, 0
        count = 1
        while n > 0:
            if n == 1:
                res[rstart][cstart] = count
                count += 1
                break
            for j in range(n - 1):
                res[rstart][cstart + j] = count
                count += 1
            for i in range(n - 1):
                res[rstart + i][cstart + n - 1] = count
                count += 1
            for j in range(n - 1):
                res[rstart + n - 1][cstart + n - 1 - j] = count
                count += 1
            for i in range(n - 1):
                res[rstart + n - 1 - i][cstart] = count
                count += 1 
           
            n -= 2
            rstart += 1
            cstart += 1
        return res




model = Solution()
maxtrix = [[ 1, 2, 3 ], [ 4, 5, 6 ], [ 7, 8, 9 ]]
print model.spiralOrder(maxtrix)
print model.generateMatrix(3)