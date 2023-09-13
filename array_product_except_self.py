'''
6      2      3       4
|234   6|34    62|4    623|

ans init to array of 1s
for i in [1:n]
    ans[i] = ans[i-1] * nums[i-1]
for i in [n-2:-1]
    ans[i] *= nums[i+1]
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1 for _ in range(n)]
        accum = 1
        for i in range(n):
            ans[i] *= accum
            accum *= nums[i]
        accum = 1
        for i in range(n-1,-1,-1):
            ans[i] *= accum
            accum *= nums[i]
        return ans

