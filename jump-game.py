'''
once i have done an index, no need to do it again in the future => dp array
at curidx, can go multiple places (number of which is in that slot)
once idx >= n, we are done
oidx in range(1,4)
canjump(0+1...3)
canjump(1 + 1..2)
canjump(2 + [1..1])
canjump(3 + )
'''
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def canjump(idx: int) -> bool:
            if idx>=n-1:
                return True
            if dp[idx] is not None:
                return dp[idx]
            for oidx in range(1,1+nums[idx]):
                if canjump(idx+oidx):
                    dp[idx]=True
                    return dp[idx]
            dp[idx]=False
            return dp[idx]

        n=len(nums)
        dp=[None for _ in range(n)]
        return canjump(0)