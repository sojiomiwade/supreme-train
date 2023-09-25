'''
       v
     ABC "
     ABD  ==target
        ^
       
     A, B, -C, +D = ABC -C
     A, B, +D, -C = ABC +D
     
     
     , and target = "ABDFFGH"
     
     
  AB +/-C CDEF
  ABGDCDGGH
  add or remove s[0]
  add t[0]
  
     v
AB-C-D-E-F+FGH
AB   DFFGH
        ^
["A", "B", "-C", "D", "-E", "F", "+F", "G", "+H"]

        
       /res
    x,y -- res
      \ res

  v    
ABCD
ABD
  ^
A
A
[A]
'''
def diffBetweenTwoStrings(source, target):
  def helper(s, t, res):
    if not s:
      return res + ['+' + ch for ch in t]
    if not t:
      return res + ["-" + ch for ch in s]

    res_same = res_remove_from_s = res_add_from_t = None
    if s[0] == t[0]:
      res_same = helper(s[1:], t[1:], res + [s[0]])
    else:
      res_remove_from_s = helper(s[1:], t, res + ["-" + s[0]])
      res_add_from_t = helper(s, t[1:], res + ["+" + t[0]])
    return min(res_same, res_remove_from_s, res_add_from_t,
                  key=lambda x: float("inf") if not x else len(x)) #
  return helper(source, target, [])

s = "ABCDEFG"
t = "ABDFFGH"
print(diffBetweenTwoStrings(s, t))


# trying to memoize and clean up the recursive calls
from typing import List, Optional

from typing import List


def diffBetweenTwoStrings(source, target) -> List[str]:
  def helper(sloc: int, tloc: int) -> None:
    # 0, 0; 1,0
    nonlocal bestres
    if sloc == len(source) or tloc == len(target):
        rest1 = ['+' + target[tloc] for i in range(tloc, len(target))]
        rest2 = ["-" + source[sloc] for i in range(sloc, len(source))]
        if not bestres or len(res)+len(rest1)+len(rest2) < len(bestres):
            bestres = res[:] + rest1 + rest2
        return 

    if source[sloc] == target[tloc]:
      res.append(source[sloc])
      helper(1 + sloc, 1 + tloc)
      res.pop()
    else:
      res.append("-" + source[sloc]) #res = [ -A 
      helper(1 + sloc, tloc)
      res.pop()
      res.append("+" + target[tloc])
      helper(sloc, 1 + tloc)
      res.pop()

  res = []
  bestres = None
  helper(0, 0)
  assert bestres
  return bestres

# source = "ABCDEFG"
# target = "ABDFFGH"
#
source = 'AB'
target = 'CA'
#output
#
print(diffBetweenTwoStrings(source, target))
