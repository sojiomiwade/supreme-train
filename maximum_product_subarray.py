'''
2 3  -2 44
2 6 -24 44
  6.    44

2 3  -2    2   2   -1  -2
2 6 -12  -24 -48   48  -96
  6                48. 

-2 | 0 -1
-2 | 0 0

summary: always aggregate the product, but always update the best
0 2

3 | -1 4
       ^
agg=-12
pos=4
res=3

2 3 -2 4
    ^
agg -48 
pos 4
res 6

-2 0 -1

0 2
  ^
agg 0
pos -inf
res 0

2,-5,-2,-4,3
agg
pos
res

output=20
exp=.  24
'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        agg=nums[0]
        pos=float('-inf') if agg <= 0 else nums[0]
        res=max(pos,agg)
        n=len(nums)
        for i in range(1,n):
          agg*=nums[i]
          if nums[i]>0:
            if pos == float('-inf'):
              pos=1
            pos*=nums[i]
          else:
            pos=float('-inf')
          res=max(pos,agg,res)
        return res
