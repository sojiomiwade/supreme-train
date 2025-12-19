'''
1100
1011
repeat n&(n-1) until it is 0. that's the ans

for -ve numbers it may be more interesting in python
got it. first off, leave only last 32 bits via a mask,
     then we can proceed as usual
n 1..1011
mask 10000 -> 01111
1000

1..1011
  01111

1111
1110
111
0001
'''
class Solution:
    def hammingWeight(self, n: int) -> int:
        mask=(1<<32)
        mask-=1
        n=mask&n
        count=0
        while n:
            n&=n-1
            count+=1
        return count