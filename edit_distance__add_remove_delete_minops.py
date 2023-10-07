'''
6:35 -- 7:01 = 26


horse
ros
replace -> advance on both strings, 
insert -> advance on only word2
delete -> advance on word1

now consider all possibilities. such branching->expo
hence, we can memo the branching

delet 
01234
oh
 t
 b
o
1 + 1
'''
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def branch(oneloc: int, twoloc: int) -> int:
            if oneloc==len(word1):
                return len(word2)-twoloc
            if twoloc==len(word2):
                return len(word1)-oneloc
            if (oneloc,twoloc) in memo:
                return memo[oneloc,twoloc]

            if word1[oneloc] == word2[twoloc]:
                res = branch(oneloc+1, twoloc+1)
            else:
                replace = branch(oneloc+1, twoloc+1)
                insert = branch(oneloc, twoloc+1)
                delete = branch(oneloc+1, twoloc)
                res = 1+min(replace,insert,delete)
            memo[oneloc,twoloc] = res
            return res
        memo = {}
        return branch(0, 0)