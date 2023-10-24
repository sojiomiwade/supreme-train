'''
  -------
7,1,5,3,6,4
  l     r 

brute force of course at O(n**2) by considering all i,j i < j
sliding window:
move r unconditionally through array
if price at anytime is lowest it could be update l to that
always calculate maxprofit as the better of current max and profit(l,r)

7,1,5,3
  l
      r
max=0,4

'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = -1
        left = 0
        for right in range(len(prices)):
            if prices[right] < prices[left]:
                left = right
            maxprofit = max(maxprofit, prices[right] - prices[left])
        return maxprofit