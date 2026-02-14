# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
	return False
# 1 2 3 4 5 6 7
# g g g g b b b
# v 4 | 6 | 5
# rem 6
# lo <= hi
# 1   2  3
# g   b  b
# h   l 
# rem 2
class Solution:
    def firstBadVersion(self, n: int) -> int:
        lo, hi = 1, n
        rem = -1
        while lo <= hi:
            mi = lo + (hi - lo) // 2
            if isBadVersion(mi):
                rem = mi
                hi = mi - 1
            else:
                lo = mi + 1
        return rem
