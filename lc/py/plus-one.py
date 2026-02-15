# 8 8 9 1 1 9 1 --> add one to the back

# 8 8 9 1 9 9 9 --> add one to all nines, then change the left dig  by 1
# 8 8 9 2 0 0 0 <-- ans

# 1 9 3
# iterate from r to l until find something not 9
# if don't find --> neeed new array (see below)
# else:
#     increment that thing by 1
#     set all subsequent back the way you came to 0
# all 9s ==> need new array
# ans becomes all zeroes with 1 at the head of new array

# 1 2 4
#       i
# alloc = 2
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        alloc = -1
        for i in range(n-1,-1,-1):
            if digits[i] != 9:
                alloc = i
                break
        if alloc == -1:
            ans = [0 for _ in range(n+1)]
            ans[0] = 1
            return ans
        digits[alloc] += 1
        for i in range(alloc+1,n):
            digits[i] = 0
        return digits