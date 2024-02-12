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

1 9 | 6 4 5
1 9 | 6 4 | 5
       1
7 8 9
t   mi
1 2 
0 invcount

'''
from typing import List

def mergesort(a: List[int]) -> int:
    '''
    algorithm: invcount increments by rem of top if 
        taking from bot and topval is a number
        8 2 | 1 9
    '''
    def merge(lo: int, mi: int, hi: int) -> None:
        nonlocal invcount
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
                if top!=mi+1:
                    invcount+=mi-top+1
                bot+=1
            val=min(topval,botval)
            assert type(val) is int and type(val) is int
            a[idx]=val
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
    invcount=0
    mergesort(0,n-1)
    return invcount

from random import randrange as rr, shuffle
a=[i for i in range(10)]
b=a[:]
assert mergesort(a) == 0
assert a==b

a=[i for i in range(10)]
b=a[:]
shuffle(a)
mergesort(a)
assert a==b

a=[2,3,0,1]
invcount=mergesort(a)
assert a==[i for i in range(4)]
print(invcount)

a=[1, 9, 6, 4, 5]
b=a[:]
invcount=mergesort(a)
assert a==sorted(b)
print(invcount)

'''
inversion count
top 0 | bot 1

2 3 | 0 1

2 3 | 0 1
0
4 count


01 
02 1
03 1
12 1
13 1
23 

1, 9, 6, 4, 5
   3. 2.     
1
9 3
6 2
5 
'''
