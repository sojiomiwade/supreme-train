#rob(i)= nums[i]+rob(i+2) OR rob(i+1)
#pass back inf if (i)first_is_there and (ii)i==n-1
# 1 2 3 4
#    fu2   fu1   
# 0  0     1    2   3  4
'''
5 7 3

rob[1]=max(nums[1],nums[2])
if n==1:
    return 1
if n==2
    retrun max(nums[0],nums[1])
fu2=False
fu1=true if nums[0]>nums[1] else false
rob[0]=nums[0]

repeat for all i in 2..n-1
    numsi=0 if i==n-1 and fu2. otherwise, it's just nums[i]
    prof_with_i=numsi+rob[i-2]
    prof_without_i=rob[i-1]
    rob[i]=max(prof_with_i,prof_without_i)
    cur=fu2 if prof_with_i>prof_without_i else fu1
    fu2,fu1=fu1,cur

does the cur robbery i make involve the first house
fu      t   f   t   f  f
rob     0   0   2   3   (0+2,3)
nums            2   3   2
hidx            0   1   2

fu      t   f   
rob     0   0   
nums            1   2   3
hidx            0   1   2
ans should be 3
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        fu2,fu1=True,False
        rob=rob1=rob2=0
        for i in range(n):
            if i==n-1 and fu2:
                rob_with_i=max(nums[i],rob2)
            else:
                rob_with_i=nums[i]+rob2
            rob=max(rob_with_i,rob1)
            cur=fu2 if rob_with_i>rob1 else fu1
            rob2,rob1=rob1,rob
            fu2,fu1=fu1,cur
        return rob

    # def rob(hasfirst: bool, hidx) -> int:
    #     if hidx>n-1 or (hidx==n-1 and hasfirst):
    #         return 0
    #     if (hasfirst,hidx) in dp:
    #         return dp[hasfirst,hidx]
    #     dp[hasfirst,hidx]=max(rob(hasfirst,hidx+2)+nums[hidx],rob(hasfirst,hidx+1))
    #     return dp[hasfirst,hidx]

    # n=len(nums)
    # dp={}
    # return max(rob(True,2)+nums[0],rob(False,1))
    