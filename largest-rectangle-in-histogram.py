'''
2 5
    r
[]   nondec
5 prev
5 ans
5*(2-1)
2*(2-0)

--
-
--
2 1 2

'''
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        nondec,ans,n=[],float('-inf'),len(heights)
        for r in range(n):
            width=1
            idx=r
            while nondec and nondec[-1][0]>heights[r]:
                h,idx=nondec.pop()
                ans=max(ans,h*(r-idx))
            nondec.append((heights[r],idx))

        r=n
        while nondec:
            h,idx=nondec.pop()
            ans=max(ans,h*(r-idx))
        return ans

            