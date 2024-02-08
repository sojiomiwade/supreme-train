class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[1 for _ in range(n)]
        for right in range(n):
            for left in range(right):
                if nums[right]>nums[left]:
                    dp[right]=max(dp[right],1+dp[left])
        return max(dp)
