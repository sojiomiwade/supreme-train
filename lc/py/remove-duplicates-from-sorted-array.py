# 1 1 2 3 3 4 5 5 5 9 --
# 1 2 3 4 5 9
#           l 
#                   r
# 1
# l
#   r
# if al = ar: move l, then a[l] = a[r]
# at the end return l + 1
# 1 2 2
# 1 2
#   l
#     r
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        for r in range(1, len(nums)):
            if nums[l] != nums[r]:
                l += 1
                nums[l] = nums[r]
        return 1 + l