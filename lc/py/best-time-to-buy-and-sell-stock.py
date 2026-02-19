from typing import List
# 7 1 5 3 6 4
#   -------

# 7 3 5 1 6 4
#   ---
#   m x i <-- new min (but still ii remember my maxp)
# always update the max
# but only after you have updated the min 
# 5     4     3       8  11  1  3
#             minp 
# xp = 0
# 1 3 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        minp = prices[0]
        for i in range(1, len(prices)):
            minp = min(prices[i], minp)
            maxp = max(maxp, prices[i] - minp)
        return maxp
        
