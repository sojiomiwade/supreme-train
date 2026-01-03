# ([]){}
# ([)]
# push if left, pop if right and matches;  return true if st is empty. false otherwise
# optimization: right not match can return false because will never match
# (]
# t [ ( ]
class Solution:
    def isValid(self, s: str) -> bool:
        lefts = "[({"
        t = [] 
        for ch in s:
            if ch in lefts:
                t.append(ch)
            else:
                if t and t[-1]+ch in ("[]","()","{}"):
                    t.pop()
                else:
                    return False
        return not t