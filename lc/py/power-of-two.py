#   010010000
# - 000000001 | 1
#   010001111 | n-1
# & 010010000 | n
#   010000000 | n & (n-1) != 0

#   010000001 != 1

#   00001000
# - 00000111
  
# 1
# 0
# 1 == 1 ok

#   000
# - 111
#   001 should not be ok and negatives too!   
# 011
# 010
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        return n & (n-1) == 0