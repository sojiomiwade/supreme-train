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
'''
implement selection sort
we haave an array a
let l be the exclusive boundary of sorted elements
then l=0
then loop n-1 times (l==0..n-2) starting from l always finding the idx with the smallest value
do a swap with l, then increment l

  0 1 2 5 3
    l   c         

complexity: time and space: O(n**2) and O(1)

2 3 5
  l r
mi,mval=2,3
'''

def ss(a):
    n=len(a)
    for l in range(n-1):
        mi,mval=l,a[l]
        for r in range(l+1,n):
            if a[r]<mval:
                mi,mval=r,a[r]
        a[l],a[mi]=a[mi],a[l]

import random
n=10
a=[i for i in range(n)]
for _ in range(n):
    random.shuffle(a)
    ss(a)
    assert(a == sorted(a))