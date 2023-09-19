class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])
        vert = ((i,0) for i in range(m))
        horiz = ((0,j) for j in range(n))
        for (i,j) in itertools.chain(horiz, vert):
            while i+1 < m and j+1 < n:
                if matrix[i][j] != matrix[i+1][j+1]:
                    return False
                i += 1
                j += 1
        return True
