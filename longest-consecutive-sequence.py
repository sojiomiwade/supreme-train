class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        put every number in a set
        now make graph for each num, if num-1 is there, then num and num-1 are neighbors
        now find the largest component
        1-2 -3-4
        \ |
         \-5
        v v v v 
        100
        400
        '''
        def count_seq(num: int) -> int:
            count=0
            visited.add(num)
            for nb in nbs[num]:
                if nb not in visited:
                    count+=count_seq(nb)
            return 1 + count

        nums=set(nums)
        nbs=defaultdict(list)
        visited=set()
        for num in nums:
            if num-1 in nums:
                nbs[num-1].append(num)
                nbs[num].append(num-1)
        
        ans=float('-inf')
        for num in nums:
            if num not in visited:
                ans=max(ans,count_seq(num))
        return ans if nums else  0