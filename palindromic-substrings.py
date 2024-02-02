'''
                i            
            aabacdefghij

            aa ba
            aab a
                a   ba
00
i+1
            a a b a
                ^
            so for each idx i, keep stretching out and counting palindromes
            if not a palindrome at any time break and add count to ans
complexity: n**2

p(i,i)=T
p(i,j)=s[i]==s[j] and i+1==j or p(i+1,j-1)
then just count all pij for all ij i in [0..n) and  i<j
 
 i
   j
 aaaa

  i j
aaaaa
12, expected 15
'''
class Solution:
    def countSubstrings(self, s: str) -> int:
        def markpal(l,r):
            if l==r:
                return True
            if (l,r) in dp:
                return dp[l,r]
            markpal(l,r-1)
            markpal(l+1,r)
            dp[l,r]=s[l]==s[r] and (l==r-1 or dp[l+1,r-1])

        n=len(s)
        dp={(i,i):True for i in range(n)}
        assert n
        markpal(0,n-1)
        return sum(dp.values())