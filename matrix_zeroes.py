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

