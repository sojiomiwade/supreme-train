'''


5 8 9 3

5
3 8 9

0 1 9 8 2 3 4 5
0 1 2 

approach: delete first then comeback

0 5 8 9 3 4 5 11
----------------
  5 8 9 
0 3 4 5 11

max 4
init all to one to start with

outer loop goes from last to first: i: n-1 .. 0
    inner loop leverages dp if it can: j > i
    inner loop find j such that a[j]>a[i]
    then set dp[i] to 1+dp[j] 

nums 0 1 0 3 2 3
dp   1 1 3 1 2 1
         i
             j


nums 0 1 0 3 2 3
     1 2 . . . . 

9,8,2,5,3,7,101,18

9
8 5   101 
2 3 7 18
if bisect-left is the length of the array, then append

nusm [3 0 4]
ans [0 1]
'''
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        ans=[]
        for x in nums:
            pos=bisect.bisect_left(ans,x)
            if pos==len(ans):
                ans.append(x)
            else:
                ans[pos]=x
        return len(ans)
