'''
0    123456
1     2345678
2          789012
            8
            8
3             0123456
loop on the array
    eat until you can't anymore.

0 1 2 3 
l
r
count 0
[[1,2],[3,4],[5,6],[7,8]]
     v
    --
    ------
       -----
          ----
     ------------
0 12
1   34
2     56
3       78
'''
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        count=0
        pos=float('-inf')
        for s,e in points:
            if pos<s:
                pos=e
                count+=1
        return count