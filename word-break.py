class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def wb(k: int) -> bool:
            if k==n:
                return True
            
            if k in dp:
                return dp[k]
            breaks=False
            for word in wordDict:#
                m=len(word)
                if n-k>=m and s[k:k+m]==word:
                    breaks=breaks or wb(k+m)
            dp[k]=breaks
            return breaks

        dp={}
        n=len(s)
        return wb(0)