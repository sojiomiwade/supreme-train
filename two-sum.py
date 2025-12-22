'''
2 7 11 15 | 9 --> 0 1
el: 7 
ans: 1,0
lookup = {2:0, 7?}
for all els, look for target - el in bag.
    if it's there, return idx(el), and lookup[t-el]
    else-- lookup[el] <- idx(el)
idx el: 2, 4
lookup = {3:0, 2:1, }
ans: 2, 1
nums, target: [3 2 4] 6
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for idx, el in enumerate(nums):
            if target - el in lookup:
                return [idx, lookup[target - el]]
            lookup[el] = idx
        return []