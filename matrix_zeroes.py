class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        '''
        since we modify inplace, can use the 1st row and col as flags
        that there is a zero. then come back from the southeast corner
        to zerofy any cell. from nr

        flag will tell us whether we ever set colone_haszero to true
        False, and we don't set that
        '''
        m,n=len(matrix),len(matrix[0])
        colone_haszero=False
        for i in range(m):
            if matrix[i][0]==0:
                colone_haszero=True
            for j in range(1,n):
                if matrix[i][j]==0:
                    matrix[0][j]=matrix[i][0]=0

        for i in range(m-1,-1,-1):
            for j in range(n-1,0,-1):
                if 0 in (matrix[i][0],matrix[0][j]):
                    matrix[i][j]=0
            if colone_haszero:
                matrix[i][0]=0
