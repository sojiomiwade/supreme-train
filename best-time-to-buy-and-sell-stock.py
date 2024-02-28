'''
first: for all i,j i<j, maxprofit is the max of pj-pi: O(n**2)
2nd: sliding window for O(n)?
    a guy behind cannot have potential for max profit (against some future)
    if something in between is lower.
    so update left when lower than left is seen.
    meanwhile all the while increment right
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left=0
        maxprofit=profit=0
        for right in range(len(prices)):
            if prices[right]<prices[left]:
                left=right
            profit=prices[right]-prices[left]
            maxprofit=max(maxprofit,profit)
        return maxprofit