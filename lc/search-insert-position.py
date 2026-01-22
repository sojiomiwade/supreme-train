class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        lo, hi = 0, n - 1
        while lo <= hi:
            mi = lo + (hi - lo) // 2
            if nums[mi] < target:
                lo = mi + 1
            else:
                hi = mi -1
        return lo