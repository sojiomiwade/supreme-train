'''
time 2:09 -- 2:21 = 12
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false


Constraints:
1 <= nums.length <= 10**5
-10**9 <= nums[i] <= 10 ** 9

0111 -> 7
6  5 6
10**9 < 2 ** 30 so we can use an int
if all bits set, the value will be 2 ** 32 - 1
1 2 3 1 -> true

1 2 3 4 -> false

could sort and see if two neighbors are the same: n lg n, n or 1
could just use set and return true if you find it again: n, n
could use a bit vector to represent you have a number: n, 1
    10 -> have 2: 
    set the numb's bit
    if the bit is already set, return true
go with bit vector

'''
from typing import List


def contains_duplicate(arr: List[int]) -> bool:
    return len(set(arr)) != len(arr)

arr = [1,2,3,1]
print(contains_duplicate(arr)) # true
arr = [1,2,3,4]
print(contains_duplicate(arr)) # false


'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

Constraints:
1 <= nums.length <= 10**5
-10**9 <= nums[i] <= 10 ** 9


time: 12:51 -- 1:01 = 10 mins

approach 1
sort; compare neighbors for increasing: time = n lg n, space = n
approach 2
use set; then if for any element curr is in set return true. otherwise return false: time: avg n; could be n**2, but unlikely space: n
'''
from typing import List


def contains_duplicate(arr: List[int]) -> bool:
    seen = set()
    for element in arr:
        if element in seen:
            return True
        seen.add(element)
    else:
        return False

arr = [1,2,3,1]
print(contains_duplicate(arr)) # true
arr = [1,2,3,4]
print(contains_duplicate(arr)) # false
arr = [1,1,1,3,3,4,3,2,4,2]
print(contains_duplicate(arr)) # true
arr = [1]
print(contains_duplicate(arr)) # false

