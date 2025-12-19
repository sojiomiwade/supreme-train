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

4 9 5
9 4 9 8 4

2
1 2 3

4 5 9
t
b
4 4 8 9 9
if match add it to ans, but only if ans[-1] is not it. advance both ptrs
else advance the smaller
stop. when any array is exhausted
0 1
    t
  b
1 2 3
ans [1]
'''
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        m,n=len(nums1),len(nums2)
        top=bot=0
        ans=[]
        while top<m and bot<n:
            topel,botel=nums1[top],nums2[bot]
            if topel==botel and (not ans or ans[-1]!=topel):
                ans.append(topel)
                top,bot=top+1,bot+1
            elif topel<botel:
                top+=1
            else:
                bot+=1
        return ans
