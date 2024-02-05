class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        dp=[[False for _ in range(n)] for _ in range(n)]
        count=0
        INF=float('inf')
        bl,br=INF,-INF
        for jd in range(2):
            for i in range(n):
                for j in range(n):
                    l,r=i-j,i+j+jd
                    if l<0 or r>=n:
                        break
                    dp[l][r]=s[l]==s[r] and (l in (r,r-1) or dp[l+1][r-1])
                    if dp[l][r] and r-l>br-bl:
                        bl,br=l,r
        return s[bl:br+1]