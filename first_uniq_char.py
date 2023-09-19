'''
time: 4:06 -- 19 = 13
loveleetcode
can use hash-table in initial pass through with boolean value it repeated or not
could alsoo just use binary number as hash table
time: O(n). will pass through once to build hash table, 
then will pass through again to find the first
space: O(1)
question. one pass possible? 
could update first ... no it isn't because you will remember l and pass through v, but when you cancel l, you don't know v anymore
'''
class Solution:
    def firstUniqChar(self, s: str) -> int:
        repeats = 0
        for ch in s:
           mask = 1 << ord(ch) - ord('a')
            if (repeats & mask) != 0:

           repeats |= mask
        for i, ch in enumerate(s): 
            mask = 1 << ord(ch) - ord('a')
            if (repeats & mask) == 0:
                return i
        return -1
        


# again but it works this time
'''
time: 7:38 -- 7:54: 16 mins
loveleetcode
t t    t 
for i 
    update already_seen
for i 
    if already_seen
        mark it as repeated
for i 
    if already_seen but not repeated
        return that one

'''
class Solution:
    def firstUniqChar(self, s: str) -> int:
        already_seen = 0
        repeated = 0
        for i, ch in enumerate(s):
            mask = 1 << ord(ch) - ord('a')
            if already_seen & mask != 0:
                repeated |= mask
            else:
                already_seen |= mask

        for i, ch in enumerate(s):
            mask = 1 << ord(ch) - ord('a')
            if repeated & mask == 0:
                return i

        return -1
