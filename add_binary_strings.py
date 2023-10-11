'''
  1
 1010
   11
 1101

1 1
1 0
0 1 
iterate from back
get a char and b char (set them to zero if they don't exist)
on next iteration have carry ready
return string from the list

0 + 1 + 1  
11
 11
  1
 00
'''
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        carry = 0
        ai = len(a)-1
        bi = len(b)-1
        while carry or ai >= 0 or bi >= 0:
            aval = bval = 0
            if ai >= 0:
                aval = int(a[ai])
                ai -= 1
            if bi >= 0:
                bval = int(b[bi])
                bi -= 1
            res += [((carry+aval+bval)%2)] # 3 // 2 = 1
            carry = (carry+aval+bval)//2
        return ''.join(['1' if res[i] else '0' for i in range(len(res)-1,-1,-1)])
