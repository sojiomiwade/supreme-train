'''

if merge: => left+right!=ints
    then get merged
return left + merged + right
merged=(min(ints[len(left)][0],s),  max(ints[-len(right)-1][1],e))

s--e                                
left=ints
right=[]
or could have it the other way. 
in these cases, can still do
left+merge+right

left and right can be collected based on s & e

a and b can be (inf,-inf) 
i=len(left) 
j=-len(right)-1

a: first overlapping interval 
b: last overlapping interval
merge is just min(a.left,s),max(b.right,e)
merge
if 
then re
          --- ----  - - -----    -- -- ----          
                                  s-------e
                        s-------e 
    s-------e
s---e
                                            s---e

          --- ----  - - -----    -- -- ----          
    s-------e
left,right=[],[all except first]
[[1,3],[6,9]]
[2,5]
output : [[1,9]]
exp :    [[1,5],[6,9]]

23456789
--- ----
---

  ------6
     2-----
overlaps=>max(ba,bb)-min(ea,eb)>=0
     
    be b
    a---5 6
        c----d
    c----d
c----d
(2,5),(5,7)
overlaps= 5 == or  5
'''
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        s,e=newInterval
        left=[[cs,ce] for (cs,ce) in intervals if ce<s]
        right=[[cs,ce]for (cs,ce) in intervals if e<cs]
        merged=[[s,e]]
        if left+right!=intervals:
            merged=[[min(intervals[len(left)][0],s),
                max(intervals[-len(right)-1][1],e)]]
        return left+merged+right
