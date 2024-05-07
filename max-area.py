'''
Reference: https://www.geeksforgeeks.org/problems/max-rectangle/1
2   -1  3   4   0
.   .   .   .   .
.   .   .   .   .
.   .   .   .   .

2 -1 3 4 0

  l     r
 -5  2 -5  3  4 x 
  2 -1 -1 -5 -3 y
 -3  2 -5 -4  3 z
  2  2  1  4 -5 a

top,bot,left,right

-1  -5  2  -3  2  1 
 p  -5 
        c
     l

-5 2 -1 2 3 
          r
        l
2 best
1,1 : ml,mr
if cur won't take the dp, set l to r
regardless update ml,mr to l,r if the dp value there
is better than best
3 4 expected
? ? got  
maximum subarray 
'''
from typing import List, Tuple


def msa(arr: List[int]) -> Tuple[int,int,int]:
    ml=mr=None
    INF=float('inf')
    maxval=-INF
    n=len(arr)
    dpprev=-1
    l=None
    for r in range(n):
        if dpprev<0:
            l=r
            dpcur=arr[r]
        else:
            dpcur=dpprev+arr[r]
        if dpcur>maxval:
            ml,mr=l,r
            maxval=dpcur
        dpprev=dpcur
    # assert None not in (ml,mr)
    assert ml is not None and mr is not None and type(maxval) is int
    # print(arr,ml,mr,maxval)
    return ml,mr,maxval

def maxarea(arr: List[List[int]]) -> Tuple[int,int,int,int]:
    m,n=len(arr),len(arr[0])
    aux=[0]*m
    ml=mr=mt=mb=None
    INF=float('inf')
    maxval=-INF

    for l in range(n):
        for r in range(l,n):
            aux=[aux[i]+arr[i][r] for i in range(m)]
            t,b,cur=msa(aux)
            if cur>maxval:
                ml,mr,mt,mb=l,r,t,b
                maxval=cur
        aux=[0 for _ in range(m)]
    assert  None not in (ml,mr,mt,mb,maxval)
    return mt,mb, ml,mr,maxval

# arr=[[-5, 2, -1, 2, 3 ]]
# print(msa(arr))
# print(maxarea(arr))
from random import randrange as rr,seed
m,n=4,5

# s='''
#.  l.    r
#   3  1  4 -4 -3
#   2 -5 -1 -2 -2
#   2  0 -2 -3 -4
#  -4  0  0 -5  3
# '''
# vals=s.split()
# iv=iter(vals)
# arr=[[0]*n for _ in range(m)]
# for i in range(m):
#     for j in range(n):
#         arr[i][j]=int(next(iv))
# for i in range(m):
#     for j in range(n):
#         print(f'{arr[i][j]:3d}',end='')
#     print()

# seed(0)
arr=[[0]*n for _ in range(m)]
for i in range(m):
    for j in range(n):
        arr[i][j]=rr(-5,5,1)
        print(f'{arr[i][j]:3d}',end='')
    print()
print(maxarea(arr))
