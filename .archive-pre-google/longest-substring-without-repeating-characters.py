'''
can just use a sliding window and a dictionary for location of elements
when we see an element, we have it if 
1. ch is in loc lookup
2. loc of ch is greater or equal to l
always update the max window via the l to r distance, 
'''

'''
aba
  i
 l
count : {a1 b1}
if there will be a violation ahead, move it (removing from the hashset first)
012345
pwwkew
     i
   l
{w1 e1 k1} count
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count=Counter()
        left=0
        for i in range(len(s)):
            count[s[i]]+=1
            if i-left+1!=len(count):
                count[s[left]]-=1
                if count[s[left]]==0:
                    del count[s[left]]
                left+=1
        return len(s)-left
