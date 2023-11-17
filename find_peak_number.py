'''
don't lose track of the problem 
Find Peak Element
A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, where all adjacent values are different, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

Example 1:

Input: nums = [1,2,3,1,5]
Output: 2


Example 2:

Input: nums = [1,2,1, 3 ,5,6,4] = 3
Output: 5

4321 3 56789
4321 3 54321

4396 3 24391
4316 3 24391

4316 9 24391

binary search
if middle is peak return
otherwise, bisect in direction that has bigger element

mi = bsearch(lo, hi)
left, right = 
if left
    bisect left
else    
-inf  ? ? ? ? ? ?  6    3    7
                       mid
-inf  11 10  9  8  7 6  3


go through 3-tuples, and if middle is bigger than left and right, return middle's idx immediately
for i in range(2, n):
    left = a[i-2]
    middle = a[i-1]
    right = a[i]   
time: n, space: 1


binary search
if middle is peak return
otherwise, bisect in direction that has bigger element
'''

from typing import List


def peak(arr: List[int]):
    n = len(arr)
    lo, hi = 0, n - 1
    while lo <= hi: # 01 2 34
        mi = lo + (hi - lo) // 2        # 2
        left = right = float("-inf")    
        if mi - 1 >= 0:             
            left = arr[mi - 1]          # 1
        if mi + 1 < n:
            right = arr[mi + 1]         # 3
        if arr[mi] > max(left, right):
            return mi
        if left > right:
            hi = mi - 1
        else:
            lo = mi + 1
    return None
# 12315
# 01234
arr = [1,2,3,1,5]
print(peak(arr)) # 3, 5 # --> 2 from code

# 12015
# 01234
arr = [1,2,0,1,5]
print(peak(arr)) # 3, 5 # --> 1 from code

arr = [1,2,1, 3 ,5,6,4]
print(peak(arr)) 

'''
1, 2, 1, 3, 5, 6, 4
lo       mi       hi
l=1
r=5
c=3
boundary: l=r=-inf, which could change if the bounds exist
raise error if none found
'''
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def findpeak(lo,hi):
            while lo <= hi:
                l=r=float('-inf')
                mi=lo+(hi-lo)//2
                if mi-1>=0:
                    l=nums[mi-1]
                if mi+1<n:
                    r=nums[mi+1]
                c=nums[mi]
                if c > max(l,r):
                    return mi
                if l > r:
                    hi=mi-1
                else:
                    lo=mi+1
            raise ValueError('no peak')

        n=len(nums)
        return findpeak(0,n-1)