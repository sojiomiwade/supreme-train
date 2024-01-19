#rob(i)= nums[i]+rob(i+2) OR rob(i+1)
#pass back inf if (i)first_is_there and (ii)i==n-1
# 1 2 3 4
#    fu2   fu1   
# 0  0     1    2   3  4
'''
5 7 3
            fu2   fu1
   0    0    2    3   2   5
             0    1   2   3
fu1=fu2=None
repeat for all i in 0..n-1
    numsi=0 if i==n-1 and fu2. otherwise, it's just nums[i]
    prof_with_i=numsi+rob[i-2]
    prof_without_i=rob[i-1]
    if i==0
        cur=true
    elif i==1
    if prof_with_i > prof_without_i
        cur=false if i==0 else (true if i==1 else fu2)
    else
        cur=fu1
        fu1=fu1 if i!=0 else fu1=
    rob[i]=max(prof_with_i,prof_without_i)

    if i==n-1, 
    numsi=0, but if fu2 is false, then numsi=nums[i]

    fu1_old=fu1
    fu1=if we use i,      then {fu1=fu2 if fu2 else if i==0 then f, if i==1 then t},
        if we don't use i then {fu1=fu1 if i!=0 else fu1=}
    fu2=fu1_old
    
    rob[i]=max(numsi+rob[i-2],rob[i-1])
'''
# if hidx==n-1 and firstused then numsi = 0
class Solution:
def rob(self, nums: List[int]) -> int:
    n=len(nums)
    fu1=fu2=F
    for i in range(n):
        if i==0:
            firstused=
        rob[i]=max(nums[i]+rob[i-2],rob[i-1])

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
    