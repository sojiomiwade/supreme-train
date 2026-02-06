# create two counters, and check if they are the same
# or use one counter, and ensure it is zero at the end: one increments, the other decrements
# either way: O(max(m,n)), O(1) <-- time and space
# a n a g r a m

# a b c 
# b a c 

# 0 0 0
# a b c
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m,n = len(s), len(t)
        if m != n:
            return False
        c = [0 for _ in range(26)]
        for i in range(m):
            sch,tch = s[i],t[i]
            c[ord(sch) - ord('a')] += 1
            c[ord(tch) - ord('a')] -= 1
        return not any(bool(c[i]) for i in range(26))
