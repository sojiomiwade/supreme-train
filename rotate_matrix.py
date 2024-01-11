class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        '''
        a b c d
        e f g h
        i j k l
        m n o p

        . . . a .
        e f g b .
        i j k c .
        m n o d .
        . . . . .
        each corner is the head of a n-1 node train

        move left to top, top to right, right to bottom, bottom to left, 

        k goes from 0 to n-1
        '''
        n=len(matrix)
        arr=matrix
        for l in range(n//2):
            for k in range(l,n-1-l):
                temp=arr[l][n-1-k] #save top
                arr[l][n-1-k]=arr[k][l] #left -> top
                arr[k][l]=arr[n-1-l][k] #bot->left
                arr[n-1-l][k]=arr[n-1-k][n-1-l] #right->bot
                arr[n-1-k][n-1-l]=temp #top->right