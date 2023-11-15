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
        return -1'''
k=1 stop => l=2 allowable leaps
l=k+1 allowable leaps

0--1--2
f[u][v] is the cost of flying from u to v

suppose L=3
02 really high, kill this 
    how? can put vis[u]=true
03452 => 4 leaps, 1 too many hops, can't leap beyond 2, so kill it 
kill future paths through done nodes (they are cycles or worse routes)
    how? vis[u]=l at the time it was found and also if any node's l >= vis[u] => discard it
    so, set vis[u]=infinity (or actually and necessarily L to start)
    ex.: vis[1]=1 after removing 1,
    then 061 is rejected since l there is 0
worst case complexity : exponential if we consider every combination of nodes
complexity: no edge processed more than once (but all reachables processed): E lg E.
            space: E, since we enqueue arbitrary number of node to node costs

   345
  /   \
0---6---2-----t
  \ | /
    1
L: 3
'''
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        f=defaultdict(dict)
        for u,v,p in flights:
            f[u][v]=p
        L=k+1
        bar=defaultdict(int)
        q=[(0,src,L)]
        while q:
            p,u,l=heapq.heappop(q)
            if u==dst:
                return p
            if l<=bar[u]: 
                continue
            bar[u]=l
            for v,vc in f[u].items():
                heapq.heappush(q,(p+vc,v,l-1))
        return -1