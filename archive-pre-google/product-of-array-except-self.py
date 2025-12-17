'''
agg 1
6      2    3   4    5
1      6    62  623  6234
5432   543  54  5    1           
agg starts at 1, each step takes the curr
in beggining of iteration, put the aggregator val into ans
going back put *= aggregator into ans to not lose ans val
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[1 for _ in range(n)]
        agg=1
        for i,x in enumerate(nums):
            ans[i]=agg
            agg*=x

        agg=1
        for i,x in enumerate(reversed(nums)):
            ans[n-1-i]*=agg
            agg*=x

        return ans
