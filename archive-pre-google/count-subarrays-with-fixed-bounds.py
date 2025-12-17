'''
3 1 5 2
1 5 2
1 5
3 1 5

similar to finding the all subarrays where el has frequency k
 1 2 3 2 1 3 1 3
             l
               r 
  0 1 2 3 4 5 
  3 1 5 2 7 5
      r 
            b
    n
      x
res 2 2
'''
class Solution:
     def countSubarrays(self, A: List[int], minK: int, maxK: int) -> int:
        res = 0
        n = x = b = -1
        for r,cur in enumerate(A):
            if not minK <= cur <= maxK:
                b = r
            else:
                if cur == minK:
                    n = r
                if cur == maxK:
                    x = r
            res += max(0, min(n, x) - b)
        return res