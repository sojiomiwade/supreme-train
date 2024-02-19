'''
1231
01234567890
12345619231
      L   R
ans is 19231

missingcount set to len(t)
need set to counter of t
missing goes down when need of something is there => need[ch]>0
and as long as something is missing, we increase right
meanwhile, as long as we are surplus of current char (and nothing is missing), remove the surplus, and update L
s,t=
8192318,1231
     r
 l
missing,need=0,{80, 9:-1, 10 20 30}
'''
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        missing,need=len(t),Counter(t)
        L,R=0,float('inf')
        l,n=0,len(s)
        for r,ch in enumerate(s):
            if need[ch]>0:
                missing-=1
            need[ch]-=1
            if not missing:
                while need[s[l]]<0:
                    need[s[l]]+=1
                    l+=1
                if r-l<R-L:
                    L,R=l,r
        return '' if R==float('inf') else s[L:R+1]

        