# flight
# flow
# flower
# count = 0
# for i = 0 .. n
#     fin = true
#     for j = 0 .. m -1
#         if a comparison fails
#         fin = false
#         break
#     if j loop finished
#         count += 1
# return strs[0][0:count]
# --> mn
# mn lg m 


# flo
# fi
# i j fin | 1 0 F
# count, m, n | 1 2 2
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = min(len(s) for s in strs)
        count, m = 0, len(strs)
        for i in range(n):
            fin = True
            for j in range(m-1):
                if strs[j][i] != strs[j+1][i]:
                    fin = False
                    break
            if fin:
                count += 1
            else:
                break
        return strs[0][:count]