'''
dp[]=dp[]
        4
     3       2       1
     2 1 0   1 0     0

      1    2
          1
          1
1 1,2,3

1 2 3

1 1 1
1 2
2 1


0 1 2 3 4
1 1 2 4 7 

dp[4] = dp[3] if (4-3) in snums
dp[i] = sum(dp[i-x] for x in nums)

dp[4] = dp[4] if (4-4) in snums

dp[3]=dp[3-1] + dp[3-2] + dp[3-3]
1 1 1
1 2
3
2 1

2
1 1

1


1 1 1 1
1 1 2
1 2 1
1 3
2 1 1
2 2
3 1

1 1
2
dp[4] = 
    dp[3] + 1
    dp[2] + 2
    dp[1] + 

dp[2-1] + , dp[2-2], dp[2-3]

7 + {1,2,3}
71 72 73
1111
112
112
snums {123}
idx 0 1 2 3 4
dp  1 0 0 0 0

'''
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp=[0 for _ in range(target+1)]
        dp[0]=1
        snums=set(nums)
        for i in range(1,1+target):
            dp[i] = sum(dp[i-x] for x in snums if i-x>=0)
        return dp[target]
        # def cs(rem):
        #     if rem<=0:
        #         return int(rem==0)
        #     if rem in dp:
        #         return dp[rem]
        #     dp[rem]=sum(cs(rem-x) for x in nums)
        #     return dp[rem]
        # dp={}
        # return cs(target)
        