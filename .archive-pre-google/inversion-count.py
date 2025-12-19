'''
1 9 6 5 | 4 8 7 3
1 9 | 5 6     |    4 8 | 3 7

  i   mi
1 5 6 9 | 3 4 7 8
1 3 4 5 6 
  * -- when we take from b, we must add m-i
      * -- otherwise we don't add anything
56 1
37 1

0 1 2 3 4 5 6 7
0 6 3 2 1 2 1 0 = 15


1 9 6 5 4 8 7 3

0 1 2 3
1 9    6 5
l h
m
i j
bidx 0
count 0

1 9 6 5
2 1 
'''
from typing import List


def inversion_count(arr: List[int]) -> int:
    def mergesort(lo: int, hi: int) -> None:
        if lo<hi:
            mi=lo+(hi-lo)//2
            mergesort(lo,mi)
            mergesort(mi+1,hi)
            merge(lo,hi)

    def merge(lo: int, hi: int):
        nonlocal count
        mi=lo+(hi-lo)//2
        i,j=lo,mi+1
        #lo...mi | mi+1 .. hi
        bidx=i
        while i<=mi or j<=hi:
            lval=INTMAX if i>mi else arr[i] 
            rval=INTMAX if j>hi else arr[j]
            if lval<=rval:
                i+=1
            else:
                j+=1
                count+=mi-i+1
            b[bidx]=min(lval,rval)
            bidx+=1
        assert bidx==hi+1
        arr[lo:hi+1]=b[lo:hi+1]

    INTMAX=2**31-1
    count,n=0,len(arr)
    b=[0 for _ in range(n)]
    mergesort(0,n-1)
    return count
    
    
s='1 9 6 5 4 8 7 3'
arr=[int(x) for x in s.split()]
print(inversion_count(arr)) # 15
print(inversion_count([1,9,6,5])) # 3
print(inversion_count([i for i in range(10)])) # 0
print(inversion_count([i for i in range(9,-1,-1)])) # 45