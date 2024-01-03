'''
a b a d e a

abca -> {a,b,c}
cba -> {a,b,c}
{a,b,c}
{b}

abc: 2 => 2 choose 2 = 1
bab: 3 => 3 choose 2 = 3
ans = 4

'''
class Solution:
    def similarPairs(self, words: List[str]) -> int:
        freq=Counter()
        for word in words:
             freq[''.join(sorted(set(word)))]+=1
        res=0
        for wfreq in freq.values():
            if wfreq>1:
                res+=math.factorial(wfreq) // math.factorial(wfreq-2) // 2
        return res