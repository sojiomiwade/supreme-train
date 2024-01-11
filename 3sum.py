'''
x        0 0                  x
i j k cannot be equal
iterate on each i, then do a 2sum with a j which is greater than i
arr[i], -arr[i] is what the 2sum must equal

-1,0,1,2,-1,-4
 i   j
 z : 1-1=0
 lookup : {0:1,}

 1 ... 2 ... 3 
 i     j
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=set()
        for i,x in enumerate(nums):
            if nums[i]>0:
                break
            lookup={}
            for j in range(i+1,len(nums)):
                z=-x-nums[j]
                if z in lookup:
                    res.add(tuple(sorted([nums[i],nums[j],nums[lookup[z]]])))
                lookup[nums[j]]=j
        return list(res)