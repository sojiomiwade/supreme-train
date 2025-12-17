class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        '''
        save right to temp
        top (head with val 11) to right
        left to top
        bot to left
        temp to bot

        then consider inside layers (n//2) of them
        1 2
        3 4
        
        '''
        n=len(matrix)
        for l in range(n//2):
            for i in range(l,n-1-l):
                temp=matrix[n-1-i][n-1-l]
                matrix[n-1-i][n-1-l]=matrix[l][n-1-i]
                matrix[l][n-1-i]=matrix[i][l]
                matrix[i][l]=matrix[n-1-l][i]
                matrix[n-1-l][i]=temp
