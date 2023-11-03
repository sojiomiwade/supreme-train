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

