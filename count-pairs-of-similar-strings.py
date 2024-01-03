class Solution:
    def similarPairs(self, words: List[str]) -> int:
        res=0
        for (i, worda) in enumerate(words):
            for (j,wordb) in enumerate(words):
                if i<j and set(worda)==set(wordb):
                    res+=1
        return res