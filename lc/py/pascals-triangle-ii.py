# 0: 1 0 0 0 0
# 1: 1 1 0 0 0
# 2: 1 2 1 0 0 -- 1 up-dependent change required
# 3: 1 3 3 1 0 -- 2 up-dependent changes required
# 4: 1 4 6 4 1 -- 3 changes required
# allocate a[rI+1]
# loop i for each row: 0..rI
#     ans[i] = 1
#     loop: j = rI - 1; j > 0 ; j--
#         ans[j] = ans[j] + ans[j-1]
# return ans
# ri = 4
# ans = [1 2 1 1 1]
# rI: 2
# ans [1 2 1]
#          i
from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [0 for _ in range(rowIndex + 1)]
        for i in range(1 + rowIndex):
            ans[i] = 1
            for j in range(i-1,0,-1):
                ans[j] += ans[j-1]
        return ans
