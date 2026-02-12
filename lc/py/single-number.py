# 1 4 2 1 2
# xor maybe? 
# 000
# 001
# 001
# 100
# 101
# 010
# 111
# 001
# 110
# 100
# just xore them all!

# another approach
# 1 2 1
# ans 10
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            ans ^= num
        return ans