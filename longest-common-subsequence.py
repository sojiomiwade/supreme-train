class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
        a c q e
        a b c d e
        lcs(s,t)=1+lcs(s[1:],t[1:]) if s0==t0. otherwise max(the two lcs where we remove 1 char on the left alternatively from both)
        time: 2**(max(m,n)) (because we branch for each char)
        use dp --> makes it 'tabular' for n**2
        dp[i][j]=1+dp[i-1][j-1] if s[i-1]==t[j-1]
                =max of two (....dp[i-1][j]
        wher dp-ij --> strings of length i and j
        ans is dp[m][n]
        init: dp[0][j] = dp[i][0] = 0
        then i goes from 1 .. m and j goes from 1 .. n
        '''
        # def lcs(top: int, bot: int)
        # dp={}
        
        # return dp[0,0]
        # a b
        # a q
        # 0 0 0 
        # 0 1 1
        # 0 1 1
        m,n=len(text1),len(text2)
        dp=[[0 for _ in range(1+n)] for _ in range(2)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if text1[i-1]==text2[j-1]:
                    dp[i%2][j]=1+dp[(i-1)%2][j-1]
                else:
                    dp[i%2][j]=max(dp[i%2][j-1],dp[(i-1)%2][j])
        return dp[m%2][n]
