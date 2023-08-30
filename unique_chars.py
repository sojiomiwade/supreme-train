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

