'''
123
3
30 + 2
320 + 1
#assume +ve for now
y = 0
isneg = 1
if x is neg
    x = -x
    isneg = -1

y = 98 => return 0; it will become 980 > 267
y = 26
y = 25 => totally ok
foo = 2^31 - 1 # 267
while x > 0 
    digit = x % 10
    x //= 10
    if y > foo
        return 0
    if y == foo and digit > 7
        return 0
    y *= 10 
    y += digit
return y * isneg

be careful when num is neg!!!
'''
class Solution:
    def reverse(self, x: int) -> int:
        y = 0
        isneg = 1
        if x < 0: 
            x, isneg = -x, -1
        highest = (pow(2, 31) - 1) // 10
        while x > 0:
            digit = x % 10
            x //= 10
            if (y > highest) or (y == highest and ((isneg == 1 and digit > 7) or (isneg == -1 and digit > 8))):
                return 0
            y = y * 10 + digit
        return y * isneg
