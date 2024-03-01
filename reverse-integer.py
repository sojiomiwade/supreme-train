'''
take from the back using modulo and div
if the next one will cause overflow, don't take it. return 0
if can make it to end, return ans

456  <--8
INTMAX 4567 let's say
is 456 > 456 or 8 > 4567%10  ==> YES return 0

457 > 456 yes ==> return 0
=> 4570 > 4567
'''
class Solution:
    def reverse(self, x: int) -> int:
        ans=0
        INTMAX=(1<<31)-1
        IM_DIV10,IM_MOD10=INTMAX//10,INTMAX%10
        xneg=x<0
        x=abs(x)
        while x:
            mod=x%10
            if ans>IM_DIV10 or (ans==IM_DIV10 and mod>(IM_MOD10+xneg)):
                return 0
            ans=ans*10+mod
            x//=10
        return ans * (-1 if xneg else 1)