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
        
