class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        agg=1
        ans=float('-inf')
        for i,x in enumerate(nums):
            if i-1>=0 and nums[i-1]==0:
                agg=x
            else:
                agg*=x
            ans=max(ans,agg)

        n=len(nums)
        # . 0 .
        # 0 1 2
        agg=1
        for i,x in enumerate(reversed(nums)):
            if i-1>=0 and nums[n-i]==0:
                agg=x
            else:
                agg*=x
            ans=max(ans,agg)

        return ans