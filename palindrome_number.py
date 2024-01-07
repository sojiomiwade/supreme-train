'''
1234
1234 % 10 = 4
div = 123
123 % 10 = 3

ans=1
ans=ans*mod

4 * 10 +3
ans=432
4*10**0 + 

ans starts from 0. for each mod, first multiply 10 into ans, then add mod
12345   +   6

does 12345 > int_max//10
123450 + 6 
int_max = 123458
6 compare to 8. not greater, so ok here.
compare int_max%10 with mod. if greater, we have overflow!

that's for positive. 
-ve has its intmax one more, so remember that, and wait! for -ve, it's always just false LOL
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        orig_x=x
        ans,INT_MAX=0,2**31-1
        while x:
            mod=x%10
            x//=10
            if ans>INT_MAX//10 or (ans==INT_MAX//10 and mod>INT_MAX%10):
                return False
            ans*=10
            ans+=mod
        print(ans,orig_x)
        return ans==orig_x