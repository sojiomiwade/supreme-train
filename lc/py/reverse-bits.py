# 011010

# 011 -- n
# 000 -- np
# 110 -- ans

#  ans

# 01

# 01

# ans = 0
# repeat 2 times
#   get last digit from n
#   apply it to ans -- add 1 or not depending on if n is even or odd
#   shift ans to left
#   shift n to right

# n 011
# n 000
# a 110
class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for _ in range(31):
            if n % 2 == 1:
                ans += 1
            ans <<= 1
            n >>= 1
        return ans