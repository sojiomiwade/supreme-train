class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        need location here so we can return result
        2 11 7  15
        2:0, 11:1, 7
        '''
        loclookup={}
        for i,x in enumerate(nums):
            if target-x in loclookup:
                return [i,loclookup[target-x]]
            loclookup[x]=i
        raise ValueError('bad input')
        