'''
bruteforce: for each i, just count the bits with modulo and div => n lg n
better: 
0 --> 0   
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
6 --> 110
7 --> 111
8 --> 1000
9 --> 1001
10 -> 1010
11 -> 1011
12 -> 1100

dp[i]=dp[i//2] + (i%2==1)
'''
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp=[0 for i in range(1+n)]
        for i in range(1,1+n):
            dp[i]=dp[i//2] + (i%2==1)
        return dp