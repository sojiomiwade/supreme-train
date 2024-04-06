'''
paper 
title 
^
tbrother {pt ai}
sbrother {tp ia}
sigh. can do it by mapping
p to t
if cur is not mapped, then map it
otherwise see if this is the right mapping. return false if it isn't

if e not there add ea
else verify map[e] is a
badc
baba
lookup {bb aa db}
'''
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        lookup={}
        for chs,cht in zip(s,t):
            if chs in lookup:
                if lookup[chs]!=cht:
                    return False
            else:
                if cht in lookup.values():
                    return False
                lookup[chs]=cht
        return True
