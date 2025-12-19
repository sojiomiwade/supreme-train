'''
48
000001001010
010100

1010 -x
0101

011
110 --> 111...110

so if the last bit is a 1 then pad the ans with 111...
    000000|101100
    111111|000000
ans|=(-1<<32) when last bit is 1
always shift, but add one if the mask is zero

input n 011 --> 110 = -6
n 000
ans 110
i 0..2 1
ans_is_neg 1

000110
111000
   
111|101

11101 --> 11 = -3
11110

11101

'''
class Solution:
    def reverseBits(self, n: int) -> int:
        ans=0
        for _ in range(32):
            ans<<=1
            ans+=(n&1)
            n>>=1
        return ans