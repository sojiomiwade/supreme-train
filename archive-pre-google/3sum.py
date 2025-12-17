'''
-1 0 1
     t
target 0
have 0

0 0 0
  t
-1 0 0 1 1
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twosum(idx: int):
            ans,target=set(),-nums[idx]
            have=set()
            for tidx in range(idx+1,n):
                if target-nums[tidx] in have:
                    ans.add(tuple(sorted([-target,target-nums[tidx],nums[tidx]])))
                have.add(nums[tidx])
            return list(ans)

        ans,n=[],len(nums)
        nums.sort()
        prev=None
        for idx,x in enumerate(nums):
            if x>0:
                break
            if prev is None or prev!=x:
                print(idx)
                ans.extend(twosum(idx))
                prev=x
        return ans
        