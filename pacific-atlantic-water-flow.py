'''
m*n*(mn)
1 2 2 <-- p p p
pacific behind and above, atlantic infront and below
i-th cell is 
p 5 4 3
p 3
p 2 1 1
  a a a 

two passes
then if pij and aij, then add (i,j) to result!

  p p p      | exp
p 1 2 2 a      f t t 
p 3 1 3 a      t f t
p 2 4 5 a      t t t
  a a a

a       p
f T t   t t t
T f t   t f f
t t t   t f f

res []

1 2  3
8 9 (4)
7 6 (5)
'''
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m,n=len(heights),len(heights[0])
        p=[[True if 0 in (i,j) else False for j in range(n)] for i in range(m)]
        a=[[True if i==m-1 or j==n-1 else False for j in range(n)] for i in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                left=p[i][j-1] and heights[i][j-1]<=heights[i][j]
                top=p[i-1][j] and heights[i-1][j]<=heights[i][j]
                p[i][j]=left or top
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                right=a[i][j+1] and heights[i][j+1]<=heights[i][j]
                bot=a[i+1][j] and heights[i+1][j]<=heights[i][j]
                a[i][j]=right or bot
        print(p,a)
        return [[i,j] for i in range(m) for j in range(n) if a[i][j] and p[i][j]]
