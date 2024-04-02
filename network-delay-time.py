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

BFS: stop when queue is empty
now do we need dist? yes.
don't proceed if it isn't better

q [42]
n,nc (31)
dist {20 11 31 42}
'''
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        cost=defaultdict(dict)
        # E
        for u,v,w in times:
            cost[u][v]=w

        q=collections.deque([(k,0)])
        dist=defaultdict(lambda :float('inf'))
        while q:
            for i in range(len(q)):
                node,nodecost=q.popleft()
                if nodecost<dist[node]:
                    dist[node]=nodecost
                    for v,w in cost[node].items():
                        q.append((v,nodecost+w))
        return -1 if len(dist)<n else max(dist.values())