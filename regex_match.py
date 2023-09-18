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

