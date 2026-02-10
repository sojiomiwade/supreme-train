# s: a b c c d
#    i
# t: a c e c d b

# c  0 0 0 0 1
#    a b c d e
# make a set of s, then find what char is in t that is not in set -- O(n), O(1) <- time and space <-- this wont work, could have multiple letters! must use a map
# map: l[a]++ if s, l[a]-- if t
# then whichever is 1 is the one we need -- O(n) and O(1)

# lookup
# 0 0 ...  1  0
# 0 1 ... 24 25
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        lookup = [0 for _ in range(26)]
        for sc,tc in zip(s,t):
            lookup[ord(sc) - ord('a')] -= 1
            lookup[ord(tc) - ord('a')] += 1
        lookup[ord(t[-1]) - ord('a')] += 1
        ans = ""
        for idx,val in enumerate(lookup):
            if val == 1:
                ans = chr(idx + ord('a'))
        return ans