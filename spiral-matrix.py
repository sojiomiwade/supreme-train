class Solution:
    '''
    left,right=1,2
    top,bottom=2,1
    row in [2]
    col in [1..2]
    m[1][1..2]
    res=[1 2 3 4 8 12 11 10 9 5 6 7]

    7 
    9 
    6
    '''
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m,n=len(matrix),len(matrix[0])
        left,right,top,bot=0,n-1,0,m-1
        res=[]
        while left<=right and top<=bot:
            for col in range(left,1+right):
                res.append(matrix[top][col])
            top+=1
            for row in range(top,1+bot):
                res.append(matrix[row][right])
            right-=1

            if left<=right and top<=bot:
                for col in range(right,left-1,-1):
                    res.append(matrix[bot][col])
                bot-=1
                for row in range(bot,top-1,-1):
                    res.append(matrix[row][left])
                left+=1
        return res
