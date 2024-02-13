class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count=[0 for _ in range(256)]
        l=size=0
        for r in range(len(s)):
            och=ord(s[r])
            count[och]+=1
            if count[och]==1:
                size+=1
            if r-l+1>size:
                olch=ord(s[l])
                count[olch]-=1
                if count[olch]==0:
                    size-=1
                l+=1
        return len(s)-l