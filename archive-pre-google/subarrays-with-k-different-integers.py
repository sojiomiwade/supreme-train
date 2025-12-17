'''
1 2 1 2 3
l
  r
ans1 1 1 1 1 1 | 5
ans2 1 2 3 4 2 | 12
=> ans is 7

at most 5 apples 3 4 5 1 2 5
at most 4 apples 3 4 . 1 2 .

1 2 1 3 | k 2 | ans 3
    l 
      r
count {11 31}
ans2 1 2 3 | 6
ans1 1 1 1 | 3
'''
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        # number of subarrays with at most k distinct elements
        def atMostK(k):
            count = collections.Counter()
            left=ans=0
            for right in range(len(nums)):
                count[nums[right]]+=1
                while len(count)>k:
                    count[nums[left]]-=1
                    if not count[nums[left]]:
                        count.pop(nums[left])
                    left+=1
                ans+=right-left+1
            return ans

        return atMostK(k) - atMostK(k-1)

