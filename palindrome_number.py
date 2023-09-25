'''
problem: given a number, check if it is a palindrome

touch
-----
49387
  ^
in a new number inited to 0, keep adding the modulo of successive divs of original number
b4 each such addition, multiply res by 10.
to avoid overflow
78...493
783..49

12321
123..12
if res > orig, then original isn't a pal, or without that last modulo, the numbers are equal

res = 0
while x > 0 #can also just say True
  mod = x % 10
  x //= 10
  if (res == x)
    True
  elif (res*10+mod > x)
    return res == x
  res*=10
  res+=mod
y = 0
while y < x # 0 < 41814, 4 < 4181, 41 < 418, 418 < 41
    digit = x % 10 # 4
    x //= 10 # 411
    y = y * 10 + digit
return (y == x) or (y // 10 == x) # if x had odd digit count

what of even digit count. don't matter. check for equality
41 < 41 => break
then check 41 (or 418) == 41, if ok, true gets returned. otherwise we check
418 // 10  == 41 (or 53 or something else not pal) // 10


compare y to x // (count + 1)

4114 <-- x even digit count


41814 <-- x odd digit count
-->41
12345
  ^
largest: 12346 (just suppose so)
but pal: 54321
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x > 0 and x % 10 == 0):
            return False
            
        y = 0
        while y < x: # 1 < 0
            digit = x % 10 # 1
            x //= 10 # 0
            y = y * 10 + digit # 0, 1
        return (y == x) or (y // 10 == x) # if x had odd digit count
