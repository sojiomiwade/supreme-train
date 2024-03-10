'''
leetcode
use two integers:
first: first one flags if first time seen
again: 2nd flags oonly if first is seen
finally loop through s and pick element that has first but not second
aabb
   ^
mask   01
first  11
second 11
'''
class Solution:
    def firstUniqChar(self, s: str) -> int:
        first=second=0
        for ch in s:
            mask=1<<ord(ch)-ord('a')
            if first&mask==0:
                first|=mask
            else:
                second|=mask
        for i,ch in enumerate(s):
            mask=1<<ord(ch)-ord('a')
            if first&mask!=0 and second&mask==0:
                return i
        return -1