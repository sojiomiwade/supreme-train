'''
8
0 1 | 2 | 3 | 4 5 6 7 8
ans 2
do a bisection search. 
find nums[mi]*nums[mi]
if bigger than target, move hi to mi-1
otherwise set ans to this, and move lo to mi + 1
break when lo crosses hi

0
l
m
h
0 1 2 | 3 4
ans 2
       
'''
class Solution:
    def mySqrt(self, x: int) -> int:
        lo,hi=0,x
        ans=None
        while lo<=hi:
            mi=lo+(hi-lo)//2
            square=mi*mi
            if square>x:
                hi=mi-1
            else:
                ans=mi
                lo=mi+1
        assert ans is not None
        return ans