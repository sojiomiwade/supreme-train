'''
determine if a string is a permutation of a palindrome
assume english chars a - z only
no arrays or hash tables allowed
'pale apples'
abcdelps
0
a = 0
b = 1
c = 2
...
and
1101 mask
1011 res
  ^
1001
res init to 0 (int)
set loc 2 ('c')
if it is set: 0 != (1 << loc) & res
    clear set bit: res ^= (1 << loc)
otherwise 
    set clear bit: res |= (1 << loc)
res |= 1 << 2
 
 set clear bit
 010 mask 
|100 res
 110 ans
 
 clear set bit
 010 
^110
 100

 101
&110
 100

 101
&010
 000

 00101
 11010 = -00101 = -5
'''

def is_palindrome_permutation(s: str) -> bool:
    res = 0
    for ch in s:
        if not ch.isalpha():
            continue
        ch = ch.lower()
        loc = ord(ch) - ord('a')
        res ^= (1 << loc) # toggle bit loc
    #true only if 0 or 1 bit set in res
    return sum(1 if res & (1 << loc) != 0 else 0 for loc in range(26)) <= 1

s = 'toca cat'
print(is_palindrome_permutation(s)) # true
s = 'tt'
print(is_palindrome_permutation(s)) # true
s = 'toca ccat'
print(is_palindrome_permutation(s)) # false
s = 'noon'
print(is_palindrome_permutation(s)) # true
s = '4noon'
print(is_palindrome_permutation(s)) # true

