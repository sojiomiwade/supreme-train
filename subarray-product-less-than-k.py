'''
0  1 2 3 4
5 5 2 6 4
l
r

1 + 2 + 3 + 4 + 5

5 2 3 | k 3 |
  l
  r
prod 1
ans 0
'''
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left,prod,ans=0,1,0
        for right in range(len(nums)):
            #ensure ok window
            prod*=nums[right]
            while prod>=k and left<=right:
                prod//=nums[left]
                left+=1
            ans+=right-left+1
        return ans
