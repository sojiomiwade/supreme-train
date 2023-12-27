class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l=rsum=0
        msum=float('-inf')
        bl=br=None
        for i,x in enumerate(nums):
            if rsum<0:
                rsum=0
                l=i
            rsum+=x
            if rsum>msum:
                msum=rsum
                bl,br=l,i
        assert msum==sum(nums[i] for i in range(bl,br+1))
        return msum