'''
nums -2 1 -3 4 -1 2 1 -5 4
dp   -2 1 -2 4  3 5 6  1 5 
return max of dp
can skip dp array, using a prev val instead
init maxsum to -inf, and update it to max(maxsum,rsum)
where rsum for that iteration is max(0,rsum)+nums[i]

5 4 
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        rsum=maxsum=float('-inf')
        for num in nums:
            rsum=max(0,rsum)+num
            maxsum=max(maxsum,rsum)
        return maxsum