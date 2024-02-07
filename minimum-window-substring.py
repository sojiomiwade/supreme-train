'''
adobecodebanc
     r
l
need={a:2,b:1,c:3}
if there is nothing missing keep growing
otherwise
    move l until we have a deficit
    don't track at deficit
abc
b:3
bbb  b ccc
210 -1 xxx 
l
     r
'''
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
                abc
        b:3
        bbb  b ccc
        210 -1 xxx 
        l
            r
        aa
        l
        r
        need={a:0}; minl,minr=-INF,INF
        missing=2; m,n=2,2
        '''
        m,n=len(s),len(t)
        need=Counter(t)
        missing=len(need)
        INF=float('inf')
        minl,minr=-INF,INF
        left=0
        for right in range(m):
            need[s[right]]-=1
            if need[s[right]]==0:
                missing-=1
            if not missing:
                while need[s[left]]<0:
                    need[s[left]]+=1
                    left+=1
                if right-left<minr-minl:
                    minl,minr=left,right
        return s[minl:minr+1] if minr!=INF else ''


