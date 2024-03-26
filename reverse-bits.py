class Solution:
    def reverseBits(self, n: int) -> int:
        return int('0b'+''.join(reversed(bin(n)[2:].zfill(32))),base=0)