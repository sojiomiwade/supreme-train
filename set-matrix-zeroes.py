'''
use first row to mark when a column has zero
use first col to denote when a row has a zero
    but then how to know when the col itself had a zero

1 1 0 3 ...
2.  0
3 . y . 
0.  x
1

if colone haszero set the flag so we can zero it out 
must go backward. to set the vals. otherwise setting col1 early will 
overrite whehter to set the whole row or not 
1 0 1
0 0 0
1 0 1
col1 F
'''
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        col1=False
        m,n=len(matrix),len(matrix[0])
        for i in range(m):
            col1=col1 or matrix[i][0]==0
            for j in range(1,n):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0

        for i in range(m-1,-1,-1):
            for j in range(n-1,0,-1):
                if 0 in (matrix[i][0],matrix[0][j]):
                    matrix[i][j]=0
            if col1:
                matrix[i][0]=0