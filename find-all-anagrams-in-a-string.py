'''
p abcc
a b x t a c b c f g h i
l
r
a b x c . . .
  l
    r
when you hit the cur, then register the l,r window
if there's a violation increment l
what's a violation? something in there beyond what we need?
need {a1 b2 c2 d0 e0 f0}

iterate entire string with a right index:
    process s[r] into count
    if we met a need, increment cur
        when cur gets to length of p, register left
    else if we surpass:
        we must have surpassed a need! so move l (and decrement cur as needed)!!!
        a b c q a t
          l
                r
b a a
  l
    r
NEED {a2 b1}
count {b0 a2}
at,over 0,0
'''
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left,m,n=0,len(p),len(s)
        at=over=0; NEED=Counter(p); ans=[]
        count=Counter()
        for right in range(n):
            count[s[right]]+=1
            at+=count[s[right]]==NEED[s[right]]
            over+=count[s[right]]>NEED[s[right]]
            if over>0:
                at-=count[s[left]]==NEED[s[left]]
                over-=count[s[left]]>NEED[s[left]]
                count[s[left]]-=1
                left+=1
            if at==len(NEED):
                ans.append(left)
        return ans
            
        