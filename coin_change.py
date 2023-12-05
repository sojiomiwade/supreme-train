'''
5       2       1
5   2  1
521
                        .
                5       2       1
            5   2  1       5
'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def coinChange(amount:int)->int:
            if amount<0:
                return float('inf')
            if amount==0:
                return 0
            if dp[amount]!=-1:
                return dp[amount]
            mc=float('inf')
            for coin in coins:
                mc=min(mc,coinChange(amount-coin))
            dp[amount]=1+mc
            return dp[amount]
            
        dp=[-1 for _ in range(1+amount)]
        ans=coinChange(amount)
        return -1 if ans==float('inf') else ans