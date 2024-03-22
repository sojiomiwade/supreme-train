'''
count starts at 1
when cannot burst, increment count
and start bursting again
.01234567890123456
  --
    --
      --
        --


3         -------
1  -------
0 -----7
     --7
2      78-----
2balloons
count starts at 1
when cannot burst, increment count
and start bursting again
 ---
  ----
.       ----
count 2
cs ce -- last one       
'''
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        count=1
        cs,ce=points[0]
        i,n=1,len(points)
        while i<n:
            while i<n and points[i][0]<=ce<=points[i][1]:
                i+=1
            if i<n:
                count+=1
                cs,ce=points[i]
                i+=1
        return count