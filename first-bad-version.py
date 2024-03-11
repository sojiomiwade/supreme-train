# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
'''

1 2 3 4 5 6 7
f f f f t t t
must squeeze the range to zero and remember the last bad version
if good version, lo gets mid + 1. otherwise hi gets mid -1
1 2 3 4
t t t t
ans 1
'''
class Solution:
    def firstBadVersion(self, n: int) -> int:
        ans=None
        lo,hi=1,n
        while lo<=hi:
            mi=lo+(hi-lo)//2
            if isBadVersion(mi):
                ans=mi
                hi=mi-1
            else:
                lo=mi+1
        assert ans is not None
        return ans
        