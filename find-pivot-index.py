'''
loop idx=0..n-1
    deduct nums[idx] from sumright
    compare sumright to sumleft and return idx if it works
    add nums[idx] to sumleft
return -1


1 7 3 6 5 6
          x
suml is 0 and sumr is the sum of all except the 1st. idx starts at 0
check if suml and sumr equal. return the idx
if idx+1==n return -1
adjust suml to include idx, and sumr to exclude idx+1
advance idx go back to check

3 2 5
  i
suml sumr : 5 5
'''
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n=len(nums)
        suml,sumr=0,sum(nums)-nums[0]
        idx=0
        while suml!=sumr:
            if idx+1==n:
                return -1
            suml+=nums[idx]
            sumr-=nums[idx+1]
            idx+=1
        return idx
