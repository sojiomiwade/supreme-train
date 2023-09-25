'''
9:19 - 9:28 = 9 mins
t = random_shuffle(s) + x
s = abbcdd
t = abbcddd
s_ch_count
t_ch_count
for each ch in t_ch_count, if it is different in s_ch_count, return it
time: build maps: m + n, space: m + n
a
aa
schcount[0] = 1
tchcount[0] = 2
'''
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sch_count = [0]*26
        tch_count = [0]*26
        for ch in t:
            tch_count[ord(ch)-ord('a')] += 1
        for ch in s:
            sch_count[ord(ch)-ord('a')] += 1
        for ch in t:
            if tch_count[ord(ch)-ord('a')] != sch_count[ord(ch)-ord('a')]:
                return ch
        return None


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        svec = tvec = 0
        for ch in s: #abcd: 
            mask = 1 << (ord(ch) - ord('a'))
            svec ^= mask
        for ch in t:
            mask = 1 << (ord(ch) - ord('a'))
            tvec ^= mask
        resvec = svec ^ tvec
        for chidx in range(26):
            char_is_set = resvec & 1 #1011 & 1
            if char_is_set:
                return chr(chidx + 97)
            resvec >>= 1
        return None
            
