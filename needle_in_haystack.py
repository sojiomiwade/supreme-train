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
        
