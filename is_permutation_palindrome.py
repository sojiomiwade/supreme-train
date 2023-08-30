'''
toca cot
space is insignificant
case is insignificant
above is true: itself is a palindrome
algorithm: sort the string, then for each unique char, no more than one should have odd count.

aaabb
l
r
toca cott
accoottt
   ^
'''
def is_pal_perm(s: str) -> bool:
    slist = sorted(s.upper())
    left = 0
    already_have = False
    while left < len(slist):
        count = 0
        while count + left < len(slist) and slist[left] == slist[count + left]:
            count += 1
        if slist[left] != ' ' and count % 2 == 1:
            if already_have:
                return False
            already_have = True
        left += count
    return True

s = 'toca cot'
print(is_pal_perm(s)) # true
s = 'cota cot'
print(is_pal_perm(s)) # true
s = 'cota cott'
print(is_pal_perm(s)) # false
s = 'coTa cot'
print(is_pal_perm(s)) # true

