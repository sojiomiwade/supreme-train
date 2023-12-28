'''
1  0
lm h

0  1
lm h
h=m

0 1 7
l m h
h=m

1 7 0
l m h

so always check the right, so iin a sorted array if the right is ok, you move to the left towoard the 0

6 7 8 0 1 2 3 4 5
      l
      m   
      h

high jumps on mid
but lo must go to mid+1 to avoid not moving
terminate when l=h => loop as long as l<h

8 0 1
  l 
  m 
  h
'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo,hi=0,len(nums)-1
        while lo<hi:
            mi=lo+(hi-lo)//2
            if nums[mi]<nums[hi]:
                hi=mi
            else:
                lo=mi+1
        return nums[lo]