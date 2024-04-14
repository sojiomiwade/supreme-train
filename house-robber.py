'''
need to do the tabulation here
     2 7 9        3        1
0 0  2 7 9+2      11        12

rob[i] is me+rob of two prior, or it's just one prior

             i
         0 1 2 3 
nums     1 2 3 1
dp   0 0 1 2 4 4 
         
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[0 for _ in range(2+n)]
        for i in range(n):
            dp[i+2]=max(nums[i]+dp[i],dp[i+1])
        return dp[-1]