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
