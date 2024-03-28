'''
create a graph of neighbors for each x. well no need: just make a set
of nums

now can check if num +/- 1 in set (which implies it is in graph)
now withh a dfs on each num, we can get our ans
need visited set

visited {100 4}
4-3-2-1
'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        def visit(val: int) -> int:
            if val not in iset or val in visited:
                return 0
            visited.add(val)
            return 1+max(visit(val-1),visit(val+1))
            
        ans=0
        iset=set(nums)
        visited=set()
        for x in sorted(nums):
            ans=max(ans,visit(x))
        return ans