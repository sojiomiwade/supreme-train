'''
first find the min. then set lo and hi based on whether target is in
4 5 6 7 8 0 1 2 3
minidx...n-1
0..minidx-1

, or min+1..n
0 1 2 3 4
'''

'''
4560

4,5,6,7,0,1,2
            m 
0           n-1

1. find the min 
2. now set l,r depending on if target is between [0..minidx-1] [minidx..n-1]
3. do a bfs on l,r for target

findmin:
-2|1|2|3
midx
l  r
2|3|1
3(1)2
min 
breakage: 
if right inclusive of mid is unsorted keep [mididx+1..right]
otherwise  keep [left...mididx]

target = 0
0 1 2 3 4 5 6 | 7 8 9 10 11 12 13 14      
4,5,6,7,0,1,2 | 4,5,6,7      X
          l r

'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        left,right=0,len(nums)-1
        while left<right:
            mid=left+(right-left)//2
            if not nums[mid]<nums[right]:
                left=mid+1
            else:
                right=mid
        minidx=left
        left,right=minidx,minidx-1+n
        while left<=right:
            mid=left+(right-left)//2
            if nums[mid%n]==target:
                return mid%n
            elif nums[mid%n]<target:
                left=mid+1
            else:
                right=mid-1
        return -1



