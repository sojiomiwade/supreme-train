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
