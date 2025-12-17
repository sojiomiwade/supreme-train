'''
1 2 2 3 3 4 2
  l e l e l g

1 3 2
  l g

1 1 1
'''
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        signs=set()
        for i in range(1,len(nums)):
            if nums[i-1]==nums[i]:
                pass
            elif nums[i-1]<nums[i]:
                signs.add('l')
            else:
                signs.add('g')
        return len(signs)<=1