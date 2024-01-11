'''
1 3 0 5 4 1
      l

0,0,0,3,5,1
      n
corner case
1 2 3
      n
n**2 way
get the last location, next, of a zero, if none exists return
from the back, if you see a nonzero, swap it with the first position of a zero if one exists, to position next
    decrement next
    repeat this for each index
'''

from typing import List


def partition(arr: List[int]) -> None:
    if all(arr):
        return
    n=len(arr)
    lastzeroloc=-1
    for i in range(n-1,-1,-1):
        if arr[i]==0:
            lastzeroloc=i
            break
    for i in range(lastzeroloc-1,-1,-1):
        if arr[i]!=0:
            arr[i],arr[lastzeroloc]=0,arr[i]
            lastzeroloc-=1

arr=[3,0,5,0,0,1]
partition(arr)
print(arr)

arr=[0,0,0,0,0]
partition(arr)
print(arr)

arr=[3,0,-5,0,0,-1]
partition(arr)
print(arr)