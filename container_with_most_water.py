'''
first: consider all a and b: O(n**2) time
second: slide but not from left, but both sides
'''
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        l,r=0,n-1
        ans=-1
        while l<r:
            hl,hr=height[l],height[r]
            cur=min(hl,hr)*(r-l)
            ans=max(cur,ans)
            if hl<hr:
                l+=1
            else:
                r-=1
        return ans
