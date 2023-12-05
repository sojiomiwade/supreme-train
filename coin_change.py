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
        return -1 if ans==float('inf') else ansclass Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        COIN_MAX=float('inf')
        dp=[COIN_MAX for _ in range(amount+1)]
        for coin in coins:
            if coin<=amount:
                dp[coin]=1
        dp[0]=0

        for subamount in range(1+amount):
            if dp[subamount]==COIN_MAX:
                for coin in coins:
                    if subamount-coin>0:
                        dp[subamount]=min(dp[subamount],dp[subamount-coin])
                dp[subamount]+=1
        return dp[amount] if dp[amount]!=COIN_MAX else -1