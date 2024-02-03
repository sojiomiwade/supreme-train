'''
10
let each prime wipe out multiples
2 3 4 5 6 7 8 9 10 11 12 13 14 | 15
    -   -   -   --    --    --
       -     -       --

# ans=[2,3,5,7]
have a map a[x]=T/F
at the end count everything that's true in a
iterate from x*2, and x=2*x, for each x
x in range(2*x,n,x)

n=7
0 1 2 3 4 5 6 
f f t t f t f 
'''
class Solution:
    def countPrimes(self, n: int) -> int:
        isprime=[True for _ in range(n)]
        isprime[0:2]=[False,False]
        for num in range(2,n):
            if isprime[num]:
                for x in range(2*num,n,num):
                    isprime[x]=False
        return sum(isprime)
