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
        last = -1
        while lo <= hi:
            mi = (lo + hi) // 2
            isbadval = isbad(mi)
            if isbadval:
                last = mi
                hi = mi - 1
            else:
                lo = mi + 1
        return last

