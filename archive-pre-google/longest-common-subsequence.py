'''
a b c d e
  .
  .
a c e
l(i,j)=1+l(i+1,j+1) if s[i]==t[j] else min(l(i+1,j),l(i,j+1))
dp to avoid repeated calculations

l[i,j] -- s[:1] and t[:j]
strings of lengths i and j
you can say what ...
l0i = 0
lj0 = 0

lij = 1 + l[i-1,j-1] if s[i-1]==t[j-1] else min of removing one end char or the other end char

a c
a

m,n=2,1

   0 1  
0  0 0
1  0 1
2  0 1
'''
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n=len(text1),len(text2)
        dp=[[0 for _ in range(1+n)] for _ in range(1+1)]
        for r in range(1,1+m):
            for c in range(1,1+n):
                dp[r%2][c]=1+dp[(r-1)%2][c-1] if text1[r-1]==text2[c-1] else max(dp[(r-1)%2][c],dp[r%2][c-1])
        return dp[m%2][n]