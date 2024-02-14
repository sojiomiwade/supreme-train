'''
2 
2**2 = 4
4**2 = 16
1 + 36 = 37
3**2 + 7**2

n=19
19
n : 82
nn : 9**2 + 1**2
'''
class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()
        while n not in seen:
            seen.add(n)
            n=sum(int(digit)**2 for digit in str(n))
        return n==1


            