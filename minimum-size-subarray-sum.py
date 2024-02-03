'''
>=target
could do it in O(n**2) by considering all l,r l<r

cursum=0
for r in [0..n-1]
    cursum+=nums[r]
    while cursum >=target 
        L,R=l,r if l,r is smaller
        cursum-=nums[l]
        l+=1
return R-L+1 if L is not -inf else 0
1 3 -7 5 1 -3 4 . . .
       L      R

target = 2
1 3 -7
     l
     r
cs=0
L,R=1,1
'''
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L,R=float('-inf'),float('inf')
        cursum,n,l=0,len(nums),0
        for r in range(n):
            cursum+=nums[r]
            while cursum>=target: 
                if r-l<R-L:
                    L,R=l,r
                cursum-=nums[l]
                l+=1
        return R-L+1 if L != float('-inf') else 0
        