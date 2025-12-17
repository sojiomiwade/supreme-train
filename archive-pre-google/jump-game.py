'''

arr 2 3 1 1 4
idx 0 1 2 3 4
            ^
mi 4
update maxidx as you go to max of itself and i+arr[i]
if at any idx maxidx<curidx return False
if idx==n-1 return True
       6
maxidx 5

'''
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mi=0
        for i,x in enumerate(nums):
            if mi<i:
                return False
            mi=max(mi,i+nums[i])
        return True