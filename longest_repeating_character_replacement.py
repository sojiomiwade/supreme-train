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




'''
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
 

Constraints:
1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length

k = 1
AABABBA 
^
l
  r
therest has to be <= k
as long as
therest = r-l+1 - maxf <= k
 maxf +   r-l+1
get a longest length by advancing right, and k replacing. at a point you will violate: 
once this is not the case move to the right
'''
from typing import Counter


def kreplace(s: str, k: int) -> int:
    left = maxf = 0
    freq = Counter()
    for right in range(len(s)):
        freq[s[right]] += 1
        if freq[s[right]] > maxf:
            maxf = freq[s[right]]
        if right - left + 1 - maxf > k: # 4 - 2 > 1
            freq[s[left]] -= 1
            left += 1
    return len(s) - left 

'''
   r
ABAB
  l
A:2 B:1 maxf:2
'''
s, k = 'ABAB', 2
print(kreplace(s, k)) # 4


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        brute force: for any string s[i:j+1] AABCD
        the one having maximum frequency is our hope, so we have
        mf+(j-i+1)
        j-i+1 - mf <= k
        5 - 1 <= 3 => bad. ABCDE
        5 - 2 <= 3 => ok.  AABCD
        5 - 3 <= 2 => ok.  AAABC
        can calculate mf in O(width of substring)
        complexity: n**2*n = n**3

        can we use sliding window? 
        sure, 
        mf is calculated how? 
        increase the substring
            remove char, if that was responsible for mf, then duck mf one point
            add a char ch, update its frequency, and update mf accordingly. 
        now check  
        max string itself is l to r

        S Q R A B A C D
                l       
                    r
        when we get good answer 

        AABBQE
        l 
            r

        a a b c d
        l
                r
        opt=s[0:2]
        f={a:1,b:2,c:1,d:1}
        mf=2
        3 - 2 > 1

        A A A B C D
        l
                r      
        Q R S A A B B D
                l
                    r
        mf=2
        f={Q:0,R:0,S:0,A:2,B:2}
        4-3>1
        '''
        l=0
        n,f=len(s),Counter()
        mf=0
        for r,ch in enumerate(s):
            f[ch]+=1
            mf=max(mf,f[ch])
            if r-l+1 - mf > k:
                f[s[l]]-=1
                l+=1
        return r-l+1class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
          l
        aababbab
               r
        k=2
        r-l+1
        3 + 2 = 5
        r-l+1 - maxf <= k ==> ok ==> more than k is unacceptable
        '''
        count=Counter()
        left=0
        maxf=0
        for right in range(len(s)):
            count[s[right]] += 1
            maxf=max(maxf,count[s[right]])
            if right-left+1-maxf > k:
                count[s[left]] -= 1
                left += 1
        return len(s)-left