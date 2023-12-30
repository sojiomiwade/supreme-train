class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n,m=len(s),len(wordDict)
        dp=[False for _ in range(n+1)]
        dp[0]=True
        for i in range(1,n+1):
            for j in range(m):
                wdj=wordDict[j]
                mj=len(wdj)
                dp[i]=dp[i] or (s[i-mj:i]==wdj and dp[i-mj])
        return dp[n]