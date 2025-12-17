'''
all possibilities: 
loop through s
applepenapple

                 .
            a/     p\
        penapple     x
        p/    a\
       apple    x
       a/  p\
      .      x 

      now can track dp[i], if we know that, no need to do it further
      -imagine taking a p p l e, but if we had apple we already did it
        when e gets there!
      wb at i is the aggregate of using each word if possible

      dp
      0123456789012
      applepenapple
      fffftfftfffft

      dp[i]=dp[i-m] and word==s[i-m:i] for any word

W=wm
memoization complexity: n/m * ?mW = nW

W + (W+1) + ... W+n/m = nW/m
<------n/m---->
2 3 4 5 

            /    \
           / \   / \  
tabulation complexity: nW
01234567
     
leetcode
fff?ffff
   i
s[4-4:4]==word
dp[4]
'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n=len(s)
        dp=[False]*(n+1)
        dp[0]=True
        for i in range(1,1+n):
            for word in wordDict:
                m=len(word)
                if i-m>=0 and dp[i-m] and word==s[i-m:i]:
                    dp[i]=True
                    break
        return dp[n]

        # def wb(i: int) -> bool:
        #     if i==n:
        #         return True
        #     if i in dp:
        #         return dp[i]
        #     for word in wordDict:
        #         m=len(word)
        #         if s[i:i+m]==word and wb(i+m):
        #             dp[i]=True
        #             return True
        #     dp[i]=False
        #     return False

        # dp={}
        # n=len(s)
        # return wb(0)