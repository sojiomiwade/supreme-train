# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
'''
bin search
1 2   3 4 5 6 7
f t   f t t t t
ans=-1
if not bad, move lo to mi+1
else ans=mi, then move hi to mi-1
return ans
0 1 2
'''
class Solution:
    def firstBadVersion(self, n: int) -> int:
        ans=-1
        lo,hi=1,n
        while lo<=hi:
            mi=lo+(hi-lo)//2
            if isBadVersion(mi):
                ans=mi
                hi=mi-1
            else:
                lo=mi+1
        assert ans!=-1
        return ans