'''
2 3 2
|      \
2 3     3 2

9 2 3 8 x x
ans=9
rob(0,end=n-2)
rob(1,end=n-1)
rob(i)=max(nums[i]+rob(i+2),rob(i+1))
    if > end, return 0

0 1 2
2 3 9
|      \
2 3      3 9
0
|     \
1      2
|   \
2    3
| \  
3  4
max(max(2,3),  max(3,9))
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob(hidx: int, end: int) -> int:
            if hidx>end:
                return 0
            if (hidx,end) in dp:
                return dp[hidx,end]
            dp[hidx,end]=max(nums[hidx]+rob(hidx+2,end),rob(hidx+1,end))
            return dp[hidx,end]
        n=len(nums)
        if n==1:
            return nums[0]
        # dp={}
        # return max(rob(0,end=n-2),rob(1,end=n-1))
        '''
              s   e
              0 1 2  3     
              9 2 3  8
        0  0  9 9 12 .       
           r2 r1 a     

            1   2   3
         0  0   .   .
         r1 r2  a
        '''
        def rob(start: int, end: int) -> int:
            r2=r1=0
            ans=None
            for i in range(start,1+end):
                ans=max(r1,r2+nums[i])
                r2,r1=r1,ans
            return ans
        return max(rob(0,n-2),rob(1,n-1))