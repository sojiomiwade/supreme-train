'''
problem: abcabcbb -> 3
stopwatch: 8:38 - 9:03 = 25 mins
confirms: ascii? lowercase only, ok, 26 length arr
example
abcabcbb
l r
pwwkew
  l r
raabcr
  l  r
qhrabcr
 l    r

we shouldn't see previous r
method: 
    go from "left" until a char repeats itself (always updating the longest)
    bring left up to char where the repeated char isn't (r + 1)
    continue searching for longest...
    keep location[char] as you go, then we know if we have next char (always update longest)
    when repeated found, also check location[s[right]] >= left, left = location[s[right]] + 1
    
a a
  l
  r
loc: {a: 1}
analysis: time: space
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        n = len(s)
        longest = 0
        location = {}
        for right in range(n):
            if s[right] in location and location[s[right]] >= left:
                left = location[s[right]] + 1
            location[s[right]] = right    
            longest = max(longest, right - left + 1)
        return longest

