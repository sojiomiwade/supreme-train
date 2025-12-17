'''
l,r at ends
if you see 2, move it to back with swap, only advance r backward
if you see 1, just move forward
otherwise, swap with l the cur, move forward and advance l

2 2 2 2
i
l     
      r
1 0 2
  i
l 
  r
'''
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n=len(nums)
        l=i=0
        r=n-1
        while i<=r:
            if nums[i]==2:
                nums[i],nums[r]=nums[r],nums[i]
                r-=1
            elif nums[i]==1:
                i+=1
            else:
                nums[l],nums[i]=nums[i],nums[l]
                l+=1
                i+=1