# s: a b c q
#          i
#                j
# t: a h b g d c
# if i falls off then return true.
# after t loop, return false

# s: a b
#        i
#        j
# t: a q b
# m, n : 2, 3
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        i = 0
        m, n = len(s), len(t)
        for j in range(n):
            if s[i] == t[j]:
                i += 1
                if i == m:
                    return True
        return False
                