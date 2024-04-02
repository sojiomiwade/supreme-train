'''
need shortest path to all nodes
when len(dist) is n, stop
can stop when heap is empty. no heap will not be empty, 
just track len(dist)
track mindist


can use BFS or heap

for heap, if we do dist[v], it will never change again

1st put (0,2)
on pop, add 11 and 13
pop 13 and add 24,
then pop 11

heap [24 94]
nc,n 13
dist {20 11 31 42}
'''
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        cost=defaultdict(dict)
        for u,v,w in times:
            cost[u][v]=w

        dist={}
        heap=[(0,k)]
        while heap:
            nodecost,node=heapq.heappop(heap)
            if node in dist:
                continue
            dist[node]=nodecost
            for nb,nb_node_cost in cost[node].items():
                heapq.heappush(heap,(nodecost+nb_node_cost,nb))
        # print(list(dist.items()))
        return -1 if len(dist)<n else max(dist.values())