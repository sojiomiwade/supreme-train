from typing import List


# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

# On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

# Find and return the maximum profit you can achieve.

 

# Example 1:

# Input: prices = [7,1,5,3,6,4] --> 
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
# Total profit is 4 + 3 = 7.

# Example 2:

# Input: prices = [1,2,3,4,5] = 4, 
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
# Total profit is 4.

'''
y        x
left
      right

12345
 l
    r

left = 0 
for right in [left, n)
    if prices[right] < prices[left]
        left = right
    profit = max (profit, prices[right] - prices[left])
return profit

brute force -->
    for i 0..n
        profit = 0
        for j in (i, n)
            profit += prices[j] - prices[i] <-- positive
1,5 + 1,6

all combinations of (i,j)
1,5 <--
3,6

[7,1,5,3,6,4] --> 1,6
'''

def maxprofit(prices: List[int]) -> int:
    # profit = left = 0
    # # O(n)
    # for right in range(len(prices)):
    #     if prices[right] < prices[left]:
    #         left = right
    #     profit = max(profit, prices[right] - prices[left])
    profit = 0
    for i in range(len(prices)-1):
        profit += max(0, prices[i+1]-prices[i])
    return profit

prices = [1,2,3,4,5]
print(maxprofit(prices)) # 4

prices = [7,1,5,3,6,4]
print(maxprofit(prices)) # 7 but will give 5 
'''
brute force
find each valid combination 
0 bs 0 b s 0
0 b  0 b s s <- invalid since we buy twice before selling
3**n

better
buy then sell once higher. 
7  1 5 3 6 4
bs b s b s .
       s   c

buy if next day is worse, then sell with curr day and update profit
    cur

otherwise move day to the next

don't forget to collect the last day's profit
1 5
  c
  s

1 5 4 6 
      c
    s
p 4
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        c=s=0
        n=len(prices)
        p=0
        while c < n-1:
            if prices[c] < prices[c+1]:
                c+=1
            else:
                p += prices[c]-prices[s]
                c=s=c+1
        p += max(0,prices[c]-prices[s])
        return p