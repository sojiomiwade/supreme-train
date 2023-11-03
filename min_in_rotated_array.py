'''
code time: 10:13 -- 10:32 --> 19 mins

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

 

Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
Example 3:

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
 

Constraints:

n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
All the integers of nums are unique.
nums is sorted and rotated between 1 and n times.

time: ...
complexity: 

[4,5,6, 7,0,1,2]
7,0, 1,2
7,0 <-- default to the right of split when both sorted

another example: 
0 1 2 3 4 <-- dont even bother we are done

another example
3 4 1 2 <-- default to the right of split when both are sorted

key observation: after splitting arr into two, the min element is in the one where a[first] > a[last]
algorithm: arr:
    func rot(arr, lo, hi)
        if arr's first < arr's last
            return arr's first
        check arr[:mid+1] and arr[mid+1:]
        set lo and hi to either array depending on key observation

'''
from typing import List

def rot(arr: List[int]) -> int:
    return helper(arr, 0, len(arr)-1)

'''
4 5 ok

5    4 ok
l,m  h 
'''
def helper(arr: List[int], lo: int, hi: int) -> int:
    if arr[lo] <= arr[hi]:
        return arr[lo]
    mid = (lo+hi) // 2
    if arr[lo] <= arr[mid]:
        return helper(arr,mid+1,hi)
    return helper(arr,lo, mid)

arr = [5,4]
print(rot(arr)) # 4
arr = [4,5]
print(rot(arr)) # 4

arr = [4,5,6, 7,0,1,2]
print(rot(arr)) # 0
arr = [11,13,15,17]
print(rot(arr)) # 11




'''
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. Given the sorted rotated array nums of unique elements, return the minimum element of this array.

assumes uniquness in elements
'''

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        there is an issue because a[lo] > a[hi]
        issue could be in either place.
        min element is with the issue
        note no issue in sorted 2 element case
        so to not get rid of the minimum, check the right
        for ok-ness. if so
        take array where a[lo] > a[hi]

        if no issue in both pick min from both left
        if issue, only one will have issue and that has the min
            => we have to keep that one

        0 1 2 | 4 5 6 7: left
        4 5 6 7 | 0 1 2: 
        7 0 | 1 2       :
        7 | 0           :right
        4 5 6 7 | 9 0 1 2: right...


        0 1 2 3 | 4 5 6: left
        6 0 1 2 | 3 4 5
        6 0 | 1 2

        0 | 7

        0 1 | 2 ->> if left arr is fine, answer is in right

        if only one element, just return it. =>
        now we have more than 1:
            if no issue in both pick min from both left
            if issue, only one will have issue and that has the min
                => we have to keep that one

        '''
        if not nums:
            raise ValueError('need numbers in input')
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mi = lo + (hi - lo) // 2
            okleft, okright = nums[lo]<nums[mi], nums[mi+1]<nums[hi]
            if okleft and okright:
                return min(nums[lo],nums[mi+1])
            if okleft:
                lo = mi + 1
            else:
                hi = mi
        return nums[lo]


nums = [4,5,6,7,0,1,2]
print(Solution().findMin(nums)) # 0

nums = [3,4,5,1,2]
print(Solution().findMin(nums)) # 1

nums = [3]
print(Solution().findMin(nums)) # 3

nums = []
print(Solution().findMin(nums)) # ValueError
