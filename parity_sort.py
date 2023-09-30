'''
time 12:32 -- 12:44 = 12
3,1,2,4

3 1 2 4
l     
    r

2 1 3
3 1 2 4 8 2
l         r
2         3

   1 2 4
   4 2 1
2 4 1 3
  r l

1 1 2 4
4 2 1 1
    l     
    r
2 4 1 3
    l
  r
move from left until hit an odd (or r) and right until hit even or l,
if l < r, swap a[l] and a[r] and loop again, else break
'''
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        while True:
            while l < r and nums[l] % 2 == 0:
                l += 1
            while l < r and nums[r] % 2 == 1:
                r -= 1
            if l == r:
                return nums
            nums[l], nums[r] = nums[r], nums[l]
