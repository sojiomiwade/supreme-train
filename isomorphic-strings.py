'''
e q a 
a a b

if chs in lookup, verify that lookup[chs]==cht
also, if chs not in lookup but cht in lookup.values()  return  false
regardless lookup[chs]=cht

'''
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        lookup={}
        for chs,cht in zip(s,t):
            if chs in lookup and lookup[chs]!=cht:
                return False
            if chs not in lookup and cht in lookup.values():
                return False
            lookup[chs]=cht
        return True
