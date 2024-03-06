'''
you want to know which idxs you've used (actually since elements unique can just 
use them instead).
1 2 3

buf [1 3 2]
'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def permute(buf: List[int]):
            if len(buf)==len(nums):
                ans.append(buf[:])
            else:
                for el in nums:
                    if el not in buf:
                        permute(buf+[el])
            
        ans=[]
        permute([])
        return ans
