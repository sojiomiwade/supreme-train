from typing import List
import bisect
# 1 2 2 1
# 2 2

# put nums2 in a set, then loop through n1, and put n1 things that are in n2 in a set ans
# return a list of the set ans
# time O(n)
# space O(n)

# could sort both and then move 2 pointers along
# time space: O(n lg n), O(n)

# could sort just one, and then binsearch in the other for each element

# n1: 1 2 2 1
#         ^
# n2: 4 4 8 9 9
# ans [9 4]
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2.sort()
        nums1.sort()
        ans = []
        for x in nums1:
            i = bisect.bisect_left(nums2,x)
            if i != len(nums2) and nums2[i] == x and (not ans or ans[-1] != x):
                ans.append(x)
        return ans
