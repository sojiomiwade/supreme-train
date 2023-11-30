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
        

#refresh
'''
0101
0110
0011 <-- xy

xord = x^y 
sum_ += xord & 1 and shift xord and do this 31 more times
time: O(1), space: O(1)
'''
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res = 0
        xy = x ^ y
        while xy:
            res += xy & 1
            xy >>= 1
        return res

x, y = 5, 6
print(Solution().hammingDistance(x, y)) # 2
'''
keep shifting and getting the xors of both at the end of the numbers
wait. just xor the two, and count the 1s
time: O(1) since 32 times
space: O(1) since only make one new number and no additional data structures
1001
   1
3210
----
   1

0123
1001
'''
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xy=x^y
        mask=1
        count=0
        for _ in range(32):
            count+=bool(xy&mask)
            mask<<=1
        return count
