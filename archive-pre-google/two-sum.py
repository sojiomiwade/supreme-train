'''
2 7 11 15 | target 9 | exp [0 1]
0 1  2  3
idxlookup {20 7}
9-7 in idxlookup? yes. then lookitup and return i and il[target-x]
i goes with x

arr 2 7 4 | 9
idx 0 1 2 
il {20 }
[01]
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        il={}
        for i,x in enumerate(nums):
            if target-x in il:
                return [il[target-x],i]
            il[x]=i
        