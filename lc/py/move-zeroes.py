# 0 1 0 2 -- 1 2 0 0
# 1 2 0 0
#     i
#       j

# 1 0 2
# 1 2 2
#     i
#     j
# leave i where you'll place the next nonzero
# j will iterate: if a[j] is nonzero, move it to i pos and increment i
# from i onward set that to zero
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i, n = 0, len(nums)
        for j in range(n):
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1
        for j in range(i,n):
            nums[j] = 0
        