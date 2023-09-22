'''
v


^
.

  v
ace
abcde
    ^
  v
aec
abcde
     ^
when done advancing through the arrays, if s has not advanced to the end, then false, otherwise true: return sloc == len(arr)

for each element in s, run through t until you find that s
at end of loop, return ()not t and not s)  or tloc != len(arr)
 v
ae
ab
  ^

v
aaa
bba
  ^ 
it is most natural to loop on t because there you 
advance on s only when there's a match on t. specifically,
looping on s is unnatural: we aren't checking off all chars of t

v
aa
ba
^
  v
axc
abcde
       ^
'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
      tloc = 0
      for sloc in range(len(s)):
        while tloc < len(t) and t[tloc] != s[sloc]:
          tloc += 1
        tloc += 1
      return tloc <= len(t)
        # sloc = 0
        # for tloc in range(len(t)):
        #     if sloc < len(s) and t[tloc] == s[sloc]:
        #         sloc += 1
        # return sloc == len(s)
