'''
0 1 2 3 4 5 6 7 8 9 0 1 2
1 . . 3 . . 2 . . 3 . . . 3 
                    l 
                          r
let l go overboard ==> be at k-1
left accumulates the new subarrays
'''
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxel=max(nums)
        left=cur=ans=0
        n=len(nums)
        for right in range(len(nums)):
            cur+=nums[right]==maxel
            while cur>=k:
                cur-=nums[left]==maxel
                left+=1
            ans+=left
        return ans
