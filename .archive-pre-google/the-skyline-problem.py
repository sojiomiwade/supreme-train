'''
if max height changes, record it in final result
a height could not start off as zero, if it could
we would just use -inf as res start

note that if 2 ends meet (end and begin), we pick the begin
this way, we can remove it when heights are the same
if the heights were differrent it wouldn't matter. 
so for l,r,h, we have l,-h,r and r,0,0
-h allows tall buildings to go first on x-tie
a tie on the ends means beginnings go first. allowing similar height building
to not have two end ppoints

r in lhr doesn't change anything (could have used -r)
but it allows us to preserve this r in tuple to add it into heap

x   nh r
[12 0  0]
       nh   r 
heap [[ 0 inf]]
ans [[42,-inf] [2 10] [3 15] ... [7 12] ]
'''
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        ans=[[42,'-inf']]
        events= sorted(
            [(l,-h,r) for l,r,h in buildings] +
            [(r,0,0) for _,r,_ in buildings]
        )
        mh=[(0,float('inf'))]
        for x,nh,r in events:
            while x>=mh[0][1]:
                heapq.heappop(mh)
            if nh:
                heapq.heappush(mh,(nh,r))

            curheight=-mh[0][0]
            if ans[-1][1]!=curheight:
                ans.append([x,curheight])
        return ans[1:]