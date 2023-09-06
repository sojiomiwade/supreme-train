'''
0001
0100
 ^ ^
 stopwatch: 8:15 - 8:33 = 18m
 confirmations: x, y is non-neg int
 examples:
 method: xor each, and count the number of 1s in end result
 mask = 1
 res = x ^ y
rescount = 0
 for i = 0 to 31
    if res & mask != 0:
        rescount ++ 
    mask << 1

analytics:
O(1)

0001
0100
0101
'''
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        mask = 1
        res = x ^ y
        rescount = 0
        for _ in range(31):
            if (res & mask) != 0:
                rescount += 1 
            mask <<= 1
        return rescount
        
