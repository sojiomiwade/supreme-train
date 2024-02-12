'''
mergesort
0 2 4 |  3 1
0 2 4 | 1 3

0 2 
  t 
b
1 3
a [ 0 1 2 3 ]
    i 
'''
from typing import List

def mergesort(a: List[int]) -> None:
    def merge(lo: int, mi: int, hi: int) -> None:
        b[lo:hi+1]=a[lo:hi+1]
        #top : lo .. mi  | bot: mi+1 .. hi
        idx=lo
        top,bot=lo,mi+1
        while top<=mi or bot<=hi:
            topval=botval=INF
            if top<=mi:
                topval=b[top]
            if bot<=hi:
                botval=b[bot]
            if topval<botval:
                top+=1
            else:
                bot+=1
            assert type(topval) is int and type(botval) is int
            a[idx]=min(topval,botval)
            idx+=1

    def mergesort(lo: int, hi: int) -> None:
        if lo<hi:
            mi=lo+(hi-lo)//2
            mergesort(lo,mi)
            mergesort(mi+1,hi)
            merge(lo,mi,hi)

    INF=float('inf')
    n=len(a)
    b=[0]*n
    mergesort(0,n-1)

from random import randrange as rr, shuffle
a=[i for i in range(10)]
shuffle(a)
print(a)
mergesort(a)
print(a)

