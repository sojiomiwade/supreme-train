'''

----
   ----
     -----------
           --------
sort them by start, then combine two if intersection
buf [15 ]
4>=4
'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        buf=[]
        for s,e in intervals:
            if buf and buf[-1][1]>=s:
                buf[-1][1]=max(buf[-1][1],e)
            else:
                buf.append([s,e])
        return buf