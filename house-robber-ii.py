'''
1 | 2 3 2 | 5
solve it like 5 is not there
solve it like 1 is not there
3+5=8

1 2 3 2 5 <-- even odd length of array doesn't matter 
           0
        /     \
       2       1
     /   \    / \
    x     y  3   2
what is 'it'?
rob
rob(i)=nums[i]+rob(i+2) or rob(i+1)
now can do this 

2 3 2
i
rob(0 1)
dp {}
            0
        /1+     \3
       2         1 
     /   \      / \0
    4     3 (0)3   2

rob(1 2)
dp {}

'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob(idx: int, last: int):
            if idx>last:
                return 0
            if idx in dp:
                return dp[idx]
            dp[idx]=max(nums[idx]+rob(idx+2,last),rob(idx+1,last))
            return dp[idx]
        
        if len(nums)==1:
            return nums[0]
        dp={}
        n=len(nums)
        max1=rob(0,last=n-2)
        dp={}
        max2=rob(1,last=n-1)
        return max(max1,max2)