'''
123 -- true
1221 -- true
-121 -- false
10 -- false
bruteforce: check if reversed(x) == x
other: use div and mod to make reversed(x) without going to strings
div approach: keep div-ing until c equals 0
c 0
y 321
check if y equals x
bother bout overflow? 
4321 -- 1234
12345 -- overflow means going into -ve domain, no? 
54321
12
c y m || 0 21 1 
225
522
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        c, y = x, 0
        while c != 0:
            m = c % 10
            c //= 10
            y = y*10 + m
        return y==x
        