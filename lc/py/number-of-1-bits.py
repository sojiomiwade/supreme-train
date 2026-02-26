# 1001000
# 1000111
# 1000000
# as long as n is not 0, increment counter, then n &= n -1
class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n != 0:
            ans += 1
            n &= n-1
        return ans
        