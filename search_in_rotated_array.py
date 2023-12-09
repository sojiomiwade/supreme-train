func call(lo, hi, x)
  if a[lo] < a[mi]
    slo, shi = lo, mi
    ulo, uhi = mi+1, hi
  else
    slo, shi = mi+1, hi
    ulo, uhi = lo, mi

  if slo<=x<=shi
    return call(slo, shi,x)
  return call(ulo, uhi,x)'''
x = 2
5 6 0 1 | 2 3 4
2 3 | 4 
2 | 3
slo,shi: 01
ul, uhi: 22
look in sorted half for the element; use that to pick the half that has the element. 
lg n time + constant space 
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo,hi=0,len(nums)-1
        while lo < hi:
            mi = lo + (hi-lo)//2
            slo,shi = lo,mi 
            ulo,uhi=mi+1,hi
            if nums[lo]>nums[mi]: 
                slo,shi=mi+1,hi
                ulo,uhi=lo,mi
            if nums[slo]<=target<=nums[shi]:
                lo,hi=slo,shi
            else:
                lo,hi=ulo,uhi
        return -1 if nums[lo]!=target else lo
'''
[4,5,6,7,0,1,2]
 0 1 2 3 4 5 6
0 6
4 6 0,1,2
6 6
'''class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        3 1
        l
          r
        m  
        '''
        l,r=0,len(nums)-1
        while l<=r:
            m=l+(r-l)//2
            if nums[m]==target:
                return m
            if nums[l]<=nums[m]:
                if nums[l]<=target<nums[m]:
                    r=m-1
                else:
                    l=m+1
            else:
                if nums[m]<target<=nums[r]:
                    l=m+1
                else:
                    r=m-1
        return -1
