'''
1 ... 8

1 2 0 --> 3

4 1 -1 3
0 1 2 3
ans is the first number not in its place but isn't 0
if all in their place return len(arr)

3 1 2 4
0 1 2 3

1 3 3 3
0 1 2 3

  1 2 3 4
0 1 2 3

1 2 0 4 
    i
0 1 2 3
1 2 3 4
'''
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(len(nums)):
            while 1<=nums[i]<=n and nums[i]!=i+1 and nums[nums[i]-1]!=nums[i]:
                nums[nums[i]-1],nums[i]=nums[i],nums[nums[i]-1]
        
        for i,x in enumerate(nums,start=1):
            if i!=x:
                return i
        return nums[-1]+1

