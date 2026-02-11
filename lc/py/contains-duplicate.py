# 4 1 8 3 1 4 1
# fill a counter map: time, space: O(n), O(n)
# sort, then see if two neighbors are the same -- time space: O(n lg n), O(n)

# 1 2 3
#   i
# i iteratates on 0 1
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        sn = sorted(nums)
        for i in range(len(sn) - 1):
            if sn[i] == sn[i+1]:
                return True
        return False
        # return len(nums) != len(set(nums))