'''

  l
1 0 1 0 1 | goal 0 | ans 4
r
ans2 1 2 3 4 4 | 14
ans1 1 2 2 3 2 | 10
ans 4
exact sum eq 2 : sum is at most 2 - sum is at most 1

  l
1 1 0 | goal 2 | ans 2
    r
cur 1
ans1 1 1 2 | 4 
ans2 1 2 3 | 6
ans 2
'''
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atmost(goal: int) -> int:
            cur=ans=left=0
            for right in range(len(nums)):
                cur+=nums[right]
                while cur>goal and left<=right:
                    cur-=nums[left]
                    left+=1
                ans+=right-left+1
            return ans

        return atmost(goal)-atmost(goal-1)