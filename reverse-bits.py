'''
first; can use another integer for ans, and mask from the 32-th bit
100111
100000 mask
000001 comp-mask
000000 ans

if val != 0 then comp-mask can be used to set the bit in ans
comp-mask and mask are updated unconditionally each iteration
ans may or may not get |= of the comp, depending on the n&mask != 0 cond

now if n is -ve, then make ans -ve:
    000-1101
   |111-0000 = -1 << 32

11111-1010
      0010 m
      0100 cm  
      0101 ans
ans=0101 !!!!!

1000=2**8 (4 bits)
(32 bits)->2**(31)
1111=-1
1110=-2
possibly just one integer possible with swapping.
'''
class Solution:
    def reverseBits(self, n: int) -> int:
        ans=0
        mask,compmask=1,2**31
        for _ in range(32):
            if n&mask!=0:
                ans|=compmask
            mask<<=1
            compmask>>=1
        if n<0:
            return (-1<<32)|ans
        return ans