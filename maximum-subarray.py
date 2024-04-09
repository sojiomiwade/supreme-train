'''
        --------
-2 1 -3 4 -1 2 1 -5 4
-2 1 -2 4  3 5 6  1 5   
        L      R

'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans=nums[0]
        prev=float('-inf')
        for x in nums:
            if prev<0:
                prev=x
            else:
                prev+=x
            ans=max(ans,prev)
        return ans