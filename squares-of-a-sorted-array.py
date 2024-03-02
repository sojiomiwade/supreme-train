'''
-3 -2 2
'''
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=len(nums)
        left,right=0,n-1
        ans=[]
        for i in range(n):
            if abs(nums[left])>abs(nums[right]):
                ans.append(nums[left]**2)
                left+=1
            else:
                ans.append(nums[right]**2)
                right-=1
        return list(reversed(ans))
        