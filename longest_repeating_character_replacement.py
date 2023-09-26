'''
10:19 -- 10:53 = 32  +/- 2
      l
A A B A B B A
            r
n - l
(n-1) - l + 1 = n - l

5 5 2
4 5 2
3 ok
2
rest cannot surpass k
rest: (r-l+1) - maxf != k+1

can extend r until maxf + k < r -l + 1 violated
at this point, increment l


A B A B
  l
      r
4-2 == 2 ? no
maxf=2 
k=1
A:1, B:2
'''
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = maxf = 0
        count = [0 for i in range(26)]
        for r in range(len(s)):
            count[ord(s[r]) - ord('A')] += 1
            maxf = max(maxf, count[ord(s[r]) - ord('A')])
            if (r-l+1) - maxf == k+1:
                count[ord(s[l]) - ord('A')] -= 1
                l += 1
        return len(s) - l

