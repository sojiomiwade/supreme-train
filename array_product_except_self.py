'''
6      2      3       4
|234   6|34    62|4    623|

ans init to array of 1s
for i in [1:n]
    ans[i] = ans[i-1] * nums[i-1]
for i in [n-2:-1]
    ans[i] *= nums[i+1]
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1 for _ in range(n)]
        accum = 1
        for i in range(n):
            ans[i] *= accum
            accum *= nums[i]
        accum = 1
        for i in range(n-1,-1,-1):
            ans[i] *= accum
            accum *= nums[i]
        return ans

'''
1   2   3   4
234 134 124 123
1   1   12  123
234 34  4   1


going left
in answer[i] i in [1..n), put aggleft, then set aggleft to  nums[i]*aggleft
going right, similar: [n-1,-1)
in answer[i], a aggright, then aggregate nums[i] into aggright
=> aggright is set to 
nums: 4 5 6
        ^
ans:  165 46 45
ar: 654
al: 456
exp:  56 46 45
initialize first to 1

'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
        aggleft = nums[0]
        for i in range(1, n):
            answer[i] = aggleft
            aggleft *= nums[i]
        aggright = nums[-1]
        for i in range(n-2,-1,-1):
            answer[i] *= aggright
            aggright *= nums[i]
        return answer
        