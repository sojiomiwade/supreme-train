# array of integers of size N is a permutation if 2 conditions hold:
# 1. a[i] in [0, N - 1]
# 2. all numbers appear exactly once
SOLUTIONS BELOW!



# array of integers of size N is a permutation if 2 conditions hold:
# 1. a[i] in [0, N - 1]
# 2. all numbers appear exactly once

# 1 2 3
'''
could use a hash set and exclude any number not satisfying 1 -- O(n) space
return len(set)==len(a)
could sort: O(n lg n) time and space could be O(1)
could put numbers their place, going through each number and 
    if a number is not in range or there's copy already in its place return F
    otherwise return True
    time: O(n) --> each number gets put in its place once; we through each element once
    space: O(1)
0 1 3 3 4
0 1 4 3 3
oops already there's a 3 there => return False
. . 
loop
1 0

'''
from typing import List


def isperm(arr: List[int]) -> bool:
    n=len(arr)
    for i,num in enumerate(arr):
        while num!=i:
            if num>=n or arr[num]==num:
                return False
            temp=arr[num]
            arr[num]=num
            num=arr[i]=temp
    return True

arr=[1,0] #true
print(isperm(arr))

arr=[0,3,1,4,3] #false: duplicate 3
print(isperm(arr))

arr=[1,2,3,4,5] #false: missing 0
print(isperm(arr))

from random import shuffle
arr=[0,1,2,3,4,5] 
shuffle(arr)
print(isperm(arr)) #true

