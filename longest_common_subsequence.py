'''
l
e
b
c
o -- can use dynamic programming
w
i
t
xx
bruteforce:...

abcde 5
a cqe 4
llcs(s,t) = 1/2 * (|s|+|t| - dd(s,t))

dp
    0 1 2 3 4 5
    a b c d e .
0 a 
1 c   ? .
2 e   .
3 .

abcde
  i    
ace
 j

dp[i][j] := dd(s[:i],t[:j])
dp[i][0] = i
dp[0][j] = j
=> dp[i][j] = dp[i-1][j-1] if text1[i-1]==text2[j-1]
              1+min(dp[i])
'''
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
        abc
        def

        '''
        m,n=len(text1),len(text2)
        dp=[[0 for j in range(n+1)] for i in range(m+1)]
        for k in range(m+1):
            dp[k][0]=k
        for k in range(n+1):
            dp[0][k]=k
        for i in range(1,m+1):
            for j in range(1,n+1):
                if text1[i-1]==text2[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=1+min(dp[i-1][j],dp[i][j-1])
        # for r in dp:
        #     print(' '.join(str(v) for v in r))
        # print(dp[m][n])
        return (m+n-dp[m][n])//2


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def dd(i,j):
            if (i,j) in dp:
                return dp[i,j]

            if i==m or j==n:
                val=max(m-i,n-j) 
            elif text1[i]==text2[j]:
                val=dd(i+1,j+1)
            else:
                val=1+min(dd(i,j+1),dd(i+1,j))
            dp[i,j]=val
            return val

        m,n=len(text1),len(text2)
        dp={}
        return (m+n-dd(0,0))//2

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n=len(text1),len(text2)
        dp=[[0 for j in range(n+1)] for i in range(2)]
        for ti in range(1,m+1):
            i=ti%2
            for j in range(1,n+1):
                if text1[ti-1]==text2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i][j-1],dp[i-1][j])
        return dp[m%2][n]
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def _lcs(i,j):
            if (i,j) in dp:
                return dp[i,j]

            if i==m or j==n:
                val=0
            elif text1[i]==text2[j]:
                val=1+_lcs(i+1,j+1)
            else:
                val=max(_lcs(i+1,j),_lcs(i,j+1))
            dp[i,j]=val
            return val

        m,n,dp=len(text1),len(text2),{}
        return _lcs(0,0)
