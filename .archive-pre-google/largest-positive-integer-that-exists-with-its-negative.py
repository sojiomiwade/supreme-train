'''
2 -2 5 -5
pass through once and put -5 in one set, and +ve iin another
now go through the positive and look for -ve. if it exists
    then it's a candidate; so update ans accordingly

now try a one pass, one set way
if i see -5 or 5, look for its complement and update ans accodingly
add this element to set regardless (really only need to add if comp isn't there)

time O(n), space O(n)
2 -2 -3 1 3
have {2 -3 1}
ans 2
'''

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        have=set()
        ans=-1
        for x in nums:
            if -x in have:
                ans=max(ans,abs(x))
            else:
                have.add(x)
        return ans