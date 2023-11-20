'''
could use brute force for all i,j with i <= j with O(n**2), O(1)
res = 5
-2  1 -2  4  3  5  6  1  5
-2, 1,-3, 4,-1, 2, 1,-5, 4
-2  1 -2  4  3  5  6  1  5

nums: -2, 1,-3, 4, -1  2
dp:   -2  1 -2  4   3  5
res = 4
exp(res) = 3
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [None for _ in nums]
        res = dp[0] = nums[0]
        for idx in range(1, len(nums)):
            dp[idx] = max(nums[idx], dp[idx - 1] + nums[idx])
            res = max(res, dp[idx])
        print(dp)
        return res


'''
at index i: i won't take worse than where i'm at

-2, 1,-3, 4, -1  2
rs=0,1, 
rs = max(0, this + rs), but immediately track max
return min element in array if rs is still -inf
exp(res) = 5

[5,4,-1,7,8]

-2, 1,-3, 4, -1  2
rs ?0?,1,-2,4,3,5
ms=-2
exp(ms) = 5
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        rs = maxsum = nums[0]
        for i in range(1, len(nums)):
            rs = max(nums[i], nums[i] + rs)
            maxsum = max(maxsum, rs)
        return maxsum
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        -2,1,-3,4,-1,2,1,-5,4
         ^
        -2
        -2

        -2,1,-2,4, 3,5,6, 1,5
        bs=6

        [5,4,-1,7,8]
        5 9 8 15 23
        bs=9

        -2,1,-3,4
        c=-2
        bs=1
        '''
        # DP style start
        return maxSubArray(nums[])
        # DP style end

        bs = curr = nums[0]
        for i in range(1, len(nums)):
            curr = max(nums[i], nums[i]+curr)
            bs = max(bs, curr)
        return bs
    