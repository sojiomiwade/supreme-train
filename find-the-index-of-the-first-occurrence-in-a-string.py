class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle): 
            return -1

        n, m = len(haystack), len(needle)
        base = 26
        hund = base ** (m-1) # 100
        nval = hval = 0

        for i in range(m):
            nval *= base
            hval *= base
            nval += (ord(needle[i]) - ord('a'))
            hval += (ord(haystack[i]) - ord('a'))

        if hval == nval:
            return 0
        
        for i in range(1, n-m+1):
            hval -= ((ord(haystack[i-1]) - ord('a')) * hund)
            hval *= base
            hval += ord(haystack[i+m-1]) - ord('a')
            (hval, nval)
            if hval == nval:
                return i

        return -1        
        