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
'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def wb(i: int) -> bool:
            if i==n:
                return True
            if i in dp:
                return dp[i]
            for word in wordDict:
                m=len(word)
                if s[i:i+m]==word and wb(i+m):
                    dp[i]=True
                    return True
            dp[i]=False
            return False

        dp={}
        n=len(s)
        return wb(0)