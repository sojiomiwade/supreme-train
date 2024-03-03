'''
s  abc
   ^
t  ahbgdc
look in t for each character of s. false if u cant 
consider each s char. true otherwise
'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        tit=iter(t)
        for ch in s:
            if ch not in tit:
                return False
        return True