'''
coins 2 4
0 1 2 3 4 5 6 7 8 9 10 11
0 i 1 i 2 i i i i i i  i
'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF=float('inf')
        dp=[INF for _ in range(1+amount)]
        dp[0]=0
        for i in range(1,len(dp)):
            dp[i]=1+min(INF if i-coin<0 else dp[i-coin] for coin in coins)
        return -1 if dp[-1]==INF else dp[-1]
