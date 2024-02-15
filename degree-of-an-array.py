'''
1,2,2,3,1,4,2

2 - minel, maxel
ans is maxel-minel+1

1,2,2,3,1
0 1 2 3 4

2 : 2 - 1 + 1 = 2
1 : 4 - 0 + 1 = 5

1. for each element, if that elem has maximal degree
2. set ans to maximum of ans and maxidx-minidx
3. return ans

now we need three lookups maxi,mini,maxd

0 1 2 3 4
1 2 2 3 1
{12 22 30} maxd <-- should be called degree
2 maxdeg
{10 21 33} mini
{14 22 33} maxi
ans : -inf
'''
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        maxd=Counter(nums)
        maxdeg=max(maxd.values())
        mini={}
        maxi={}
        for i,elem in enumerate(nums):
            if elem not in mini:
                mini[elem]=i
        for i,elem in enumerate(reversed(nums)):
            if elem not in maxi:
                maxi[elem]=n-1-i
        ans=float('inf')
        for elem,deg in maxd.items():
            if deg==maxdeg:
                ans=min(ans,maxi[elem]-mini[elem]+1)
        return ans