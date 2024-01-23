'''
selection sort 
5 1 8 3 4
1 5 8 3 4
1 3 8 5 4

curridx=0
sidx=find idx of smallest
swap(arr[curridx],arr[sidx])

5 1 8
c
    i
maxidx,maxval=1,1
'''
from typing import List


def selectionsort(arr: List[int]) -> None:
    n=len(arr)    
    for cidx in range(n-1):
        minidx,minval=-1,float('inf')
        for idx in range(cidx,n):
            if arr[idx]<minval:
                minidx,minval=idx,arr[idx]
        arr[cidx],arr[minidx]=arr[minidx],arr[cidx]

from random import shuffle
arr=[i for i in range(10)]
sarr=arr[:]
while arr==sarr:
    shuffle(arr)
selectionsort(arr)
assert arr==sarr
