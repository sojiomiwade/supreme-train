class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        '''
        [[0,1,5],[1,2,5],[0,3,2],[3,1,2],[1,4,1],[4,2,1]]
                   0
               5/    \2
               V      V
               1<-(2)-3
             5/  \1
             V    V
             2<---4
                1
        src,dst,k = 0,2,2; fl = {0:{1:5,3:2},1:{2:5,4:1},3:{1:2},4:{2:1}}
        vis =          320200
                       012345
        q = 003 232 411 512 540 641 | 920  10,21 
        cumcost, node, k = 641
         ==
         0 >= 1
        friend, friend_node_cost = 41
        641
        '''
        q = [(0,src,k+1)]
        fl = defaultdict(dict)
        vis = [0 for _ in range(n)]
        for u,v,w in flights:
            fl[u][v] = w
        while q:
            nc, node, k = heapq.heappop(q)
            if node == dst: 
                return nc
            if k > vis[node]:
                vis[node] = k
                for f,fc in fl[node].items():
                    heappush(q, (nc+fc, f, k-1))
        return -1