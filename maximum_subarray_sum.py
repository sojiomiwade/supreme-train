'''
could use brute force for all i,j with i <= j with O(n**2), O(1)
res = 5
-2  1 -2  4  3  5  6  1  5
-2, 1,-3, 4,-1, 2, 1,-5, 4
-2  1 -2  4  3  5  6  1  5

nums: -2, 1,-3, 4, -1  2
dp:   -2  1 -2  4   3  5
res = 4
exp(res) = 3
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [None for _ in nums]
        res = dp[0] = nums[0]
        for idx in range(1, len(nums)):
            dp[idx] = max(nums[idx], dp[idx - 1] + nums[idx])
            res = max(res, dp[idx])
        print(dp)
        return res

