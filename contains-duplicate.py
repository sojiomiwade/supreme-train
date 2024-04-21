class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count=Counter(nums)
        return any(x>1 for x in count.values())