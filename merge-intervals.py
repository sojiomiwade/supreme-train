'''
123
 23456
      -890
          ----5678
sort them by start
[123456,890,5678]
start with an empty result
if incoming merges with last, replace last with merge of it and incoming
return result
complexity: O(n lg n)
'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def merge(inta,intb):
            # ---
            #   ----
            return [min(inta[0],intb[0]),max(inta[1],intb[1])]

        def overlaps(inta,intb):
            #       ------6
            #             6--------
            # max of left ends comes after or equal to min of right ends
            return max(inta[0],intb[0])<=min(inta[1],intb[1])

        intervals.sort()
        ans=[intervals[0]]
        for i in range(1,len(intervals)):
            cur,last=intervals[i],ans[-1]
            if overlaps(cur,last):
                ans[-1]=merge(cur,last)
            else:
                ans.append(cur)
        return ans
