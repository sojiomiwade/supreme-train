'''
1. sort the string, and compare adjacent chars for inequality. time: O(n lg n); space: O(1)
2. use counter, and check counter[key] <= 1 for all keys. time: O(n), space: O(n) 
3. use boolean array instead of counter; False if at anytime a bit is already set for a given char
3b. bitmap could be implemented in fixed size type, if alphabet can fit into that size [space can be O(a) as is alphabet size]
3a, 3b => time: O(n); space: O(n), O(a) respectively

implement 3b assuming alphanumeric. that's 26*2 + 10 = 62. 
A - Z  = 0 25 -- A
a - z = 26 51 -- a
0 - 9 = 52 - 61 -- 0
bitmap[]
'''
def unique_by_bitmap(s: str) -> bool:
    bitmap = 0
    for ch in s:
        if 'A' <= ch <= 'Z':
            pos = ord(ch) - ord('A')
        elif 'a' <= ch <= 'z':
            pos = ord(ch) - ord('a')
            pos += 26
        else:
            pos = ord(ch) - ord('0')
            pos += 52
        if (1 << pos) & bitmap != 0: 
            return False
        bitmap |= (1 << pos)
    return True

def unique_by_sort(s: str) -> bool:
    s = sorted(s.upper())
    for i in range(1, len(s)):
        left, right = s[i-1], s[i]
        if left == right:
            return False
    return True

unique = unique_by_bitmap
s = "fish"
print(unique(s)) #true
s = "fisheS"
print(unique(s)) #true
s = "123456"
print(unique(s)) # true
s = "1"
print(unique(s)) # true
s = "111111"
print(unique(s)) #false


#again
'''
does a string have all unique characters
frid
if we know alphabet size, then if string beyond that, False
can use set, see it again, return False
otherwise, true
O(n), O(n) 

could use inplace sort, then if si == s_i-1, False i in 1:n
O(n lg n), O(1)
'''
def all_unique(s: str) -> bool:
    sset = set()
    for ch in s:
        if ch in sset:
            return False
        sset.add(ch)
    return True

def all_unique(s: str) -> bool:
    rs = list(reversed(s))
    for i in range(1, len(s)):
        if rs[i] == rs[i-1]:
            return False
    return True
    
s = 'Friday'
print(all_unique(s)) # true
s = 'Non'
print(all_unique(s)) # true
s = 'Noon'
print(all_unique(s)) # false
s = ''
print(all_unique(s)) # true



#again
'''
check if an alphanumeric string has all unique characters in O(n) time, but O(1) space
abcde: true
aa: false
: true

aplep
00000
aple

use three integers one each for 
lowercase, uppercase, numbers
start with lowercase

alg: when about to set: if a char's bit is already set, then return False. if never so for the entire string, return True. 
'''
def all_unique_chars(s: str) -> bool:
    vec = [0,0,0]
    for ch in s:
        pos = ord(ch)
        if ord('A') <= pos <= ord('Z'):
            pos -= ord('A')
            vecidx = 1
        elif ord('a') <= pos <= ord('z'):
            pos -= ord('a')
            vecidx = 0
        else:
            pos -= ord('0')
            vecidx = 2
        mask = 1 << pos
        # print('pos', pos, mask, vec, vec | mask)
        if vec[vecidx] & mask != 0:
            return False
        vec[vecidx] |= mask
    return True

s = 'aa'
print(all_unique_chars(s)) # false
s = 'aple'
print(all_unique_chars(s)) # true
s = ''
print(all_unique_chars(s)) # true
s = 'Aple'
print(all_unique_chars(s)) # true
s = 'ApA'
print(all_unique_chars(s)) # false
s = '12312'
print(all_unique_chars(s)) # false




'''
implement an algorithm to check if a string has all unique characters

abcdea -> false
^
abcde  -> true

hash table, if you see element you've seen return false. at the end return true. O(n) + O(n)
but if restricted to lower case for example, can use an int for 0-25 characters if we have seen it: space becomes O(1)

also consider an algorithm that uses constant space
here we could sort and check neighboring characters: O(n lg n) + O(n), space can become O(1) if we use heapsort, since quicksort is n**2 time, and merge sort is n space

abca

bitvec: 0..000
0..111
000001 
'''
def is_unique(s: str) -> bool:
    lowerbitvec: int = 0
    upperbitvec: int = 0
    for ch in s:
        if ord('a') <= ord(ch) <= ord('z'):
            bitvec = lowerbitvec
            base = 'a'
        else:
            bitvec = upperbitvec
            base = 'A'

        pos = ord(ch) - ord(base)
        mask = 1 << pos
        if bitvec & mask != 0: #we have seen it
            return False
        bitvec |= mask
        if ord('a') <= ord(ch) <= ord('z'):
            lowerbitvec = bitvec
        else:
            upperbitvec = bitvec

    return True

print(is_unique('abca')) # false
print(is_unique('abc')) # true
print(is_unique('abcA')) # true
print(is_unique('ABCA')) # false
print(is_unique('BCA')) # true