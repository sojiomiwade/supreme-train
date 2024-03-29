'''
3 1 3 4 2
0 1 2 3 4

slow 0  
fast 0
'''
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow=fast=0
        while not slow or slow!=fast:
            slow=nums[slow]
            fast=nums[nums[fast]]
        slow=0
        while slow!=fast:
            slow=nums[slow]
            fast=nums[fast]
        return slow