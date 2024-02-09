'''
0 1 2 3 4 5 6
a a b a b b a, k=2
        r
l 
w rest maxf

highest-freq maxf
width - maxf cannot be more than k. when this happens, time to 
slide the window (move l, since r moves already). 
if width - maxf , don't move l
at the end the ans is (n-1)-l+1 = n-l
now maxf cost is m (number of unique chars)=>
time is O(m*n) 

k=1
A B A B
      r
  l 
freq  A2 B2
maxf 2

'''
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq=Counter()
        l=0
        maxf=float('-inf')
        for r in range(len(s)):
            freq[s[r]]+=1
            maxf=max(maxf,freq[s[r]])
            if (r-l+1)-maxf>k:
                freq[s[l]]-=1
                l+=1
                maxf=max(val for val in freq.values())
        return len(s)-l