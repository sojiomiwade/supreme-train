'''
0123|456
7012|456
1245|670

12|3
23|1
32|1

0124|567
l

      r
0..9
9..0


l
m
 h
if left is sorted 
as long as the range is defined, if both left and right 
arrays are sorted, the min is the min of the two left ends
otherwise:
01
90
 l
m
 r
'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        discard the right (will keep mid) if mid to right is sorted.
        otherwise, use the right (won't keep mid)
        note we then search on l<r, and return nums[l]
        '''
        l,r=0,len(nums)-1
        while l<r:
            mid=l+(r-l)//2
            if nums[mid]<=nums[r]:
                r=mid
            else:
                l=mid+1
        return nums[l]