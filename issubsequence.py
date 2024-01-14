'''
need to just check if each s char can be found in t
each char checked from s, start from that loc in t

abcde
     t
  s
aec

''
aq
s
t
ahabc
'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        #alternative way - outside idx on t
        if not s:
            return True
        sidx=0
        for tch in t: 
            if tch==s[sidx]:
                sidx+=1
            if sidx==len(s):
                return True
        return False
        # tit=iter(t)
        # return all(sch in tit for sch in s)