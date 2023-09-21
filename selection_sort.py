from typing import List

'''
time: 12:07 - 12:19 = 12 but should have used a big example at first,  +/- 1

   v
12345
     ^
   *
on inner loop, update best when something better found in that loop 
outer loop iterates n - 1 times

simple testcase
 v
54
^
*
n=2
'''

def ssort(arr: List[int]) -> List[int]:
    n = len(arr)
    for i in range(n - 1):
        best = i # 0
        for j in range(i+1, n):
            if arr[j] < arr[best]: #arr 1 < arr 0
                best = j # best = 1
        arr[i],arr[best] = arr[best],arr[i]
    return arr

from random import randrange
for _ in range(5):
    n = 10
    arr = [randrange(n) for _ in range(n)]
    assert sorted(arr) == ssort(arr)
