'''
2:55 - 3:09 = 14 
n
for each number x between 0 and n inclusive, compute the number of 1s

x = 5
101 = 2
how to get 101
approach 1
could use a mask to iterate 32 bits and count number of 1s, shifting the mask by 1 for each iteration, and using & (not |). time is O(1) for each x

    5 % 2 = 1
5 // 2 = 2
    2 % 2 = 0
2 // 2 = 1
    1 % 2 = 1
1 // 2 = 0 
stop!

so keep dividing n by 2 until you get 0, for each % (including n itself) increment counter. if n were INT_MAX, it would be 32 divs, so O(1) too

for both space is constant
n = 1
[0, 1]

'''
class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for x in range(n + 1): # 0, 1
            res.append(0) # 1
            while x != 0:
                res[-1] += int((x % 2) == 1)
                x //= 2
        return res

#again, but with Dynamic programming
class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0 for _ in range(n + 1)]
        for i in range(1, n + 1):
            res[i] = res[i >> 1] + i % 2
        return res



'''
took a while (and was sleepy)
but did it myself in < 30m
'''
class Solution:
    def countBits(self, n: int) -> List[int]:
        '''
        3
        0112
        0123
        '''
        res = [0 for _ in range(n+1)]
        res[0] = 0
        for x in range(1,n+1):
            if x % 2 == 1:
                res[x] = res[x - 1] + 1
            else:
                res[x] = res[x // 2]
        return res