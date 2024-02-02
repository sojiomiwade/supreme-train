'''
get the frequenies with a counter
insert them into heap as (freq,num), then pull out the first k => n lg n
better: add element. if heap size is k+1, remove one
return the heap
comp: n lg k + n = n lg k

time,space:O(n lg k)
13 22 31

[31 22]
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        heap=[]
        for num,freq in count.items():
            heapq.heappush(heap,(freq,num))
            if len(heap)>k:
                heapq.heappop(heap)
        return [x for _,x in heap]
