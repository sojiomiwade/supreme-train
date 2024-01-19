'''
return a list of all pairs with difference k in a given array
example
arr = [1,7,5,9,2,12,3]
res = [(1,3), (3,5), (5,7), (7,9)]

k = 3
1 2 3 5 7 9 12
          l
              r
res = (2,5), (9,12) 
brute force: 
    two index loop through all pairs, and check: n**2, 1
better: 
    sort array
    repeat till r == n
        if diff is greater than k 
            l += 1
        elif equal
            update res
            r += 1
        else
            r += 1

^ above is n log n, we could do better with hash table
[1,7,5,9,2,12,3]
walk through keeping each entry you see in a hashset, and do this
    add the current one to the set
    check if curr + k   OR  curr - k is there, and update res accordingly

k - x or x -k is there
a - b = k
a = b - k = 6 - 7
b = a - k = 7 - 6

7   1

1 + k = x or 1 - k = x



10 20 30 
k 
use a left and right index starting at 0
repeat the following for each right idnex 0..n-1
    while l <= r
        check l and r for difference, and update as res as needed
        if found 
            can just move left to right index (but won't change runtime)
        if difference is less
            break
        if it is more
'''
from typing import List, Tuple


def k_diff(arr: List[int], k: int) -> List[Tuple]:
    left = right = 0
    arr.sort()
    res = []
    while right < len(arr):
        diff = arr[right] - arr[left]
        if diff > k:
            left += 1
        elif diff == k:
            res.append((arr[left], arr[right]))
            right += 1
        else:
            right += 1
    return res

def two_difference(arr: List[int], k: int) -> List[Tuple]:
    res = []
    vals = set()
    for val in arr:
        if val + k in vals:
            res.append((val, val + k))
        elif val - k in vals:
            res.append((val - k, val))
        vals.add(val)
    return res

arr = [1,7,5,9,2,12,3]
# (2,5), (9,12) 
print(k_diff(arr, 3))

arr = [1,7,5,9,2,12,3]
# res = [(1,3), (3,5), (5,7), (7,9)]
print(k_diff(arr, 2))

arr = [1,7,5]
# res = [(5,7)]
print(k_diff(arr, 2))

arr = [1,7,5]
# res = [(1,5)]
print(k_diff(arr, 4))
'''
return a list of all pairs with difference k in a given array
example
arr,k = [1,7,5,9,2,12,3],2
res = [(1,3), (3,5), (5,7), (7,9)]
k = 2

comp={1,7,}
res={(5,7),()}
7 will look for 5 and 9
1 will look for 1+k, and -1 (1-k)
can do bruteforce for each pair -> n**2 time, constant space
could use hashtable as a set to remember elements that exist
'''
def two_diff(arr, k):
    comp = set()
    res = set()
    for x in arr:
        y = None
        if x+k in comp:
            y = x+k
        if y is not None:
            if x > y:
                x,y = y,x
            res.add((x,y))
        y=None
        if x-k in comp:
            y = x-k
        if y is not None:
            if x > y:
                x,y = y,x
            res.add((x,y))
        comp.add(x)
    return list(res)


arr,k = [1,7,5,9,2,12,3],2
#res = [(1,3), (3,5), (5,7), (7,9)]
print(two_diff(arr,k))