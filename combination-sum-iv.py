'''
dp[]=dp[]
        0
      1    2
          1
          1
1 1,2,3

7 + {1,2,3}
71 72 73
1111
112
112
'''
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        def cs(rem):
            if rem<=0:
                return int(rem==0)
            if rem in dp:
                return dp[rem]
            dp[rem]=sum(cs(rem-x) for x in nums)
            return dp[rem]
        dp={}
        return cs(target)
        