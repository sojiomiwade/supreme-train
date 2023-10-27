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


# reverse int again -- 17 min
'''
reverse integer while avoiding overflow
if overflow will occur return -1

num = 2318, res = 8132
pull from the back with % to get last, and // to chop off last
for overflow, 

res about to be 649
curr 64
64 > maxint //
'''
def reverseint(num: int) -> int:
    res = 0
    maxint = 2**31-1
    while num:
        lastdigit = num % 10
        if res>maxint // 10 or (res == maxint//10 and lastdigit > 7):
            return -1
        res *= 10
        res += lastdigit
        num //= 10
    return res

num = 2318
print(reverseint(num)) #8132
num = 2
print(reverseint(num)) #2
num = 2**31 - 1 # 011 = 2
print(reverseint(num)) # -1
num=7463847412
print(reverseint(num)) # 2147483647
num=8463847412
print(reverseint(num)) # -1
class Solution:
    def reverse(self, x: int) -> int:
        '''
        1234
        4321
        keep adding to res 10*res +module(x), then dividing x  by 10
        at some point res * 10 is more than max_int or if not
        10res + mod is more. 
        (1) 10res > max_int => res > max_int//10
        below x is the 10res which less than max int now
        (2) also x + mod > max_int => x > max_int - mod
        for negative how to do this? max_int can be one more! this applies just to (2)

        max_int = 1235
        res = 12

        res = 123
        123*10 = 1230
        123 <-> 123
        res = 154
        154*10 = 1540
        154 <-> 123 violation

        max_int=232...7
        123
        mod=2
        x=1
        res=32
        320 + 1
        32 > max_int//10
        33 > 32
        '''
        res = 0 #
        isneg = True if x < 0 else False
        x = abs(x)
        max_int = (2**31-1)
        max_int_div10 = max_int // 10
        max_int_mod = max_int % 10
        while x > 0:
            mod = x % 10
            x //= 10
            if res > max_int_div10 and 10*res > max_int_mod+int(isneg)-mod:
                return 0
            res = 10*res + mod
        return -res if isneg else res 
        class Solution:
    def reverse(self, x: int) -> int:
        '''
        1234
        4321
        keep adding to res 10*res +module(x), then dividing x  by 10
        at some point res * 10 is more than max_int or if not
        10res + mod is more. 
        (1) 10res > max_int => res > max_int//10
        below x is the 10res which less than max int now
        (2) also x + mod > max_int => x > max_int - mod
        for negative how to do this? max_int can be one more! this applies just to (2)

        max_int = 1235
        res = 12

        res = 123
        123*10 = 1230
        123 <-> 123
        res = 154
        154*10 = 1540
        154 <-> 123 violation

        max_int=232...7
        123
        mod=2
        x=1
        res=32
        320 + 1
        32 > max_int//10
        33 > 32

        2143, 2159, 2156, 2161<--> 2158
        2150 + 9 > 
        '''
        res = 0 #
        isneg = True if x < 0 else False
        x = abs(x)
        max_int = (2**31-1)
        max_int_div10 = max_int // 10
        max_int_mod = max_int % 10
        while x > 0:
            mod = x % 10
            if res > max_int_div10 or (
                res==max_int_div10 and mod >  max_int_mod + isneg):
                return 0
            res = 10*res + mod
            x //= 10
        return -res if isneg else res 
        