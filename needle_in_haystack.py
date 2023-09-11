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
