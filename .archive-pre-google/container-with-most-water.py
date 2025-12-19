'''
8 3 7
0 1 2
l
  r
ans=2*7=14
candans=3
'''
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left,right=0,len(height)-1
        ans=0
        while left<right:
            candans=min(height[left],height[right])*(right-left)
            ans=max(ans,candans)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return ans