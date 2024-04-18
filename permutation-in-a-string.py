'''
eidbaooo
l
r
as long as left is under, bring it forward

s1 abcd
abcxdabc
    l
       r
need {a1 b1 c1 x0 d1}
'''
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left=0
        m,n=len(s1),len(s2)
        need=Counter(s1)
        for right,c in enumerate(s2):
            need[c]-=1
            while need[c]<0:
                need[s2[left]]+=1
                left+=1
            if right-left+1==m:
                return True
        return False