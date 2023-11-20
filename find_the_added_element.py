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
           

# the no sweat bit manipulation way of doing this
'''
fish
fiysh
sum of si and ti. at the end just add t_last

by xor
s, t
res ^= ch
then return result
'''
from itertools import chain
def find_the_difference(s: str, t: str) -> str:
    res = 0
    for sch, tch in zip(s, t):
        res += ord(tch) - ord(sch)
    return chr(ord(t[-1]) + res)

def find_the_difference_xor(s: str, t: str) -> str:
    res = 0
    for ch in chain(s, t):
        res ^= ord(ch)
    return chr(res)

find_the_difference = find_the_difference_xor

s, t = 'fish', 'fishy'
print(find_the_difference(s, t)) #y
s, t = '', 'a'
print(find_the_difference(s, t)) #a
s, t = 'fish', 'shiyf'
print(find_the_difference(s, t)) #y
 
'''
1 2 3 = x
1 2 3 5 = 5 + x
1+2+3+5 - (1-2-3)
a
aa
tot=2*97-2*97=0
'''
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        tot=0
        for x,y in zip(s,t):
            tot+=ord(y)-ord(x)
            tot%=26
        tot+=(ord(t[-1])-ord('a'))
        tot%=26
        return chr(tot+ord('a'))

            '''
can be done with bit toggle

abc
abca

abc
abcd

 ab
x01
y10
v10
 
0010
0001
'''
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        v=0
        for x,y in zip(s,t):
            mx=1<<(ord(x)-ord('a'))
            my=1<<(ord(y)-ord('a'))
            v^= mx ^ my
        v^=1<<(ord(t[-1])-ord('a'))
        m=1
        for i in range(26):
            if v&m != 0:
                return chr(i+ord('a'))
            m<<=1
