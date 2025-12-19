class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        a = -1
        for valb in nums:
            if valb != val:
                a += 1
                nums[a] = valb
        return a + 1
