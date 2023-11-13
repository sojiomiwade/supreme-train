'''
code time: 10:38 -- 10:57 = 19m
time:
space:
examples
key observation: bin search and always remember the last bad
algorithm: when bin-search fails return last remembered

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

 
1 2 3 4 5
    f t t

1 2 3 4 5
  f t t t
3 is bad? remember it.
call isbad(lo, 2)
none found? return remembered. 

1 2 3 4 5
t t t t t
1 2
1
1 is last remembered

firstbad(n)
        
Example 1:

Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.
Example 2:

Input: n = 1, bad = 1
Output: 1
 
1 2 3 
f f t

1 2 3 4 5 
f f f t t

Constraints:

1 <= bad <= n <= 231 - 1

'''
class Solution:
    def firstBadVersion(self, n: int) -> int:
        lo, hi = 1, n
        while lo <= hi:
            mi = (lo + hi) // 2
            isbadval = isBadVersion(mi)
            if isbadval:
                hi = mi - 1
            else:
                lo = mi + 1
        return hi+1


# again but this time no api
from typing import List


# Find the First True in a Sorted Boolean Array

# An array of boolean values is divided into two sections; the left section consists of all false and the right section consists of all true.
# Find the First True in a Sorted Boolean Array of the right section, i.e.the index of the first true element.If there is no true element, return -1.

#  Input: arr = [false,..., false, | true, true, true]
# O(lg n)
'''
bisect to left if true
bisect to right if false
key observation: return hi + 1

boundary
'''
#  Output: 2

# Explanation: first true's index is 2.
def first_true(arr: List[bool]) -> int:
    lo, hi = 0, len(arr) - 1
    while lo <= hi: # 0,1,2; 2,1
        mi = lo + (hi - lo) // 2
        if arr[mi] == True:
            hi = mi - 1
        else:
            lo = mi + 1
    return hi + 1

arr = [False, False, True]
print(first_true(arr)) # 2
arr = [False, False, True, True]
print(first_true(arr)) # 2
arr = [False, False, True, True, True]
print(first_true(arr)) # 2
arr = [True, True, True, True]
print(first_true(arr)) # 0

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
class Solution:
    def firstBadVersion(self, n: int) -> int:
        '''
        012345678
        1234 5 6. 7 89
        ffff f f. t tt

        12345
        ffftt
        3,4
        use binary search and 
        new lo/hi is mi-1, or mi+1
        brute-force: linear is a no-no at O(n)
        time: O(lg n)
        space: O(1)
        '''
        lo,hi=1,n
        res=-1
        while lo <= hi:
            mi = lo + (hi - lo)//2
            isbad = isBadVersion(mi)
            if isbad:
                hi = mi - 1
                res = mi
            else:
                lo = mi + 1
        if res==-1:
            raise ValueError('no bad version')
        return res
            
            
        