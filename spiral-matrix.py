'''
walls left,right,top,bottom provide the start and end for 4 directions
when there's no space between the walls we are done
for a run in any dir, bring the wall in that dir down
1 2
4 5

left,right,top,bottom=01,0,1,0
res=[1 2 5 4]
c in r(0,-1,-1)
'''
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m,n=len(matrix),len(matrix[0])
        left,right,top,bottom=0,n-1,0,m-1
        res=[]
        while left<=right and top<=bottom:
            for c in range(left,1+right):
                res.append(matrix[top][c])
            top+=1
            for r in range(top,1+bottom):
                res.append(matrix[r][right])
            right-=1
            if left<=right and top<=bottom:
                for c in range(right,left-1,-1):
                    res.append(matrix[bottom][c])
                bottom-=1
                for r in range(bottom,top-1,-1):
                    res.append(matrix[r][left])
                left+=1
        return res
'''
2
3
4
l,r,t,b=0,-1,1,1
'''