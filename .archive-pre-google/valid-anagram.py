'''
can be done with two sets.
but can just use two bit masks instead
aa a
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s)==Counter(t)