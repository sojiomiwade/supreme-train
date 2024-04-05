'''
sad
... --> pval
ksa --> sval

012
ksadx butsad
01234 | n = 4
7148
714 --> 148
714 - 7 * 100 = 14
14 * 10 = 140
140 + 8 = 148
'''
class Solution:
    def strStr(self, s: str, p: str) -> int:
        pval=sval=0
        n,m=len(s),len(p)
        mult=pow(10,m-1)
        if m>n:
            return -1
        for i in range(m):
            pval=pval*10+(ord(p[i])-ord('a'))
            sval=sval*10+(ord(s[i])-ord('a'))
        for i in range(m,1+n):
            if pval==sval:
                return i-m # n
            if i==n:
                return -1
            rididx=i-m
            sval-=(ord(s[rididx])-ord('a'))*mult
            sval*=10
            sval+=ord(s[i])-ord('a')
