'''
s .
. .  
. f 
DFS gives all possibilities, need backtracking
if we make it to finish line, add to count
dont think we need visited since we cant go back
'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def getpaths(r: int, c: int) -> int:
            if (r,c) in dp:
                return dp[r,c]
            if (r,c)==(m-1,n-1):
                return 1
            if r>=m or c>=n:
                return 0
            dp[r,c]=getpaths(r,c+1)+getpaths(r+1,c)
            return dp[r,c]

        dp={}
        return getpaths(0,0)