'''
13=3, 22=4, 31=3
    l
      r
1 2 4 3
  l   r -> 4

'''
class Solution:
    def maxArea(self, height: List[int]) -> int:
        def area(l: int, r: int) -> int:
            areaheight = min(height[l], height[r])
            width = r - l
            return width * areaheight

        left, right = 0, len(height) - 1
        res = 0
        while left < right:
            res = max(res, area(left, right))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return res
