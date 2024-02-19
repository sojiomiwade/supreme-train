'''
 1010
&1001
 1000
n & (n-1) == 0

 1000
&0111
 0000

0000
1111
0000 --> true ? false

 11110000 --> -16 1000
&11101111
 11100000 --> 
 
-8-1 = -9
-16-1=-17 --> -000010001 --> 111101111
'''
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==0:
            return False
        return n&(n-1)==0