'''
pij = p(i-1,j-1) and s[i]==s[j]
abaa
 i
  j 

            0(n-1)
           /   \
          1n    0(n-2)   
                05
            04
                14
             x04
         03 -- 12 
              13
      02 
              x13
   01      12
       11
            
00


4+1=5

abaa
l  r = 
 lr 
dp={}
10:T,0(-1):T

abaca
 i
  j

0
11
05 -- 14
pij = p(i-1)(j-1) and i==j 
 a
 0


aaaaa
01234
  i
    j
i=2
j=2
jd=1
l,r= should be (2,3), (1,4), stop
l,r=i-j,i+(j+jd)
l,r=(2,3),(1,4)
012
True False True
False True False
False False True

'''
class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s)
        dp=[[False for _ in range(n)] for _ in range(n)]
        count=0
        for jd in range(2):
            for i in range(n):
                for j in range(n):
                    l,r=i-j,i+j+jd
                    if l<0 or r>=n:
                        break
                    dp[l][r]=s[l]==s[r] and (l in (r,r-1) or dp[l+1][r-1])
        return sum(sum(row) for row in dp)
                    
        # dp=[[False for _ in range(n)] for _ in range(n)]
        # for l in range(n-1,-1,-1):
        #     for r in range(n):
        #         dp[l+1][r]=ispal(l+1,r)
        #         dp[l][r-1]=ispal(l,r-1)
        #         dp[l][r]=s[l]==s[r] and dp[l+1][r-1]
        # return sum(dp)
        # def ispal(l: int, r: int):
        #     if (l,r) in dp:
        #         return dp[l,r]
        #     if l>r:
        #         return True
        #     ispal(l+1,r)
        #     ispal(l,r-1)
        #     dp[l,r]=s[l]==s[r] and ispal(l+1,r-1)
        #     return dp[l,r]

        # dp,n={},len(s)
        # ispal(0,n-1)
        # return sum(dp.values())
