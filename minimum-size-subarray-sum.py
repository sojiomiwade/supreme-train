'''
2,3,1,2,4,3,2 2
        l
          r
7
ans=2
when sum is too big, increment l until it's too small => while loop on l
but do check at l or r if we get the sum. 
2 4 3
  l
    r
cur,ans=7,2
target=7

1,2,3,4,5
l
r
cur,ans=0,0
target=7
'''
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left,n=0,len(nums)
        ans=1+n
        cur=0
        for right in range(n):
            cur+=nums[right]
            while cur>=target:
                ans=min(ans,right-left+1)
                cur-=nums[left]
                left+=1
        if ans==1+n:
            return 0
        return ansquote> 2 1 -4 4 7
quote> 2 3 -1 4 11
quote> l resets when prev is rejected
quote> when nums[i] is negative or nums[i] or , update minsize_maxl and minsize_maxr with l and r-1
quote> prev is rejected when nums[i-1] is <=0 
quote> minsize_maxr and minsize_maxl are changed only if cursum is bigger than maxsum
