'''
use a default-dict(list)
sort the input as key and add it to appropriate list

sort is (k lg k) n
actually can use a 32 bit vector as the mapping, which 
is not really faster, but more space efficient

ab ba ac

[ab,ba] [ac]
d2g3 == g3d2
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group=collections.defaultdict(list)
        for s in strs:
            group[tuple(sorted(Counter(s).items()))].append(s)
        return group.values()
