# 2 2 3 1 2 2 1 2 -- 8 
# 010
# 010
# 011
# 001

#   0000|11011 --> 
# | 1111|00000
# -------------

# 111111110000 --> 
# 000000001111 --> 32 
# 1:2 2:5 3:1 -- O(n) time and space
# could use a dictionary counter
# go through each number to see if bit i is set more than the floor, if so 
# ans gets that bit set.
# for each bit i, for each number
# 1010010 
# mask shift by 1 to the right 31 times
from counter import Counter
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums)
        mv = max(c.values())
        for i in c:
            if c[i] == mv:
                return i
        raise Exception("should not be here!")
