# In a given string s, replace all spaces with %20
# 012345678
# a b c    
# a%20b%20c
'''
cannot write from left otherwise will overwrite!
but can get new size calculation, and write from back
because then it all works out
one idx to write in new array another to know where we are 
    in old
upon finding space, write three chars and move idx by 3, otherwise move idx by 1
'''
from typing import List


def replace(arr: List[str], nlen: int, olen: int) -> None:
    nidx=nlen-1
    oidx=olen-1
    while nidx>=0:
        if arr[oidx]!=' ':
            arr[nidx]=arr[oidx]
            nidx,oidx=nidx-1,oidx-1
        else:
            arr[nidx-2:nidx+1]=list('%20')
            nidx,oidx=nidx-3,oidx-1

# 012345678
# a b cn
# a%20b%20c
# n
# o      
# a%20b%20c
arr='a b c    '
# arr='abc'
arr=list(arr)
assert(len(arr)==9), f'{len(arr)} not 9'
print(arr)
replace(arr,9,5)
# replace(arr,3,3)
print(arr)