'''
0 1 2 3 4 5 6 7 8
4,3,2,7,8,2,3,1
1 2 3 4 . . 7 8 

[3 2]
try to put each element in the right place
anything that can't go, put it in ans, then advance

0 1 2
1 1 2 --> [1]
    ^
ans []
1 == 
'''
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans=set()
        for i in range(len(nums)):
            while nums[i]!=i+1: # 2 3
                if nums[nums[i]-1]==nums[i]: # n[1] n[2]
                    ans.add(nums[i])
                    break
                else:
                    nums[nums[i]-1],nums[i]=nums[i],nums[nums[i]-1] #n[1],n[2]
        return list(ans)