'''
1. find the connected components, this requires setup of the neighbor graph
2. return the length of the longest one

2 0 5 1

visited {2 1 0}
comp {2 1 0}
'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        def compcount(num,comp):
            if num not in visited:
                comp.add(num)
                visited.add(num)
                for nb in nbs[num]:
                    compcount(nb,comp)
            return comp
            
        nbs=collections.defaultdict(list)
        numsset=set(nums)
        for num in numsset:
            if num-1 in numsset:
                nbs[num].append(num-1)
                nbs[num-1].append(num)
        
        visited=set()
        ans=0
        for num in numsset:
            ans=max(ans,len(compcount(num,set())))
        return ans