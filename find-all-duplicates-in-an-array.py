'''
0   1  2  3 4 5  6  7
-4 -3 -2 -7 8 2 -3 -1
ans [2 3]
for a number x, set x to abs(x) if arr[x-1] is negative already, add it to ans
otherwise, make arr[x-1] negative

0  1 2
1 -1 2
ans [1]
'''
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans=[]
        for x in nums:
            x=abs(x)
            if nums[x-1]<0:
                ans.append(x)
            nums[x-1]*=-1
        return ans

