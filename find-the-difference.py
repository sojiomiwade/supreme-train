'''
abcd
baecd
could sort both and see where a char is different, the t char is the difference - nlgn
could use one hashmap. t increments, s decrements. the one char with a 1 is the ans
bbb--
bbbb
can use a 32 bit integer actually. similar to hashmap, but for either string we use xor
the one bit that is one is the added char. <-- optimal in time and space!
10000
4 
log(bitvec)/log(2) = 
'''
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        bitvec=0
        for ch in itertools.chain(s,t):
            mask=1<<(ord(ch)-ord('a'))
            bitvec^=mask
        return chr(97+int(math.log(bitvec)/math.log(2)))