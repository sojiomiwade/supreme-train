class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left,right=[],[]
        # -- -- ---45  -- - .--  9-- -- --
        #               ------
        nstart,nend=newInterval
        for start,end in intervals:
            if end<nstart:
                left.append([start,end])
            elif start>nend:
                right.append([start,end])
            else:
                nstart=min(start,nstart)
                nend=max(nend,end)
        return left+[[nstart,nend]]+right        