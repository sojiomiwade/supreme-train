'''
9 9 9 9 
4 9 5
           9
n1=[ ... true]
n2=[     true]
bool arrays. 
if set in n1 and n2, add it to ans

3 1 2
1
idx [0 1 2 3 4]
n1  [f f f f f]
n2  [f f f f f]
runtime is constant. next we do a sort approach
'''
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ARRMAX=1001
        n1=[False for _ in range(ARRMAX)]
        n2=[False for _ in range(ARRMAX)]
        for x in nums1:
            n1[x]=True
        for y in nums2:
            n2[y]=True
        ans=[]
        for i,(x,y) in enumerate(zip(n1,n2)):
            if x and y:
                ans.append(i)
        return ans