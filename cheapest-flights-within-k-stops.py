class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        '''
        if a (ucost,u,rem_hops) is removed, we will check if rem_hops is strictly less 
        than  the last there
        if it does, it could (i.e., not guaranteed to) win: the last didn't make it!
        criteria to allow: if rem_hops > last_rem_lookup[u]
        now if lrl[u] starts 0, and we hit a node with 0 rem_hops, we cannot advance!
        now, we can freely change the cost (increase it because the last one couldn't)
        now set the cost[u] (hashmap) to 5 from 3
        what do we start each rem_hops to!
            the 1st node must always make it, no matter. 
            could use -inf. could also use 0. since if you come to a node
            and you only have 0, then you can't move forward
            src b c dst
             3  2 1 0
                rem_hops : 2
        we don't have to exhaust the heap, but if we do, there's no way to get to 
        dst in k stops

        complexity: up to k times we run a 
            heapsearch: E (lg E)
        => k E lg E ? 
        break it down to BFS
        initialization: E (the number of nodes is the number of connections)
        loop: think BFS but we do it k times:
             k E lg E
        '''
        f=defaultdict(dict)
        for u,v,cuv in flights:
            f[u][v]=cuv
        lrl=defaultdict(int)
        MAXHOPS=k+1
        heap=[(0,MAXHOPS,src)]
        cost={}
        while heap:
            (cu,remhops,u)=heapq.heappop(heap)
            if u==dst:
                return cu
            if remhops>lrl[u]:
                cost[u]=cu
                lrl[u]=remhops
                for v,cuv in f[u].items():
                    heapq.heappush(heap,(cu+cuv,remhops-1,v))
        return -1