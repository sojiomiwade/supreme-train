class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n=len(nums)
        count=0
        for i in range(n):
            prefix=0
            for j in range(i,n):
                prefix+=nums[j]
                if prefix==goal:
                    count+=1
        return count