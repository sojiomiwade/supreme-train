'''
sadbutsadbut
012345678901
ans(but) : 3
bruteforce : try for a match for all haystack[i:i+len(needle)]
    complexity: mn
better? : 
hash the needle to hn
then can do incremental hash of haystack? 
cost on avg: n + m
worstcase: n + nm
still have to check at the end in case hash function got it wrong
m,n=
s a d b u t
base = 26 (will make it lower)
but -> b*26**0 + u*26**1 + t*26**2
do first of haystack
sad but -> ...
    i
012 34
range(nl,inf)# 

first check nval against hval. if ok return true
now if there's more chars(i<hl), prepare the next hval
incrementally: 
    hval -= h[i-nl]
    hval //= 26
    hval += h[i]*26**(nl-1) 
sadbut -> ...
    i
01234
'''
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack)<len(needle):
            return -1
        hl,nl=len(haystack),len(needle)
        base=10
        BASE_MAX=base**(nl-1) 
        nval=hval=0
        for i in range(nl-1,-1,-1):
            hval=hval*base+ord(haystack[i])
            nval=nval*base+ord(needle[i])
        for i in range(nl,hl+1):
            if hval==nval and haystack[i-nl:i]==needle:
                return i-nl
            if i<hl:
                hval -= ord(haystack[i-nl])
                hval //= base
                hval += ord(haystack[i])*BASE_MAX
        return -1
        
                