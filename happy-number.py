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
        while True:
            nn=0
            while n:
                nn+=(n%10)**2
                n//=10
            n=nn
            if n in seen:
                return 1 in seen
            seen.add(n)


            