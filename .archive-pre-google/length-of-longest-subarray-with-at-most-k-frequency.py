'''
2 1 . . . . 3 1 2 3 1 2 
l--> 
              r
'''
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        l,n,ans=0,len(nums),0
        count=collections.Counter()
        for r in range(n):
            count[nums[r]]+=1
            while count[nums[r]]>k:
                count[nums[l]]-=1
                l+=1
            ans=max(ans,r-l+1)
        return ans

