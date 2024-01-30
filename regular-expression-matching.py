'''
aa,a,false
aa,aa,true
aaa,a*a,true
,a*,true
a,,false
abcd ab*..

func match(s,p) -> boolean:
    if not p
        return not s
    if no * on p's next char
        return s and s0==p0 and match(s[1:n],p[1:n])
    else # eat zero, one or more 
        zero = match(s,p[2:])
        more = false
        if s0 == p0
            more = match(s[1:],p)
        return zero or more
ab
^
.*
  ^
'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def helper(sloc, ploc) -> bool:
            if memo[sloc][ploc] is not None:
                return memo[sloc][ploc]
            if ploc == len(p):
                memo[sloc][ploc] = val = sloc == len(s)
                return val
            if ploc == len(p)-1 or p[ploc+1] != '*': #no star
                memo[sloc][ploc] = val = (sloc != len(s) and
                    p[ploc] in (s[sloc], '.') and helper(1+sloc,1+ploc))
                return val
            val = zero = memo[sloc][ploc] = helper(sloc,2+ploc)
            print(sloc,ploc)
            more = sloc != len(s) and (
                p[ploc] in (s[sloc], '.') and helper(1+sloc,ploc))
            memo[sloc][ploc] = val = zero or more
            return val
        memo = [[None for _ in range(1+len(p))] for _ in range(1+len(s))]
        return helper(0, 0)
        


# again
'''
Basic Regex Parser
Implement a regular expression function isMatch that supports the '.' and '*' symbols. The function receives two strings - text and pattern - and should return true if the text matches the pattern as a regular expression. For simplicity, assume that the actual symbols '.' and '*' do not appear in the text string and are used as special symbols only in the pattern string.

In case you aren’t familiar with regular expressions, the function determines if the text and pattern are the equal, where the '.' is treated as a single a character wildcard (see third example), and '*' is matched for a zero or more sequence of the previous letter (see fourth and fifth examples). For more information on regular expression matching, see the Regular Expression Wikipedia page.

Explain your algorithm, and analyze its time and space complexities.

Examples:

input:  text = "aa", pattern = "a"
output: false

input:  text = "aa", pattern = "aa"
output: true

input:  text = "abc", pattern = "a.c"
output: true

input:  text = "abbb", pattern = "ab*"
output: true

input:  text = "acd", pattern = "ab*c."
output: true
Constraints:

[time limit] 5000ms
[input] string text
[input] string pattern
[output] boolean

time: 8:27 -- 8:58 = 31
time comp: exponential; but can memoize for O(n**2)
space comp:

