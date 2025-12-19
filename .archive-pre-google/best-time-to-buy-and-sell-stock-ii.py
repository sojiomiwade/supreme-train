# if you can make a profit between 2 days take it
'''
7 1 5
         
ans=0
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans=0
        for i in range(1,len(prices)):
            ans+=max(0,prices[i]-prices[i-1])
        return ans
        