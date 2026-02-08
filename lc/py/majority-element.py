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
# 0010 -- 
# go through each number to see if bit i is set: n & mask != 0
# if more numbers than the floor have it set, then: 
# ans gets that bit set. 1001(1)01: ans |= mask
# for each bit i, for each number
# 1010010 
# mask shift by 1 to the right [31] times
# -2  -3  -2
# 110 101 110
# mask 100
# n    010
# count 1
#    ....     
# ans 1xx
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        mask = 1
        for _ in range(32):
            count = 0
            for num in nums:
                if num & mask != 0:
                    count += 1                
            if count > n//2:
                ans |= mask
            mask <<= 1
        if (1 << 31) & ans != 0:
            ans |= (-1 << 32)
        return ans