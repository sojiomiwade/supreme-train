'''
9,8,2,5,3,7,101,18
0 0 0 1 2 

0 1 9 8 2 3 4 5

0 1 0 1 7
init all to one to start with

outer loop goes from last to first: i: n-1 .. 0
    inner loop leverages dp if it can: j > i
    inner loop find j such that a[j]>a[i]
    then set dp[i] to 1+dp[j] 

nums 0 1 0 3 2 3
dp   1 1 3 1 2 1
         i
             j
'''
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[1]*n
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                if nums[j]>nums[i]:
                    dp[i]=max(dp[i],1+dp[j])
        return max(dp)