class Solution:
    def hammingWeight(self, n: int) -> int:
        mask = 1
        res = 0
        for _ in range(32):
            res += (n & mask) != 0
            mask <<= 1
        return res