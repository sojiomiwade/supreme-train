'''
[0,1,2,2,3,0,4,2]
     i       j 
[0,1,4,0,3,_,_,2]
come from both sides, and swap; repeat this until cross

leftside stops if val. rightstide if not val. then can swap

3 2 2 3
2 3 2 3
  l
    r
3 2 2 3
2 2 3 3
    l
      r

2 2 3 3
    l
      r
ans 0
'''
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l=0
        for r in range(len(nums)):
            if nums[r]!=val:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
        return l

        # n=len(nums)
        # left,right=0,n-1
        # ans=0
        # while True:
        #     while left<n and nums[left]!=val:
        #         left+=1
        #     while right>=0 and nums[right]==val:
        #         right-=1
        #     if left<right:
        #         nums[left],nums[right]=nums[right],nums[left]
        #         ans+=1
        #     else:
        #         break
        # return sum(1 for x in nums if x != val)