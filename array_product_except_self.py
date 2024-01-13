class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
       '''
       use 2 loops,
       ans starts as 1
       left: dump the aggregate in the cell, aggregate the product, 
       right: same
       5       2     3.    4
       1       5.    52.   523
       1|234  5|34  52|4.  523|1
       going forward .. i in (0,n)
       agg=1
       loop 
        answer[i]=agg  
        agg*=nums[i] : 5

       coming back .. i in [n-1,1]
       agg=1
       loop
        answer[i]*=agg
        agg*=nums[i] : 34
       '''
       n=len(nums)
       answer=[1 for _ in range(n)]
       agg=1
       for i in range(n):
           answer[i]=agg  
           agg*=nums[i]
       agg=1
       for i in range(n-1,-1,-1):
           answer[i]*=agg  
           agg*=nums[i]
       return answer
