'''
10 9  2  5  3  7  25 18
10 25
9 25
2 5 7 25
2 3 7 25
2 3 7 25

2, 6, 8, 3, 4, 5, 1 2 6 6
-        -  -  -
[2 3 8]
bisect left, so existing number is overwritten
if ans == n, then append
2 3
max=3
'''

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans=[]
        for num in nums:
            idx=bisect.bisect_left(ans,num)
            if idx==len(ans):
                ans.append(num)
            else:
                ans[idx]=num
        return len(ans)

