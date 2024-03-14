'''
ab 3 p1 p2 p3
a b c
ab ac bc --> 3
ab ac bc --> 
a b c ... d
for each word
    x map it
    ans+=freq[x]
    freq[x]+=1

runtime: nw
fish

aba bba   ab c
uu 00011
ans 3
freq {00011:2}
'''
class Solution:
    def similarPairs(self, words: List[str]) -> int:
        freq=collections.Counter() # space : n
        ans=0
        for word in words: # n
            uu=0
            for ch in word: # w
                uu|=1<<ord(ch)-ord('a')
            ans+=freq[uu]
            freq[uu]+=1
        return ans
                