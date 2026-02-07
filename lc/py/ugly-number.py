# -ve is not ugly
# 14 -- 7 not ugly
# div out all the 2 3 5
# if not left with 1, then it is not ugly. 
# otherwise it is ugly
# ug 3
# n 1
# mod 1
class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        ugs = [2, 3, 5]
        for ug in ugs:
            while n % ug == 0:
                n //= ug
        return n == 1