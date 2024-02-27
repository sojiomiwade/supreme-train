'''
1 0 0 0 0 1,2,2,3,,4
^ ^     
    i
ans=None
maxdeg=-inf
loop the array on
    update deg[cur] and first[cur]
    if deg[cur] is more than maxdeg
        update ans to i-first[cur]
        maxdeg=deg of cur
    elif deg[cur] == maxdeg
        ans=min(ans,i-first[cur])

maxdeg
also now update maxdeg to max(deg[cur],maxdeg)
if current element has highest degree so far, then update ans to i-first[cur]
also need to track deg[cur]
0 1 2 3
1 0 1 0
      i
deg 02 12 
first 01 10
maxdeg 2
ans 3
'''
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        ans,maxdeg=None,float('-inf')
        deg,first=Counter(),{}
        for i,cur in enumerate(nums):
            deg[cur]+=1
            first.setdefault(cur,i)
            if deg[cur]>maxdeg:
                maxdeg=deg[cur]
                ans=i-first[cur]+1
            elif deg[cur]==maxdeg:
                ans=min(ans,i-first[cur]+1)
        return ans
