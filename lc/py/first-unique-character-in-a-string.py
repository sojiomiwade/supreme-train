# 0 1 2 3 4 5 6 7
# l e e t c o d e
# ^

# c(4,1) e(7,3) d(6,1) t(3,1) o(5,1) l(0,1)
# 1. build the map
# 2. run through it, and update ans if it doesn't repeat and it is lower in ord than others

# l e q e
# m = {e:[12], q:[21], l:[01]}
# ans = 2
class Solution:
    def firstUniqChar(self, s: str) -> int:
        m = {}
        for i,ch in enumerate(s):
            if ch not in m:
                m[ch] = [i,1]
            else:
                m[ch][1] += 1

        ans = -1
        for ch, (chord,chfreq) in m.items():
            if chfreq == 1 and (ans==-1 or chord < ans):
                ans = chord
        return ans