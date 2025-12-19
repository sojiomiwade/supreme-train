'''
approach: advance r as long as no excess violation.
at some point, 
s [c b a c e b a b a c d] | p [a b c]
     l
         r
ans [0 1]
need {a1 b1 c0 d0 e0}
'''
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left=0
        ans=[]
        need=Counter(p)
        for right,char in enumerate(s):
            need[char]-=1
            while need[char]<0:
                need[s[left]]+=1
                left+=1
            if right-left+1==len(p):
                ans.append(left)
        return ans
        