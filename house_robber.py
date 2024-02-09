'''
1 2 3 1
ans = 4

1 2 3 1 9 12
ans = ...
use a tree. 
    take current house, skip the next, and rob 2 down 
    rob the next (which will recursively cauze )
                                r(2)
                      2 /               \
                   r(9)                   r(7)
                 /     \           7 /           \
              r(1)     r(3)              7+r(3)        r(3)
amount take   

dp[idx]=
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob(idx: int) -> int:
            if idx >= len(nums):
                return 0
            if idx in dp:
                return dp[idx]
            dp[idx]=max(nums[idx]+rob(idx+2),rob(idx+1))
            return dp[idx]
        dp={}
        return rob(0)