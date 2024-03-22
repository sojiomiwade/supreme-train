'''
3 0 1 -- 0 1 2 3
ra
'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans=0
        for x in itertools.chain(nums,range(len(nums)+1)):
            ans^=x
        return ans