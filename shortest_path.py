'''
There are n cities connected by m flights. Each fight starts from city src and arrives at dest with a price p. Now given all the cities and fights as input, find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.

Input: 
flights = [[0,1,100],[1,2,100],[0,2,500]] / [src city, dest city, price]

Example 1:
src = 0, dst = 2, k = 1
Output: 200

Example 2: 
src = 0, dst = 2, k = 0
Output: 500

Example 3: 
src = 1, dst = 0, k = 1
output: -1
01234567890123456789012345678901234567890123456789012345678901234567890123456789
'''

from collections import defaultdict
from typing import DefaultDict, Dict, List, Tuple
INT_MAX = 2**31 - 1

class PriorityQueue:
    pass

class ArrayPriorityQueue(PriorityQueue):
    def __init__(self, size: int) -> None:
        self.key = [INT_MAX for _ in range(size)]

    def get_min(self) -> Tuple[int,int]:
        minnode = -1
        minkey = INT_MAX # guarantees minnode will be updated
        for idx in range(len(self.key)):
            if self.key[idx] >= 0 and self.key[idx] < minkey:
                minnode = idx
                minkey = self.key[idx]
        assert minnode >= 0
        self.key[minnode] = -1
        return (minnode, minkey)

    def decrease_key(self, item: int, key: int) -> None:
        self.key[item] = key


def build_graph(flights: List[List[int]]) -> DefaultDict[int,List[int]]:
    nbs = defaultdict(list)
    for (node, nb, _) in flights:
        nbs[node].append(nb)
        nbs[nb]
    return nbs

#01234567890123456789012345678901234567890123456789012345678901234567890123456789
def minpath(previous: List[int], src: int, dst: int) -> List[int]:
    path = []
    cur = dst
    while cur >= 0:
        path.append(cur)
        cur = previous[cur]
    return list(reversed(path))

def minprice(
        nbs: DefaultDict[int, List[int]], 
        edge_weight: Dict[Tuple[int,int], int], 
        src: int, 
        dst: int,
        ) -> Tuple[int, List[int]]:
    previous: List[int] = [-1 for _ in range(len(nbs))]
    rem: PriorityQueue = ArrayPriorityQueue(len(nbs))
    rem.decrease_key(src, 0)
    mincost = 0
    for _ in range(len(nbs)):
        (n, minkey) = rem.get_min()
        for nb in nbs[n]:
            if minkey + edge_weight[n,nb] < rem.key[nb]:
                rem.decrease_key(nb, minkey + edge_weight[n,nb])
                previous[nb] = n
                if nb == dst:
                    mincost = minkey + edge_weight[n,nb]
    return mincost, minpath(previous, src, dst)
'''
        0
     1 / \ 5
      v   v
      1-->2
        1
key: -1,100,200
n:0, nb:2
prev: -1,0,1
'''
flights = [[0,1,100],[1,2,100],[0,2,500]]
edge_weight = {(v,w):weight for (v,w,weight) in flights}
nbs = build_graph(flights)
print(minprice(nbs, edge_weight, 0, 2)) # 200

flights = [[0,1,100],[1,2,100],[0,2,150]]
edge_weight = {(v,w):weight for (v,w,weight) in flights}
nbs = build_graph(flights)
print(minprice(nbs, edge_weight, 0, 2)) # 150

from itertools import count
from collections import defaultdict
from typing import Dict, List, Tuple
from heapq import heapify, heappop, heappush

"""
        0
     1 / \ 5
      1 - 2
        1
"""
def build_graph(
        edges: List[Tuple[int,int,int]]
        ) -> Tuple[Dict[int, List[int]], Dict[Tuple[int,int],int]]:
    edge_cost = {}
    nbs = defaultdict(list)
    for node, nb, cost in edges: #01 02 12
        nbs[node].append(nb) # {0:12,12:,2:}
        nbs[nb]
        edge_cost[node,nb] = cost
    return nbs, edge_cost

class PriorityQueue:
    def __init__(self, tasklist_size: int, special: int) -> None:
        INT_MAX = 2**31 - 1
        self.counter = count()
        self.heap = [[INT_MAX,next(self.counter),i] for i in range(tasklist_size)]
        self.heapitem = {i: self.heap[i] for i in range(tasklist_size)}
        # heap = [[inf,0,0], [inf,0,1], [inf,0,2]]
        # heapitem = {0:h0,   1:h1,        2:h2}
        heapentry_for_start_node = self.heapitem[special] # [inf,0,start]
        heapentry_for_start_node[0] = 0
        heapify(self.heap)

    def task_key(self, task: int) -> int:
        print(self.heapitem)
        heapitem = self.heapitem[task]
        return heapitem[0]

    def decrease_key(self, task: int, key: int) -> None:
        heapentry = self.heapitem.pop(task) # {0:[0,0,], ...}
        heapentry[-1] = None
        newentry = [key, next(self.counter), task]
        heappush(self.heap, newentry)

    def pop_task(self) -> int:
        heapentry = heappop(self.heap)
        assert heapentry[-1] != -1
        self.size -= 1
        del self.heapitem_lookup[heapentry[-1]]
        return heapentry[-1]

    def __len__(self) -> int:
        return len(self.heap)
        