m(t, p) = 
    base: if no pattern, then true if no string; false otherwise
    if p[1] (or there's no p[1]) not a star: return 1st chars match and m(t[1:],p[1:]))
    else 
        zero to match:
        zero = m(t, p[2:]) --> memo[][ploc+2]
        one = first character matchers and m(t[1:], p)
        return zero or one

func isMatch(...
a
qbcdefg

t = a
p = a*b*
'''
def isMatch(t, p):
    def helper(tloc: int, ploc: int):
        if memo[tloc][ploc] != -1:
            return memo[tloc][ploc]

        if ploc == len(p):
            val = int(tloc == len(t))
        else:
            firstmatch = tloc != len(t) and p[ploc] in (t[tloc],'.')
            if ploc+1==len(p) or p[ploc+1]!='*':
                val = int(firstmatch) and helper(tloc+1,ploc+1)
            else:
                zero = helper(tloc, 2+ploc)
                one = int(firstmatch) and helper(1+tloc, ploc)
                val = zero or one
        memo[tloc][ploc] = val
        return val

    memo = [[-1 for _ in range(1+len(p))] for _ in range(1+len(t))]
    return helper(0, 0)

t, p = ('', 'b') #false
print(isMatch(t, p))
t, p = 'aa', 'a' #false
print(isMatch(t, p)) 
t, p = ('aa', 'aa') # true
print(isMatch(t, p)) 
t, p = ('abc', 'a.c') #true
print(isMatch(t, p))
t, p = ('abbb', 'ab*') #true
print(isMatch(t, p))
t, p = ('acd', 'ab*c.') #true
print(isMatch(t, p))
t, p = ('abd', 'ab*c.') #false
print(isMatch(t, p))

# tabulation
'''
Basic Regex Parser
Implement a regular expression function isMatch that supports the '.' and '*' symbols. The function receives two strings - text and pattern - and should return true if the text matches the pattern as a regular expression. For simplicity, assume that the actual symbols '.' and '*' do not appear in the text string and are used as special symbols only in the pattern string.

In case you aren’t familiar with regular expressions, the function determines if the text and pattern are the equal, where the '.' is treated as a single a character wildcard (see third example), and '*' is matched for a zero or more sequence of the previous letter (see fourth and fifth examples). For more information on regular expression matching, see the Regular Expression Wikipedia page.

Explain your algorithm, and analyze its time and space complexities.

Examples:

input:  text = "aa", pattern = "a"
output: false

input:  text = "aa", pattern = "aa"
output: true

input:  text = "abc", pattern = "a.c"
output: true

input:  text = "abbb", pattern = "ab*"
output: true

input:  text = "acd", pattern = "ab*c."
output: true
Constraints:

[time limit] 5000ms
[input] string text
[input] string pattern
[output] boolean

time: 8:27 -- 8:58 = 31
time comp: exponential; but can memoize for O(n**2)
space comp:

m(t, p) = 
    base: if no pattern, then true if no string; false otherwise
    if p[1] (or there's no p[1]) not a star: return 1st chars match and m(t[1:],p[1:]))
    else 
        zero to match:
        zero = m(t, p[2:]) --> memo[][ploc+2]
        one = first character matchers and m(t[1:], p)
        return zero or one

func isMatch(...
a
qbcdefg

t = a
p = a*b*

tab[i][j] = true iff t[:i] is matched by p[:j] => res = t[m][n]
t,p = "bar",a*
ans = tab[0][2]
tab[i][0] = False iff i > 0 
t[:i] p[:0]


p = 'a*'
t = 'a'

bar
sheep
tab[2][0] = false

text = '', pattern = 'a*p*c*' =>
  a*p*
 01234
0tftf
1f
2f 
    0        1         2            3
0   t        f         f            f 
1   f   
if a star can get the one before

1   false
2   true
            
for i in range
t[0][j] = t[0][j-2]

'''
from typing import Optional


def isMatch(t, p):
    m, n = len(t), len(p)
    tab = [[False for _ in range(n+1)] for _ in range(m+1)]
    tab[0][0] = True
    for j in range(1,n+1):
        if p[j-1] == '*':
            tab[0][j] = tab[0][j-2]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if p[j-1] != '*':
                tab[i][j] = p[j-1] in (t[i-1],'.') and tab[i-1][j-1]
            else:
                zero = tab[i][j-2]
                one = p[j-2] in (t[i-1],'.') and tab[i-1][j]
                tab[i][j] = zero or one
    # print(tab)
    return tab[m][n]
# t, p = ('', 'b') #false
# print(isMatch(t, p))
#       a
#     0 1
#   0 t f
# a 1 f t
# a 2 f f
# i = [1, 2]
# j = [1, 1] 
# t11
t, p = 'q', 'a' #false
print(isMatch(t, p)) 
t, p = 'aa', 'a' #false
print(isMatch(t, p)) 
t, p = ('aa', 'aa') # true
print(isMatch(t, p)) 
t, p = ('abc', 'a.c') #true
print(isMatch(t, p))
t, p = ('ab', 'ad') #false
print(isMatch(t, p))
t, p = ('abbb', 'ab*') #true
print(isMatch(t, p))
t, p = ('acd', 'ab*c.') #true
print(isMatch(t, p))
t, p = ('abd', 'ab*c.') #false
print(isMatch(t, p))

'''
aa
a.
-> true

aaa
a*b
-> false because of b

pj not equal *
    if si and pj match, advance i and j
    otherwise return false
pj equal *
    try couple things:
        remove the a*: i stays, advance j by 2
        try with one or more a: j stays, adbance i by 1
the result will be s[:i] and p[:j]
can always cache the i, j

p=a*aa => true
    ^
s=, p=a* => true
s=, p=q => false
s=ab,p=ac


aa, 
^
a
^
'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def helper(sidx: int, pidx: int):
            if pidx == n:
                return sidx == m
            if (sidx,pidx) in cache:
                return cache[sidx,pidx]
            # not a *
            if pidx + 1 == n or p[pidx + 1] != '*':
                cache[sidx,pidx] = sidx<m and p[pidx]in(s[sidx],'.') and helper(sidx+1,pidx+1)
                return cache[sidx,pidx]
            # is a *
            zeromatch = helper(sidx,2+pidx)
            morematch = sidx<m and p[pidx]in(s[sidx],'.') and helper(sidx+1,pidx)
            cache[sidx,pidx] = zeromatch or morematch
            return cache[sidx,pidx]

        cache = {}
        m, n = len(s), len(p)
        return helper(0, 0)'''
if fm(si,pj) then move to s_i+1,p_j+1 if pj+1 is not a *
if it is a *, then two branches: 
    1) return ismatch(si,p_j+2) or
    2) return fm(si,pj) and ismatch(s_i+1,pj)

p=b*, s=<empty>
p=<empty>, s=fish

p: .*    b . c
     j          
s: aaa   b e c
      i          
fm=t
'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def isMatch(i, j):
            if j==n:
                return i==m
            if (i,j) in dp:
                return dp[i,j]

            fm=i<m and p[j] in ('.',s[i])
            if j+1<n and p[j+1]=='*':
                zero=isMatch(i,j+2)
                more=fm and isMatch(i+1,j)
                dp[i,j]=zero or more
                return dp[i,j]
            dp[i,j] = fm and isMatch(i+1,j+1)
            return dp[i,j]

        m,n=len(s),len(p)
        dp={}
        return isMatch(0,0)'''
     0 1 2 3 4
     x a a a d e
   x t f f f f f
 0 a . . . . . .
 1 * . . . . . .
 2 d . . . . . .
 3 e . . . . . .
 
aa
a*

a
a*

00
0==2
fm=true
'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def isMatch(si:int,pi:int)->bool:
            if pi==n:
                return si==m
            #there is pattern
            if (si,pi) in dp:
                return dp[si,pi]
            fm_schar=si<m and p[pi] in (s[si],'.')
            #star-case
            if pi+1<n and p[pi+1]=='*':
                none=isMatch(si,pi+2)
                more=fm_schar and isMatch(si+1,pi)
                dp[si,pi]=none or more
                return dp[si,pi]
            #no-star case
            dp[si,pi]=fm_schar and isMatch(si+1,pi+1)
            return dp[si,pi]

        m,n=len(s),len(p)
        dp={}
        return isMatch(0,0)