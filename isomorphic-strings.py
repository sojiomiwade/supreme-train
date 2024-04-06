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
'''
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sbrother,tbrother={},{}
        for chs,cht in zip(s,t):
            if chs in tbrother and cht in sbrother:
                if tbrother[chs]!=cht:
                    return False
                assert sbrother[cht]==chs
            elif chs not in tbrother and cht not in sbrother:
                tbrother[chs],sbrother[cht]=cht,chs
            else:
                return False
        return True
