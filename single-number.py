'''
2 2 3 3 6 
constant extra space, linear runtime
just xor the whole thing 
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans=0
        for x in nums:
            ans^=x
        return ans