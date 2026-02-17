# 3 0 1 
# 0 1 3 . n = 3 ==> iterate 0...3
# 0 1 2 3

# 3 0 1
# a 0 |3 0 | 0 1 | 1 2 |  3 
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        a = 0
        for i,x in enumerate(nums):
            a ^= x ^ i
        return a ^ (n)