'''
       L    R
2 5 -8 4 5 -3 4 -1
2 7 -1 4 9 7 11 10 
       l
                r
find L,R with maximum sum
don't forget max sum subarray problem: if newsum with me is greater
than me, take me otherwise take new sum. at this point reset l
update L,R always

'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        INF=float('inf')
        l=L=R=None
        LRsum=-INF
        n,cursum=len(nums),0
        for r in range(n):
            if cursum<=0:
                l=r
                cursum=0
            cursum+=nums[r]
            if cursum>LRsum:
                L,R=l,r
                LRsum=cursum
        return sum(nums[i] for i in range(L,R+1))
