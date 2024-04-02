'''
13 22 31 --> counter space is u
sort --> u log u with space possibly 1
heap
put el. if beyond heap size eject one

k + (u-k) lg k VS u lg k

count []
heap [22 31]

[(5, 3), (2, 1), (3, 3), (1, 2)]
 heap
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=collections.Counter(nums)
        heap=[]
        count_tups=list(count.items())
        for i in range(min(k,len(count_tups))):
            heap.append((count_tups[i][1],count_tups[i][0]))
        heapq.heapify(heap)
        for i in range(k,len(count_tups)):
            heapq.heappushpop(heap,(count_tups[i][1],count_tups[i][0]))
        return [el for freq,el in heap]