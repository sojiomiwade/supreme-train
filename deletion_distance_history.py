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



'''
So far the impl is top-down to get the bestres. 
To build the cache, this has to be bottom up (because to
the left is different for different i,j)... so stay tuned
 s
dog
frog
  t
res = -d +f +r o g
all others will be less
put d before f and r because that's the question ask. 

delete from source => increment sidx
add from target => increment tidx

takes exponential => use memo or tab
dog
'''
def diffBetweenTwoStrings(source, target):
    def helper(sidx, tidx, candres, bestres):
        if sidx == m or tidx == n:
            rest = max(n - tidx, m - sidx)
            if not bestres or rest + len(candres) < len(bestres):
                bestres = candres[:]
                for i in range(sidx, m):
                    bestres.append('-' + source[i])
                for i in range(tidx, n):
                    bestres.append('+' + target[i])
            return bestres, rest

        if source[sidx] == target[tidx]:
            bestres, bu_dist = helper(sidx + 1, tidx + 1, candres + [source[sidx]], bestres)
            cache[sidx, tidx] = bu_dist
        else:
            bestres, bu_dist1 = helper(sidx + 1, tidx, candres + ['-' + source[sidx]], bestres)
            bestres, bu_dist2 = helper(sidx, tidx + 1, candres + ['+' + target[tidx]], bestres)
            cache[sidx, tidx] = 1 + min(bu_dist1 + bu_dist2)
        return bestres, cache[sidx, tidx]

    m, n = len(source), len(target)
    cache = {}
    return helper(0, 0, [], None)

source, target = 's', 't'
source, target = 'dog', 'frog'
source, target = "ABCDEFG", "ABDFFGH"  # A B -C D -E F +F G +H
print(diffBetweenTwoStrings(source, target))
# ["A", "B", "-C", "D", "-E", "F", "+F", "G", "+H"
# AB C D E   FG
# AB   D   F FGH
