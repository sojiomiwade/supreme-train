'''
2
1 1
2
cs(n)=cs(n-1)+cs(n-2)
if n<=0 return int(n==0). otherwise recurse
dp yes!
cs[5]=cs[4]+cs[3]
cs[1]=1
cs[0]=1
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        # dp=[0 for _ in range(1+n)]
        p0=p1=p2=1
        for i in range(2,1+n):
            p2=p0+p1
            p0,p1=p1,p2
        return p2
        # def cs(n):
        #     if n<=0:
        #         return int(n==0)
        #     if n in dp:
        #         return dp[n]
        #     dp[n]=cs(n-1)+cs(n-2)
        #     return dp[n]
        # dp={}
        # return cs(n)