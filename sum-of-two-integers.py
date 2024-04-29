'''
1
010
011
101

1100 -4
1101 -3 1100 -> 3
1001
1001 -7 via 2 comp 1110 -> 7


1101 -3 1100 -> 3
0001  1
1110 -2

...x...
...y...
0001000

carry is or(a,b) and not xor(a,b)
val is xor(a,b)
repeat 32 times starting from the rightmost bit
get the bit val (mask everything away)
then mask the bit val into ans
mask moves from bit0 to bit 31
-7
8
15


 |0010  2
 |1111 -1
  0001
carry 0
mask 1
rc
bm
am
val
'''
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask=1
        carry=0
        ans=0
        for _ in range(32):
            realcarry=mask if carry else 0
            bm,am=b&mask,a&mask
            val=bm^am^realcarry
            carry=sum(bool(x) for x in (bm,am,realcarry))>1
            ans|=val
            mask<<=1
        return ((-1*bool(val))<<32)|ans



