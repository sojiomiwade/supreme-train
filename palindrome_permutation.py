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




'''
Given a string write a method to decide if it is a permutation of a palindrome
abcd - f
aabaa - or any of its permutations - t
^
1 character can have odd freq
all others must have even number of freq
hash table of freq, and check above conditions
can use a bitmap
aaaa
1010 <-- 0 means even
then only 1 bit can be set in the map
aabaac

0000110 -> false
0000101
-------
0000100
-------
can check if only 1 bit is set with
n & (n-1) == 0  implies 1 or 0 bits set
note 0 & -1 == 0


'''

def ispalperm(s: str) -> bool:
    vec = 0
    for ch in s:
        pos = ord(ch) - ord('a')
        vec ^= 1 << pos
    return vec & (vec-1) == 0
    
s='aaaa'
print(ispalperm(s)) # t
s='aaaabbb'
print(ispalperm(s)) # t
s='aaaab'
print(ispalperm(s)) # t
s='aabaa'
print(ispalperm(s)) # t
s='aaaabc'
print(ispalperm(s)) # f
s='aaqraa'
print(ispalperm(s)) # f
