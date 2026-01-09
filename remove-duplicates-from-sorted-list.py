# 0 1 1 1 3 3 4 5
#         i
#               j
# 0 1 3 4 5
# start with a[i] val equal to 101, or just from 2nd element
# if a[j] is different from a[i], then i++, a[i] = a[j]
# return i + 1
# 0 1 3 4 5 . . . --> 5

#   1 2 3
#       i
#       j 

# 1  1  2
# 1  2  2
#    li
#       j

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lastindex = 0
        for j in range(1,len(nums)):
            if nums[j] != nums[lastindex]:
                lastindex += 1
                nums[lastindex] = nums[j]
        return 1 + lastindex
