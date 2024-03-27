'''
10 5 2 6 k=100 --> 8
   l
     r
count 1
prod 100
'''
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count,left,prod=0,0,1
        for right in range(len(nums)):
            prod*=nums[right]
            while prod>=k and left<=right:
                prod//=nums[left]
                left+=1
            count+=right-left+1
        return count