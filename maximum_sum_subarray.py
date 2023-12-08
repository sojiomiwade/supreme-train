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
    '''
nums:-2,1,-3,4,-1,2,1,-5,4
dp:[-2,1,-2,4,3,5,6,1,5]
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp=[nums[0]]
        n=len(nums)
        for i in range(1,n):
            dp.append(max(dp[-1]+nums[i],nums[i]))
        return max(dp)

'''
l  h  l  h
  
  1.   
-2  1 -3        4    -1 2 1 -5 4
 1  1 -3  inf
max(-2,0)+msa()
-2 1 -2  4    3 5 6  1 5

[-2,1,-3,4,-1,2,1,-5,4]
  2 4  3 6  2 3 1 -1 4 
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def msa(mi):
            if mi==len(nums):
                return float('-inf')
            msa_right=msa(mi+1)
            msa_mi=max(nums[mi],nums[mi]+msa_right)

        res=float('-inf')
        return msa(0)'''
l  h  l  h
  
  1.   
-2  1 -3        4    -1 2 1 -5 4
 1  1 -3  inf
max(-2,0)+msa()
-2 1 -2  4    3 5 6  1 5

[-2,1,-3,4,-1,2,1,-5,4]
  2 4  3 6  2 3 1 -1 4 
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def msa(mi):
            nonlocal res
            if mi==len(nums):
                return float('-inf')
            msa_right=msa(mi+1)
            cur=max(nums[mi],nums[mi]+msa_right)
            res=max(res,cur)
            return cur
        res=float('-inf')
        msa(0)
        return res'''
l  h  l  h
  
  1.   
-2  1 -3        4    -1 2 1 -5 4
 1  1 -3  inf
max(-2,0)+msa()
-2 1 -2  4    3 5 6  1 5

[-2,1,-3,4,-1,2,1,-5,4]
  2 4  3 6  2 3 1 -1 4 
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def msa(mi):
            if mi==len(nums):
                return (0,float('-inf'))
            sumip1,maxsum=msa(mi+1)
            sumi=nums[mi]+max(0,sumip1)
            return (sumi,max(maxsum,sumi))
        return msa(0)[1]