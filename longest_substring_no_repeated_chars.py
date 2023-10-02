'''
using longest repeating character replacement method from LC lee315
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        top = 0
        count = Counter()
        for bottom in range(len(s)):
            count[s[bottom]] += 1
            if len(count) < bottom - top + 1 : # time to advance
                count[s[top]] -= 1
                if count[s[top]] == 0:
                    del count[s[top]]
                top += 1
        return len(s) - top



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
a a
  l
  r
loc: {a: 1}

   l 
we shouldn't see previous r
method: 
    go from "left" until a char repeats itself (always updating the longest)
    bring left up to char where the repeated char isn't (r + 1)
    continue searching for longest...
    keep location[char] as you go, then we know if we have next char (always update longest)
    when repeated found, also check location[s[right]] >= left, left = location[s[right]] + 1

analysis: time: O(n) space: O(n)
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        n = len(s)
        longest = 0
        location = defaultdict(lambda :-1)
        for right in range(n):
            left = max(left, location[s[right]] + 1)
            location[s[right]] = right
            longest = max(longest, right - left + 1)
        return longest

# again, but try to follow CTIC methodology
'''
Given a string s, find the length of the longest substring without repeating characters.

time: 12:20 --  12:45 == 25


Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:
0 <= s.length <= 5 * 10**4
s consists of English letters, digits, symbols and spaces

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

       r
x...abcxabcbb
    l

on each iteration move r along doing the following, until r = n
when r sees something already seen, first move l to r-char's loc in dictionary, plus 1
update longest based on l and r

dictionary to remember r-char's loc: O(n)
time: O(n)

simple Example
 l
aba; ans = 2
   r
s = {a:0, b:1, }
longest = 2
'''
from collections import defaultdict
def longest_substring(s: str) -> int:
    l = 0 # default
    longest = 0
    loc = defaultdict(lambda :float("-inf"))
    for r in range(len(s)):
        l = max(l, loc[s[r]] + 1)
        loc[s[r]] = r
        longest = max(longest, r - l + 1)
    assert type(longest) is int
    return longest
  
s = ""
print(longest_substring(s)) # 0
s = "a"
print(longest_substring(s)) # 1
s = "abcabcbb"
print(longest_substring(s)) # 3
s = "bbbbb"
print(longest_substring(s)) # 1
s = "pwwkew"
print(longest_substring(s)) # 3, wke or kew

