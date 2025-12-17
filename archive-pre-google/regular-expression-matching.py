'''
s=aa 
p=a*

have to allow for no s --> can be true.

if no p:
    return no s

if p1 is not *
    if s and s0 and p0 match return match(s1,p1) -- need s0
    otherwise return False

if p1 is *
    zero match: val1 : match(s,p2)         -- need s0? no!
    nonzero match: val2: if s and s0==p0 and match(s1,p) -- need s0
    return val1 or val2

'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def ismatch(i: int, j: int):
            if j==n:
                return i==m
            if (i,j) in dp:
                return dp[i,j]
            firstcharmatch=i<m and p[j] in ('.',s[i])
            if j+1>=n or p[j+1]!='*':
                dp[i,j]=firstcharmatch and ismatch(i+1,j+1)
                return dp[i,j]
            iszeromatch=ismatch(i,j+2)
            ismorematch=firstcharmatch and ismatch(i+1,j)
            dp[i,j]=iszeromatch or ismorematch
            return dp[i,j]

        dp={}
        m,n=len(s),len(p)
        return ismatch(0,0)