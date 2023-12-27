class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def msa(lo,hi):
            if lo>hi:
                return float('-inf')
            mi=lo+(hi-lo)//2
            lsum=msa(lo,mi-1)
            rsum=msa(mi+1,hi)
            lhalf=rhalf=ml=mr=0
            for i in range(mi-1,lo-1,-1):
                lhalf+=nums[i]
                ml=max(ml,lhalf)
            for i in range(mi+1,hi+1):
                rhalf+=nums[i]
                mr=max(mr,rhalf)
            return max(lsum,rsum,ml+nums[mi]+mr)
        return msa(0,len(nums)-1)