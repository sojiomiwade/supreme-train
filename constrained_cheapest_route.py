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

from collections import defaultdict, deque
from typing import DefaultDict, Dict, List, Tuple

def build_graph(
        flights: List[Tuple[int, int, int]],
        ) -> Tuple[DefaultDict[int,List[int]], Dict[int, int]]:
    nbs = defaultdict(list)
    for (node, nb, _) in flights:
        nbs[node].append(nb)
    nprice = {node: INT_MAX for node in nbs}
    return (nbs, nprice)

def minprice(
        nbs: DefaultDict[int,List[int]], 
        nprice: Dict[int, int], 
        src: int, 
        dst: int,
        maxstops: int,
        ) -> int:
        
    visited = set()

    update_nb_prices(src)
    while True:
        minprice = INT_MAX
        for node in nbs:
            if nprice[node] < minprice:
                minnb = node
                visited.add(node)
                update_nb_prices(node)



INT_MAX = 2**31 - 1
flights = [[0,1,100],[1,2,100],[0,2,500]]
k = len(flights) - 1 # the highest number of stops possible
nbs, nprice = build_graph(flights)
print(minprice(nbs, nprice))
