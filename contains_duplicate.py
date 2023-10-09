'''
7:46 -- 
1,1,1,3,3,4,3,2,4,2 -> true
could use map and see if map[idx] > 1 for any => truee; false otherwise: O(n), O(n)
could sort; then if neighboring is the same anytime => true; false otherwise: O(n lg n), O(n)
could use array of bit vector as hash table? yes constant size of ~ 1GB: O(n), O(1)

0 - 31    idx 0
31 - 63   idx 1
64 - 95.  idx 2
64 5 6 7 8 9
0  1 2 3 4 5
...
0000
69 --> 69//32 = 2; 69%32 = 69-64 =5 <-- exact bit we need 2 set
10**9 ~ 2**30
then div by 4
~  10**9 B elements  *  1 slot/4B  *  1B/32 elements = 
781 + 1 <-- size == 782

2 3 -> False
2 2 -> True

2 // 32 = 0
00000
'''
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        def setbit(num: int) -> None:
            isneg = False
            if num < 0:
                isneg = True
                num = -num
            vidx = num // wordsize_bits
            if isneg:
                vidx += m
            bidx = num % wordsize_bits
            bitvec[vidx] |= (1 << bidx)
        
        def bitset(num: int) -> bool:
            isneg = False
            if num < 0:
                isneg = True
                num = -num
            vidx = num // wordsize_bits
            if isneg:
                vidx += m
            bidx = num % wordsize_bits
            return (bitvec[vidx] & (1 << bidx)) != 0

        wordsize_bits = 32
        largest_num = 10**9
        m = largest_num // wordsize_bits
        # use 2*m to hold negative numbers
        bitvec = [0 for _ in range(2*m)]
        for num in nums:
            if bitset(num):
                return True
            setbit(num)
        return False

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

