'''
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
        if x < 0:
            return False
        y = 0
        while y < x: # 1 < 0
            digit = x % 10 # 1
            x //= 10 # 0
            y = y * 10 + digit # 0, 1
        return (y == x) or (y // 10 == x) # if x had odd digit count
        
