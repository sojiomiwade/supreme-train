'''
1 3 4 2 2
1 4 3
  ^
0 1 2 3 4

iterate on each number
    if number in its place, just move to next number
    otherwise
        find the right number for current idx
            if the same value is already in its place for the other
                numbers, return that specific number
            otherwise: do the swap, repeatedly until we get curidx right 
'''
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while nums[i]!=i+1: # 3 2
                if nums[nums[i]-1]==nums[i]: # [2] == 3
                    return nums[i]
                nums[nums[i]-1],nums[i]=nums[i],nums[nums[i]-1] # =3,4
        raise Exception('duplication shouldve been found')