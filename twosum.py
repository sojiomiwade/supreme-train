'''
no sort
keep comp[x] as you go. 
and along the way, once you see comp[x], we are done
let comp[x] = idx of x
then we can return [idx[x], curr-idx]
time: O(n)
space: O(n)

sort: 
time: Omega(n lg n) 
space: O(1)
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp = {}
        for idx in range(len(nums)):
            if nums[idx] in comp:
                return [idx, comp[nums[idx]]]
            comp[target-nums[idx]] = idx
'''
comp = {7: 0, }
retval = [1, 0]
'''
