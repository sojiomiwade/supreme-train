# s: p a p e r
# t: t i t l e

# m: {pt, ai, pt el re}
# loop through 
#     if ch in map, return false if curr tval != map val. 
#     if ch not in map, put it there with tval
# return true
# time, space: O(n), O(n)
# s: b b b
# t: a a c
# m: {b:a}
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        m = {}
        tvals = set()
        for sch,tch in zip(s,t):
            if sch in m:
                if tch != m[sch]:
                    return False
            else:
                if tch in tvals:
                    return False
                m[sch] = tch
                tvals.add(tch)
        return True