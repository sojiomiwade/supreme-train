'''
-2 1 -3 4 | -1 2 1 -5 4 
going from the middle in any direction, there is a greatest sum you can get
that is the allleft (or allright)
10
5 5
3 3 3 3
1 1 1 1 
n + n + ... + n = nlgn
go
msa=max of (left half, right half, whole thing)

-2 | -1

'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def msa(lo: int, hi: int) -> int:
            if lo>hi:
                return 0
            if lo==hi:
                return nums[lo]
            mi=lo+(hi-lo)//2
            left,right=msa(lo,mi),msa(mi+1,hi)
            cur,thisleft=0,-INF
            for i in range(mi,lo-1,-1):
                cur+=nums[i]
                thisleft=max(thisleft,cur)
            cur,thisright=0,-INF
            for i in range(mi+1,hi+1):
                cur+=nums[i]
                thisright=max(thisright,cur)
            return max(left,right,thisleft+thisright)
        INF=float('inf')
        return msa(0,len(nums)-1)