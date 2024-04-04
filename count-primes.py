'''
n 18
sieve of eratosthenes
arr [2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17]
     x x . x .   . .  .     .     .  .  .
primes [2 3 5]

36
19
6 6

n 10
      0 1 2 3 4 5 6 7 8 9
comp [f f f f t f t f t t]
          1 2   3 
'''
class Solution:
    def countPrimes(self, n: int) -> int:
        comp=[False for i in range(n)]
        ans=0
        for cand in range(2,n):
            if not comp[cand]:
                ans+=1
                arrlen=len(range(cand,n,cand))
                comp[cand::cand]=arrlen*[True]
        return ans
