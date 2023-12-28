'''
search 8
6 7 8 0 1 2 3 4 5
l
        m     
                h

1 7 0
l
  m
h


0 8
l
m
  h

8 0
l
m
  h

check mid and return if it is key
otherwise, check mi+1 to h is sorted. 
if it isn't, then we must look for key in [lo,mid-1]
    if it isn't there, set lo to mid + 1
    else, set hi to mid -1
if [mi+1,hi] is sorted
    if it is here, set lo to mi+1
    else set hi to mi-1
return -1

    0 7 
    l
    m
   h
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo,hi=0,len(nums)-1
        while lo<hi:
            mi=lo+(hi-lo)//2
            if nums[mi]==target:
                return mi
            if nums[mi+1]<=nums[hi]:
                if nums[mi+1]<=target<=nums[hi]:
                    lo=mi+1
                else:
                    hi=mi-1
            else:
                if nums[lo]<=target<=nums[mi]:
                    hi=mi-1
                else:
                    lo=mi+1
        return -1 if nums[lo]!=target else lo
