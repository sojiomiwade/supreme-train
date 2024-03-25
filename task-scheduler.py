'''
aaabbbcd

  n=5
---maxfreq minus 1----
a-b-c-d-i
a b c i i
--rem--
a b   <-- number of top guys
 
possible that the letters all fit
same example above
--n=3--
. . .
. . .
---
a b
6 + 2 = 8 < maximum chars = 9

so result is max(squrestuff, total number of chars)
squre stuff

a b c d a b, n=1 --> 
exp
a b c
a b d
ans=6

aaabbb
a b i i 
a b i i
a b 

(3-1)*(3+1)+2  against 6= 
'''
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        ans=0
        m=len(tasks)
        count=Counter(tasks)
        maxfreq=max(count.values())
        maxelcount=sum(1 for x in count.values() if x==maxfreq)
        return max((maxfreq-1)*(n+1)+maxelcount,m)