def shortest_path(
        edges: List[Tuple[int,int,int]],
        src: int, dst: int) -> List[int]:
    nbs, edge_cost = build_graph(edges)
    pq = PriorityQueue(len(nbs), src)
    # pq.decrease_key(task=src, key=0)
    path = []
    """
               1
            1 / \ 5
             0 - 2
               1
        
    """
    while len(pq) > 0:
        print('b4', pq.heap)
        min_city_cost = pq.task_key(task=pq.top())
        min_city = pq.pop_task() #0
        path.append(min_city) # [0]
        if min_city == dst:
            return path
        print('hi', pq.heap)
        for nb in nbs[min_city]:
            nb_cost = pq.task_key(task=nb)
            newval = min(nb_cost, mc_cost + edge_cost[(min_city, nb)])
            pq.decrease_key(task=nb, key=newval)
    return path

edges = [(0,1,1),(0,2,5),(1,2,1)]
src,dst = (0,2)
print(shortest_path(edges,src,dst)) # 0-1-2

    from itertools import count
from collections import defaultdict
from typing import Dict, List, Tuple
from heapq import heapify, heappop, heappush

"""
        0
     1 / \ 5
      1 - 2
        1
"""
def build_graph(
        edges: List[Tuple[int,int,int]]
        ) -> Tuple[Dict[int, List[int]], Dict[Tuple[int,int],int]]:
    edge_cost = {}
    nbs = defaultdict(list)
    for node, nb, cost in edges: #01 02 12
        nbs[node].append(nb) # {0:12,12:,2:}
        nbs[nb]
        edge_cost[node,nb] = cost
    return nbs, edge_cost

class PriorityQueue:
    def __init__(self, tasklist_size: int, special: int) -> None:
        INT_MAX = 9 #2**31 - 1
        self.size = tasklist_size
        self.counter = count()
        self.heap = [[INT_MAX,next(self.counter),i] for i in range(tasklist_size)]
        self.heapitem_lookup = {i: self.heap[i] for i in range(tasklist_size)}
        heapentry_for_start_node = self.heapitem_lookup[special] # [inf,0,start]
        heapentry_for_start_node[0] = 0
        heapify(self.heap)

    def task_key(self, task: int) -> int:
        heapitem = self.heapitem_lookup[task]
        return heapitem[0]

    def peek(self) -> int:
        while self.heap[0][-1] is None:
            heappop(self.heap)
        return self.heap[0][-1]

    def decrease_key(self, task: int, key: int) -> None:
        self.heapitem_lookup[task][-1] = -1
        heapitem = [key, next(self.counter), task]
        heappush(self.heap, heapitem)
        self.heapitem_lookup[task] = heapitem


    def pop_task(self) -> int:
        while self.heap:
            heapentry = heappop(self.heap)
            if heapentry[-1] != -1:
                self.size -= 1
                del self.heapitem_lookup[heapentry[-1]]
                return heapentry[-1]
        raise IndexError('empty heap')

    def __len__(self) -> int:
        return self.size
        
def shortest_path(
        edges: List[Tuple[int,int,int]],
        src: int, dst: int) -> List[int]:
    nbs, edge_cost = build_graph(edges)
    pq = PriorityQueue(len(nbs), src)
    """
                [0]
                 0
            1 /    \ 5
             1 ---- 2
          [inf]  1  [inf]
        
    """
    pi_lookup = {src: -1}
    while len(pq) > 0: # 3
        min_city_cost = pq.task_key(task=pq.peek()) 
        min_city = pq.pop_task()
        for nb in nbs[min_city]:
            nbcost = pq.task_key(task=nb)
            cand = min_city_cost + edge_cost[(min_city, nb)]
            if cand < nbcost:
                pq.decrease_key(task=nb, key=cand)
                pi_lookup[nb] = min_city

    cur = dst
    path = []
    while cur != -1:
        path.append(cur)
        cur = pi_lookup[cur]
    return path[::-1]

edges = [(0,1,1),(0,2,5),(1,2,1)]
src,dst = (0,2)
print(shortest_path(edges,src,dst)) # 0-1-2

edges = [(0,1,1),(0,2,1),(1,2,1)]
src,dst = (0,2)
print(shortest_path(edges,src,dst)) # 0-2
    




class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        q = [(0,k)]
        elookup = defaultdict(list)
        for u,v,w in times:
            elookup[u].append((v,w)) 
        dlookup = {}
        '''
        elookup: {2:[(1,1),(3,1)], 1:, 3:[(4,1)], 4:}
        q: [ ]
        dlookup: {2:0, 1:1, 3:1, 4:2}
        delay,node: (1,4)
        v,w: 4,1
        '''
        while q: 
            delay, node = heapq.heappop(q) 
            if node not in dlookup: 
                dlookup[node] = delay
                for v, w in elookup[node]: 
                    heapq.heappush(q, (dlookup[node] + w, v))
        return max(dlookup.values()) if len(dlookup) == n else -1class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        r,q,f={},[(0,k)],defaultdict(dict)
        '''
        f={0:{2:1,1:4},2:{1:1}}
        r exp = {0:0,1:2,2:1}=>2
        q=[  ]
        c,u=41
        r={00 21 12}
        '''
        for u,v,w in times:
            f[u][v]=w
        while q:
            c,u=heapq.heappop(q)
            if u in r:
                continue
            r[u]=c
            for (v,vc) in f[u].items():
                heapq.heappush(q,(vc+c,v))
        if len(r)<n:
            return -1
        return max(r.values())