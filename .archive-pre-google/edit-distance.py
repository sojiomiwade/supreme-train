'''
ros
ros

delete
ros
ros
insert into word1 - 

word1 word2

ros
ros
ans 1
dis(i,j)=
    dis(i+1,j+1) if the same
    1+min((dis(i,j+1), dis(i+1,j), dis(i+1,j+1))) if different
    min(dis)

    hor   se
    ro    s
    dp[i,j] -- with strings s[:i] and t[:j], what's dis?
    if different s[i-1] and t[j-1], 
        dpij is 1 + min of three different ways
    a
    ham
    dp 0k  and dp k0 
    dp    
    13 = 
    03
    dp k0 = 
    dp 00 = 0

        dp
    dp[m,n]

ros
horse
dp 
  0 1 2 3 4 5
0 0 1 2 3 4 5
1 1 1 0 0 0 0
2 2 0 0 0 0 0 
3 3 0 0 0 0 0
'''
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n=len(word1),len(word2)
        dp=[[0 for j in range(1+n)] for i in range(1+m)]
        for i in range(1+m):
            dp[i][0]=i
        for j in range(1+n):
            dp[0][j]=j
        if m==0 or n==0:
            return max(dp[0][n],dp[m][0])
        for i in range(1,1+m):
            for j in range(1,1+n):
                if word1[i-1]==word2[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=1+min(
                        dp[i-1][j-1],
                        dp[i][j-1],
                        dp[i-1][j]
                    )
        return dp[m][n]

        # def dis(i: int, j: int) -> int:
        #     if i==m or j==n:
        #         return max(n-j,m-i)
        #     if (i,j) in dp:
        #         return dp[i,j]
        #     if word1[i]==word2[j]:
        #         dp[i,j]=dis(i+1,j+1)
        #     else:
        #         dp[i,j]=1+min(
        #             dis(i+1,j+1),
        #             dis(i,j+1),
        #             dis(i+1,j)
        #         )
        #     return dp[i,j]
        # dp={}
        # m,n=len(word1),len(word2)
        # return dis(0,0)