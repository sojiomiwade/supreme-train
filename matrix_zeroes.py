class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n, is_col0_zero = len(matrix), len(matrix[0]), False
        for r in range(m):
            is_col0_zero |= not matrix[r][0]
            for c in range(1, n):
                if matrix[r][c] == 0:
                    matrix[r][0] = matrix[0][c] = 0

        for r in range(m-1, -1, -1):
            for c in range(n-1, 0, -1):
                if 0 in (matrix[r][0], matrix[0][c]):
                    matrix[r][c] = 0
            if is_col0_zero:
                matrix[r][0] = 0





'''
matrix zeroes
fill with zeroes, the columns and rows that have a zero in them. 


in n**2 time and 0 space we can do this: use a col0 variable to check for whether a[i][0] had a 0 for any i; for arbitrary aij, use ai0 to remember (on 2nd pass) to zero that row, and a0j to zero the column.  2nd pass must come from bottom right to top left. otherwise, we set aij on a col (because that col should be zero) and then go zero out the row, which is wrong.
for all  entries, aij on 2nd pass, aij = 0 if a0j or ai0 is zero, 
'''
from typing import List


def zero_matrix(matrix: List[List[int]]) -> None:
    is_col0_zero = False
    m, n = len(matrix), len(matrix[0])
    for i in range(m):
        if matrix[i][0] == 0:
            is_col0_zero = True
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = matrix[0][j] = 0

    for i in range(m - 1, -1, -1):
        for j in range(n - 1, 0, -1):
            if 0 in (matrix[0][j], matrix[i][0]):
                matrix[i][j] = 0
        if is_col0_zero:
            matrix[i][0] = 0

'''
1 2 0     0 0 0
5 4 2 --> 0 4 0
0 3 1     0 0 0

1 2 0     0 0 0
5 4 2 --> 5 4 0
8 3 0     0 0 0
'''
matrix = [
    [1, 2, 0],
    [5, 4, 2],
    [0, 3, 1],
]
zero_matrix(matrix)
print(matrix)

matrix = [
    [1, 2, 0],
    [5, 4, 2],
    [8, 3, 0],
]
zero_matrix(matrix)
print(matrix)