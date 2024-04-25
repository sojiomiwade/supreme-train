'''
with bfs, can head to dst, but prune at k

so a node abstraction is (l,c,id)
0 -- 1 -- 2
k=1 stop => 1+k leaps
src starts at 0 leaps

time: k(v+e)
space: queue can have k(v+e)
when processing a node, (l,c,id)
    if i am dst, return l
    if leaps l for me is already L, then discard me
    for all nbs, if i can't make the cost to nb cheaper, then do not add nb
    keep a step on each node, so that we can prune when hit k

f {0{1:100 2:500} 1{2:100} 2{}}
q [(0 0 0)]
L 1
cost {0:0, 2:inf}
l,cv,v (0 0 0)
'''
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        q=collections.deque([(0,0,src)])
        f,L=defaultdict(dict),1+k
        cost=defaultdict(lambda :float('inf'))
        for u,v,price in flights:
            f[u][v]=price
        while q:
            l,cv,v=q.popleft()
            if cv>=cost[v]:
                continue
            cost[v]=cv
            if l<L:
                for w,cvw in f[v].items():
                    q.append((1+l,cv+cvw,w))
        return -1 if cost[dst]==float('inf') else cost[dst]
