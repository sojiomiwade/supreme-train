# # 0 1 2 3 4 5 6 7 8
#       l
#       m       
#         h
# prod 4
# x 8
# a 1
class Solution:
    def mySqrt(self, x: int) -> int:
        lo, hi = 0, x
        ans = -1
        while lo <= hi:
            mi = lo + (hi - lo) // 2
            prod = mi * mi
            if prod == x:
                ans = mi
                break
            elif prod < x:
                lo = mi + 1
                ans = max(mi, ans)
            else:
                hi = mi - 1
        return ans