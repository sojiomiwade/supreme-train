'''
have to go through whole string no matter
leetcode
l1 e3 t1 c1 o1 d1
l->(1,l)
0,1,2,3
first: counter
then loop again and take the first one with counter 0
'''
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count=Counter(s)
        for i,x in enumerate(s):
            if count[x]==1:
                return i
        return -1