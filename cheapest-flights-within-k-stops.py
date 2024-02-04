'''
s --> m --> d
L : the number of leaps allowed. k = 1 => L = 2, 
leaps[src]=L
can use BFS or heap(dijkstra)
BFS: with src starting in queue as (cost,src,remleaps), 
    any dequeue must satisfy this to add children
    if is dst, update cost as needed and be done
    otherwise, 
        1. remleaps>0
        2. cost is cheaper than cost at the node
        3. then go ahead and add downstreams
time,space: O(V + E**2): every edge's addition can trigger E edges to be re-added
'''
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        f,L,INF=defaultdict(dict),k+1,float('inf')
        for u,v,w in flights:
            f[u][v]=w
        heap=[(0,src,L)]
        '''
        key question in heap: can ans[x] get changed?
        yes, only to be made more expensive since cheaper
        routes had prior claimed it was cheaper, but now
        it must be made more expensive
        so remleaps is the only admission control
        so to 
        a --- b
        |\__  |
        |   \ |
        c --- d
        cheapest routes must be pruned =>
        '''
        minremleaps=defaultdict(lambda :-INF)
        while heap:
            cu,u,remleaps=heapq.heappop(heap)
            if u==dst:
                return cu
            if remleaps==0:
                continue
            if remleaps>=minremleaps[u]:
                minremleaps[u]=remleaps
                for v,cuv in f[u].items():
                    heapq.heappush(heap,(cu+cuv,v,remleaps-1))
        return -1 # once i hit the destination i am done

        # q=deque([(0,src,L)])
        # ans=defaultdict(lambda :INF)
        # while q:
        #     cu,u,remleaps=q.popleft()
        #     if cu<ans[u]:
        #         ans[u]=cu
        #         if remleaps>0:
        #             for v,cuv in f[u].items():
        #                 q.append((cu+cuv,v,remleaps-1))
        # return ans[dst] if ans[dst] != INF else -1