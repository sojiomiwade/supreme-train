'''
a b a d e a

abca -> {a,b,c}
cba -> {a,b,c}
{a,b,c}
{b}

abc: 2 => 2 choose 2 = 1
bab: 3 => 3 choose 2 = 3
ans = 4

bbaaac
'''
class Solution:
    def similarPairs(self, words: List[str]) -> int:
        freq=Counter()
        res=0
        for word in words:
            key=0
            for ch in word:
                key|=(1<<(ord(ch)-ord('a')))
            res+=freq[key]
            freq[key]+=1
        return res