'''
6 3 1 0 
3 2 1 0  
1 1 1 0
0 0 1 0
gp(r,c)=gp(r+1,c) + gp(r,c+1)

2 1 0 
1 1 0
0 1  
'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[0 for c in range(n+1)] for r in range(1+m)]
        dp[m][n-1]=1
        for r in range(m-1,-1,-1):
            for c in range(n-1,-1,-1):
                dp[r][c]=dp[r][c+1]+dp[r+1][c]
        return dp[0][0]