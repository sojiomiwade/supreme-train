'''
7:10 - 7:19?
[0 1 2 4]
0     3

  0 1 2 4 3
  0 1 2 4

[1]
0 ^ 1 ^ 1
[0]
0 ^ 1 ^ 0
'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(1, len(nums) + 1):
            res ^= i ^ nums[i-1]
        return res

# again, but propagate the difference
'''
abcd, abcde

0123

1 2 3
0 1 2 3

1 0 0 1
3 0 0 3 = 0

3 5 3
0 1 1
1 0 1
0 1 1
1 0 1   

02
12
res=0
'''
from typing import List


def missing_number(arr: List[int]) -> int:
    res = 0
    for i in range(1, 1 + len(arr)):
        res += i - arr[i - 1]
    return res

arr = [1,2,3]
print(missing_number(arr)) # 0
arr = [0,1]
print(missing_number(arr)) # 2

