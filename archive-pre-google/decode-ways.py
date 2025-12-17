'''


1 | k
current is sum of
    prior if cur is between 1 and 9
    two priors ago if s[cur-1:cur+1] is bet 10 & 26
    1     1      1    0       6
0 1 10   11     21   02       2 


1110
aaj
kj
12
i
'''
class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)
        dp=[0,1]+[0 for _ in range(n)]
        for i in range(n):
            dp[i+2]= int(1<= int(s[i])<=9)*dp[i-1+2]
            # print(f'foo-{i}-{s[i-1:i+1]}-')
            dp[i+2]+=int(10<=int(s[max(0,i-1):i+1])<=26)*dp[i-2+2]
        return dp[-1]