'''
s=QRSADOBECAODEABANC
  l       r
        l      r
               l   r
ABCA
EABANC
build up the string until you have a count of everything you need
then bring l forward until you don't have something and then repeat
while keeping track of the minimum length

EABANC; ABCA; need={A:2,B:1,C:1}; exp=ABANC
l       
     r           
hc=1
have={A:1,B:1}
'''
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m,n=len(s),len(t)
        have=Counter()
        need=Counter(t)
        hc=0
        l=0
        ml,mr=float('-inf'),float('inf')
        for r in range(m):
            char=s[r]
            if char in need:
                have[char]+=1
                if have[char]==need[char]:
                    hc+=1
                while hc==len(need):
                    if r-l<mr-ml:
                        ml,mr=l,r
                    char=s[l]
                    if char in need and have[char]==need[char]:
                        hc-=1
                    have[char]-=1
                    l+=1
        return '' if mr==float('inf') else s[ml:mr+1]
        


            