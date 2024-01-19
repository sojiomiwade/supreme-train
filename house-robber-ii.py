#rob(i)= nums[i]+rob(i+2) OR rob(i+1)
#pass back inf if (i)first_is_there and (ii)i==n-1
# 1 2 3 4
class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob(hasfirst: bool, hidx) -> int:
            if hidx>n-1 or (hidx==n-1 and hasfirst):
                return 0
            if (hasfirst,hidx) in dp:
                return dp[hasfirst,hidx]
            dp[hasfirst,hidx]=max(rob(hasfirst,hidx+2)+nums[hidx],rob(hasfirst,hidx+1))
            return dp[hasfirst,hidx]

        n=len(nums)
        dp={}
        return max(rob(True,2)+nums[0],rob(False,1))
        