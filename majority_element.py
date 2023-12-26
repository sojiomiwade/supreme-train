'''
2 2 1 1 1 2 2
1 1 1 2 2 2 2
0 1 2 3 4 5 6
7//2 = 3


1 1 2 2 2 2
0 1 2 3 4 5
6//2=3

'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
       nums.sort()
       return nums[(len(nums))//2] 
