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


'''
aec
abxdcee

build loc apriori
ps = 0
for each char in s, bisect in loc[s], start=prior_start
  ps = for e bisect(loc[e], start=ps)
  if ps == -1
    return False
  ps += 1
 return True 
 a
 ab
 loc = {a: [0], b: [1]}
 ps = 0
 0
 aec
abxdcee
0123456
loc = {a:[0], e:[5,6] c:[4]}

v
abxdcee
aec
^
0123456
ps = 1
loc = {a:[0],b:[1],x:[2],d:[3],c:[4],e:[5,6]}
bl(loc[e], 1)
'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        char_locs = defaultdict(list)
        for ch_loc, ch in enumerate(t):
            char_locs[ch].append(ch_loc)            
        prior_start = 0
        for ch in s: 
            ch_loc = bisect.bisect_left(char_locs[ch], prior_start)
            if ch_loc == len(char_locs[ch]):
                return False
            prior_start = char_locs[ch][ch_loc] + 1
        return True 


# again but using char array instead of defaultdict, sincee input is limited to lowercase english alphabet
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sublocs = [[] for _ in range(26)]
        for tloc, ch in enumerate(t):
            sublocs[ord(ch) - ord('a')].append(tloc)            
        prior_start = 0
        for ch in s: 
            idxidx = bisect.bisect_left(sublocs[ord(ch) - ord('a')], prior_start)
            if idxidx == len(sublocs[ord(ch) - ord('a')]):
                return False
            prior_start = sublocs[ord(ch) - ord('a')][idxidx] + 1
        return True 

'''
 ace
 abcde
      ^
(tt)
'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        it = iter(t)
        return all(ch in it for ch in s)
            