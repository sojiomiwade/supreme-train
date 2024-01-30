'''
0 0 0 1
0 1 0 0
  ^   ^
order matters, can't just get the next bit
use power of 2 instead of mask to get the next one
and do this 32 times
cur bit of x is x & 1
advance x is x>>1

'''
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count=0
        while x or y:
            if x&1!=y&1:
                count+=1
            x>>=1
            y>>=1
        return count

        