'''
0 2--
1 3---
2 5-----
3 2--
4 0
index

02 13 25 | 32
           i
go forward as long as the rectangles grow adding idx,height to stack
when we hit something smaller (chi, chh) checkpoint, compute some results
result is max of itself or (chi-topi)*toph
pop stack
push (i-popcount,chh)
at the end, can just add zero to array to flush it of residue result

0 2--
1 3---
2 1-
3 2--
4 0
ans 4
st [  ]
prevh 1
i,curh (30)
topi,toph 01

area is more than it should be
'''
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans=0
        st=[]
        heights.append(0)
        prevh=0
        for i,curh in enumerate(heights):
            if curh>=prevh:
                st.append((i,curh))
            else:
                topi=i
                while st and st[-1][1]>=curh:
                    topi,toph=st.pop()
                    ans=max(ans,(i-topi)*toph)
                st.append((topi,curh))
            prevh=curh
        heights.pop()
        return ans

