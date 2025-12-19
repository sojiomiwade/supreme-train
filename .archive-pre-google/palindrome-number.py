'''
123456
2224222
let us say 
10
40
40f
INTMAX
if at any point agg > INTMAX we are done and no pal
agg > INTMAX//10 and mod > INTMAX%10, ==> false
123  123(7)
8
odd cannot be palindrome, so forget it. 
x=
agg=321
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        INTMAX=2**31-1
        INTMAXMOD10=INTMAX%10
        INTMAXDIV10=INTMAX//10
        origx,agg=x,0
        while x:
            mod=x%10
            if agg>INTMAXDIV10 and mod>INTMAXMOD10:
                return False
            agg=10*agg+mod
            x//=10
        return agg==origx