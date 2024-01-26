class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''
        0 1 2 x 4
        0 1 2 3 4
        '''
        ans = 0
        for x in itertools.chain(nums, (i for i in range(len(nums) + 1))):
            ans ^= x
        return ans