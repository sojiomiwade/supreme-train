'''
bacabcbb
 r
l
rl,rr
loc = initally -1s
    now [1 0 2]
if a is in dictmove l to where a is, but a may be gone, so l = max(loc[a],l)

         l
               r
s  : p w w k e w
idx: 0 1 2 3 4 5
loc: 0 2 2 3 4 n
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        loc=[-1 for _ in range(256)]
        l=rl=0
        rr=-1
        for r in range(len(s)):
            sr=ord(s[r])
            l=max(l,1+loc[sr])
            loc[sr]=r
            if r-l>rr-rl:
                rl,rr=l,r
        return rr-rl+1