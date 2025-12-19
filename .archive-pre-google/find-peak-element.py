'''
1 2 1 3 5 6 4
  p       p      
use binary search with invariant that if we don't have a peak
then we going where the peak is guarantees we will have an ans
'''
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n=len(nums)
        lo,hi=0,n-1
        INTMIN=-2**31
        while lo<hi:
            mi=lo+(hi-lo)//2
            lval=nums[mi-1] if mi>0 else INTMIN
            rval=nums[mi+1] if mi<n-1 else INTMIN
            mval=nums[mi]
            if mval>max(lval,rval):
                return mi
            if lval>rval:
                hi=mi-1
            else:
                lo=mi+1
        return lo
        