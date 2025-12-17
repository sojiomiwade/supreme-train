'''
0 1 2 3 4 5
2 3 1 2 4 3
        l
          r
sum_ 7
al,ar (2 4)
'''
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum_=left=0; al=-1; n=len(nums); ar=n
        for right in range(n):
            sum_+=nums[right]
            while sum_>=target:
                if right-left<ar-al:
                    al,ar=left,right
                sum_-=nums[left]
                left+=1
        if al!=-1:
            return ar-al+1
        return 0