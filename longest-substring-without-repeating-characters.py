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
