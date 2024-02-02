'''

---
    ---
         -
            --------
      -------             <--new
    ---------------      <-- all 3 above replaced with this
find all the intervals i have intersection with and mark them 
tomerge=[a,b,c,new]
new2 is just minstart+maxend
ans=[everything except tomerge + new2]
put intervals into a set. then can now remove a tuple in O(1) time
tomerge must be a set, and this is the only set
ans can be a list
            -
            44
             -
             55
                      1-----5
                       4------9
            ea

123456789
-
  ---
   ------ new
'''
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def overlaps(inta,intb) -> bool:
            ba,ea=inta
            bb,eb=intb
            # return bb<=ba<=eb or ba<=bb<=ea 
            #     ------
            #        -------
            return max(bb,ba)<=min(ea,eb)

        def merge(inta,intb):
            ba,ea=inta
            bb,eb=intb
            return [min(bb,ba),max(ea,eb)]


        n=len(intervals)
        ans=[]
        for idx,interval in enumerate(intervals):
            if interval[1]<newInterval[0]:
                ans.append(interval)
            elif overlaps(interval,newInterval):
                newInterval=merge(interval,newInterval)
            else:
                break
        else:
            idx=n # new is to the right of everything
        
        ans.append(newInterval)

        for sidx in range(idx,n):
            ans.append(intervals[sidx])
        return ans