'''
number-of-connected-components-in-an-undirected-graph

Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.

Example 1:

Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]

     0          3
     |          |
     1 --- 2    4

Output: 2
Example 2:

Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]

     0           4
     |           |
     1 --- 2 --- 3

Output:  1
'''
from collections import defaultdict
from typing import List, Tuple


'''
visit each node, if unvisited, increment count, and visit all nodes in that comp (DFS)
'''
def count_comps(n: int, edges: List[List[int]]) -> int:
    def count_comps(node: int) -> None:
        visited.add(node)
        for nb in nbs[node]:
            if nb not in visited:
                count_comps(nb)

    visited,count,nbs=set(),0,defaultdict(list)
    for u,v in edges:
        nbs[u].append(v)
        nbs[v].append(u)

    for node in range(n):
        if node not in visited:
            count+=1
            count_comps(node)
    return count

n = 5; edges = [[0, 1], [1, 2], [3, 4]]
print(count_comps(n,edges)) #2
n = 5; edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
print(count_comps(n,edges)) #1
