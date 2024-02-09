'''
yabccdex
l    r
one service updates frequency of item

if increasing frequency puts item at its bar, increment size
if decreasing frequency puts item at its bar, decrement size
if size==SIZE, append idx to result
a3 b4 c2

and if so 
a1b1c1
n,m=len(s),len(p)
complexity is then O(n)
bab

--+
'''
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n,m=len(s),len(p)
        bar=Counter(p)
        cur=Counter()
        size=0
        res=[]
        '''
        012
        baa
          i
        cur,bar,p={a2},{a2},aa
        size=1
        res []
        '''
        for i,x in enumerate(s):
            if x in bar:
                cur[x]+=1
                if cur[x]==bar[x]:
                    size+=1
                elif cur[x]==bar[x]+1:
                    size-=1
            if i-m>=0 and s[i-m] in bar:
                y=s[i-m]
                cur[y]-=1
                if cur[y]==bar[y]-1:
                    size-=1
                elif cur[y]==bar[y]:
                    size+=1
            if size==len(bar):
                res.append(i-m+1)
        return res
