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
        


            class Solution:
    def minWindow(self, s, t):
        need, m = collections.Counter(t), len(t)
        i = I = J = 0
        for j, c in enumerate(s, 1):
            m -= need[c] > 0
            need[c] -= 1
            if m==0:
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if J==0 or j - i <= J - I:
                    I, J = i, j
        return s[I:J]
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m,n=len(s),len(t)

        '''
        always add the r character
        but internally will move l until it's in violation


        ADOBAECODEBANC, AABC
        l     
              r
        brute force: iterate over all substrings and check if the contain t. m*n**2
        for each substring, construct a counter-lookup, and compare these counts with 
        the corresponding counts in t

        better: consider everything is missing
        when nothing is missing anymore (based on the t levels)
        can move l (and update need[s[l]])
        as long as there is

        QBAC AB
        missing = 4

        '''
        missing = len(t)
        ml=l=0
        mr=float('inf')
        need=Counter(t)
        for r in range(m):
            missing -= need[s[r]] > 0
            need[s[r]] -= 1
            if not missing:
                while need[s[l]] < 0:
                    need[s[l]]+=1
                    l+=1
                if r-l<mr-ml:
                    ml,mr=l,r
                need[s[l]]=1
                l+=1
                missing+=1
        return '' if mr==float('inf') else s[ml:mr+1]class Solution:
    def minWindow(self, s: str, t: str) -> str:
        missing = len(t)
        need = Counter(t)
        i, im, jm = 0, float('-inf'), float('inf')
        for j in range(len(s)):
            missing -= need[s[j]] > 0
            need[s[j]] -= 1
            if not missing:
                while need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if j-i < jm-im:
                    im, jm = i, j
        print(im,jm)
        return s[im:jm+1] if jm!=float('inf') else ''