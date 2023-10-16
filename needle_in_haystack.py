'''
sad, adb, dbu, but, ...
m, n = 3, 9
sadb utsad
   ^
012345678
sa
get neval
add first m-1 chars of hs to hsval
loop on characters to add (i) in (m-1, n-1)
    add hs(i) to hsval
    validate(neval, hsval)
    remove hs(i-m+1) from hsval # 2-3+1 = 0
    
complexity: O((n-m)), O(1)
largest val: 26**(1e4)
hs
ne
hsval
neval
sa --> sad
sad --> ad
713 --> 13
%100
71 -> 713
713 -> 13
'''
class Solution:
    def strStr(self, hs: str, ne: str) -> int:
        m, n, base = len(ne), len(hs), 26
        mfac = base ** (m-1)
        neval = hsval = 0
        for ch in ne:
            neval = base * neval + ord(ch) - ord('a')
        for ch in hs[:m-1]:
            hsval = base * hsval + ord(ch) - ord('a')
        for i in range(m-1, n):
            hsval *= base
            hsval += ord(hs[i]) - ord('a')
            if hsval == neval:
                return i-m+1
            hsval %= mfac
        return -1
       

#DUD. rushed? terrible!
'''
function int[] grep(string haystack, string needle)
haystack = "aaabcdddbbddddabcdefghi"
needle = "abc"
[2,14]
aaabcddd bbddddabcdefghi
01234567 8901234
  ^.   m
m = haystack.length
n = needle.length
could use brute force in O(mn)
could use a hash for O(m+n): compare sliding window of haystack with hash(abc)

needlehash = hash(needle)
num = num(haystack[:n-1])
for lh_idx in [n-1:m+1] #n=3,m=8 -- 2:8
    hash(haystack[lh_idx-n-1:lh_idx+1]) # k=7 -- [7-4:7] -- 3:7
    if hashes are equal
        res.append(lh_idx-n-1)
print(res)
'''
from typing import List

def num(pattern: str) -> int:

def hash(pattern: str) -> int: 
    ...
# 256 -- 56 -- 567
def adjust(hashval, nextdigit) -> int:
    ...
def grep(haystack: str, needle: str) -> List[int]:
    base = 26
    m, n = len(haystack), len(needle)
    needlehash = hash(needle)
    haystackhash = hash(haystack)
    for lh_idx in [n-1:m+1] #n=3,m=8 -- 2:8
        haystackhash = adjust()
        hash(haystack[lh_idx-n-1:lh_idx+1]) # k=7 -- [7-4:7] -- 3:7
        if hashes are equal
            res.append(lh_idx-n-1)
    print(res)
    
haystack, needle = 'abc', 'aaabcdddbbddddabcdefghi'
grep(haystack, needle) #[2,14] 

#under 25 mins, but still didn't use example in couple lines: //= instead of %=



'''
function int[] grep(string haystack, string needle)
haystack = "aaabcdddbbddddabcdefghi"
needle = "abc"
[2,14]

aaabcdddbbddddabcdefghi
0123456789012345678901

nh = hash(needle)
for each substring of haystack, hash it. 
to get the next hash of the haystack
xa b c d e
21 0 ^
    
curr-=x*10**(length-1)
curr*=10
curr+=c

buildup. build up length - 1
then make hl-nl+1 checks in while loop for 
[nl-1..hl-1]

813392
3 * 10**0 + 3 * 10**1 + 1 * 10**2
'''
from typing import List
def grep(needle: str, haystack: str) -> List[int]:
    def hash(s: str, sidx: int, length: int) -> int:
        shiftval = 1
        res = 0
        for i in reversed(range(sidx, length)):
            res += ord(s[i]) * shiftval
            shiftval *= base
        print(res)
        return res

    base = 256
    needle_len = len(needle) # 2
    needle_val = hash(needle, 0, needle_len)
    curr = hash(haystack, 0, needle_len)
    bigshift = base ** (needle_len - 1)
    res = []
    for i in range(needle_len, len(haystack)):
        if curr == needle_val:
            res += [i - needle_len]
        curr -= ord(haystack[i - needle_len]) * bigshift
        curr *= base
        curr += ord(haystack[i])
    if curr == needle_val:
        res += [len(haystack) - needle_len]
    return res

needle, haystack = 'ab', 'cabqrab'
#                         0123456 
print(grep(needle, haystack)) # 1
#
