'''
now let's use heap
cost is the picker (cv lv v)
invariant is if we heap pop, then the node there has its ans as cv,
    so if dst can return immediately
before adding neighbors, check lv is not yet L
can allow cost changes, only if lv is less than leaps[v]
so can initialize leaps[v] to zero for all nodes
that's it
. --- .
f {0:{1:100, 2:500}, 1:{2:100}, 2:{}}
leaps {00 12 22}
heap [ (500 1 2)]
cv,lv,v (100 1 1)
'''
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        f,L=defaultdict(dict),1+k
        # cost=defaultdict(lambda :float('inf'))
        leaps=defaultdict(lambda :L)
        for u,v,price in flights:
            f[u][v]=price
        heap=[(0,0,src)]
        while heap:
            cv,lv,v=heapq.heappop(heap)
            if v==dst:
                return cv
            if lv<leaps[v]:
                leaps[v]=lv
                for w,cvw in f[v].items():
                    heapq.heappush(heap,(cv+cvw,1+lv,w))
        return -1