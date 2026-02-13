# need a set: if you see something youve seen b4, return false
# if you hit 1, return true
# 19
# 1 + 9 = 82
# 8 + 2 = 68

# mod, n |  1 1
# ss 1
# have (100 1)
# agg the next n as per the square, until n == 0. then make n the ss -- sum of squares
class Solution:
    def isHappy(self, n: int) -> bool:
        have = set()
        while n != 1:
            ss = 0
            while n != 0:
                mod, n = n % 10, n // 10
                ss += mod * mod
            n = ss
            if n in have:
                return False
            have.add(n)
        return True