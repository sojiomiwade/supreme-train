'''
cc(11)= 1 + min(cc(1),cc(2),cc(5))
if change<=0 return int(change==0)
will need dp because multiple ways you can get an amount x

tabulation
0 1 2 3 4 5 6 7 8 9 10 11
0 1 1 0 0 1 0 0 0 0  0  0
dp [0]
cc[i]=
3 -- 1 2
4 -- 2 2
5 -- 1
6 -- dp[5]+dp[1] -- 2
    dp[6-1],dp[6-2],dp[6-5]
7 -- dp[5]+dp[2] -- 7 
8 -- dp[]
dp[4] = 1+dp
dp[11] -- will consider holding a 5 2 and 1 coin
coins [2] | amount 3
dp [0 0 1 0]
    0 1 2 3
'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF=float('inf')
        coinsset=set(coins)
        dp=[1 if x in coinsset else 0 for x in range(1+amount)]
        for cur in range(1,1+amount):
            dp[cur]=1+min((dp[cur-coin] for coin in coins if cur-coin>=0),default=INF)
        return dp[amount] if dp[amount] < INF else -1