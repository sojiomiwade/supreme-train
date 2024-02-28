'''

7 1 5 3 
  l
      r
ans 4

can correct left first before updating max profit
when something lower comes, change left to right
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans=0
        left=0
        for right in range(len(prices)):
            if prices[right]<prices[left]:
                left=right
            else:
                ans=max(ans,prices[right]-prices[left])
        return ans